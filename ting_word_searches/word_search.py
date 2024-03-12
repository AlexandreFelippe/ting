def exists_word(word, instance):
    results = []

    for file_data in instance.data:
        filename = file_data["nome_do_arquivo"]
        occurrences = []

        for index, line in enumerate(file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": index})

        if occurrences:
            results.append({
                "palavra": word.lower(),
                "arquivo": filename,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for file_data in instance.data:
        filename = file_data["nome_do_arquivo"]
        occurrences = []

        for index, line in enumerate(file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": index, "conteudo": line})

        if occurrences:
            results.append({
                "palavra": word.lower(),
                "arquivo": filename,
                "ocorrencias": occurrences
            })
    return results
