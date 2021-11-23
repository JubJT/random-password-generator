#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JubJT
# Created Date: 23/11/2021
# version ='1.0'
# ---------------------------------------------------------------------------
# Imports:
# ---------------------------------------------------------------------------
import string
import secrets

def random_password_generator(length,has_alpha=True,case='m',has_num=True,has_symbols=True,exception=None):
    '''
    * Random Password Generator:
        Generate a password based on the following conditions.
    * Inputs:
        - length : The length of the password.
        - has_alpha : If the password should contain alphabets. [Default : True]
        - case : The case of the alphabets ('m' : Lowercase + Uppercase, 'u' : Uppercase, 'l' : Lowercase) [Default : 'm']
        - has_numeric : If the password should contain numbers. [Default : True] 
        - has_symbols : If the password should contain symbols. [Default : True]
        - exception : A string of characters that should not be included in the password. [Default : None]
    * Returns:
        - password : The generated based on the conditions provided.
    '''
    characters = ''
    password = ''
    
    # Assigns alphabets based on the conditions of 'has_alpha' and 'case' 
    if has_alpha:   
        if case in 'Mm': characters += string.ascii_letters
        elif case in 'Uu':   characters += string.ascii_uppercase
        else:   characters += string.ascii_lowercase
    
    # Assigns numbers based on the conditions of 'has_num' 
    if has_num: characters += string.digits
    
    # Assigns alphabets based on the conditions of 'has_symbols' 
    if has_symbols: characters += '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
    
    # Remove characters based on the characters provided by 'exception'
    if exception != None:
        for char in exception:
            if char in characters:
                characters=characters.replace(char,"")
    
    # Generate password using 'choice' function from 'secrets'. (It randomly 
    # picks a character from 'characters' and repeats the process equivalent to 'length')
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password
