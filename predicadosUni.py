universo = [
    "Diego", "Sandy", "Alain", "Carlos", "Michelle",
    "Adrian", "Sophia", "Selene", "Magaly", "Sebas" ]

estudiantes = set(universo)

carreras = {
    "Diego": "sistemas",
    "Sandy": "aduanas",
    "Alain": "sistemas",
    "Carlos": "quimica",
    "Michelle": "deportes",
    "Adrian": "moda",
    "Sophia": "teatro",
    "Selene": "contabilidad",
    "Magaly": "derecho",
    "Sebas": "gastronomia" }

asistencias = {
    ("Diego", "programacion"),
    ("Sandy", "legislacion"),
    ("Alain", "calculo"),
    ("Carlos", "quimica"),
    ("Michelle", "futbol"),
     ("Adrian", "costura"),
    ("Sophia", "canto"),
    ("Selene", "matematicas"),
    ("Magaly", "leyes"),
    ("Sebas", "comida") }

aprobados = {"Sandy", "Michelle", "Adrian"}
reprobados = {"Alain", "Sophia", "Selene"}

def Estudiante(x):
    return x in estudiantes

def Estudia(x, carrera):
    return carreras.get(x) == carrera

def Asiste(x, materia):
    return (x, materia) in asistencias

def Aprobado(x):
    return x in aprobados

def Reprobado(x):
    return x in reprobados

consultas = [
    ("Estudiante(Diego)", Estudiante("Diego"), True),
    ("Estudiante(Juan)", Estudiante("Juan"), False),

    ("Estudia(Diego, sistemas)", Estudia("Diego", "sistemas"), True),
    ("Estudia(Diego, redes)", Estudia("Diego", "redes"), False),

    ("Asiste(Diego, programacion)", Asiste("Diego", "programacion"), True),
    ("Asiste(Alain, programacion)", Asiste("Alain", "programacion"), False),

    ("Aprobado(Sandy)", Aprobado("Sandy"), True),
    ("Aprobado(Carlos)", Aprobado("Carlos"), False),

    ("Reprobado(Alain)", Reprobado("Alain"), True),
    ("Reprobado(Diego)", Reprobado("Diego"), False),
]

print("CONSULTAS:")
for consulta, resultado, esperado in consultas:
    estado = "CORRECTA" if resultado == esperado else "ERROR"
    print(f"{consulta} -> {resultado} | {estado}")
