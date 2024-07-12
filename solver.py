#!/usr/bin/env python3

def solver():
    list_of_sequences = ['No_Found']
    sequence = 4111
    checks = [False, False, False, False, False, False]
    while sequence < 8999:

        sequence = str(sequence)

        skip = False
        if len(set(sequence)) != len(sequence):
            skip = True            
        
        if skip == False:

        
            # Check if First number is larger than the second number.
            if int(sequence[0]) > int(sequence[1]):
                checks[0] = True
            #print(checks)

            # Check if Second number is twice the third number.
            if int(sequence[1]) == int(sequence[2]) * 2:
                checks[1] = True

            # Check if Third number is smaller than the fourth number.
            if int(sequence[2]) < int(sequence[3]):
                checks[2] = True

            # Check if Fourth number is half the first.
            if int(sequence[3]) == int(sequence[0]) / 2:
                checks[3] = True
        

        if checks[0] == True and checks[1] == True and checks[2] == True and checks[3] == True:
            
            print(f'\nSequence {sequence} fulfills the first 5 rules. Checking columns now.')
            
            # Check of the numbers are not in the top row
            counter = 0
            for letter in sequence:
                if letter == "1":
                    counter += 1
                elif letter == "2":
                    counter += 1
                elif letter == "3":
                    counter += 1
            if counter <= 1:
                checks[4] = True
                print(f'Sequence {sequence} fulfills "Three are not in the top row"')
            else:
                print(f'But {sequence} fails the "Three are not in the top row"')
            
            
            
            # Check if the numbers are not in the right colum

            counter = 0
            for letter in sequence:
                if letter == "3":
                    counter += 1
                elif letter == "6":
                    counter += 1
                elif letter == "9":
                    counter += 1
            if counter <= 2:
                checks[5] = True
                print(f'Sequence {sequence} fulfills "Two are not in the right row"')
            else:
                print(f'But {sequence} fails the "Two are not in the right row"')

  
        if checks[0] == True and checks[1] == True and checks[2] == True and checks[3] == True and checks[4] == True and checks[5] == True:  
            if list_of_sequences[0] == 'No_Found':
                list_of_sequences[0] = sequence
            else:
                list_of_sequences.append(sequence)


        # Convert back to int and add 1.

        sequence = int(sequence) + 1

        # Reset checks
        checks = [False, False, False, False, False, False]

    return list_of_sequences









print(f'Possible answer: {solver()}')


quit()



