
import string


def count_words(txt):

    special_char_list = ["$", "@", "#", "&", "%", ".", "?", "!", ",", ":" ]
    clean_txt = "".join([str for str in txt.lower() if str not in special_char_list])

    new_list = {str: len(str) for str in clean_txt.split()}
    return (new_list)

 #list_of_words =re.findall(r'\w+', txt)
#list_of_words= ["".join(stri) for stri in txt.lower().split() if  stri.isalpha()]
#list_of_words = [str for str in txt.lower().split()]