import sys


def txt_importer(path_file):
    try:
        if not path_file.lower().endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(path_file, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
    except ValueError as ve:
        print(ve, file=sys.stderr)
        return []
