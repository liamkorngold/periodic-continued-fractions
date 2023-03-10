import math

# get number
number = int(input("Enter a number to find the periodic continued fraction of that number's square root: "))

# checks if number is a perfect square
if math.floor(math.sqrt(number)) != math.sqrt(number):
    # holds each a term
    sequence = []

    # first a term is floor of the square root of the number
    azero = math.floor(math.sqrt(number))

    # initial values for a, d, and m
    a = 0
    d = 0
    dtemp = 1
    mtemp = 0
    m = 0

    # fraction becomes periodic after a becomes 2 times the first a term
    while a != 2*azero:
        # condition for first time the loop has been run
        if a == 0:
            # appends first a term to array
            sequence.append(azero)
            a = azero
        else:
            # calculating m, d and the next a term
            m = dtemp*a - mtemp
            mtemp = m
            d = (number - m*m)/dtemp
            dtemp = d
            a = math.floor((azero+m)/d)

            # appends the current a term to the array
            sequence.append(a)
        
    # prints the periodic continued fraction
    print(sequence)
else:
    print("That number is a perfect square, so does not have a continued fraction")
