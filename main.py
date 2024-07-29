import os
import getpass
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def main():
    
    os.system('cls')

    option = interface()
    
    while True:

        optional_string = ''

        if option in ['C', 'c']:
            optional_string = create_database()

        if option in ['D', 'd']:
            optional_string = draw_row()

        if option in ['E', 'e']:
            break

        if option in ['S', 's']:
            show_databases()
        
        if option in ['DEL', 'del']:
            optional_string = delete_database()

        option = interface(optional_string)

def delete_database():

    os.system('exit')

    print('            --- AVAILABLE DATABASES ---\n')
    databases_names = os.listdir('data')
    databases_cardinality = len(databases_names)

    if databases_cardinality > 0:

        number_of_lines = databases_cardinality//3
        last_line = databases_cardinality%3

        for i in range(number_of_lines):
            print(f'{databases_names[i*3]:20}{databases_names[i*3+1]:20}{databases_names[i*3+2]:20}')

        for i in range(last_line):
            print(databases_names[i + number_of_lines*3].ljust(20), end='')

        print('\nEnter the name of the database you want to delete')
        print("(or enter 'E' go back to main menu)\n")
        selection = input('Type here: ')

        try:

            file = open('data/' + selection + '.txt', 'r')
            file.close()
            
            os.system('del data\\' + selection + '.txt')

            optional_string = "File '" + selection + "' deleted succesfully!"
            optional_string = Fore.GREEN + optional_string

        except FileNotFoundError:
            optional_string = "File '" + selection + "' does not exist."
            optional_string = Fore.RED + optional_string 
    
    else:
        
        print('There are no databases available :(', end='')

        print('\nPress Enter to continue...', end='')
        getpass.getpass(prompt='')
        

        optional_string = ''

    os.system('cls')

    return optional_string
    

def interface(optional_string=''):
   
    while True:
        
        print('          ---MAIN MENU---')
        print() 
        print("Press 'C' to CREATE a DATABASE")
        print("Press 'D' to DRAW a ROW")
        print("Press 'E' to EXIT the Test Randomizer")
        print("Press 'S' to SHOW your Databases")
        print("Press 'DEL' to DELETE a DATABASE")
        print(Fore.GREEN + optional_string)
        option = input('SELECT AN OPTION: ')

        os.system('cls')

        if option in ['C', 'c', 'D', 'd', 'E', 'e', 'S', 's', 'DEL', 'del']:
            return option

def create_database():
    
    while True:
        try:
            database_name = input('Name your database: ')
            database_address = 'data/' + database_name + '.txt'
            file = open(database_address, 'w')

            while True:
                try:
                    number_of_rows = int(input(f'Type how many rows you want {database_name} to have: '))
                    content = '0'
                    for i in range(number_of_rows - 1):
                        content = content + '0'
                    file.write(content)
                    break
                except:
                    print(f'{Fore.RED}There was an error. Please, try again{Fore.RESET}')

            file.close()
            break

        except ValueError:
            print(Fore.RED + '(Invalid name) ', end = '')
        except FileExistsError:
            print(Fore.RED + '(Name of database already in use. Choose another one)')
        except:
            print(Fore.RED + '(Something went wrong. If the problem persists, please, contact us)')

    
    os.system('cls')

    optional_string = "Database '" + database_name + "' created successfully!"
    return optional_string

def show_databases():
    warning_msg = ''
    while True:
        
        try:
            print('            --- AVAILABLE DATABASES ---\n')
            databases_names = os.listdir('data')
            databases_cardinality = len(databases_names)

            if databases_cardinality > 0:

                number_of_lines = databases_cardinality//3
                last_line = databases_cardinality%3

                for i in range(number_of_lines):
                    print(f'{databases_names[i*3]:20}{databases_names[i*3+1]:20}{databases_names[i*3+2]:20}')

                for i in range(last_line):
                    print(databases_names[i + number_of_lines*3].ljust(20), end='')

                print()
                print(Fore.RED + warning_msg)
                print("Select a Database to see its state by typing its name.\nEnter 'E' to get back to main menu")
                selection = input('Your selection: ')

                if selection in ['E', 'e']:
                   
                    break
                    
                else:
                    
                    os.system('cls')

                    print('STATE OF DATABASE: ' + selection)
                    print()

                    file = open(f'data/{selection}.txt', 'r')
                    file_content = file.read()

                    file_cardinality = len(file_content)
                    number_of_lines = file_cardinality//5
                    last_line = file_cardinality%5

                    for i in range(number_of_lines):

                        list_of_tests = []
                        for j in range(5):

                            if file_content[i*5 + j] == '0':
                                list_of_tests.append(str(1 + i*5 + j) + 'º UNDONE')
                            elif file_content[i*5 + j] == '1':
                                list_of_tests.append(str(1 + i*5 + j) + 'º DONE')

                        print(f'{list_of_tests[0]:13}{list_of_tests[1]:13}{list_of_tests[2]:13}{list_of_tests[3]:13}{list_of_tests[4]:13}')

                    for i in range(number_of_lines*5, number_of_lines*5 + last_line):
                        
                        if file_content[i] == '0':
                            aux_string = str(i + 1) + 'º UNDONE'
                        elif file_content[i] == '1':
                            aux_string = str(i + 1) + 'º DONE'

                        print(aux_string.ljust(13), end='')

                    print()
                
                print('\nPress Enter to continue...', end='')
                getpass.getpass(prompt='')
                os.system('cls')


            else:

                print('There are no databases available :(', end='')

                print('\nPress Enter to continue...', end='')
                getpass.getpass(prompt='')
                break


        except FileNotFoundError:
            os.system('cls')
            warning_msg = 'No Database named ' + selection
        
    os.system('cls')



def draw_row():

    databases_names = os.listdir('data')
    databases_cardinality = len(databases_names)

    sorted_row_value = '1'
    while sorted_row_value == '1':
        sorted_file_id = random.randint(0, databases_cardinality - 1)
        sorted_file_name = databases_names[sorted_file_id]

        file = open(f'data/{sorted_file_name}', 'r')
        content_string = file.read()
        content_list = [content_string[i] for i in range(len(content_string))]
        sorted_row_id = random.randint(0, len(content_list) - 1)
        sorted_row_value = content_list[sorted_row_id]
        file.close()

    content_list[sorted_row_id] = '1'
    new_content_string = ''
    for i in range(len(content_list)):
        new_content_string = new_content_string + content_list[i]

    file = open(f'data/{sorted_file_name}', 'w')
    file.write(new_content_string)
    file.close()
    

    optional_string = Fore.LIGHTBLUE_EX + 'Database Selected: ' + sorted_file_name + '.\nRow Selected: ' + str(sorted_row_id + 1)
    return optional_string

main()