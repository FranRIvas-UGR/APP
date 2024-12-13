<?php

$product_ids = ablancodev_get_categories();
foreach ($product_ids as $product) {
    ablancodev_get_product_details($product);
}

function ablancodev_get_categories() {
    $product_ids = array();
    $url = 'https://tienda.mercadona.es/api/categories/';
    $data = file_get_contents($url);

    if ($data) {
        $categorias = json_decode($data);

        if (isset($categorias->results)) {
            echo '<ul>';
            foreach ($categorias->results as $category) {
                echo '<li><b>ID ' . $category->id . ': ' . $category->name . '</b></li>';
                $product_ids = array_merge($product_ids, ablancodev_get_category($category));
            }
            echo '</ul>';
        } else {
            echo 'No se encontraron resultados en la respuesta de categorías.';
        }
    } else {
        echo 'No se pudo obtener datos del archivo JSON de categorías.';
    }

    return $product_ids;
}

function ablancodev_get_category($category) {
    $product_ids = array();
    if (isset($category->categories) && count($category->categories) > 0) {
        echo '<ul>';
        foreach ($category->categories as $cat_info) {
            echo '<li>ID ' . $cat_info->id . ': ' . $cat_info->name . '</li>';
            $product_ids = array_merge($product_ids, ablancodev_get_category($cat_info));
        }
        echo '</ul>';
    }
    return $product_ids;
}

function ablancodev_get_product_details($product_id) {
    $url = 'https://tienda.mercadona.es/api/categories/' . $product_id;
    $product_data = file_get_contents($url);
    echo '<p>URL: ' . $url . '</p>';

    if ($product_data) {
        $product_details = json_decode($product_data);

        if (isset($product_details->products) && count($product_details->products) > 0) {
            echo '<ul>';
            foreach ($product_details->products as $product) {
                echo '<li>Product ID: ' . $product->id . '</li>';
            }
            echo '</ul>';
        } else {
            echo 'No se encontraron productos en la respuesta de la API.';
        }
    } else {
        echo 'No se pudo obtener datos del producto desde la API.';
    }
}
?>
