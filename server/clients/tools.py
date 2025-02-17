from datetime import datetime, timedelta
from .models import Client, Calendario, Tramite


def get_rif_of_day_report(dia_reporte):
    response = {}
    calendar = Calendario.objects.get(
        mes=dia_reporte.month,
        year=dia_reporte.year,
        tramites__nombre="DECLARACIONES DE IMPUESTO AL VALOR AGREGADO (I.V.A.)",
    )
    for evento in calendar.dias.values():
        for i, declaracion in enumerate(evento):
            if dia_reporte.day in declaracion:
                return i


def get_report_of_rif(rif):
    hoy = datetime.now()
    response = []
    calendar = Calendario.objects.filter(
        mes=hoy.month,
        year=hoy.year,
    )
    for tramite in calendar.values():
        values = list(tramite["dias"].values())
        tramite = Tramite.objects.get(id=tramite["tramites_id"])
        response.append(f"{tramite.nombre}: {values[0][rif][0]} y {values[0][rif][1]}")
        # response[tramite.nombre] = values[0][rif]
    return response
