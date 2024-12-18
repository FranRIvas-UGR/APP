import csv

input_file = 'productos.csv'
output_file = 'output.csv'

def categoria_12(reader, salsas, id):
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'vinagre' in producto_nombre:
                row['Categoría Nombre'] = 'Vinagre'
                row['Categoría ID'] = 2
            elif any(salsa in producto_nombre for salsa in salsas):
                row['Categoría Nombre'] = 'Salsa'
                row['Categoría ID'] = 3
            elif 'sal' in producto_nombre:
                row['Categoría Nombre'] = 'Sal'
                row['Categoría ID'] = 4
            elif 'sazonador' in producto_nombre:
                row['Categoría Nombre'] = 'Sazonador'
                row['Categoría ID'] = 5
            elif 'bicarbonato' in producto_nombre:
                row['Categoría Nombre'] = 'Bicarbonato'
                row['Categoría ID'] = 6
            elif 'limón' in producto_nombre:
                row['Categoría Nombre'] = 'Limon'
                row['Categoría ID'] = 7
            elif 'aceite' in producto_nombre:
                row['Categoría Nombre'] = 'Aceite'
                row['Categoría ID'] = 1
            else:
                row['Categoría Nombre'] = 'Especias'
                row['Categoría ID'] = 8
            filas.append(row)
    return filas

def categoria_18(reader, refrescos, id):
    # Agua y refrescos
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if any(refresco in producto_nombre for refresco in refrescos):
                row['Categoría Nombre'] = 'Refrescos'
                row['Categoría ID'] = 9
            elif 'agua' in producto_nombre:
                row['Categoría Nombre'] = 'Agua'
                row['Categoría ID'] = 10
            elif 'zumo' in producto_nombre:
                row['Categoría Nombre'] = 'Zumo'
                row['Categoría ID'] = 11
            elif 'energética' in producto_nombre or 'energético' in producto_nombre:
                row['Categoría Nombre'] = 'Bebida energética'
                row['Categoría ID'] = 12
            elif 'isotónica' in producto_nombre:
                row['Categoría Nombre'] = 'Bebida isotónica'
                row['Categoría ID'] = 13
            elif 'té' in producto_nombre:
                row['Categoría Nombre'] = 'Té'
                row['Categoría ID'] = 14
            elif 'tónica' in producto_nombre:
                row['Categoría Nombre'] = 'Tónica'
                row['Categoría ID'] = 15
            elif 'café' in producto_nombre:
                row['Categoría Nombre'] = 'Café'
                row['Categoría ID'] = 16
            else:
                row['Categoría Nombre'] = 'Agua y refrescos'
                row['Categoría ID'] = 17
            filas.append(row)
    return filas

def categoria_3(reader, id):
    # Carne
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'pollo' in producto_nombre:
                row['Categoría Nombre'] = 'Pollo'
                row['Categoría ID'] = 18
            elif 'ternera' in producto_nombre or 'vacuno' in producto_nombre:
                row['Categoría Nombre'] = 'Ternera'
                row['Categoría ID'] = 19
            elif 'cerdo' in producto_nombre:
                row['Categoría Nombre'] = 'Cerdo'
                row['Categoría ID'] = 20
            elif 'cordero' in producto_nombre:
                row['Categoría Nombre'] = 'Cordero'
                row['Categoría ID'] = 21
            elif 'pavo' in producto_nombre:
                row['Categoría Nombre'] = 'Pavo'
                row['Categoría ID'] = 22
            elif 'conejo' in producto_nombre:
                row['Categoría Nombre'] = 'Conejo'
                row['Categoría ID'] = 23
            elif 'burguer' in producto_nombre:
                row['Categoría Nombre'] = 'Hamburguesa'
                row['Categoría ID'] = 24
            elif 'salchicha' in producto_nombre:
                row['Categoría Nombre'] = 'Salchicha'
                row['Categoría ID'] = 25
            else:
                row['Categoría Nombre'] = 'Carne'
                row['Categoría ID'] = 26
            filas.append(row)
    return filas

def categoria_4(reader, id):
    # Charcutería y quesos
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'queso' in producto_nombre:
                row['Categoría Nombre'] = 'Queso'
                row['Categoría ID'] = 27
            elif 'embutido' in producto_nombre:
                row['Categoría Nombre'] = 'Embutido'
                row['Categoría ID'] = 28
            elif 'jamón' in producto_nombre:
                row['Categoría Nombre'] = 'Jamón'
                row['Categoría ID'] = 29
            elif 'chorizo' in producto_nombre:
                row['Categoría Nombre'] = 'Chorizo'
                row['Categoría ID'] = 30
            elif 'salchichón' in producto_nombre:
                row['Categoría Nombre'] = 'Salchichón'
                row['Categoría ID'] = 31
            elif 'lomo' in producto_nombre:
                row['Categoría Nombre'] = 'Lomo'
                row['Categoría ID'] = 32
            elif 'mortadela' in producto_nombre:
                row['Categoría Nombre'] = 'Mortadela'
                row['Categoría ID'] = 33
            elif 'salami' in producto_nombre:
                row['Categoría Nombre'] = 'Salami'
                row['Categoría ID'] = 34
            elif 'fuet' in producto_nombre:
                row['Categoría Nombre'] = 'Fuet'
                row['Categoría ID'] = 35
            elif 'sobrasada' in producto_nombre:
                row['Categoría Nombre'] = 'Sobrasada'
                row['Categoría ID'] = 36
            elif 'longaniza' in producto_nombre:
                row['Categoría Nombre'] = 'Longaniza'
                row['Categoría ID'] = 37
            else:
                row['Categoría Nombre'] = 'Charcutería'
                row['Categoría ID'] = 38
            filas.append(row)
    return filas

def categoria_5(reader, id):
    # Panadería y pastelería
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'pan' in producto_nombre:
                row['Categoría Nombre'] = 'Pan'
                row['Categoría ID'] = 39
            elif 'pastel' in producto_nombre or 'tarta' in producto_nombre:
                row['Categoría Nombre'] = 'Pastel'
                row['Categoría ID'] = 40
            elif 'galleta' in producto_nombre:
                row['Categoría Nombre'] = 'Galleta'
                row['Categoría ID'] = 41
            elif 'bollería' in producto_nombre or 'croissant' in producto_nombre:
                row['Categoría Nombre'] = 'Bollería'
                row['Categoría ID'] = 42
            else:
                row['Categoría Nombre'] = 'Panadería y pastelería'
                row['Categoría ID'] = 43
            filas.append(row)
    return filas

def categoria_6(reader, id):
    # Huevos, leche y mantequilla
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'huevo' in producto_nombre:
                row['Categoría Nombre'] = 'Huevos'
                row['Categoría ID'] = 44
            elif 'leche' in producto_nombre:
                row['Categoría Nombre'] = 'Leche'
                row['Categoría ID'] = 45
            elif 'mantequilla' in producto_nombre:
                row['Categoría Nombre'] = 'Mantequilla'
                row['Categoría ID'] = 46
            elif 'bebida' in producto_nombre:
                row['Categoría Nombre'] = 'Bebida'
                row['Categoría ID'] = 47
            elif 'batido' in producto_nombre:
                row['Categoría Nombre'] = 'Batido'
                row['Categoría ID'] = 47
            else:
                row['Categoría Nombre'] = 'Huevos, leche y mantequilla'
                row['Categoría ID'] = 48
            filas.append(row)
    return filas

def categoria_7(reader, id):
    # Cereales y galletas
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'cereal' in producto_nombre:
                row['Categoría Nombre'] = 'Cereales'
                row['Categoría ID'] = 49
            elif 'galleta' in producto_nombre or 'barquillo' in producto_nombre:
                row['Categoría Nombre'] = 'Galletas'
                row['Categoría ID'] = 50
            elif 'muesli' in producto_nombre:
                row['Categoría Nombre'] = 'Muesli'
                row['Categoría ID'] = 51
            elif 'avena' in producto_nombre:
                row['Categoría Nombre'] = 'Avena'
                row['Categoría ID'] = 52
            elif 'barrita' in producto_nombre:
                row['Categoría Nombre'] = 'Barritas'
                row['Categoría ID'] = 53
            elif 'obleas' or 'tubitos' or 'tartaletes' in producto_nombre:
                row['Categoría Nombre'] = 'Obleas, tubitos y tartaletes'
                row['Categoría ID'] = 54
            elif 'tortitas' or 'pastas' in producto_nombre:
                row['Categoría Nombre'] = 'Tortitas y pastas'
                row['Categoría ID'] = 55
            elif 'bollitos' in producto_nombre:
                row['Categoría Nombre'] = 'Bollitos'
                row['Categoría ID'] = 56
            else:
                row['Categoría Nombre'] = 'Cereales y galletas'
                row['Categoría ID'] = 57
            filas.append(row)
    return filas

def categoria_8(reader, id):
    # Cacao, café e infusiones
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'cacao' in producto_nombre:
                row['Categoría Nombre'] = 'Cacao'
                row['Categoría ID'] = 58
            elif 'café' in producto_nombre or 'cápsula' in producto_nombre:
                row['Categoría Nombre'] = 'Café'
                row['Categoría ID'] = 16
            elif 'infusión' in producto_nombre:
                row['Categoría Nombre'] = 'Infusión'
                row['Categoría ID'] = 59
            elif 'chocolate' in producto_nombre:
                row['Categoría Nombre'] = 'Chocolate'
                row['Categoría ID'] = 60
            elif 'cereales' in producto_nombre:
                row['Categoría Nombre'] = 'Cereales'
                row['Categoría ID'] = 49
            elif 'té' in producto_nombre:
                row['Categoría Nombre'] = 'Té'
                row['Categoría ID'] = 14
            else:
                row['Categoría Nombre'] = 'Cacao, café e infusiones'
                row['Categoría ID'] = 62
            filas.append(row)
    return filas

def categoria_9(reader, id):
    # Azúcar, caramelos y chocolate
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'caramelo' in producto_nombre:
                row['Categoría Nombre'] = 'Caramelo'
                row['Categoría ID'] = 63
            elif 'chocolate' in producto_nombre:
                row['Categoría Nombre'] = 'Chocolate'
                row['Categoría ID'] = 60
            elif 'edulcorante' in producto_nombre:
                row['Categoría Nombre'] = 'Edulcorante'
                row['Categoría ID'] = 64
            elif 'sirope' in producto_nombre:
                row['Categoría Nombre'] = 'Siropes'
                row['Categoría ID'] = 65
            elif 'chicle' in producto_nombre:
                row['Categoría Nombre'] = 'Chicle'
                row['Categoría ID'] = 66
            elif 'bombones' in producto_nombre:
                row['Categoría Nombre'] = 'Bombones'
                row['Categoría ID'] = 67
            elif 'azúcar' in producto_nombre:
                row['Categoría Nombre'] = 'Azúcar'
                row['Categoría ID'] = 68
            elif 'crema' in producto_nombre:
                row['Categoría Nombre'] = 'Cremas'
                row['Categoría ID'] = 69
            elif 'golosina' in producto_nombre:
                row['Categoría Nombre'] = 'Golosinas'
                row['Categoría ID'] = 70
            elif 'mermelada' in producto_nombre or 'confitura' in producto_nombre or 'confitado' in producto_nombre:
                row['Categoría Nombre'] = 'Mermeladas y confituras'
                row['Categoría ID'] = 71
            elif 'miel' in producto_nombre:
                row['Categoría Nombre'] = 'Miel'
                row['Categoría ID'] = 72
            elif 'turrón' in producto_nombre:
                row['Categoría Nombre'] = 'Turrón'
                row['Categoría ID'] = 73
            else:
                row['Categoría Nombre'] = 'Azúcar, caramelos y chocolate'
                row['Categoría ID'] = 74
            filas.append(row)
    return filas

def categoria_10(reader, id):
    # Zumos
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'fruta + leche' in producto_nombre:
                row['Categoría Nombre'] = 'Fruta + Leche'
                row['Categoría ID'] = 75
            elif 'zumo' in producto_nombre:
                row['Categoría Nombre'] = 'Zumo'
                row['Categoría ID'] = 11
            elif 'nectar' in producto_nombre:
                row['Categoría Nombre'] = 'Néctar'
                row['Categoría ID'] = 76
            elif 'bebida' in producto_nombre:
                row['Categoría Nombre'] = 'Bebida'
                row['Categoría ID'] = 47
            elif 'smoothie' in producto_nombre:
                row['Categoría Nombre'] = 'Smoothie'
                row['Categoría ID'] = 77
            else:
                row['Categoría Nombre'] = 'Zumo'
                row['Categoría ID'] = 11
            filas.append(row)
    return filas

def categoria_11(reader, id):
    # Postres y yogures
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'yogur' in producto_nombre:
                row['Categoría Nombre'] = 'Yogur'
                row['Categoría ID'] = 78
            elif 'postre' in producto_nombre:
                row['Categoría Nombre'] = 'Postre'
                row['Categoría ID'] = 79
            elif 'flan' in producto_nombre:
                row['Categoría Nombre'] = 'Flan'
                row['Categoría ID'] = 80
            elif 'natillas' in producto_nombre:
                row['Categoría Nombre'] = 'Natillas'
                row['Categoría ID'] = 81
            elif 'bífidus' in producto_nombre:
                row['Categoría Nombre'] = 'Bífidus'
                row['Categoría ID'] = 82
            elif 'gelatina' in producto_nombre:
                row['Categoría Nombre'] = 'Gelatina'
                row['Categoría ID'] = 83
            elif 'queso' in producto_nombre:
                row['Categoría Nombre'] = 'Queso'
                row['Categoría ID'] = 27
            elif 'bebida láctea' in producto_nombre:
                row['Categoría Nombre'] = 'Bebida láctea'
                row['Categoría ID'] = 47
            elif 'postre lácteo' in producto_nombre:
                row['Categoría Nombre'] = 'Postre lácteo'
                row['Categoría ID'] = 84
            else:
                row['Categoría Nombre'] = 'Postre'
                row['Categoría ID'] = 79
            filas.append(row)
    return filas

def categoria_1(reader, id):
    # Frutas y verduras
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'manzana' in producto_nombre:
                row['Categoría Nombre'] = 'Manzana'
                row['Categoría ID'] = 85
            elif 'pera' in producto_nombre:
                row['Categoría Nombre'] = 'Pera'
                row['Categoría ID'] = 86
            elif 'uva' in producto_nombre:
                row['Categoría Nombre'] = 'Uva'
                row['Categoría ID'] = 87
            elif 'ensalada' in producto_nombre:
                row['Categoría Nombre'] = 'Ensalada'
                row['Categoría ID'] = 88
            elif 'tomate' in producto_nombre:
                row['Categoría Nombre'] = 'Tomate'
                row['Categoría ID'] = 89
            elif 'lechuga' in producto_nombre:
                row['Categoría Nombre'] = 'Lechuga'
                row['Categoría ID'] = 90
            elif 'patata' in producto_nombre:
                row['Categoría Nombre'] = 'Patata'
                row['Categoría ID'] = 91
            elif 'zanahoria' in producto_nombre:
                row['Categoría Nombre'] = 'Zanahoria'
                row['Categoría ID'] = 92
            elif 'plátano' in producto_nombre:
                row['Categoría Nombre'] = 'Plátano'
                row['Categoría ID'] = 93
            elif 'naranja' in producto_nombre:
                row['Categoría Nombre'] = 'Naranja'
                row['Categoría ID'] = 94
            elif 'limón' in producto_nombre:
                row['Categoría Nombre'] = 'Limón'
                row['Categoría ID'] = 95
            elif 'fresa' in producto_nombre:
                row['Categoría Nombre'] = 'Fresa'
                row['Categoría ID'] = 96
            elif 'melón' in producto_nombre:
                row['Categoría Nombre'] = 'Melón'
                row['Categoría ID'] = 97
            elif 'sandía' in producto_nombre:
                row['Categoría Nombre'] = 'Sandía'
                row['Categoría ID'] = 98
            elif 'piña' in producto_nombre:
                row['Categoría Nombre'] = 'Piña'
                row['Categoría ID'] = 99
            elif 'kiwi' in producto_nombre:
                row['Categoría Nombre'] = 'Kiwi'
                row['Categoría ID'] = 100
            elif 'mango' in producto_nombre:
                row['Categoría Nombre'] = 'Mango'
                row['Categoría ID'] = 101
            elif 'papaya' in producto_nombre:
                row['Categoría Nombre'] = 'Papaya'
                row['Categoría ID'] = 102
            elif 'aguacate' in producto_nombre:
                row['Categoría Nombre'] = 'Aguacate'
                row['Categoría ID'] = 103
            elif 'cebolla' in producto_nombre:
                row['Categoría Nombre'] = 'Cebolla'
                row['Categoría ID'] = 104
            elif 'pimiento' in producto_nombre:
                row['Categoría Nombre'] = 'Pimiento'
                row['Categoría ID'] = 105
            elif 'calabacín' in producto_nombre:
                row['Categoría Nombre'] = 'Calabacín'
                row['Categoría ID'] = 106
            elif 'berenjena' in producto_nombre:
                row['Categoría Nombre'] = 'Berenjena'
                row['Categoría ID'] = 107
            elif 'pepino' in producto_nombre:
                row['Categoría Nombre'] = 'Pepino'
                row['Categoría ID'] = 108
            elif 'calabaza' in producto_nombre:
                row['Categoría Nombre'] = 'Calabaza'
                row['Categoría ID'] = 109
            elif 'brócoli' in producto_nombre:
                row['Categoría Nombre'] = 'Brócoli'
                row['Categoría ID'] = 110
            elif 'coliflor' in producto_nombre:
                row['Categoría Nombre'] = 'Coliflor'
                row['Categoría ID'] = 111
            elif 'espinaca' in producto_nombre:
                row['Categoría Nombre'] = 'Espinaca'
                row['Categoría ID'] = 112
            elif 'alcachofa' in producto_nombre:
                row['Categoría Nombre'] = 'Alcachofa'
                row['Categoría ID'] = 113
            elif 'apio' in producto_nombre:
                row['Categoría Nombre'] = 'Apio'
                row['Categoría ID'] = 114
            elif 'remolacha' in producto_nombre:
                row['Categoría Nombre'] = 'Remolacha'
                row['Categoría ID'] = 115
            elif 'rábano' in producto_nombre:
                row['Categoría Nombre'] = 'Rábano'
                row['Categoría ID'] = 116
            elif 'champiñón' in producto_nombre:
                row['Categoría Nombre'] = 'Champiñón'
                row['Categoría ID'] = 117
            elif 'seta' in producto_nombre:
                row['Categoría Nombre'] = 'Seta'
                row['Categoría ID'] = 118
            else:
                row['Categoría Nombre'] = 'Fruta y verdura'
                row['Categoría ID'] = 119
            filas.append(row)
    return filas

def categoria_13(reader, id):
    # Arroz, legumbres y pasta
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'arroz' in producto_nombre:
                row['Categoría Nombre'] = 'Arroz'
                row['Categoría ID'] = 120
            elif 'quinoa' in producto_nombre:
                row['Categoría Nombre'] = 'Quinoa'
                row['Categoría ID'] = 121
            elif 'cous cous' in producto_nombre:
                row['Categoría Nombre'] = 'Cous cous'
                row['Categoría ID'] = 122
            elif 'garbanzo' in producto_nombre:
                row['Categoría Nombre'] = 'Garbanzo'
                row['Categoría ID'] = 123
            elif 'alubia' in producto_nombre:
                row['Categoría Nombre'] = 'Alubia'
                row['Categoría ID'] = 124
            elif 'lenteja' in producto_nombre:
                row['Categoría Nombre'] = 'Lenteja'
                row['Categoría ID'] = 125
            elif 'soja' in producto_nombre:
                row['Categoría Nombre'] = 'Soja'
                row['Categoría ID'] = 126
            elif 'fideo' in producto_nombre or 'pasta' in producto_nombre or 'macarrón' in producto_nombre or 'spaghetti' in producto_nombre or 'tortellini' in producto_nombre or 'ravioli' in producto_nombre or 'gnocchi' in producto_nombre:
                row['Categoría Nombre'] = 'Pasta'
                row['Categoría ID'] = 127
            else:
                row['Categoría Nombre'] = 'Arroz, legumbres y pasta'
                row['Categoría ID'] = 128
            filas.append(row)
    return filas

def categoria_14(reader, id):
    # Conservas, caldos y cremas
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'atún' in producto_nombre:
                row['Categoría Nombre'] = 'Atún'
                row['Categoría ID'] = 129
            elif 'bonito' in producto_nombre:
                row['Categoría Nombre'] = 'Bonito'
                row['Categoría ID'] = 130
            elif 'caballa' in producto_nombre:
                row['Categoría Nombre'] = 'Caballa'
                row['Categoría ID'] = 131
            elif 'melva' in producto_nombre:
                row['Categoría Nombre'] = 'Melva'
                row['Categoría ID'] = 132
            elif 'sardina' in producto_nombre or 'sardinilla' in producto_nombre:
                row['Categoría Nombre'] = 'Sardinas'
                row['Categoría ID'] = 133
            elif 'calamar' in producto_nombre or 'pota' in producto_nombre or 'chipirones' in producto_nombre:
                row['Categoría Nombre'] = 'Calamares'
                row['Categoría ID'] = 134
            elif 'salmón' in producto_nombre:
                row['Categoría Nombre'] = 'Salmón'
                row['Categoría ID'] = 135
            elif 'berberecho' in producto_nombre:
                row['Categoría Nombre'] = 'Berberechos'
                row['Categoría ID'] = 136
            elif 'almeja' in producto_nombre or 'almejón' in producto_nombre:
                row['Categoría Nombre'] = 'Almejas'
                row['Categoría ID'] = 137
            elif 'zamburiña' in producto_nombre:
                row['Categoría Nombre'] = 'Zamburiñas'
                row['Categoría ID'] = 138
            elif 'mejillón' in producto_nombre:
                row['Categoría Nombre'] = 'Mejillones'
                row['Categoría ID'] = 139
            elif 'maíz' in producto_nombre:
                row['Categoría Nombre'] = 'Maíz'
            elif 'espárrago' in producto_nombre:
                row['Categoría Nombre'] = 'Espárragos'
            elif 'champiñón' in producto_nombre:
                row['Categoría Nombre'] = 'Champiñones'
                row['Categoría ID'] = 117
            elif 'pimiento' in producto_nombre:
                row['Categoría Nombre'] = 'Pimientos'
                row['Categoría ID'] = 140
            elif 'guisante' in producto_nombre:
                row['Categoría Nombre'] = 'Guisantes'
                row['Categoría ID'] = 141
            elif 'judía' in producto_nombre:
                row['Categoría Nombre'] = 'Judías'
                row['Categoría ID'] = 142
            elif 'alcachofa' in producto_nombre:
                row['Categoría Nombre'] = 'Alcachofas'
                row['Categoría ID'] = 143
            elif 'zanahoria' in producto_nombre:
                row['Categoría Nombre'] = 'Zanahorias'
                row['Categoría ID'] = 144
            elif 'remolacha' in producto_nombre:
                row['Categoría Nombre'] = 'Remolacha'
                row['Categoría ID'] = 115
            elif 'macedonia' in producto_nombre:
                row['Categoría Nombre'] = 'Macedonia'
                row['Categoría ID'] = 146
            elif 'verdura' in producto_nombre:
                row['Categoría Nombre'] = 'Verduras'
                row['Categoría ID'] = 147
            elif 'patata' in producto_nombre:
                row['Categoría Nombre'] = 'Patatas'
                row['Categoría ID'] = 148
            elif 'ensalada' in producto_nombre:
                row['Categoría Nombre'] = 'Ensalada'
                row['Categoría ID'] = 88
            elif 'brotes' in producto_nombre:
                row['Categoría Nombre'] = 'Brotes'
                row['Categoría ID'] = 150
            elif 'cebolla' in producto_nombre:
                row['Categoría Nombre'] = 'Cebolla'
                row['Categoría ID'] = 104
            elif 'yema' in producto_nombre:
                row['Categoría Nombre'] = 'Yemas'
                row['Categoría ID'] = 152
            elif 'chucrut' in producto_nombre:
                row['Categoría Nombre'] = 'Chucrut'
                row['Categoría ID'] = 153
            elif 'piña' in producto_nombre:
                row['Categoría Nombre'] = 'Piña'
                row['Categoría ID'] = 99
            elif 'melocotón' in producto_nombre:
                row['Categoría Nombre'] = 'Melocotón'
                row['Categoría ID'] = 155
            elif 'membrillo' in producto_nombre:
                row['Categoría Nombre'] = 'Membrillo'
                row['Categoría ID'] = 156
            elif 'cerezas' in producto_nombre:
                row['Categoría Nombre'] = 'Cerezas'
                row['Categoría ID'] = 157
            elif 'uva' in producto_nombre:
                row['Categoría Nombre'] = 'Uva'
                row['Categoría ID'] = 87
            elif 'gazpacho' in producto_nombre:
                row['Categoría Nombre'] = 'Gazpacho'
                row['Categoría ID'] = 159
            elif 'salmorejo' in producto_nombre:
                row['Categoría Nombre'] = 'Salmorejo'
                row['Categoría ID'] = 160
            elif 'crema' in producto_nombre:
                row['Categoría Nombre'] = 'Cremas'
                row['Categoría ID'] = 69
            elif 'puré' in producto_nombre:
                row['Categoría Nombre'] = 'Puré'
                row['Categoría ID'] = 162
            elif 'sopa' in producto_nombre:
                row['Categoría Nombre'] = 'Sopa'
                row['Categoría ID'] = 163
            elif 'caldo' in producto_nombre:
                row['Categoría Nombre'] = 'Caldo'
                row['Categoría ID'] = 164
            elif 'tomate' in producto_nombre:
                row['Categoría Nombre'] = 'Tomate'
                row['Categoría ID'] = 89
            else:
                row['Categoría Nombre'] = 'Conservas, caldos y cremas'
                row['Categoría ID'] = 166
            filas.append(row)
    return filas

def categoria_15(reader, id):
    # Aperitivos y snacks
    snacks = ['palomitas', 'gusanitos', 'tiras', 'nachos']
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'patatas' in producto_nombre:
                row['Categoría Nombre'] = 'Patatas fritas'
                row['Categoría ID'] = 167
            elif 'snack' in producto_nombre:
                row['Categoría Nombre'] = 'Snacks'
                row['Categoría ID'] = 168
            elif 'frutos secos' in producto_nombre or 'pistachos' in producto_nombre or 'cacahuetes' in producto_nombre or 'almendra' in producto_nombre or 'nuez' in producto_nombre or 'avellana' in producto_nombre or 'anacardo' in producto_nombre or 'piñón' in producto_nombre or 'castaña' in producto_nombre or 'nueces' in producto_nombre or 'pipa' in producto_nombre or 'pistacho' in producto_nombre or 'semilla' in producto_nombre or 'semillas' in producto_nombre or 'cacahuete' in producto_nombre or 'almendras' in producto_nombre or 'nueces' in producto_nombre or 'avellanas' in producto_nombre or 'piñones' in producto_nombre or 'castañas' in producto_nombre or 'pistachos' in producto_nombre:
                row['Categoría Nombre'] = 'Frutos secos'
                row['Categoría ID'] = 169
            elif 'aceitunas' in producto_nombre:
                row['Categoría Nombre'] = 'Aceitunas'
                row['Categoría ID'] = 170
            elif 'pepinillos' in producto_nombre:
                row['Categoría Nombre'] = 'Pepinillos'
                row['Categoría ID'] = 171
            elif any(snack in producto_nombre for snack in snacks):
                row['Categoría Nombre'] = 'Snacks'
                row['Categoría ID'] = 168
            filas.append(row)
    return filas

def categoria_16(reader, id):
    # Pizzas y platos preparados
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'pizza' in producto_nombre:
                row['Categoría Nombre'] = 'Pizza'
                row['Categoría ID'] = 173
            elif 'lasaña' in producto_nombre:
                row['Categoría Nombre'] = 'Lasaña'
                row['Categoría ID'] = 174
            elif 'canelones' in producto_nombre:
                row['Categoría Nombre'] = 'Canelones'
                row['Categoría ID'] = 175
            elif 'croquetas' in producto_nombre:
                row['Categoría Nombre'] = 'Croquetas'
                row['Categoría ID'] = 176
            elif 'empanada' in producto_nombre:
                row['Categoría Nombre'] = 'Empanada'
                row['Categoría ID'] = 177
            elif 'tortilla' in producto_nombre:
                row['Categoría Nombre'] = 'Tortilla'
                row['Categoría ID'] = 178
            elif 'paella' in producto_nombre:
                row['Categoría Nombre'] = 'Paella'
                row['Categoría ID'] = 179
            elif 'arroz' in producto_nombre:
                row['Categoría Nombre'] = 'Arroz'
                row['Categoría ID'] = 120
            elif 'sopa' in producto_nombre:
                row['Categoría Nombre'] = 'Sopa'
                row['Categoría ID'] = 181
            elif 'caldo' in producto_nombre:
                row['Categoría Nombre'] = 'Caldo'
                row['Categoría ID'] = 182
            elif 'crema' in producto_nombre:
                row['Categoría Nombre'] = 'Crema'
                row['Categoría ID'] = 183
            elif 'puré' in producto_nombre:
                row['Categoría Nombre'] = 'Puré'
                row['Categoría ID'] = 184
            else:
                row['Categoría Nombre'] = 'Platos preparados'
                row['Categoría ID'] = 185
            filas.append(row)
    return filas

def categoria_17(reader, id):
    # Congelados
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'arroz' in producto_nombre:
                row['Categoría Nombre'] = 'Arroz'
                row['Categoría ID'] = 120
            elif 'lasaña' in producto_nombre:
                row['Categoría Nombre'] = 'Lasaña'
                row['Categoría ID'] = 174
            elif 'canelones' in producto_nombre:
                row['Categoría Nombre'] = 'Canelones'
                row['Categoría ID'] = 175
            elif 'gnocchi' in producto_nombre:
                row['Categoría Nombre'] = 'Gnocchi'
                row['Categoría ID'] = 189
            elif 'sopa' in producto_nombre:
                row['Categoría Nombre'] = 'Sopa'
                row['Categoría ID'] = 163
            elif 'pollo' in producto_nombre:
                row['Categoría Nombre'] = 'Pollo'
                row['Categoría ID'] = 18
            elif 'cerdo' in producto_nombre:
                row['Categoría Nombre'] = 'Cerdo'
                row['Categoría ID'] = 20
            elif 'pavo' in producto_nombre:
                row['Categoría Nombre'] = 'Pavo'
                row['Categoría ID'] = 22
            elif 'cordero' in producto_nombre:
                row['Categoría Nombre'] = 'Cordero'
                row['Categoría ID'] = 21
            elif 'cochinillo' in producto_nombre:
                row['Categoría Nombre'] = 'Cochinillo'
                row['Categoría ID'] = 195
            elif 'vacuno' in producto_nombre:
                row['Categoría Nombre'] = 'Vacuno'
                row['Categoría ID'] = 196
            elif 'helado' in producto_nombre:
                row['Categoría Nombre'] = 'Helado'
                row['Categoría ID'] = 197
            elif 'granizado' in producto_nombre:
                row['Categoría Nombre'] = 'Granizado'
                row['Categoría ID'] = 198
            elif 'tarta' in producto_nombre:
                row['Categoría Nombre'] = 'Tarta'
                row['Categoría ID'] = 199
            elif 'churros' in producto_nombre:
                row['Categoría Nombre'] = 'Churros'
                row['Categoría ID'] = 200
            elif 'crepes' in producto_nombre:
                row['Categoría Nombre'] = 'Crepes'
                row['Categoría ID'] = 201
            elif 'frutos rojos' in producto_nombre:
                row['Categoría Nombre'] = 'Frutos rojos'
                row['Categoría ID'] = 202
            elif 'verdura' in producto_nombre:
                row['Categoría Nombre'] = 'Verdura'
                row['Categoría ID'] = 203
            elif 'gamba' in producto_nombre or 'langostino' in producto_nombre or 'camarón' in producto_nombre or 'bogavante' in producto_nombre or 'cangrejo' in producto_nombre or 'vieira' in producto_nombre or 'buey de mar' in producto_nombre or 'nécora' in producto_nombre or 'surimi' in producto_nombre or 'mejillón' in producto_nombre or 'almeja' in producto_nombre or 'caracol' in producto_nombre or 'merluza' in producto_nombre or 'bacalao' in producto_nombre or 'pota' in producto_nombre or 'sepia' in producto_nombre or 'salmón' in producto_nombre or 'rape' in producto_nombre or 'tinta' in producto_nombre or 'atún' in producto_nombre or 'hueva' in producto_nombre or 'calamar' in producto_nombre or 'croqueta' in producto_nombre or 'pizza' in producto_nombre or 'nugget' in producto_nombre or 'empanadilla' in producto_nombre or 'rabas' in producto_nombre or 'anillas' in producto_nombre or 'muslitos' in producto_nombre or 'palitos' in producto_nombre or 'figuritas' in producto_nombre or 'chipirones' in producto_nombre or 'boquerón' in producto_nombre or 'torpedos' in producto_nombre or 'rollitos' in producto_nombre or 'gyozas' in producto_nombre or 'patatas' in producto_nombre:
                row['Categoría Nombre'] = 'Pescado y marisco'
                row['Categoría ID'] = 204
            else:
                row['Categoría Nombre'] = 'Congelados'
                row['Categoría ID'] = 205
            filas.append(row)
    return filas

def categoria_2(reader, id):
    # Marisco y pescado
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'gamba' in producto_nombre or 'langostino' in producto_nombre:
                row['Categoría Nombre'] = 'Gambas y langostinos'
                row['Categoría ID'] = 206
            elif 'camarón' in producto_nombre:
                row['Categoría Nombre'] = 'Camarones'
                row['Categoría ID'] = 207
            elif 'bogavante' in producto_nombre or 'cangrejo' in producto_nombre or 'centollo' in producto_nombre or 'nécora' in producto_nombre or 'percebe' in producto_nombre or 'mejillón' in producto_nombre or 'almeja' in producto_nombre or 'ostra' in producto_nombre or 'vieira' in producto_nombre or 'berberecho' in producto_nombre or 'zamburiña' in producto_nombre or 'caracol' in producto_nombre:
                row['Categoría Nombre'] = 'Moluscos'
                row['Categoría ID'] = 208
            elif 'merluza' in producto_nombre or 'bacalao' in producto_nombre or 'salmón' in producto_nombre or 'atún' in producto_nombre or 'trucha' in producto_nombre or 'pez espada' in producto_nombre or 'dorada' in producto_nombre or 'lubina' in producto_nombre or 'caballa' in producto_nombre or 'sardina' in producto_nombre or 'boquerón' in producto_nombre:
                row['Categoría Nombre'] = 'Pescados'
                row['Categoría ID'] = 209
            else:
                row['Categoría Nombre'] = 'Marisco y pescado'
                row['Categoría ID'] = 210
            filas.append(row)
    return filas

def categoria_19(reader, id):
    # Bodega
    filas = []
    for row in reader:
        if row['Categoría ID'] == id:
            producto_nombre = row['Producto Nombre'].lower()
            if 'vino' in producto_nombre:
                row['Categoría Nombre'] = 'Vino'
                row['Categoría ID'] = 211
            elif 'cerveza' in producto_nombre:
                row['Categoría Nombre'] = 'Cerveza'
                row['Categoría ID'] = 212
            elif 'licor' in producto_nombre or 'whisky' in producto_nombre or 'ron' in producto_nombre or 'vodka' in producto_nombre or 'ginebra' in producto_nombre:
                row['Categoría Nombre'] = 'Licor'
                row['Categoría ID'] = 213
            elif 'cava' in producto_nombre or 'champán' in producto_nombre:
                row['Categoría Nombre'] = 'Cava y Champán'
                row['Categoría ID'] = 214
            else:
                row['Categoría Nombre'] = 'Bebida alcohólica'
                row['Categoría ID'] = 215
            filas.append(row)
    return filas


with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = []

    categorias = [
        (categoria_12, ['salsa', 'ketchup', 'mostaza', 'mayonesa', 'mostaza', 'allioli', 'tomate frito', 'guacamole'], '12'),
        (categoria_18, ['refresco', 'cola', 'limonada', 'naranja', 'tonica', 'sprite', 'fanta', 'pepsi', '7up', 'kas', 'gaseosa', 'malta', 'sunny'], '18'),
        (categoria_15, [], '15'),
        (categoria_13, [], '13'),
        (categoria_9, [], '9'),
        (categoria_19, [], '19'),
        (categoria_8, [], '8'),
        (categoria_3, [], '3'),
        (categoria_7, [], '7'),
        (categoria_4, [], '4'),
        (categoria_17, [], '17'),
        (categoria_14, [], '14'),
        (categoria_1, [], '1'),
        (categoria_6, [], '6'),
        (categoria_2, [], '2'),
        (categoria_5, [], '5'),
        (categoria_16, [], '16'),
        (categoria_11, [], '11'),
        (categoria_10, [], '10')
    ]

    for categoria_func, extra_args, id in categorias:
        infile.seek(0)
        reader = csv.DictReader(infile)
        if extra_args:
            filas = categoria_func(reader, extra_args, id)
        else:
            filas = categoria_func(reader, id)
        rows.extend(filas)

fieldnames = ['Categoría ID', 'Categoría Nombre', 'Producto ID', 'Producto Nombre', 'Precio']

with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
