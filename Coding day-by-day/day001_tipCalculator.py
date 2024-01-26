import random

print("Welcome to the tip calculator")
# Description hos this program works
print("this program .... ")

try:
    total_bill = float(input("what was the totla bill? $"))
    how_many = int(input("How many people to split the bill? "))
    tip_percentage = float(0)
    #TODO: feature : press "R" to set a random percentage value between 10 to 15 :Done

    tip_percentageStr = input("What percentage tip would you like to give? 10, 12 or 15? or Press 'R' to set a random percentage: ")
    if tip_percentageStr == str("R"):
        tip_percentage = float(random.randrange(100,150)/10)
        print("the tip percentage is set to "+ str(tip_percentage)+"%")
    else:
        try:
            tip_percentage = int (tip_percentageStr)
        except:
            tip_percentage = int (10)
            print(f"there is an error, so we put tip percentage at default value: {tip_percentage}%")

    # tip percentage control:
    while not (tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15 or tip_percentageStr == str("R") ):
        tip_percentageStr = input("\n Warning! You entered the wrong value, Please try again: ")
        if tip_percentageStr == str("R"):
            tip_percentage = float(random.randrange(100,150)/10)
            print("the tip percentage is set to "+ str(tip_percentage)+"%")
        else:
            tip_percentage = int (tip_percentageStr)


    print("Each person shoul pay: " + str ( float(int(10*total_bill * (1 + tip_percentage / 100)/how_many)/10)))
    #TODO: use round feature :Done
except:
    print("unable to execute this code")