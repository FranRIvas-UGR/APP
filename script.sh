#!/bin/bash

# Borrar el archivo de texto si existe
if [ -f logs.txt ]; then
    rm logs.txt
fi

if [ -f lista_productos.html ]; then
    rm lista_productos.html
fi

if [ -f productos.csv ]; then
    rm productos.csv
fi



# Este script ejecuta un programa en PHP y redigire la salida a un archivo de texto

php -f prueba.php > prueba.html