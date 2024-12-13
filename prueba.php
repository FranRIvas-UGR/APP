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
// Crear un array con los IDs de las categorías
$categoryIDs = [];

// Imprimir las categorías disponibles en formato HTML
echo "<h2>Categorías disponibles:</h2>";
echo "<ul>";
foreach ($categories['results'] as $category) {
    echo "<li>ID: " . $category['id'] . " - " . $category['name'] . "</li>";
}
echo "</ul>";

// Paso 2: Obtener productos de la categoría 112,, que está en el archivo producto.json

/* // Leer el cuerpo JSON de la respuesta de la API
$categoryID = 112;
$productUrl = $baseUrl . $categoryID;
$productData = apiRequest($productUrl, $headers);

// Imprimir los productos de la categoría en formato HTML
echo "<h2>Productos de la categoría 112</h2>";
echo "<ul>";
foreach ($productData['categories'] as $product) {
    foreach ($product['products'] as $productInfo) {
        echo "<li>Producto ID: " . $productInfo['id'] . " - " . $productInfo['display_name'] . " - Precio: " . $productInfo['price_instructions']['bulk_price'] . "</li>";
    }
} */

// Paso 3: Obtener los productos de todas las categorías

// Iterar sobre cada ID de categoría y obtener los productos
foreach ($categories['results'] as $category) {
    foreach ($category['categories'] as $subCategory) {
        $categoryIDs[] = $subCategory['id'];
    }
}


foreach ($categoryIDs as $categoryID) {
    $productUrl = $baseUrl . $categoryID;
    $productData = apiRequest($productUrl, $headers);

    echo "<h2>Productos de la categoría $categoryID</h2>";
    echo "<ul>";
    foreach ($productData['categories'] as $product) {
        foreach ($product['products'] as $productInfo) {
            echo "<li>Producto ID: " . $productInfo['id'] . " - " . $productInfo['display_name'] . " - Precio: " . $productInfo['price_instructions']['unit_price'] . "</li>";
        }
    }
    echo "</ul>";
}
?>
