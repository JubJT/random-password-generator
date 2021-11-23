# Random Password Generator

### Random Password Generator:
      Generate a password based on the following conditions.
### Inputs:
      - length : The length of the password.
      - has_alpha : If the password should contain alphabets. [Default : True]
      - case : The case of the alphabets ('m' : Lowercase + Uppercase, 'u' : Uppercase, 'l' : Lowercase) [Default : 'm']
      - has_numeric : If the password should contain numbers. [Default : True] 
      - has_symbols : If the password should contain symbols. [Default : True]
      - exception : A string of character(s) to be excluded in the password. [Default : None]
### Returns:
      - password : The generated based on the conditions provided.
      
## Example:
      Calling the function to return a password with the following conditions:
        - length : 10 
        - has_alpha : True
        - case : 'm'
        - has_numeric : True
        - has_symbols : True
        - exception : '`^*()-+{[}]|\\"\'<,>./'
      
```python 
print(random_password_generator(10,has_alpha=True,case='m',has_num=True,has_symbols=True,exception='`^*()-+{[}]|\\"\'<,>./'))
```
      Sample Output:
        riym:_XH12
