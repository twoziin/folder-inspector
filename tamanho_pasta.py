import os
from datetime import datetime

def get_folder_size(folder_path):
    """Retorna o tamanho total de uma pasta em megabytes e a última modificação."""
    total_size = 0
    latest_mtime = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # Verifica a data de modificação do diretório atual
        dir_mtime = os.path.getmtime(dirpath)
        if dir_mtime > latest_mtime:
            latest_mtime = dir_mtime
            
        # Verifica cada arquivo no diretório atual
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):  # Verifica se é um arquivo
                total_size += os.path.getsize(file_path)
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > latest_mtime:
                    latest_mtime = file_mtime
                    
    return total_size / (1024 * 1024), latest_mtime  # Converte bytes para MB e retorna ambos

def list_folders_with_sizes(main_folder):
    """Lista o tamanho e a última modificação de cada subpasta dentro da pasta principal."""
    if not os.path.exists(main_folder):
        print(f"A pasta {main_folder} não existe ou não está acessível!")
        return

    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        if os.path.isdir(item_path):  # Verifica se é uma subpasta
            folder_size, latest_mtime = get_folder_size(item_path)
            last_modified = datetime.fromtimestamp(latest_mtime).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Pasta: {item} - Tamanho: {folder_size:.2f} MB - Última Modificação: {last_modified}")

# Caminho da pasta principal
main_folder = r"\\CAMINHO ATÉ\SUA PASTA"

list_folders_with_sizes(main_folder)
