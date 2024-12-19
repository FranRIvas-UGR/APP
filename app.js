const fs = require('fs');
const readline = require('readline');
const { obtenerArticulosPorCategoria, getCategorias, insertarCategoria, insertarArticulo, crearTablas } = require('./database');
const { resolverMochilaLimitedPresupuesto } = require('./utils');

// app.js

async function leerCSV() {
    await crearTablas();
    console.log("Leyendo datos de productos.csv...");
    const categorias = new Set();
    const data = fs.readFileSync('productos.csv', 'utf8');
    const rows = data.split('\n').slice(1);

    for (const row of rows) {
        const [categoriaNombre, productoNombre, precio] = row.split(',');
        if (!categorias.has(categoriaNombre)) {
            categorias.add(categoriaNombre);
            await insertarCategoria(categoriaNombre);
        }
        const val = Math.floor(Math.random() * 10) + 1;
        await insertarArticulo(productoNombre, parseFloat(precio), categoriaNombre, val);
    }
}

async function main() {
    const categoriasDict = await getCategorias();
    console.log("Seleccione las categorías (separadas por comas):");
    for (const [id, nombre] of Object.entries(categoriasDict)) {
        console.log(`${id}: ${nombre}`);
    }

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Ingrese los IDs de las categorías seleccionadas: ", async (seleccion) => {
        const selectedIds = seleccion.split(',').map(id => parseInt(id.trim())).filter(id => !isNaN(id));
        if (selectedIds.length === 0) {
            console.log("Debe seleccionar al menos una categoría.");
            rl.close();
            return;
        }

        const articulos = [];
        for (const categoria of selectedIds) {
            const articulosCategoria = await obtenerArticulosPorCategoria(categoria);
            articulos.push({ categoria_id: categoria, articulos_categoria: articulosCategoria });
        }

        const keys = ["id", "nombre", "precio", "valoracion", "categoria_id", "min", "max"];
        const articulosDict = [];
        for (const articulo of articulos) {
            for (const item of articulo.articulos_categoria) {
                if (item[0] !== 'id') {
                    const articuloObj = {};
                    keys.forEach((key, index) => {
                        articuloObj[key] = item[index];
                    });
                    articulosDict.push(articuloObj);
                }
            }
        }

        rl.question("Ingrese el presupuesto: ", async (presupuesto) => {
            presupuesto = parseFloat(presupuesto);
            const presupuestosParciales = {};
            if (selectedIds.length > 1) {
                rl.question("¿Desea repartir el presupuesto entre las categorías? (s/n): ", async (seRepartePresupuesto) => {
                    if (seRepartePresupuesto.toLowerCase() === 's') {
                        for (const categoria of selectedIds) {
                            rl.question(`Ingrese el presupuesto para la categoría ${categoriasDict[categoria]}: `, (presupuestoCategoria) => {
                                presupuestosParciales[categoria] = parseFloat(presupuestoCategoria);
                            });
                        }
                    } else {
                        selectedIds.forEach(categoria => {
                            presupuestosParciales[categoria] = presupuesto / selectedIds.length;
                        });
                    }
                });
            } else {
                presupuestosParciales[selectedIds[0]] = presupuesto;
            }

            const dicNumArticulos = {};
            for (const categoria of selectedIds) {
                rl.question(`Ingrese el número de artículos a seleccionar para la categoría ${categoriasDict[categoria]}: `, (numArticulos) => {
                    dicNumArticulos[categoria] = parseInt(numArticulos);
                });
            }

            console.log(presupuestosParciales);
            console.log("\nResultado de la optimización 3:");
            for (const categoria of selectedIds) {
                const resultadoCategoria = calcularProductosCategoria(articulosDict, presupuestosParciales[categoria], categoria, dicNumArticulos[categoria]);
                imprimirResultadoOptimizacion(resultadoCategoria);
                console.log("\n");
            }

            console.log("\nResultado de la optimización 4:");
            for (const categoria of selectedIds) {
                const resultadoCategoria = calcularProductosCategoriaMax(articulosDict, presupuestosParciales[categoria], categoria);
                imprimirResultadoOptimizacion(resultadoCategoria);
                console.log("\n");
            }

            rl.close();
        });
    });
}

function imprimirResultadoOptimizacion(resultado) {
    console.log("Artículos seleccionados:");
    let precioTotal = 0;
    for (const articulo of resultado.articulos_seleccionados) {
        if (articulo.cantidad > 0) {
            console.log(`  - ${articulo.nombre} (Cantidad: ${articulo.cantidad}, Precio: ${articulo.precio}, Valoración: ${articulo.valoracion})`);
            precioTotal += articulo.cantidad * articulo.precio;
        }
    }
    console.log(`Valoración total: ${resultado.valoracion_total}`);
    console.log(`Precio total: ${precioTotal.toFixed(2)}`);
}

function calcularProductosCategoria(diccionarioArticulosGeneral, presupuestoReducido, categoriaId, numArticulos) {
    const articulosCat = diccionarioArticulosGeneral.filter(articulo => articulo.categoria_id === categoriaId);
    const art = resolverMochilaLimitedPresupuesto(articulosCat, presupuestoReducido);

    const artResult = { articulos_seleccionados: [], valoracion_total: 0, precio_total: 0 };

    for (const articulo of art.articulos_seleccionados) {
        if (artResult.articulos_seleccionados.length >= numArticulos) {
            break;
        }
        if (articulo.cantidad > 0) {
            artResult.articulos_seleccionados.push({ nombre: articulo.nombre, precio: articulo.precio, valoracion: articulo.valoracion, cantidad: articulo.cantidad });
            artResult.valoracion_total += articulo.valoracion;
            artResult.precio_total += articulo.precio;
        }
    }

    return artResult;
}

function calcularProductosCategoriaMax(diccionarioArticulosGeneral, presupuestoReducido, categoriaId) {
    const articulosCat = diccionarioArticulosGeneral.filter(articulo => articulo.categoria_id === categoriaId);
    const art = resolverMochilaLimitedPresupuesto(articulosCat, presupuestoReducido);

    const artResult = { articulos_seleccionados: [], valoracion_total: 0, precio_total: 0 };

    for (const articulo of art.articulos_seleccionados) {
        if (articulo.cantidad > 0) {
            artResult.articulos_seleccionados.push({ nombre: articulo.nombre, precio: articulo.precio, valoracion: articulo.valoracion, cantidad: articulo.cantidad });
            artResult.valoracion_total += articulo.valoracion;
            artResult.precio_total += articulo.precio;
        }
    }

    return artResult;
}

if (require.main === module) {
    console.log("Bienvenido al sistema de recomendación de compras.");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("¿Desea leer los datos de productos desde el archivo productos.csv (1) o usar la app (2) ?", (opcion) => {
        if (opcion === '1') {
            leerCSV().then(() => rl.close());
        } else if (opcion === '2') {
            main().then(() => rl.close());
        } else {
            console.log("Opción no válida.");
            rl.close();
        }
    });
}