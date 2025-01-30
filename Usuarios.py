Usuarios = [
                {
                  "nombre":"Antonio",
                  "Edad": 55,
                  "Sexo": "M",
                  "mail": ["antonio@ejemplo.com"]
                },
                {
                  "nombre":"Pol",
                  "Edad": 18,
                  "Sexo": "M",
                  "mail": ["pol@ejemplo.com"]
                },
                {
                    "nombre":"Marta",
                    "Edad": 32,
                    "Sexo": "F",
                    "mail": ["marta@ejemplo.com"]
                },
                {
                    "nombre":"Juan",
                    "Edad": 25,
                    "Sexo": "M",
                    "mail": ["juan@ejemplo.com"]
                },
                {
                    "nombre":"Ana",
                    "Edad": 65,
                    "Sexo": "F",
                    "mail": ["ana@ejemplo.com"]
                },
                {
                    "nombre":"Faustino",
                    "Edad": 85,
                    "Sexo": "M",
                    "mail": ["faustino@ejemplo.com"]
                }
                ]

def contar_generos(lista_usuarios): #Cuenta numero de hombres y de mujeres
  hombres = sum(1 for u in lista_usuarios if u["Sexo"] == "M")
  mujeres = sum(1 for u in lista_usuarios if u["Sexo"] == "F")
  return {"Hombres": hombres, "Mujeres": mujeres}


def usuarios_aptos_para_socios(lista_usuarios): #Devuelve los usuarios aptos para convertirse en socios
  aptos = [u["nombre"] for u in lista_usuarios if u.get("Edad",0)>50]
  return {"Aptos para socios": aptos}

def mails_menores_35(lista_usuarios): #Devuelve los mails de los usuarios a los que se les asigna una carga de trabajo
  mails = [u["mail"][0] for u in lista_usuarios if u.get("Edad",0)<35]
  return {"Emails para carga de trabajo": mails}

def numero_usuarios(lista_usuarios): #Devuelve el numero de usuarios registrados
  usuarios = sum(1 for a in lista_usuarios)
  return {"Numero de usuarios registrados" : usuarios}

print(contar_generos(Usuarios))
print(usuarios_aptos_para_socios(Usuarios))
print(mails_menores_35(Usuarios))
print(numero_usuarios(Usuarios))