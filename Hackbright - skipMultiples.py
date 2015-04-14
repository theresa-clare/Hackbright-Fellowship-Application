import random

# Hackbright Academy application submitted on 02/06/2015

# Hackbright Academy application prompt:
# "Write a function that prints all numbers between 1 and 50, skipping any multples of 7 and
# replacing tem with an inspirational quote of your choosing."

def skipMultiples(x,y,multiple,quotes):
    """Prints all numbers between var x and var y, skipping any multiples of var multiple
    and replacing them with an inspirational quote from the list var quotes"""

    #make sure y is greater of the two numbers
    if x>y:
        temp = y
        y = x
        x = temp
    
    #check if there are enough unique quotes to print
    necessary_quotes = int((y-x)/multiple)
    if len(quotes) < necessary_quotes:
        more_quotes = necessary_quotes - len(quotes)
        print ("You need " + str(more_quotes) + " more quotes in your list of favorite quotes.")
        
    #check if range is large enough to iterate through at least once
    elif y-x == 0 | y-x < multiple:
        print ("Range is not great enough.")
    
    else:
        for i in range(x,y+1):
            if (i%multiple) == 0:
                quote = random.choice(quotes)
                print (quote)
                quotes.remove(quote)
            else:
                print (i)

# list of 17 of favorite quotes for this application instead of opening and reading a .txt file
quotes = [
    "I am the master of my fate; I am the captain of my soul. - William Ernest Henley, Invictus",
    "I am a woman. Phenomenally. Phenomenal Woman, That's me. - Maya Angelou",
    "Intelligence without ambition is a bird without wings. - Salvador Dali",
    "Kintsukuroi - (n) (v.phr.) 'to repair with gold'; the art of repairing pottery with gold or silver lacquer and understanding that the piece is more beautiful for having been broken",
    "Man cannot remake himself without suffering, for he is both the marble and the sculptor. - Alexis Carrel",
    "We are all in the gutter, but some of us are looking at the stars. - Oscar Wilde",
    "Keep your plan as dark as night, and when it's time to strike. Strike like thunder. - Sun Tzu, The Art of War",
    "You have to be odd to be number one. - Dr. Seuss",
    "And the men said that the blood of the stars flowed in her veins. - C.S. Lewis",
    "The moon lives in the lining of your skin. - Pablo Neruda",
    "May your choices reflect your hopes, not your fears. - Nelson Mandela",
    "No one can make you feel inferior without your consent. - Eleanor Roosevelt",
    "For a star to be born, there is one thing that must happen: A gaseous nebula must collapse. So collapse. Crumble. This is not your destruction. This is your birth. - n.t.",
    "Because when I read, I don't really read; I pop a beautiful sentence into my mouth and suck it like a fruit drop, or I sip it like liqueur until the thought dissolves in me like alcohol, infusing brain and heart and coursing on through the veins to the root of each blood vessel. - Bohumil Hrabal, Too Loud a Solitude.",
    "President Obama then said, 'So if you had married him, you would now be the owner of this lovely restaurant,' to which Michelle responded, 'No. If I had married him, he would now be the President.'",
    "Forget stardust - you are iron. Your blood is nothing but ferrous liquid. When you bleed, you reek of dust. It is iron that fills your heart and sits in your veins. And what is iron, really, unless it's forged? You are iron. And you are strong. - n.t.",
    "Everything not saved will be lost. - Nintendo 'Quit Screen' message",
          ]
skipMultiples(1,50,7,quotes)
