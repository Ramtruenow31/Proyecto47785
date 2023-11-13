
from django.http import HttpResponse


def saludo(request):
	return HttpResponse("Hola Django - Coder")


def saludo_html(request):
	return HttpResponse("<b>Hola Django</b> - Coder")


def saludo_nombre(request, nombre):
	return HttpResponse(f"<h1>{nombre}</h1><br><b>Hola Django</b> - Coder")



def saludo_plantilla(request):
    contexto = {
	  "nombre": "Ram",
	  "edad": 35,
		"mascotas": [
			{
			"nombre": "Loli",
			 "edad": 3
		},
			{
			"nombre": "Mandy"
			"edad" : 10
			}


		]

	}

    return render(request, tample_name: "index.html", contexto)
