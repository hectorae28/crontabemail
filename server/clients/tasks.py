from .models import Client, Calendario, Tramite
from datetime import datetime, timedelta
from .tools import get_rif_day


def test():
    end_rif = get_rif_day(Calendario)
    clients = Client.objects.filter(rif__endswith=end_rif)
    print(clients.values_list("email", flat=True))
