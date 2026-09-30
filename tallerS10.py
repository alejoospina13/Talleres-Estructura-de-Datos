#Alejandro ospina y Jeronimo Granda
class Nodo:
    __slots__ = ("dato", "siguiente")

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


def hacer_cadena(valores):
    """Encadena los valores en ese orden y devuelve el primer nodo."""
    primero = None
    for v in reversed(list(valores)):
        primero = Nodo(v, primero)
    return primero


def largo(nodo):
    if nodo is None:        # caso base
        return 0
    return 1 + largo(nodo.siguiente)

#RETO1
#hubo 4 marcos a la vez en el punto mas hondo
def largo_traza(nodo, nivel=0):
    sangria = "    " * nivel
    dato = "None" if nodo is None else nodo.dato
    print(f"{sangria}entra largo({dato})")
    if nodo is None:
        print(f"{sangria}sale  0   (caso base)")
        return 0
    r = 1 + largo_traza(nodo.siguiente, nivel + 1)
    print(f"{sangria}sale  {r}")
    return r


largo_traza(hacer_cadena([7, 3, 9]))

#RETO2

def suma(nodo):
    # 1. ¿caso más pequeño?  2. ¿cómo se achica?  3. ¿cómo se arma?
    if nodo is None:
        return 0
    return nodo.dato + suma(nodo.siguiente)

def contiene(nodo, x):
    if nodo is None:
        return False
    return nodo.dato == x or contiene(nodo.siguiente, x)


def al_reves(nodo, salida):
    """Deja en la lista salida los datos del último al primero."""
    if nodo is None:
        return
    al_reves(nodo.siguiente, salida)
    salida.append(nodo.dato)
  
#PRUEBA RETO2
c = hacer_cadena([7, 3, 9])
assert suma(c) == 19, "suma de 7, 3 y 9"
assert suma(None) == 0, "la cadena vacía suma 0"
assert contiene(c, 3) and not contiene(c, 5), "contiene: el 3 sí está, el 5 no"
assert not contiene(None, 7), "la cadena vacía no contiene nada"
salida = []
al_reves(c, salida)
assert salida == [9, 3, 7], "al revés"
assert largo(c) == 3, "al_reves no puede tocar la cadena"
print("reto 2: todo bien")

#RETO 3
#Numero obtenido: 998 nodos.
n = 900
while True:
    try:
        largo(hacer_cadena(range(n)))
    except RecursionError:
        break
    n += 1
print("la primera cadena que largo no pudo contar tiene", n, "nodos")

#PRUEBA reto3
#largo iterativo conto un millon
def largo_iterativo(nodo):
    total = 0
    while nodo is not None:
        total += 1
        nodo = nodo.siguiente
    return total
assert largo_iterativo(None) == 0
assert largo_iterativo(hacer_cadena([7, 3, 9])) == 3
assert largo_iterativo(hacer_cadena(range(1_000_000))) == 1_000_000
print("el bucle contó un millón")

#RETO4

prof = {"ahora": 0, "tope": 0}


def largo_medido(nodo):
    prof["ahora"] += 1                              # entra un marco
    prof["tope"] = max(prof["tope"], prof["ahora"])
    if nodo is None:
        r = 0
    else:
        r = 1 + largo_medido(nodo.siguiente)
    prof["ahora"] -= 1                              # sale el marco
    return r


for n in (2, 10, 100, 500):
    prof["ahora"] = prof["tope"] = 0
    largo_medido(hacer_cadena(range(n)))
    print(f"{n:>4} nodos: {prof['tope']:>4} marcos de largo a la vez")

def contiene_medido(nodo, x):
    prof["ahora"] += 1                              
    prof["tope"] = max(prof["tope"], prof["ahora"])
    if nodo is None:
        r = False
    else:
        r = nodo.dato == x or contiene_medido(nodo.siguiente, x)
    prof["ahora"] -= 1                            
    return r
