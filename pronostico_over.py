# Análisis de OVER 2.5 goles por equipo

partidos = [
    {"equipo": "Palmeiras", "goles": 3},
    {"equipo": "Botafogo", "goles": 2},
    {"equipo": "Mushuc Runa", "goles": 1},
    {"equipo": "Cuenca", "goles": 4}
]

for partido in partidos:
    if partido["goles"] >= 3:
        print(f"{partido['equipo']} es buen candidato a OVER 2.5 ⚽")
    else:
        print(f"{partido['equipo']} con pocos goles, cuidado con el under.")
