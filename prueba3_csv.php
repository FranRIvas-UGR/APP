<?php
// Endpoint base para la API de Mercadona
$baseUrl = "https://tienda.mercadona.es/api/categories/";

// Configuración inicial: cabeceras para la solicitud
$headers = [
    'Accept: application/json',
    'Content-Type: application/json'
];

// Función para realizar solicitudes GET a la API
function apiRequest($url, $headers = []) {
    $curl = curl_init();

    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => $headers
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    curl_close($curl);

    if ($httpCode !== 200) {
        die("Error: No se pudo conectar a la API. Código HTTP: $httpCode\n");
    }

    return json_decode($response, true);
}

// Paso 1: Obtener la lista de categorías
$categoriesUrl = $baseUrl;
$categories = apiRequest($categoriesUrl, $headers);

// Abrir un archivo CSV para escribir
$csvFile = fopen('productos.csv', 'w');

// Escribir la cabecera del CSV
fputcsv($csvFile, ['Categoría ID', 'Categoría Nombre', 'Producto ID', 'Producto Nombre', 'Precio']);

// Recorrer las categorías y productos para escribir en el CSV
foreach ($categories['results'] as $category) {
    foreach ($category['categories'] as $subCategory) {
        $categoryID = $subCategory['id'];
        $productUrl = $baseUrl . $categoryID;
        $productData = apiRequest($productUrl, $headers);

        foreach ($productData['categories'] as $product) {
            foreach ($product['products'] as $productInfo) {
                fputcsv($csvFile, [
                    $category['id'],
                    $category['name'],
                    $productInfo['id'],
                    $productInfo['display_name'],
                    $productInfo['price_instructions']['unit_price']
                ]);
            }
        }
    }
}

// Cerrar el archivo CSV
fclose($csvFile);

echo "Datos exportados a productos.csv\n";
?>
