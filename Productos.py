Productos = [
                {
                  "nombre":"Bistec",
                  "categoria": "Carns",
                  "stock": 20,
                  "proveedor": ["antonio@ejemplo.com"]
                },
                {
                  "nombre":"Mayonesa",
                  "categoria": "Salses",
                  "stock": 40,
                  "proveedor": ["helmans@ejemplo.com"]
                },
                {
                  "nombre":"Patates",
                  "categoria": "Verdures",
                  "stock": 8,
                  "proveedor": ["lays@ejemplo.com"]
                },
                {
                  "nombre":"Cabrales",
                  "categoria": "Formatges",
                  "stock": 10,
                  "proveedor": ["quesos@ejemplo.com"]
                },
                {
                  "nombre":"Llom",
                  "categoria": "Carns",
                  "stock": 50,
                  "proveedor": ["granjaperez@ejemplo.com"]
                }
                ]

def contar_categorias(lista_productos): #cuenta el total que hay en cada categoria
  categorias = {}
  for p in lista_productos:
    cat = p.get("categoria", "otros")
    categorias[cat] = categorias.get(cat, 0) + 1
  return categorias

def productos_para_reposicion(lista_productos): #Mira cuales son los productos que necessitan reposicion
  return {"Reposicion necesaria":[p["nombre"] for p in lista_productos if p.get("stock",0) < 20]}

def mails_proveedores_electronicos(lista_productos): #Devuelve los mails de los proveedores de la categoria electronica
  return{"Proveedores Carns":[p["proveedor"] for p in lista_productos if p.get("categoria") == "Carns"]}

print(contar_categorias(Productos))
print(productos_para_reposicion(Productos))
print(mails_proveedores_electronicos(Productos))