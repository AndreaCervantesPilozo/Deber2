from django.contrib import admin

# Register your models here.
<! DOCTYPE html>
<.html >
<cabeza>
    <meta charset="UTF-8">
    <title>Sistemas de Administraciopn de Personas</title>
</cabeza>
<cuerpo>
<h1>Sistemas de Administración de Personas</h1>
<p>Cantidad de personas: {{cantidad}}</p>

{% para persona en personas %}
    <p>{{persona.nombre}}   {{persona.apellido}}    {{persona.email}}</p>

{% endfor %}

<Br>
<Br>
<Br>
<Br>

{% para nombre en nombres_personas %}
    <p>{{nombre}}</p>

{% endfor %}
</cuerpo>
</.html>
