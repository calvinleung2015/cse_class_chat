import random
import nltk
import webbrowser


# These lists are the information about the CSE professors and the classes in 2019 winter. 
NO_OFFER_IN = ['CSE3', 'CSE4GS', 'CSE5A', 'CSE6GS', 'CSE42', 'CSE103', 'CSE107', 'CSE112', 'CSE118', 'CSE123', 'CSE125',
              'CSE131', 'CSE132B', 'CSE136', 'CSE143', 'CSE145', 'CSE148', 'CSE150B', 'CSE154', 'CSE156', 'CSE158', 'CSE160',
              'CSE163', 'CSE166', 'CSE168', 'CSE169', 'CSE176A', 'CSE176E', 'CSE180', 'CSE182', 'CSE185', 'CSE190', 'CSE191',
              'CSE193']
NO_OFFER_OUT = ['Sorry, we don\'t offer this class in winter 2019.' ,
               'Sorry, this class may not have offering in winter 2019',
               'Unfortunately, we will not have this class in winter 2019',
               'Unfortunately, this class probably has no offered in winter 2019']

STAFF_IN = ['CSE100', 'CSE101', 'CSE140L', 'CSE150A', 'CSE165', 'CSE167']
STAFF_OUT = ['We are still looking for a staff for this class.',
            'We are looking for a instructor for this class.',
            'The lecturer for this class is going to be announced.',
            'We will announce who is the instructor in this class for you later.']

GILLESPIE_IN = ['CSE12', 'CSE15L', 'CSE95']
GILLESPIE_OUT = ['69% students recommend Professor Gillespie.',
                '93% students recommend this class with Professor Gillespie.',
                '40% students got an A with Professor Gillespie.']

POLITZ_IN = ['CSE8A']
POLITZ_OUT = ['98% students recommend Professor Politz.',
              '95% students recommend this class with Professor Politz.',
              '64% students got an A in this class with Professor Politz.']

CAO_IN = ['CSE30']
CAO_OUT = ['78% students recommend Professor Cao.',
           '85% students recommend this class with Professor Cao.',
           '46% students got an A in this class with Professor Cao.']

SOOSAI_IN = ['CSE8B']
SOOSAI_OUT = ['65% students recommend Professor Soosai.',
              '94% students recommend this class with Professor Soosai.',
             '50% students got an A in this class with Professor Soosai.']

MOSHIRI_IN = ['CSE11']
MOSHIRI_OUT = ['99% students recommend Professor Moshiri.',
              '96% students recommend this class with Professor Moshiri.',
              '60% students got an A in this class with Professor Moshiri.']

MINNES_IN = ['CSE20', 'CSE197']
MINNES_OUT = ['85% students recommend Professor Minnes.',
             '94% students recommend this class with Professor Minnes.',
             '54% students got an A in this class with Professor Minnes.']

KAHNG_IN = ['CSE21']
KAHNG_OUT = ['87% students recommend Professor Kahng.',
            '75 % students recommend this class with Professor Kahng.',
            '55% students got an A in this class with Professor Kahng.']

JONES_IN = ['CSE105']
JONES_OUT = ['80% students recommend Professor Jones.',
            '77% students recommend this class with Professor Jones.',
            '50% students got an A in this class with Professor Jones.']

GRISWOLD_IN = ['CSE110']
GRISWOLD_OUT = ['89% students recommend Professor Griswold',
               '83% students recommend this class with Professor Griswold.',
               '55% students got an A in this class with Professor Griswold.']

PASQUALE_IN = ['CSE120']
PASQUALE_OUT = ['74% students recommend Professor Pasquale',
               '80 % students recommend this class with Professor Pasquale.',
               '48% students got an A in this class with Professor Pasquale.']

PORTER_IN = ['CSE124', 'CSE141', 'CSE141L']
PORTER_OUT = ['84% students recommend this class with Professor Porte.',
              '90% students recommend Professor Porter'
             '50% students got an A in this class with Professor Porte.']

DEIAN_IN = ['CSE127']
DEIAN_OUT = ['76% students recommend Professor Deian.',
            '78% students recommend this class with Professor Deian.',
            '57% students got an A in this class with Professor Deian.']

JHALA_IN = ['CSE130']
JHALA_OUT = ['80% students recommend Professor Jhala.',
            '70% students recommend this class with Professor Jhala.',
            '54% students got an A in this class with Professor Jhala.']

VIANU_IN = ['CSE132A']
VIANU_OUT = ['90% students recommend Professor Vianu.',
            '85% students recommend this class with Professor Vianu.',
            '50% students got an A in this class with Professor Vianu.']

POWELL_IN = ['CSE135']
POWELL_OUT = ['87% students recommend Professor Powell.',
             '80% students recommend this class with Professor Powell.',
             '44% students got an A in this class with Professor Powell.']

ROSING_IN = ['CSE140']
ROSING_OUT = ['92% students recommend Professor Rosing.',
             '87% students recommend this class with Professor Rosing.',
             '47% students got an A in this class with Professor Rosing.']

KRIEGMAN_IN = ['CSE152']
KRIEGMAN_OUT = ['88% students recommend Professor Kriegman.',
               '83% students recommend this class with Professor Kriegman.',
               '54% students got an A in this class with Professor Kriegman.']

KLEMMER_IN = ['CSE170']
KLEMMER_OUT = ['96% students recommend Professor Klemmer.',
              '89% students recommend this class with Professor Klemmer.',
              '47% students got an A in this class with Professor Klemmer.']

PEVZNER_IN = ['CSE181']
PEVZNER_OUT = ['85% students recommend Professor Pevzner',
              '78% students recommend this class with Professor Pevzner.',
              '43% students got an A in this class with Professor Pevzner.']

#I borrow this function from A3 to end chat.
def end_chat(input_string):
    """ End the chat if the user input the word "QUIT".
    
    Parameters
    ----------
    input_string : string
        The input string, to be checked whether it is "QUIT" or not.
        
    Returns
    -------
    True : boolean
        The input string is "QUIT".
    False : boolean
        The input string is not "QUIT".   
    """
    
    if input_string == "QUIT":
        return True
    else:
        return False

def checklist():
    # This webbrowser is about the list of CSE classes.
    url = "https://cse.ucsd.edu/undergraduate/tentative-course-offerings"
    webbrowser.open_new_tab(url)

#I borrow this function from A3 to select an output from the return_list.
def selector(input_string, check_list, return_list):
    """ Select an output from the return_list based on the input_string.
    
    Parameters
    ----------
    input_string : string
        The input string to be checked whether it is in the check_list or not.
    check_list : list
        The list of all possible input strings.
    return_list : list
        The list of all possible output strings.
        
    Returns
    -------
    output : string
        Return the output from the return_list that randomly selected.      
    """
    
    #Initially, there is no output to be assigned.
    output = None
    
    if input_string not in check_list:
        output = None
        
    if input_string in check_list:
        output = random.choice(return_list)
        
    return output  

def choose_classes(chose, msg):
    """ To ask whether the user wants to register for this class.
    
    Parameters
    ----------
    chose : list
        The list of classes that the user has chosen.
    msg : string
        The class that the user wants to register for.
        
    Returns
    -------
    chose : list
        The list contains the new added class.   
    """
    
    msg2 = input("Do you want to choose this class?\n")
    
    if msg2 == "YES":
        #If the user has chosen more than 4 classes,
        #tell the user that they cannot register more than 4 classes.
        if len(chose) == 4:                                                                
            print("Sorry, you have registered 4 classes, you cannot register for this class.")      
        else:
            print("Congratulation! you have registered " + str(msg) + "!")
            chose.append(msg)       
    else:
        return chose
    
def show_classes(chose):
    """ To show the classes that the user has chosen.
    
    Parameters
    ----------
    chose : list
        The list of classes that the user has chosen.   
    """
    
    #If the user has not chosen any classes, 
    #tell the user that they have not chosen any classes.
    if len(chose) == 0:
        print("You haven't chosen any classes.")
        # For testing the if statement will print.
        return 0;
    else:
        print("You have chosen " + ' '.join(chose))
        # For testing the else statement will print.
        return 1; 
    
def remove_class(chose):
    """ To remove the class that the user wants to remove.
    
    Parameters
    ----------
    chose : list
        The list of classes that the user has chosen.
    """
       
    if len(chose) == 0:
        print("You haven't chosen any classes.")
        # For testing this statement will print.
        return 0;
    else:
        cls = input("Which class you want to remove?: ")
    
    #Check whether the user has registered for that class or not.
    for item in chose:
        if cls != item:
            print("You did not register for this class before.")
            # For testing the if statement will print.
            return 1;
        else:
            chose.remove(cls)
            print("You have removed ", cls, ".")
            # For testing the else statement will print.
            return 2;

def cse_class_chat():
    """
    The main function that the user registers for CSE classes. 
    """
    
    #To create the empty list so that the user can add the class into the list if they registered .
    chose = []
    
    #This is a flag that checking whether the user wants to quit the program or not.
    chat = True
    
    #Header message.
    print("Welcome to 2019 CSE course registration service!")
    
    while chat:     
        #To get a message from the user
        msg = input("To choose your classes, just type the class name. " + \
                    "\nTo show checklist, press 2." + \
                    "\nTo show how many classes you have already chosen, press 3: " + \
                    "\nTo remove a class that you chose, press 4: "+ \
                    "\nTo quit, press 'QUIT': \n")
        
        #initially, we have not assigned any output message yet.
        out_msg = None

        if msg in chose:
            print("You have already chosen this class.")
            continue   
            
        elif msg == "2":
            checklist()
            continue    
            
        elif msg == "3":
            show_classes(chose)
            continue      
            
        elif msg == "4":
            remove_class(chose)
            continue      
            
        # Check for an end message.      
        elif end_chat(msg):
            if len(chose) == 0 and chose == []:
                respone = input("You have not chosen any classes, are you sure to quit? 'YES' or 'NO' ")                
                if respone == "YES":
                    out_msg = "Thank you for using 2019 CSE course registration service! Bye!"
                    #End chat
                    chat = False  
                elif respone == "NO":
                    print("Please continue to choose your classes.")
                    continue    
            else:
                out_msg = "You have registered " + str(len(chose)) + " classes: " + ' '.join(chose) + \
                ". Thank you for using 2019 CSE course registration service! Bye!"
                #End chat
                chat = False
                    
        # Check for a selection of CSE classes that we have defined.
        # If the user has picked a class, it will assign to an output message.
        # This is similar to A3 that append the output into outs list.
        if not out_msg:
        
            #This initial list is for appending all output messages, such as None.
            outs = []
        
            outs.append(selector(msg, NO_OFFER_IN, NO_OFFER_OUT))
            outs.append(selector(msg, STAFF_IN, STAFF_OUT))
            outs.append(selector(msg, GILLESPIE_IN, GILLESPIE_OUT))
            outs.append(selector(msg, POLITZ_IN, POLITZ_OUT))
            outs.append(selector(msg, CAO_IN, CAO_OUT))
            outs.append(selector(msg, SOOSAI_IN, SOOSAI_OUT))
            outs.append(selector(msg, MOSHIRI_IN, MOSHIRI_OUT))
            outs.append(selector(msg, MINNES_IN, MINNES_OUT))
            outs.append(selector(msg, KAHNG_IN, KAHNG_OUT))
            outs.append(selector(msg, JONES_IN, JONES_OUT))
            outs.append(selector(msg, MINNES_IN, MINNES_OUT))
            outs.append(selector(msg, GRISWOLD_IN, GRISWOLD_OUT))
            outs.append(selector(msg, PASQUALE_IN, PASQUALE_OUT))
            outs.append(selector(msg, PORTER_IN, PORTER_OUT))
            outs.append(selector(msg, DEIAN_IN, DEIAN_OUT))
            outs.append(selector(msg, JHALA_IN, JHALA_OUT))
            outs.append(selector(msg, VIANU_IN, VIANU_OUT))
            outs.append(selector(msg, POWELL_IN, POWELL_OUT))
            outs.append(selector(msg, ROSING_IN, ROSING_OUT))
            outs.append(selector(msg, KRIEGMAN_IN, KRIEGMAN_OUT))
            outs.append(selector(msg, PEVZNER_IN, PEVZNER_OUT))
        
            #To get the output message and to assign to the option list.
            option = list(filter(None, outs))
            
            #Assign the output string into out_msg if the option list is not empty.
            if option != []:
                out_msg = ' '.join(option)   
        
        #Print a message that the class is not offered in 2019 winter.
        if msg in NO_OFFER_IN:
            print(out_msg)
            continue  
            
        #If the out_msg is still None, that means there is no such a class.    
        if out_msg == None:
            print("Sorry, we do not have '" + str(msg) + "', please give a valid class name.")    
        else:
            print(out_msg)
            
        #To confirm whether the user chooses this class if the class is valid.
        if chat != False and out_msg != None:
            choose_classes(chose, msg)
      
