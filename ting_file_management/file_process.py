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


def remove(instance: Queue):
    if instance.is_empty():
        return print("Não há elementos")

    removed_process = instance.dequeue()
    process_name = removed_process["nome_do_arquivo"]
    return print(f"Arquivo {process_name} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     instance = Queue()
#     process("../statics/arquivo_teste.txt", instance)
#     remove(instance)
