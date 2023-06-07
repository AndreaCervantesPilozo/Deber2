from django.test import TestCase

# Create your tests here.
class Migration(migrations. Migración):

    inicial = Verdadero

    Dependencias = [
    ]

    Operaciones = [
        migraciones. CreateModel(
            name='Persona',
            Campos=[
                ('id', modelos. BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', modelos. CharField(max_length=50)),
                ('apellido', modelos. CharField(max_length=50)),
                ('email', modelos. CharField(max_length=50)),
                ('activo', modelos. BooleanField(default=True)),
            ],
        ),
    ]
