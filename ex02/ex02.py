def multiply(*args:int )-> int:
    result=1
    for num in args:
        result*=num
    return result
    
if __name__ == "__main__":
    args=input()
    numbers=[int(x) for x in args.split()]
    print(multiply(*numbers))