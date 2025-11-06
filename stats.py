def get_num_words(text):
    split_text = text.split()
    count = 0
    for word in split_text:
        count += 1

    return count

def each_char_count(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] +=1
        else:
            char_dict[lower_char] = 1

    return char_dict


def sorted_char_num(char_num_dict):
    sorted_list = []
    for char in char_num_dict:
        sorted_list.append({"char" : char, "num" : char_num_dict[char]})
    sorted_list.sort(key=lambda x: x["num"], reverse = True)
    return sorted_list
    