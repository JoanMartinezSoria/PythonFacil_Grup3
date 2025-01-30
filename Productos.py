Productos = [
                {
                  "nombre":"Bistec",
                  "categoria": "Carns",
                  "stock": 20,
                  "proveedor": ["antonio@ejemplo.com"],
                  "precio": 15
                },
                {
                  "nombre":"Mayonesa",
                  "categoria": "Salses",
                  "stock": 40,
                  "proveedor": ["helmans@ejemplo.com"],
                  "precio": 6
                },
                {
                  "nombre":"Patates",
                  "categoria": "Verdures",
                  "stock": 8,
                  "proveedor": ["lays@ejemplo.com"],
                  "precio": 5
                },
                {
                  "nombre":"Cabrales",
                  "categoria": "Formatges",
                  "stock": 10,
                  "proveedor": ["quesos@ejemplo.com"],
                  "precio": 3
                },
                {
                  "nombre":"Llom",
                  "categoria": "Carns",
                  "stock": 50,
                  "proveedor": ["granjaperez@ejemplo.com"],
                  "precio":9
                }
                ]

def contar_categorias(lista_productos): #cuenta el total que hay en cada categoria
  categorias = {}
  for p in lista_productos:
    cat = p.get("categoria", "otros")
    categorias[cat] = categorias.get(cat, 0) + 1
  return categorias

def productos_para_reposicion(lista_productos): #Mira cuales son los productos que necessitan reposicion
  return {"Reposicion necesaria":[p["nombre"] for p in lista_productos if p.get("stock") < 20]}

def mails_proveedores(lista_productos,clase): #Devuelve los mails de los proveedores de la categoria electronica
  return{"Proveedores Carns":[p["proveedor"] for p in lista_productos if p.get("categoria") == clase]}

def productos_caros(lista_productos):
  return {"Productos mas caros":[p["nombre"] for p in lista_productos if p.get("precio") > 6]}
  
  
#print(contar_categorias(Productos))
print(productos_para_reposicion(Productos))
#print(mails_proveedores(Productos,"Verdures"))
print(productos_caros(Productos))