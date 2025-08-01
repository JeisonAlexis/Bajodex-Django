import os
import pandas as pd
from django.core.files import File
import django

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_django.settings.local')
django.setup()

from applications.babosas.models import babosas

# Mapeo de tipos y elementos
tipo_map = {
    'Malvada': '1',
    'Elemental': '2',
    'Megamorfica': '3',
    'Guardiana': '4',
    'Extra': '5',
}

elemento_map = {
    'Aire': '1',
    'Tierra': '2',
    'Fuego': '3',
    'Energía': '4',
    'Agua': '5',
    'Desconocido': '6',
}

# Rutas
excel_path = 'Prueba1.xlsx'
protoforma_path = 'media/protoforma/'
transformacion_path = 'media/transformacion/'

# Leer el Excel con dtype para codigoBabosa como string
df = pd.read_excel(excel_path, dtype={'codigoBabosa': str})

# Limpiar espacios en codigoBabosa (por si acaso)
df['codigoBabosa'] = df['codigoBabosa'].str.strip()

# Crear e insertar babosas
for index, row in df.iterrows():
    tipo_codigo = tipo_map.get(str(row['tipoBabosa']).strip(), '6')
    elemento_codigo = elemento_map.get(str(row['elementoBabosa']).strip(), '6')

    babosa = babosas(
        codigoBabosa=row['codigoBabosa'],
        NombreBabosa=row['nombreBabosa'],
        tipoBabosa=tipo_codigo,
        elementoBabosa=elemento_codigo,
    )

    # Protoforma
    protoforma_img = os.path.join(protoforma_path, os.path.basename(str(row['Protoforma'])))
    if os.path.exists(protoforma_img):
        with open(protoforma_img, 'rb') as f:
            babosa.Protoforma.save(os.path.basename(protoforma_img), File(f), save=False)
    else:
        print(f"⚠️ No se encontró Protoforma: {protoforma_img}")

    # Transformación
    transformacion_img = os.path.join(transformacion_path, os.path.basename(str(row['Transformacion'])))
    if os.path.exists(transformacion_img):
        with open(transformacion_img, 'rb') as f:
            babosa.Transformacion.save(os.path.basename(transformacion_img), File(f), save=False)
    else:
        print(f"⚠️ No se encontró Transformacion: {transformacion_img}")

    babosa.save()

print("✅ Todas las babosas fueron insertadas correctamente.")
