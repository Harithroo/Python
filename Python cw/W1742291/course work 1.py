def check(num): # check wheather the input is a number or not
    try:
        num=int(num)
        return(num)
    except ValueError:
        num=""  # make "num" an empty string
        return(num)
# start
count=0
tot=0 #total
max=0
min=100
s1=0 #star line 1
s2=0 #star line 2
s3=0 #star line 3
s4=0 #star line 4
num=(input("enter marks:"))
num=check(num)
while num=="": # repeat until input is a number
    print("invaild")
    num=(input("enter marks:"))
    num=check(num)
else:
    while num>=0: #check if the number is valid
        if num<=100: #check if the number is valid
            if num>max: #check wheather the number is greater than max
                max=num
            if num<min: #check wheather the number is less than mix
                min=num
            count=count+1 # increment counter to count the number of sudents
            tot=tot+num # get a total to calculate average 
            if num>=70:
                s4=s4+1 # increment star line 4
            elif num>=40:
                s3=s3+1 # increment star line 3
            elif num>=30:
                s2=s2+1 # increment star line 2
            else:
                s1=s1+1 # increment star line 1
            num=(input("enter marks:"))
            num=check(num)
            while num=="": # repeat until input is a number
                print("invaild")
                num=(input("enter marks:"))
                num=check(num)
        else:
            print("invaild") # can't have marks higher han 100
            num=(input("enter marks:"))
            num=check(num)
            while num=="": # repeat until input is a number
                print("invaild")
                num=(input("enter marks:"))
                num=check(num)
    print("0-29  : ","*"*s1)
    print("30-39 : ","*"*s2)
    print("40-69 : ","*"*s3)
    print("70-100: ","*"*s4)
    print("Number of students = ",count)
    if count>0: # doesn't print average if no number is given
        print("Average = ",tot/count)
    print("Number of students with a pass mark:",s3+s4)
    print("Highest: ",max)
    print("Lowest: ",min)

# verical
print("") #useed to take a blank line when running
print("Vertical")
print("") #useed to take a blank line when running
print(" 0-29  30-39  40-69  70-100")

m=s1 #to get the longest line
if m<s2:
    m=s2
if m<s3:
    m=s3
if m<s4:
    m=s4
    
for i in range(0,m): # use the longest
    if i<s1:
        print("   *  ",end="")
    else:
        print("      ",end="")
    if i<s2:
        print("   *  ",end="")
    else:
        print("      ",end="")
    if i<s3:
        print("    *  ",end="")
    else:
        print("       ",end="")
    if i<s4:
        print("    *  ",end="")
    else:
        print("       ",end="")
    print("")

        
            
                
