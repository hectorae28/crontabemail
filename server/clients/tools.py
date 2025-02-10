from datetime import datetime, timedelta


def get_rif_of_day_report(calendar_class):
    hoy = datetime.now()
    response = {}
    dia_reporte = hoy + timedelta(days=3)
    calendar = calendar_class.objects.get(
        mes=dia_reporte.month,
        year=dia_reporte.year,
        tramites__nombre="DECLARACIONES DE IMPUESTO AL VALOR AGREGADO (I.V.A.)",
    )
    for evento in calendar.dias.values():
        for i, declaracion in enumerate(evento):
            if dia_reporte.day in declaracion:
                response["end_rif"] = i


def get_report_of_rif(calendar_class):
    hoy = datetime.now()
    # response = {}
    calendar = calendar_class.objects.filter(
        mes=hoy.month,
        year=hoy.year,
    )
    for tramite in calendar.values():
        print(tramite)
        for evento in tramite.dias.values():
            print(evento)
            for i, declaracion in enumerate(evento):
                print(declaracion)
