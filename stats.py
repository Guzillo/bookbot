def get_book_text (file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
        
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text_lower_case = text.lower()
    chars = list(text_lower_case)
    char_map = dict()
    for char in chars:
        if(char_map.get(char) != None):
            current_count = char_map[char]
            updated_count = current_count + 1
            char_map[char] = updated_count
        else: 
            char_map[char] = 1
    return char_map
    
def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_named_dicts = []
    for entry in dict:
        list_of_named_dicts.append({"char": entry, "num": dict[entry]})
    list_of_named_dicts.sort(key=sort_on)
    return list_of_named_dicts


