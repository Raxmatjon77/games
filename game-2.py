# -*- coding: utf-8 -*-




import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ""
    print(f" men {len(word)} xonali so'z oyladim topa olasizmi ?(krill alifbosida)")
    # print(word)
    while word_letters:
    
        print(display(user_letters, word))
        if user_letters:
            print(f"siz kititgan harflar {user_letters}")

        letter = input("harf kiriting: ").upper()
        if letter in user_letters:
            print(" bu harfni oldin kiritgansiz , iltimos boshqa harf kirirting")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri.")
        else:
            print("bunday harf yo'q.")
        user_letters += letter
    print(f"tabriklaymiz! {word} so'zini {len(user_letters)} ta urunishda topdingiiz !")


play()
