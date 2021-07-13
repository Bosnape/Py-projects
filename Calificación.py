# Promedio de Notas

name1 = str(input("Nombre del estudiante: "))
name2 = name1.capitalize()
if "" in name2:
    name2 = name2.strip()

last_name = str(input("Apellido del estudiante: "))
last_name1 = last_name.capitalize()
if "" in last_name1:
    last_name1 = last_name1.strip()

print("\n1. Saber la nota final de un periodo.")
print("\n2. Saber la nota final del año.")
print("\n3. Saber si usted puede eximir.")

choice = int(input("\nElija algunas de las opciones: "))
print("")

if choice == 1:

    quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento: "))
    range_of_data = range(1, (quantity_of_data + 1))

    notes = list()

    for every_single_data in range_of_data:
        every_note = float(input("Nota {}: ".format(every_single_data)))
        notes.append(every_note)

    sum1 = sum(notes)

    print("Aviso: si colocas 0 en Nota del examén se te calculará el promedio")

    exam = float(input("Nota del examen: "))

    if exam == 0:

        # Seguimiento
        p = sum1 / quantity_of_data
        seguimiento = p

        # Nota final
        nota_final = float(round(seguimiento, 2))

        # Name
        name = "{} {}".format(name2, last_name1)

        print("{}, usted tiene un seguimiento de {}%".format(name, nota_final))
    else:
        act = float(input("Nota actitudinal: "))

        # Seguimiento
        p = sum1 / quantity_of_data
        seguimiento = p * 65 / 100

        # Examen
        ex = exam * 30 / 100

        # Actitudinal
        att = act * 5 / 100

        # Nota final
        nota_final = float(round(att + ex + seguimiento, 2))

        # Name
        name = "{} {}".format(name2, last_name1)

        if 95.0 <= nota_final <= 100.0:
            print("{0}, FELICIDADES. \n Excelente trabajo. \nSu calificación es {1}%".format(name, nota_final))
        elif 85.0 <= nota_final <= 94.9999:
            print("{0}, buen trabajo. \nSu calificación es {1}%".format(name, nota_final))
        elif 70.0 <= nota_final <= 84.9999:
            print("{0}, puedes mejorar. ( ´･･)ﾉ(._.`)\nSu calificación es {1}%".format(name, nota_final))
        elif 65.0 <= nota_final <= 69.9999:
            print("{0}, usted ha aprobado la materia.\nSu calificación es {1}%".format(name, nota_final))
        else:
            print("{0}, usted no ha aprobado la materia.\nu calificación es {1}%".format(name, nota_final))

elif choice == 2:

    every_period = list()

    list_of_periods = ["primer periodo", "segundo periodo", "tercer periodo"]

    for every_string in list_of_periods:

        quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento del {}: ".format(every_string)))
        range_of_data = range(1, (quantity_of_data + 1))

        notes = list()

        for every_single_data in range_of_data:
            every_note = float(input("Nota {}: ".format(every_single_data)))
            notes.append(every_note)

        sum1 = sum(notes)

        exam = float(input("Nota del examen en el {}: ".format(every_string)))

        act = float(input("Nota actitudinal en el {}: ".format(every_string)))

        # Seguimiento
        p = sum1 / quantity_of_data
        seguimiento = p * 65 / 100

        # Examen
        ex = exam * 30 / 100

        # Actitudinal
        att = act * 5 / 100

        # Nota final
        nota_final = float(att + ex + seguimiento)

        every_period.append(nota_final)
        print("\n")

    # Periodo 1
    periodo_1 = every_period[0]
    nota_final_periodo_1 = periodo_1 * 30 / 100

    # Periodo 2
    perido_2 = every_period[1]
    nota_final_periodo_2 = perido_2 * 35 / 100

    # Periodo 3
    periodo_3 = every_period[2]
    nota_final_periodo_3 = periodo_3 * 35 / 100

    nota_def = float(round(nota_final_periodo_1 + nota_final_periodo_2 + nota_final_periodo_3, 2))

    # Name
    name = "{} {}".format(name2, last_name1)

    if 95.0 <= nota_def <= 100.0:
        print("{0}, FELICIDADES.\nExcelente trabajo.\nSu calificación es {1}%".format(name, nota_def))
    elif 85.0 <= nota_def <= 94.999:
        print("{0}, buen trabajo.\nSu calificación es {1}%".format(name, nota_def))
    elif 70.0 <= nota_def <= 84.9999:
        print("{0}, puedes mejorar. ( ´･･)ﾉ(._.`)\nSu calificación es {1}%".format(name, nota_def))
    elif 65.0 <= nota_def <= 69.9999:
        print("{0}, usted ha aprobado la materia.\nSu calificación es {1}%".format(name, nota_def))
    else:
        print("{0}, usted no ha aprobado la materia.\nSu calificación es {1}%".format(name, nota_def))

elif choice == 3:

    pp = float(input("Primer periodo: "))

    if pp == 0.0:

        print("\n")

        every_period = list()

        list_of_periods = ["primer periodo", "segundo periodo"]

        for every_string in list_of_periods:

            quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento del {}: ".format(every_string)))
            range_of_data = range(1, (quantity_of_data + 1))

            notes = list()

            for every_single_data in range_of_data:
                every_note = float(input("Nota {}: ".format(every_single_data)))
                notes.append(every_note)

            sum1 = sum(notes)

            exam = float(input("Nota del examen en el {}: ".format(every_string)))

            act = float(input("Nota actitudinal en el {}: ".format(every_string)))

            # Seguimiento
            p = sum1 / quantity_of_data
            seguimiento = p * 65 / 100

            # Examen
            ex = exam * 30 / 100

            # Actitudinal
            att = act * 5 / 100

            # Nota final
            nota_final = float(att + ex + seguimiento)

            every_period.append(nota_final)
            print("\n")

        quantity_of_data1 = int(input("Ingrese el numero de notas en el seguimiento del tercer periodo: "))
        range_of_data1 = range(1, (quantity_of_data1 + 1))

        notes1 = list()

        for every_single_data in range_of_data1:
            every_note = float(input("Nota {}: ".format(every_single_data)))
            notes1.append(every_note)

        sum2 = sum(notes1)

        # Periodo 1
        periodo_1 = every_period[0]
        nota_final_periodo_1 = periodo_1 * 30 / 100

        # Periodo 2
        perido_2 = every_period[1]
        nota_final_periodo_2 = perido_2 * 35 / 100

        # Periodo 3
        periodo_3 = sum2 / quantity_of_data1
        seguimiento_del_periodo_3 = periodo_3 * 35 / 100

        nota_def = float(round(nota_final_periodo_1 + nota_final_periodo_2 + seguimiento_del_periodo_3, 2))

        # Name
        name = "{} {}".format(name2, last_name1)

        if 95.0 <= nota_def <= 100.0:
            print("{0}, FELICIDADES.\nUsted puede eximir. \nSu calificación es {1}%".format(name, nota_def))
        elif 90.0 <= nota_def <= 94.999:
            print("{0}, estuviste muy cerca.\nNo podrás eximir. ( ´･･)ﾉ(._.`) \nSu calificación es {1}%"
                  .format(name, nota_def))
        elif 70.0 <= nota_def <= 89.9999:
            print("{0}, puedes mejorar. \nNo podrás eximir. \nSu calificación es {1}%".format(name, nota_def))
        elif 65.0 <= nota_def <= 69.9999:
            print("{0}, usted por ahora tiene aprobada la materia.\nTenga cuidado. \nSu calificación es {1}%"
                  .format(name, nota_def))
        else:
            print("{0}, usted por ahora no tiene aprobada la materia.\nSu calificación es {1}%".format(name, nota_def))
    else:
        primer_periodo = pp * 30 / 100

        print("")

        sp = float(input("Segundo periodo: "))

        segundo_periodo = sp * 35 / 100

        print("")

        quantity_of_data = int(input("Ingrese el numero de notas en el seguimiento del tercer periodo: "))
        range_of_data = range(1, (quantity_of_data + 1))

        notes_of_third_period = list()

        for every_single_data in range_of_data:
            every_note = float(input("Nota {}: ".format(every_single_data)))
            notes_of_third_period.append(every_note)

        s = sum(notes_of_third_period)

        promedio_del_tercer_perido = s / quantity_of_data

        tercer_periodo = promedio_del_tercer_perido * 35 / 100

        nota_def = float(round(primer_periodo + segundo_periodo + tercer_periodo, 2))

        # Name
        name = "{} {}".format(name2, last_name1)

        if 95.0 <= nota_def <= 100.0:
            print("{0}, FELICIDADES.\nUsted puede eximir.\nSu calificación es {1}%".format(name, nota_def))
        elif 90.0 <= nota_def <= 94.999:
            print("{0}, estuviste muy cerca.\nNo podrás eximir. ( ´･･)ﾉ(._.`)\nSu calificación es {1}%"
                  .format(name, nota_def))
        elif 70.0 <= nota_def <= 89.9999:
            print("{0}, puedes mejorar. \nNo podrás eximir. \nSu calificación es {1}%".format(name, nota_def))
        elif 65.0 <= nota_def <= 69.9999:
            print("{0}, usted por ahora tiene aprobada la materia.\nTenga cuidado. \nSu calificación es {1}%"
                  .format(name, nota_def))
        else:
            print("{0}, usted por ahora no tiene aprobada la materia.\nSu calificación es {1}%".format(name, nota_def))
