import os

def read():
    words = []
    with open("./files/data.txt","r",encoding="utf-8") as f:
        for word in f:
            words.append(word)
    words = [i.replace("\n","") for i in words]
    
    return (words)

def clear():
    """
    Clean depends on operating system
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce","int","dos"):
        os.system("cls")
    
