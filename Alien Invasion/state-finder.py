print("Welcome to Capitol Finder.")
print("Please enter a zipcode to find")

def enter_zipcode():
    #Allows visitor to input their zipcode
    while True:
        zipcode = input(int)

        if z in zipcode > 5:
            print("Those are two many numbers!")
        if int(zipcode) <5:
            print("Those are not enough numbers! Try again.")
