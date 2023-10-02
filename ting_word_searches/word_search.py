from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance: Queue):
    found_word_process = []
    word = word.lower()
    for data in instance._data:
        has_word = False
        file_lines = data["linhas_do_arquivo"]
        formatted_dict = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index, line in enumerate(file_lines):
            line_lower = line.lower()
            if word in line_lower:
                ocorrencia = {"linha": index + 1}
                formatted_dict["ocorrencias"].append(ocorrencia)
                has_word = True
        if has_word:
            found_word_process.append(formatted_dict)
    return found_word_process


def search_by_word(word, instance: Queue):
    """Aqui irá sua implementação"""


queue = Queue()
process("./statics/nome_pedro.txt", queue)
# process("./statics/arquivo_teste.txt", queue)
print("----------------------")
print(queue._data)

print(exists_word("Pedro", queue))
