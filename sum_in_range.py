# Sum in range

def input_data():
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num > 0:
                return num
                break
            else:
                print("Input a positive number please")
                print()
        except Exception:
            print("You shall input an integer, not float type or string")
            print()

def sum(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        sum = sum + i
    return sum

if __name__ == '__main__':
    num1 = input_data()
    num2 = input_data()

    print("The sum of range ({}, {}) is {}".format(min(num1,num2), max(num1, num2),sum(min(num1,num2),max(num1,num2))))
