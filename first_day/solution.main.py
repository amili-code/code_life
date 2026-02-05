def create_dict(order: list[str]) -> dict:
    final_dict = {}
    i = len(order)
    for char in order:
        final_dict.update({char: i})
        i -= 1

    return final_dict


def calc_word(order: dict, word_one: str, word_two) -> str:
    i = 0
    while i < len(word_one):
        if order.get(word_one[i], 0) > order.get(word_two[i], 0):
            return word_one
        elif order.get(word_one[i], 0) < order.get(word_two[i], 0):
            return word_two
        else:
            i += 1

    if len(word_one) > len(word_two):
        return word_one
    else:
        return word_two


def queranumeric(order: list[str], words: list[str]) -> list[str]:
    point_dict = create_dict(order)
    i = 0
    j = 0
    while j < len(words) - 1:
        check = words.copy()
        while i < len(words) - 1:
            result = calc_word(point_dict, words[i], words[i + 1])
            print(words[i], words[i + 1], result)
            if result != words[i]:
                words[i + 1] = words[i]
                words[i] = result
            i += 1
        j += 1
        i = 0
        if words == check:
            break
        print(j , words)

    return words


order = list("cba")
words = ["a", "ba", "cc"]
final_data = queranumeric(order, words)

print(final_data)
