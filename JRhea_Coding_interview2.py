

def letter_count(string):

    unique_count = 0

    unique_letters = ""

    for i in string:

        print(i)

        if i not in unique_letters:

            unique_letters = string.isalpha()

            unique_letters = unique_letters + i



        #print(unique_letters)

        unique_count = unique_count + 1


        #print(unique_count)



def main():

    string = "Coding is awesome!"

    letter_count(string)



main()