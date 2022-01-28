def demo(got):
    print("Jayesh")
    new_got = str.split(got)
    print("Bye")
    return new_got

def getgot():
    print("Hi")
    got = "am"
    print("I")
    return got

def main():
    got = getgot()
    print(got)
    new_got = demo(got)
    print(new_got)

if __name__ == "__main__": 
    main()