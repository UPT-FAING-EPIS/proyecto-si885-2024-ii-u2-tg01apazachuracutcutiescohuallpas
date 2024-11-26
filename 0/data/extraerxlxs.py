import pandas as pd
import os
from table import create_connection  # Importar la función desde table.py

# Establecer conexión con la base de datos usando la función de table.py
cnxn = create_connection()
cursor = cnxn.cursor()

file_directory = './data'

for i in range(1, 5):
    file_path = os.path.join(file_directory, f'trafico_red_exc_{i}.xlsx')
    
    df = pd.read_excel(file_path, sheet_name='Tráfico de Red')

    df_selected = df[['Fecha', 'Total Enviado (MB)', 'Total Recibido (MB)', 'Total General (MB)', 'IP']]

    df_selected.rename(columns={
        'Fecha': 'fecha',
        'Total Enviado (MB)': 'total_enviado_mb',
        'Total Recibido (MB)': 'total_recibido_mb',
        'Total General (MB)': 'total_mbps',
        'IP': 'ip'
    }, inplace=True)

    df_selected['fecha'] = pd.to_datetime(df_selected['fecha'], errors='coerce')

    df_grouped = df_selected.groupby('ip').agg({
        'total_enviado_mb': 'sum',
        'total_recibido_mb': 'sum',
        'total_mbps': 'sum',
        'fecha': 'first'
    }).reset_index()

    for index, row in df_grouped.iterrows():
        fecha = row['fecha']
        total_enviado_mb = row['total_enviado_mb']
        total_recibido_mb = row['total_recibido_mb']
        total_mbps = row['total_mbps']
        ip = row['ip']

        if pd.isnull(fecha):
            continue

        dia = fecha.strftime('%A')

        cursor.execute("""
            INSERT INTO trafico_red 
            (fecha, ip, dia, total_enviado_mb, total_recibido_mb, total_mbps)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (fecha, ip, dia, total_enviado_mb, total_recibido_mb, total_mbps))

cnxn.commit()

cursor.close()
cnxn.close()

print("Datos insertados correctamente.")
