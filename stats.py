def get_book_text(filename):

    with open(filename) as file_object:

        text= file_object.read()
        return text
    

def count_text(string:str):

    return len(string.split())


def count_chars(character:str):
    
    character = character.lower()
    dictionary = {}

    for i in range(0, len(character)):
        if character[i] in dictionary:
                dictionary[character[i]] += 1
        else:
            dictionary[character[i]] = 1
            
            

    return dictionary

        

def create_report(dictionary:dict):
     
    #create list from dictionary
    list_from_dictionary = []

    

    for i in range(0, len(dictionary.keys())):
        key = [*dictionary.keys()][i]
        if not key.isalpha(): continue
        new_dict = {"character": key, "count": dictionary[key]}
        list_from_dictionary.append(new_dict)
    
    return list_from_dictionary

    


def display_report(list):
    sort_func = lambda x: x["count"]
    copy = list[:]
    copy.sort(key=sort_func, reverse=True)
    print(f"--------- Character Count -------")

    for char in copy:
        print(f"{char["character"]}: {char["count"]}")
    print("============= END ===============")

    


