def LS_X(string_input, X):
    """
        Summary and Description of Function:
    
        This function shifts all of the characters of a string by "X" places to the left. 
        The leftmost characters are deleted in replacement of "X" hashtags ("#") to the right.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters shifted in the string.
        
        Returns:
        string_LS (string): The manipulated string done by the LS_X function.
        
        Example:
        LS-4, ELECTRONICS (X = 4, string_input = ELECTRONICS): TRONICS####
    """
    
def RS_X(string_input, X): 
    """
        Summary and Description of Function:
    
        This function shifts all of the characters of a string by "X" places to the right. 
        The rightmost characters are deleted in replacement of "X" hashtags ("#") to the left.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters shifted in the string.
        
        Returns:
        string_RS (string): The manipulated string done by the RS_X function.
        
        Example:
        RS-3, CHAIRS (X = 3, string_input = CHAIRS): ###CHA
    """
    
def LC_X(string_input, X):
    """
        Summary and Description of Function:
    
        This function circulates the leftmost characters to the right-hand side of the string by X characters.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        
        Returns:
        string_LC (string): The manipulated string done by the LC_X function.
        
        Example:
        LC-2, NOTEBOOK (X = 2, string_input = NOTEBOOK): TEBOOKNO
    """
    
def RC_X(string_input, X):
    """
        Summary and Description of Function:
    
        This function circulates the rightmost characters to the left-hand side of the string by X characters.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        
        Returns:
        string_RC (string): The manipulated string done by the RC_X function.
        
        Example:
        RC-5, WHITEBOARD (X = 5, string_input = BLACKBOARD): BOARDBLACK
    """
    
def MC_SLXD(string_input, starting_position, length, X, direction):
    """
        Summary and Description of Function:
    
        This function circulates X characters from starting position S with a length of L, in the direction D.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        X (int): The number of characters circulated in the string.
        length (int): Length of the string being circulated from S.
        starting_position (int): Character starting position.
        direction (string): Direction, right or left (R, L)
        
        Returns:
        string_MC (string): The manipulated string done by the MC_SLXD function.
        
        Example:
        MC_332R, BOXCUTTER (S = 3, string_input = BOXCUTTER, L = 3, X = 3, D = R): "NOT SURE HOW THIS ONE WORKS"
    """
    
def REV_SL(string_input, starting_position, length):
    """
        Summary and Description of Function:
    
        This function reverses the order of the characters starting at position S with a length L.
        
        Parameters: 
        
        string_input (string): The string inserted by the user.
        starting_position (int): Character starting position.
        length (int): The number of characters in the string to be reversed.
        
        
        Returns:
        string_REV (string): The manipulated string done by the REV_SL function.
        
        Example:
        REV_24, PEOPLE (S = 2, L = 4, string_input = PEOPLE): PLPOEE 
    """

def main():                                                                                                                                     # Define the main (the main menu)
    
    
    
    
    
    
           
if __name__ == '__main__':
    main()
