from datetime import datetime, time
import re

def validarFecha(fecha):
    try:
        if fecha != datetime.strptime(fecha, "%d/%m/%Y").strftime('%d/%m/%Y') :
            raise ValueError
        return True
    except ValueError:
        return False


def validarHora(hora):
    timeformat = "%H:%M"
    try:
        if hora != datetime.strptime(hora, timeformat).strftime(timeformat):
            raise ValueError
        return True
    except ValueError:
        return False


def fechaParser(fecha):
    fechaParseada = re.split('/|-',fecha)
    year = int(fechaParseada[2])
    month = int(fechaParseada[1])
    day = int(fechaParseada[0])
    fechaFormateada = datetime(year, month, day).strftime('%d/%m/%Y')
    return fechaFormateada


def horaParser(hora):
    horaParseada = re.split(':',hora)
    hours = int(horaParseada[0])
    minutes = int(horaParseada[1])
    horaFormateada = time(hours,minutes).strftime('%H:%M')
    return horaFormateada


# print(fechaParser('13/06/2022'))
# print(horaParser('10:13'))