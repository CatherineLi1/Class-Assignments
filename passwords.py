# Catherine Li
import zipfile
from itertools import product

def extract_zip(zip_filename, password):
    '''
    Parameter: a string corresponding to a zip filename,
           and a string corresponding to a password.
    Return value: boolean indicating whether the password unlocked the zip file.
    '''
    zip_file = zipfile.ZipFile(zip_filename)
    try: # we will see what "try" and "except" do in a couple weeks :)
        zip_file.extractall(pwd=password.encode())
        return True
    except:
        return False


def get_alphabet_combinations(pass_length):
    '''
    Parameter: an integer corresponding to a password length
    Return value: a list of all possible combinations of the lowercase letters a-z
                  of the given length.
    '''
    return [''.join(pw) for pw in product('qwertyuiopasdfghjklzxcvbnm', repeat=pass_length)]    


def brute_force(zip_filename):
    '''
    Parameter: zip_filename (string)
    Return: None
    Function goes through passwords lengths 1 to 4, a through z
    If correct password is found, print "Password found: x"
    If none found, print "No password found of length z"
    '''
    pass_length = 1
    
    #test for passwords of lengths 1-4
    while pass_length <= 4:
        #all_password_length_i is a list of strings
        all_password_length_i = get_alphabet_combinations(pass_length)
        password_found = False
        for password in all_password_length_i:
            if extract_zip(zip_filename, password):
                #this is true, so password is correct
                password_found = True
                print("Password found:", password)
                return

        #check if password is found for specific length
        if password_found == False:
            print("No password found of length", pass_length)
        pass_length += 1
    print("done")


def dictionary(zip_filename, dict_filename):
    '''
    Parameters: zip_filename, dict_filename (both strings)
    Return: None
    Function should open filename, read the list of words, and open that zip file with each word
    If password is correctm print "Password found: x"
    Else, print "No password found."
    '''
    file_obj = open(dict_filename, 'r')
    
    #check for password
    for line in file_obj:
        x = line.split() #x is a list with one string
        x = x[0] #change x into a string
        
        #check if password is correct
        if extract_zip(zip_filename, x):
            print("Password found:", x)
            file_obj.close()
            return
    
    #if this line is reached, no password is found
    print("No password found.")
    file_obj.close()


def test_password_strength(password, dict_filename):
    '''
    Parameters: password, dict_filename (both strings)
    Return: None
    Function checks if password is susceptible to brute force and dictionary attacks
    If so, prints "Password is susceptible to brute_force attack."
    And/or "Password is susceptible to dictionary attack."
    '''
    #test for brute-force attack
    pass_length = 1
    while pass_length <= 4: #test for passwords of lengths 1-4
        #all_password_length_i is a list of strings
        all_password_length_i = get_alphabet_combinations(pass_length)
        
        #check if password can be found using brute-force
        for element in range(len(all_password_length_i)):
            if password == all_password_length_i[element]:
                print("Password is susceptible to brute-force attack.")
        pass_length += 1

    #test for dictionary attack
    file_obj = open(dict_filename, 'r')
    
    #check for password
    for line in file_obj:
        x = line.split() #x is a list with one string
        x = x[0] #change x into a string
        
        #check if password is correct
        if password == x:
            print("Password is susceptible to dictionary attack.")
            file_obj.close()
            return
    file_obj.close()
    

def menu():
    '''
    Parameter: None
    Return: None
    Function prints introductory messages and list the four options
    User inputs a choice and corresponding option is played
    This is repeated until 4) Exit is chosen
    Note: must include the consequences of unauthorized password usage
    '''
    #code continues forever until user chooses 4) Exit
    while (True):
        print("Welcome to the Passwords Program")
        print("*** \nNote: Under Section 342.1 of the Canadian Criminal Code,")
        print("it is a federal crime in Canada to have unauthorized access to")
        print("password-protected data and usage of said data or password for the")
        print("intent to commit an offence may result in severe consequences.")
        print("The maximum sentence is 10 years of imprisonment.")
        print("Please use the Passwords Program with caution. \n***" )
        
        print("What would you like to do?")
        print("1) Test a password")
        print("2) Find a password for zip file using brute_force")
        print("3) Find a password for zip file using dictionary")
        print("4) Exit")
        option = input("> ")
    
        #test a password
        if option == "1":
            password = input("Enter a password: ")
            dict_filename = input("Enter a dictionary file name: ")
            test_password_strength(password, dict_filename)
        
        #use brute-force
        elif option == "2":
            zip_filename = input("Enter zip file name: ")
            brute_force(zip_filename)
            
        #use dictionary
        elif option == "3":
            zip_filename = input("Enter zip file name: ")
            dict_filename = input("Enter dictionary file name: ")
            dictionary(zip_filename, dict_filename)
            
        #exit program
        elif option == "4":
            print("See ya!")
            break
        
        #check if input is valid
        else:
            print("Invalid input.")
    
        print('----------')


# Please do not alter anything below this line.
if __name__ == '__main__':
    menu()