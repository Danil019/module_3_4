def single_root_words(root_word, *other_words):
    words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            words.append(i)
        else:
            pass
    return words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)