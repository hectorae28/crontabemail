from datetime import datetime, timedelta


def get_rif_day(calendar_class):
    hoy = datetime.now()
    dia_reporte = hoy + timedelta(days=3)
    calendar = calendar_class.objects.get(mes=dia_reporte.month, year=dia_reporte.year)
    # tramites = Tramite.objects.all()
    for evento in calendar.dias.values():
        for i, declaracion in enumerate(evento):
            if dia_reporte.day in declaracion:
                return i
