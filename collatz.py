def collatz(givenNumber):
    if givenNumber % 2 ==0:
        print(int(givenNumber // 2))
        return int(givenNumber // 2)
    elif givenNumber % 2 == 1:
        result = 3 * givenNumber + 1
        print(result)
        return result

n = input('chose a number. ')
while n != 1:
    n = collatz(int(n))




