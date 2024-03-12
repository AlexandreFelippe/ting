import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido")

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
            striped_lines = [
                line.strip() for line in lines
            ]
            return striped_lines
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
