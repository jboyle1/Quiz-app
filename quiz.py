#Simple menu function for quiz

def show_menu():
    print('1. Ask questions')
    print('2. Add a question')
    print('3. Exit game')
    
    option = input('Enter option: ')
    return option

#A loop that continues as long as you keep playing the game.

def game_loop():
    while True:
        option = show_menu()
        if option == '1':
            print("You selected 'Ask questions'")
        elif option == '2':
            print("You selected 'Add a question'")
        elif option == '3':
            break
        else :
            print('Invalid option')
        print('')
        
game_loop()

#Add the option to add a question to our file. We want to be prompted for a question and answer, and then we want both of them to be appended to the questions.txt file

def add_question():
    print('')
    question = input('Enter a question\n> ')
    
    print('')
    print('OK then, tell me the answer')
    answer = input('{0}\n '.format(question))
    
#Here I add this to the file. We'll open our questions.txt file for appending using the 'a' access mode flag.
    
    file = open('questions.txt', 'a')
    file.write(question + '\n')
    file.write(answer + '\n')
    file.close()