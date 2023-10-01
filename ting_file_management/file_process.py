from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    curr_file = txt_importer(path_file)
    processed = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(curr_file),
        "linhas_do_arquivo": curr_file,
    }

    already_processed = False
    for process in instance._data:
        if process["nome_do_arquivo"] == processed["nome_do_arquivo"]:
            already_processed = True
            break

    if already_processed:
        return None

    instance.enqueue(processed)
    print(processed)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


instance = Queue()


# if __name__ == "__main__":
#     print(
#         process(
#             "../statics/arquivo_teste.txt",
#             instance,
#         )
#     )
#     print(
#         process(
#             "../statics/arquivo_teste.txt",
#             instance,
#         )
#     )
