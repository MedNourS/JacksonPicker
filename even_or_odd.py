def deductionType(a:str, n:int):
    if "fast" in a.lower():
        return fastDeduction(n)
    elif "slow" in a.lower():
        return slowDeduction(n)
    else:
        raise Exception("No specified type of deduction.")

def fastDeduction(n:int):

    modified_number = abs(n)
    modified_number = [int(x) for x in str(modified_number)]
    if modified_number[-1] in (1, 3, 5, 7, 9):
        return print(f"This number is odd!\n")
    else:
        return print(f"This number is even!\n")

def slowDeduction(n:int):
    i = 0
    while True:
        if n == 2*i:
            return print("This number is even!\n")
            break
        elif n < 2*i:
            return print("This number is odd!\n")
            break
        else:
            i += 1
            print(f"{i}, {2*i}")

def main():
    try:
        number = int(input("What is the number?\n    -> "))
        answer = input("What deduction type do you want? (OPTIONS: SLOW OR FAST)\n    -> ")

        deductionType(answer, number)
    except:
        print("\nTry again!\n")
        main()
    else:
        main()



if __name__ == "__main__":
    main()