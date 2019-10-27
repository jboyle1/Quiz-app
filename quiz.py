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