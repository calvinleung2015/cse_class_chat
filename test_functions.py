from functions import *
import pytest

def test_show_classes():
    """Tests for the 'show_classes' function."""
    
    # Testing the user does not choose any classes.
    assert show_classes([]) == 0
    
    # Testing the user has chosen some classes.
    assert show_classes(['CSE12', 'CSE30']) == 1
    
def test_end_chat():
    """Tests for the 'end_chat' function."""
    
    # Testing the input is "QUIT"
    assert end_chat("QUIT") == True
    
    # Testing the input is not "QUIT"
    assert end_chat("2") == False

def test_selector():
    """Tests for the 'selector' function."""
    
    # Testing the class is not in the check_list
    assert selector('CSE1', GILLESPIE_IN, GILLESPIE_OUT) == None
    
    # Testing the class is in the check_list and will return a string
    assert isinstance(selector('CSE12', GILLESPIE_IN, GILLESPIE_OUT), str)
