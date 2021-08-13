from game_hangman import read,clear
import random
import time
def main():
    
    words = read()
    num_random = random.randrange(len(words))

    word = words[num_random]
    no_attemps = 0

    selected_word = list(enumerate(word))

    output_word = []
    for i in range(len(word)):
        output_word.append("___")

    clear()
    completed = 1

    while no_attemps<=4:
        print_title()
        print(output_word, end= f"\t\tNumero de intentos: {no_attemps}\n")
        print(word)
        

        letter = input("Ingrese una letra: ")
        if (letter in word):
            for i in range(len(selected_word)):
                print(selected_word[i][0])
                if selected_word[i][1]==letter:
                    output_word[i]= " "+letter+" "
            
            completed+=1
            if completed==len(word):
                print_win()
                break
        
        else:
            no_attemps+=1

        clear()

            
    if no_attemps>=4:
        print_lose()


def print_title():
    print(""" \t\t
         ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █  ███▄    █ 
        ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █  ██ ▀█   █ 
        ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒
        ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒
        ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░
         ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ 
         ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░
         ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░    ░   ░ ░ 
     ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░          ░ 
                                                                                    
""")

def print_lose():
    for i in range(4):
        print("""
                    ▓█████▄▓█████▄▄▄     ▓█████▄     ▐██▌  ▐██▌ 
                    ▒██▀ ██▓█   ▒████▄   ▒██▀ ██▌    ▐██▌  ▐██▌ 
                    ░██   █▒███ ▒██  ▀█▄ ░██   █▌    ▐██▌  ▐██▌ 
                    ░▓█▄   ▒▓█  ░██▄▄▄▄██░▓█▄   ▌    ▓██▒  ▓██▒ 
                    ░▒████▓░▒████▓█   ▓██░▒████▓     ▒▄▄   ▒▄▄  
                     ▒▒▓  ▒░░ ▒░ ▒▒   ▓▒█░▒▒▓  ▒     ░▀▀▒  ░▀▀▒ 
                     ░ ▒  ▒ ░ ░  ░▒   ▒▒ ░░ ▒  ▒     ░  ░  ░  ░ 
                     ░ ░  ░   ░   ░   ▒   ░ ░  ░        ░     ░ 
                       ░      ░  ░    ░  ░  ░        ░     ░    
                     ░                    ░                     
    """)
        time.sleep(0.3)
        clear()
        time.sleep(0.3)


def print_win():
    clear()
    print("""
    ▓██   ██▓▒█████  █    ██     █     █▓█████ ██▀███ ▓█████     ██▓    █    ██ ▄████▄  ██ ▄█▓██   ██▓    ▐██▌  ▐██▌ 
     ▒██  ██▒██▒  ██▒██  ▓██▒   ▓█░ █ ░█▓█   ▀▓██ ▒ ██▓█   ▀    ▓██▒    ██  ▓██▒██▀ ▀█  ██▄█▒ ▒██  ██▒    ▐██▌  ▐██▌ 
      ▒██ ██▒██░  ██▓██  ▒██░   ▒█░ █ ░█▒███  ▓██ ░▄█ ▒███      ▒██░   ▓██  ▒██▒▓█    ▄▓███▄░  ▒██ ██░    ▐██▌  ▐██▌ 
      ░ ▐██▓▒██   ██▓▓█  ░██░   ░█░ █ ░█▒▓█  ▄▒██▀▀█▄ ▒▓█  ▄    ▒██░   ▓▓█  ░██▒▓▓▄ ▄██▓██ █▄  ░ ▐██▓░    ▓██▒  ▓██▒ 
      ░ ██▒▓░ ████▓▒▒▒█████▓    ░░██▒██▓░▒████░██▓ ▒██░▒████▒   ░██████▒▒█████▓▒ ▓███▀ ▒██▒ █▄ ░ ██▒▓░    ▒▄▄   ▒▄▄  
       ██▒▒▒░ ▒░▒░▒░░▒▓▒ ▒ ▒    ░ ▓░▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░░ ▒░ ░   ░ ▒░▓  ░▒▓▒ ▒ ▒░ ░▒ ▒  ▒ ▒▒ ▓▒  ██▒▒▒     ░▀▀▒  ░▀▀▒ 
     ▓██ ░▒░  ░ ▒ ▒░░░▒░ ░ ░      ▒ ░ ░  ░ ░  ░ ░▒ ░ ▒░░ ░  ░   ░ ░ ▒  ░░▒░ ░ ░  ░  ▒  ░ ░▒ ▒░▓██ ░▒░     ░  ░  ░  ░ 
     ▒ ▒ ░░ ░ ░ ░ ▒  ░░░ ░ ░      ░   ░    ░    ░░   ░   ░        ░ ░   ░░░ ░ ░░       ░ ░░ ░ ▒ ▒ ░░         ░     ░ 
 ░ ░        ░ ░    ░            ░      ░  ░  ░       ░  ░       ░  ░  ░    ░ ░     ░  ░   ░ ░         ░     ░    
 ░ ░                                                                       ░              ░ ░                    
""")

if __name__ == '__main__':
    main()
