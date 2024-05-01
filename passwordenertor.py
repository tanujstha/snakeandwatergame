
import random 
def main():


    char = 'qwertyuiopasdfghjklzxcvbnm1234567890<>?":+_)(*&^%$#@!~))'
   
    ap = ''
    for i in range(12):
        
        ap += random.choice(char)
    print(ap)
main()


# name = ["namrth"]
# tabm = name[:-1]


