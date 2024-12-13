<?php

    $csvFile = fopen('/home/francisco/Escritorio/App/categories.csv', 'w');
    fputcsv($csvFile, ['ID', 'Name', 'Parent ID']); // Header row

    ablancodev_get_categories();

    fclose($csvFile);

    function ablancodev_get_categories() {
        global $csvFile;
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://tienda.mercadona.es/api/categories/'); 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
        curl_setopt($ch, CURLOPT_HEADER, 0); 
        $data = curl_exec($ch); 
        curl_close($ch); 

        if ( $data ) {
            $categorias = json_decode($data);
            
            if ( isset($categorias->results) ) {
                foreach ( $categorias->results as $category ) {
                    fputcsv($csvFile, [$category->id, $category->name, '']);

                    // Llamamos a dicha categoría para ver si tiene más niveles
                    ablancodev_get_category($category->id, $category->id);
                }
            }
        }
    }

    function ablancodev_get_category( $category_id, $parent_id ) {
        global $csvFile;
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, 'https://tienda.mercadona.es/api/categories/' . $category_id); 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
        curl_setopt($ch, CURLOPT_HEADER, 0); 
        $data = curl_exec($ch); 
        curl_close($ch); 
        if ( $data ) {
            $category = json_decode($data);
            if ( isset($category->categories) ) {
                foreach ( $category->categories as $cat_info ) {
                    fputcsv($csvFile, [$cat_info->id, $cat_info->name, $parent_id]);

                    // Llamamos a dicha categoría para ver si tiene más niveles
                    ablancodev_get_category($cat_info->id, $cat_info->id);
                }
            }
        }
    }
?>