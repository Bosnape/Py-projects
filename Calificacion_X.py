# Promedio de Notas

name1 = str(input("Nombre del estudiante: "))
name2 = name1.capitalize()
if "" in name2:
    name2 = name2.strip()

last_name = str(input("Apellido del estudiante: "))
last_name1 = last_name.capitalize()
if "" in last_name1:
    last_name1 = last_name1.strip()

choice = int(input("Presione 1 si va a calificar un periodo \nPresione 2 si va a calificar todo el año\n"))

if choice == 1:
    quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento: "))
    range_of_data = range(1, (quantity_of_data + 1))

    notes = list()

    for every_single_data in range_of_data:
        every_note = float(input("Nota {}: ".format(every_single_data)))
        notes.append(every_note)

    sum1 = sum(notes)

    quantity_of_grades = len(notes)

    exam = float(input("Nota del examen: "))
    if exam == 0:

        # Seguimiento
        p = sum1 / quantity_of_grades
        seguimiento = p * 65 / 100

        # Nota final
        nota_final = float(seguimiento)

        # Name
        name = "{} {}".format(name2, last_name1)

        print("{}, usted tiene un seguimiento de {}%".format(name, nota_final))
    else:
        act = float(input("Nota actitudinal: "))

        # Seguimiento
        p = sum1 / quantity_of_grades
        seguimiento = p * 65 / 100

        # Examen
        ex = exam * 30 / 100

        # Actitudinal
        att = act * 5 / 100

        # Nota final
        nota_final = float(att + ex + seguimiento)

        # Name
        name = "{} {}".format(name2, last_name1)

        if 85.0 <= nota_final <= 100.0:
            print("{0}, FELICIDADES. \nSu calificación es {1}%".format(name, nota_final))
        elif 69.0 <= nota_final <= 84.999:
            print("{0}, usted tiene mas potencial.\nSu calificación es {1}%".format(name, nota_final))
        elif 65.0 <= nota_final <= 68.999:
            print("{0}, usted ha aprobado la materia por poco.\nSu calificación es {1}%".format(name, nota_final))
        else:
            print("{0}, usted no ha aprobado la materia.\nu calificación es {1}%".format(name, nota_final))
x = 1
if choice == 2:
    every_period = list()
    while x <= 3:
        quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento: "))
        range_of_data = range(1, (quantity_of_data + 1))

        notes = list()

        for every_single_data in range_of_data:
            every_note = float(input("Nota {}: ".format(every_single_data)))
            notes.append(every_note)

        sum1 = sum(notes)

        quantity_of_grades = len(notes)

        exam = float(input("Nota del examen: "))

        act = float(input("Nota actitudinal: "))

        # Seguimiento
        p = sum1 / quantity_of_grades
        seguimiento = p * 65 / 100

        # Examen
        ex = exam * 30 / 100

        # Actitudinal
        att = act * 5 / 100

        # Nota final
        nota_final = float(att + ex + seguimiento)

        x += 1
        every_period.append(nota_final)
    print(every_period)
