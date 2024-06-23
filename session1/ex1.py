from typing import Callable

def minion_game(string: str) -> None:
    vowels = "AEIOU"
    tComb = 0 # total combinations
    vComb = 0 # vowel combinations
    cComb = 0 # consonant combinations
    n = len(string)

    # count the number of combinations
    for i in range(n):
        j = 0
        #j is the next index to evaluate
        while j + i < n:
            tComb += 1
            j += 1
    
    # count the number of vowel combinations
    # explain: let v be a vowel at index i, and length of string is n
    # since anything after v and v itself can form a combination
    # the number of combinations that can be formed start from v is: 1 + [n - (i+1)] = n - i
    for i in range(n):
        if string[i] in vowels:
            vComb += n-i
    
    cComb = tComb - vComb

    if cComb > vComb:
        print(f"An {cComb}")
    elif cComb < vComb:
        print(f"Minh {vComb}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input("Enter a string S:")
    minion_game(s)
