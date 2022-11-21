def check(key): # check wheather the input is a number or not
    try:
        key=int(key)
        return(key)
    except ValueError:
        key=""  # make "key" an empty string
        return(key)

word=input("enter word: ")
key=(input("enter key: "))
key=check(key)
while key=="": # repeat until input is a number
    key=(input("enter key: "))
    key=check(key)
else:
    while key>25:
        print("Not a valid key,should be in the range 1-25")
        key=int(input("enter key: "))
        key=check(key)
        while key=="": # repeat until input is a number
            key=(input("enter key: "))
            key=check(key)
    else:
        c=0 # character
        count=1 
        change="" # empty veriable
        alphabet="abcdefghijklmnopqrstuvwxyz"
        while count<=len(word):
            if word[c] in alphabet:
                find=alphabet.find(word[c]) #find the character in the alphabet
                shift=int(find)+key # shift character by the key amount
                if shift > 25: # if the shift amount is over 25
                    if find<key: # used two ways to wrap around
                        shift=shift-(key+1) # to wrap around (to make "b" to "a" if the key is "25")
                    else:
                        shift=shift-26 # to wrap around (to make "y" to "b" if the key is "3")
                change=str(change)+alphabet[shift] # add to the empty variable
            else:
                change=str(change)+(word[c])
            count=count+1 # increment counter
            c=c+1 # increment to next character
        print(change)
