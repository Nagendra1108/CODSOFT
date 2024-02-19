import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    #print(s1)
    s2 = string.ascii_lowercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    pass_len = int(input("Enter your password length: "))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    #print(s)
    random.shuffle(s)
    #print(s)
    print("Your Password is: ","".join(s[0 : pass_len]))


