# hecho por Alejandro Ospina Blandon

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

mas_alta = nota1
if nota2 > mas_alta:
    mas_alta = nota2
if nota3 > mas_alta:
    mas_alta = nota3
if nota4 > mas_alta:
    mas_alta = nota4
if nota5 > mas_alta:
    mas_alta = nota5

mas_baja = nota1
if nota2 < mas_baja:
    mas_baja = nota2
if nota3 < mas_baja:
    mas_baja = nota3
if nota4 < mas_baja:
    mas_baja = nota4
if nota5 < mas_baja:
    mas_baja = nota5

print(f"\nPromedio: {promedio:.2f}")

if promedio >= 3.0:
    print("Aprobó")
else:
    print("No aprobó")

print(f"Nota más alta: {mas_alta}")
print(f"Nota más baja: {mas_baja}")
