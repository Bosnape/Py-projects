# Proyecto de 12

print("Bienvenido a tu consultorio en linea.")

print("")

nombre_del_paciente = str(input("Primero, ingrese su nombre: "))
nombre_del_paciente1 = nombre_del_paciente.capitalize()
if "" in nombre_del_paciente1:
    nombre_del_paciente1 = nombre_del_paciente1.strip()

apellido_del_paciente = str(input("Ahora, ingrese su apellido: "))
apellido_del_paciente1 = apellido_del_paciente.capitalize()
if "" in apellido_del_paciente1:
    apellido_del_paciente1 = apellido_del_paciente1.strip()

sexo_del_paciente = input("Ingrese su sexo (M/F): ")
sexo_del_paciente1 = sexo_del_paciente.capitalize()
if "" in sexo_del_paciente1:
    sexo_del_paciente1 = sexo_del_paciente1.strip()

if len(sexo_del_paciente1) > 1:
    sexo_del_paciente1 = sexo_del_paciente1.strip(sexo_del_paciente1[1:])

try:
    altura = float(input("Ingrese su estatura (en metros): "))
except ValueError:
    altura = float(input("Ingrese su estatura (en metros), por favor no ingrese letras ni simbolos: "))

try:
    peso = float(input("Ingrese su peso (en kilogramos): "))
except ValueError:
    peso = float(input("Ingrese su peso (en kilogramos), por favor no ingrese letras ni simbolos: "))

# Calcular el IMC
imc = peso / (altura ** 2)

print(imc)

# Name
name = "{} {}".format(nombre_del_paciente1, apellido_del_paciente1)

if 95.0 <= imc <= 100.0:
    print("{0}, FELICIDADES.\nUsted puede eximir.\nSu calificación es {1}%".format(name, imc))
elif 90.0 <= imc <= 94.999:
    print("{0}, estuviste muy cerca.\nNo podrás eximir. ( ´･･)ﾉ(._.`)\nSu calificación es {1}%"
          .format(name, imc ))
elif 70.0 <= imc <= 89.9999:
    print("{0}, puedes mejorar. \nNo podrás eximir. \nSu calificación es {1}%".format(name, imc))
elif 65.0 <= imc <= 69.9999:
    print("{0}, usted por ahora tiene aprobada la materia.\nTenga cuidado. \nSu calificación es {1}%"
          .format(name, imc))
else:
    print("{0}, usted por ahora no tiene aprobada la materia.\nSu calificación es {1}%".format(name, imc))
