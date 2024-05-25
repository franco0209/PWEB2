## Determine si una matriz es escalar
def esEscalar(m):
  d = m[0][0]
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          return False
      elif m[i][j] != d:
        print(m[i][j])
        return False
  return True

## Determine si una matriz es unitaria
def esUnitaria(m):
  return m[0][0] == 1 and esEscalar(m)

# Dimensiones de la matriz
# Dimensiones de la matriz
filas2 = 3
columnas2 = 3

# Crear una matriz 3x3 llena de ceros usando comprensión de listas
matriz = [[0 for _ in range(columnas2)] for _ in range(filas2)]

# Imprimir la matriz
print("Matriz 1:")
for fila2 in matriz:
    print(fila2)

#Definición de otra matriz

# Dimensiones de la matriz
filas = 5
columnas = 5
# Crear una matriz 5x5 llena de ceros usando bucles explícitos
matriz2=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        if i==j:
            fila.append(1)
        else:
            fila.append(0)
    matriz2.append(fila)

print("Matriz 2:")
# Imprimir la matriz
for f in matriz2:
    print(f)

print(esUnitaria(matriz))
print(esUnitaria(matriz2))
