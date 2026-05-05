import os
from funciones import suma, resta, multiplicacion

print("Prueba de funciones:")
print("Suma de 5 y 3:", suma(5, 3))
print("Resta de 10 y 4:", resta(10, 4))

# Creación de la carpeta y un archivo simulado para el paso de gitignore
os.makedirs("resultados", exist_ok=True)
with open("resultados/grafica.png", "w") as f:
    f.write("Archivo de imagen simulado")
print("Se generó un archivo simulado en la carpeta resultados.")