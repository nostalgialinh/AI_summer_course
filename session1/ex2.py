alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

#Originally I tried to use string, but it's not mutable (cannot passed by reference).
#Therefore, I used list instead.

def rangoliUlti(sz, cur_char, list):
    if sz == 1:
        list.append(cur_char)
        return
    
    list.append(alphabet[ord(cur_char)-98+sz])
    list.append("-")
    rangoliUlti(sz-1, cur_char,list)
    list.append("-")
    list.append(alphabet[ord(cur_char)-98+sz])


def rangoliOuter(n,sz,cur_char,strlen):
    if sz == n:
        list = []
        rangoliUlti(sz, cur_char, list)
        print("".join(list).center(strlen, "-"))
        return
    
    list = []
    rangoliUlti(sz, alphabet[n-sz], list)
    print("".join(list).center(strlen, "-"))
    list.clear()

    rangoliOuter(n, sz+1, cur_char, strlen)

    rangoliUlti(sz, alphabet[n-sz], list)
    print("".join(list).center(strlen, "-"))


def rangoli(n):
    strlen = 4*n-3
    rangoliOuter(n,1, 'a', strlen)

if __name__ == "__main__":
    n = int(input("Enter a number n:"))
    rangoli(n)

#This version uses recursion to generate the rangoli
#The idea is to generate the rangoli from the outermost layer to the innermost layer
#The idea for this method comes from this problem:
#print the following pattern for n = 10: 10 5 0 5 10
#The code is as follows:
#def printPattern(n):
#    if n == 0:
#        print(n, end=" ")
#        return
#    print(n, end=" ")
#    printPattern(n-5)
#    print(n, end=" ")