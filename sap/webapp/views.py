from django.shortcuts import render

# Create your views here.
webapp
# Crea tus vistas aquí.
Desde Django. Cargador de importación de plantillas

de personas. modelos importar Persona


def bienvenida:
    #return HttpResponse('<! DOCTYPE html><head><title>APP</title></head><body><p>Hola Mundo desde Django</p></body></html>')
    pagina = cargador. get_template('saludo.html')
    return HttpResponse(pagina. hacer())
def hola (request, nombre):
    apellido = petición. GET["apellido"]
    nivel = solicitud. GET["nivel"]
    curso = solicitud. GET["curso"]
    pagina = cargador. get_template('saludo.html')
    nombreCompleto = nombre  + " " + apellido
    datos = {'nombre': nombreCompleto, 'Curso':curso, 'nivel':nivel}

    return HttpResponse(pagina. render(datos, request))

def edad(request,edad):
    pagina = cargador. get_template('edad.html')
    mensaje = {'edad': edad}

    return HttpResponse(pagina. render(mensaje, request))

def mostrar_personas(solicitud):
    cantidad_personas = Persona. objetos. contar()
    personas = Persona. objetos. todos(). valores()


    nombres_personas = lista()
    Para persona en personas:

        nombres_personas. append(persona['nombre'])

    datos = {'cantidad': cantidad_personas, 'personas': personas,'nombres_personas':nombres_personas}
    pagina = cargador. get_template('personas.html')
    return HttpResponse(pagina. render(datos, request))
