# Script para convertir todas las hojas de un Excel a CSV
import pandas as pd
import os


excel_path = 'data/HND.xlsx'  # Corregida la ruta
output_dir = 'data/'

# Leer todas las hojas
df_dict = pd.read_excel(excel_path, sheet_name=None)

for sheet, df in df_dict.items():
    # Limpiar nombre de la hoja para el archivo
    safe_sheet = sheet.replace(' ', '_').replace('/', '_')
    csv_path = os.path.join(output_dir, f'HND_{safe_sheet}.csv')
    df.to_csv(csv_path, index=False)
    print(f'Guardado: {csv_path}')
