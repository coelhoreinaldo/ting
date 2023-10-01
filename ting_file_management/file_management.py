import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            file_content = file.read().split("\n")
            return file_content
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


print(txt_importer("/statics/arquivo_teste.txt"))
