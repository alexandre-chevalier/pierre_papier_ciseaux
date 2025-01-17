str = "hello, how are you ? i'm fine thank you"
char = "a"

def compare(str, char):
    i = 0
    c = 0
    for i in str:
        if i == char:
            c += 1
            print(c)
        

compare(str, char)