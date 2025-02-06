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
    """
    full_calendar = calendar_class.objects.filter(
        mes=dia_reporte.month, year=dia_reporte.year
    )
    response["tramites"] = []
    for full_event in full_calendar:
        for days in full_event.dias.values():
            response["tramites"].append(
                {full_event.tramites.nombre: days[response["end_rif"]]}
            )
        # print(full_event)
    return response
"""
