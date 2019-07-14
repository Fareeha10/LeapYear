def leap(yr):
    if(yr%4==0 | yr%400==0):
       print("Leap Year")
    elif(yr%100==0):
       print("NOT Leap Year")


y=int(input("Enter year to check if its leap:"))
leap(y)
