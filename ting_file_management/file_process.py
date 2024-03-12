import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_data = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data
    }

    if data not in instance.data:
        instance.enqueue(data)
        print(data)


def remove(instance):
    try:
        removed_item = instance.dequeue()
        print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso\n"
            )
    except IndexError as e:
        print(str(e))


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        sys.stderr.write("Posição inválida")
