from random import randint
def pick_random_word():
    word_list=["ironman","captain america","black widow","hawkeye","hulk","thor","loki","captain marvel","antman","vision","wanda","spiderman","war machine","winter soldier"]
    selected_index=randint(0,len(word_list)-1)
    return word_list[selected_index]
