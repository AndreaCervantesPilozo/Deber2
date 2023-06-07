class Migration(migrations. Migración):

    inicial = Verdadero

    Dependencias = [
    ]

    Operaciones = [
        migraciones. CreateModel(
            name='Persona',
            Campos=[
                ('id', modelos. BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models. CharField(max_length=50)),
                ('apellido', modelos. CharField(max_length=50)),
                ('email', models. CharField(max_length=50)),
                ('activo', models. BooleanField(default=True)),
            ],
        ),
    ]