from .models import Client, Calendario, Tramite
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .tools import get_rif_of_day_report, get_report_of_rif
from datetime import datetime, timedelta


def test():
    hoy = datetime.now()
    dia_reporte = hoy + timedelta(days=3)
    end_rif = get_rif_of_day_report(hoy)
    print(end_rif)
    reports = get_report_of_rif(end_rif)
    print(f"Report: {reports}")
    clients = Client.objects.filter(rif__endswith=end_rif)
    print(clients.values_list("name", flat=True))


"""
    for i in reports:
        for report in reports.values():
            print(f"{i} {report[0]} {report[1]}")

        clients = Client.objects.filter(rif__endswith=end_rif)
    print(clients.values_list("name", flat=True))
    html_content = render_to_string("report.html")
    email = EmailMessage(
        "Recordatorio",
        html_content,
        "harcher5c@gmail.com",
        list(clients.values_list("email", flat=True)),
    )
    email.content_subtype = "html"
    email.send()
    """


"""

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recordatorio de Pago de Impuestos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background-color: #003366;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .logo {
            max-width: 150px;
            height: auto;
        }
        .content {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
        }
        .button {
            display: inline-block;
            background-color: #003366;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="/placeholder.svg?height=60&width=150" alt="Logo de la Empresa" class="logo">
        <h1>Recordatorio Importante</h1>
    </div>
    <div class="content">
        <p>Estimado cliente,</p>
        <p>Le recordamos que la fecha límite para el pago de sus impuestos está próxima. Es fundamental realizar el pago a tiempo para evitar recargos o sanciones.</p>
        <p>Detalles importantes:</p>
        <ul>
            <li>Fecha límite de pago: [Insertar fecha]</li>
            <li>Monto a pagar: [Insertar monto]</li>
            <li>Método de pago: [Insertar métodos disponibles]</li>
        </ul>
        <p>Si necesita asistencia o tiene alguna pregunta, no dude en contactarnos. Estamos aquí para ayudarle.</p>
        <a href="#" class="button">Ver Detalles de Pago</a>
    </div>
    <div class="footer">
        <p>Este es un correo automático, por favor no responda a este mensaje.</p>
        <p>© 2025 [Nombre de la Empresa de Contaduría]. Todos los derechos reservados.</p>
    </div>
</body>
</html>

    """
