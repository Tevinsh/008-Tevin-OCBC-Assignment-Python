import math
def convert_celcius_kelvin (fr,to,value):
    '''
    this function is to convert from celcius to kelvin
    :param fr is to declare from. it can be C or K
    :param to is to declare to what you are want to convert. it can be C or K
    :param value is the value of fr it must integer or float or number
    '''
    if (fr == 'C' and to == 'K'):
        print('-------converting Celcius to Kelvin--------')
        print('value :',value,'C')
        result = value + 273.15
        print('result :',"{:.2f}".format(result),'K')
    elif(fr == 'K' and to == 'C'):
        print('-------converting Kelvin to Celcius--------')
        print('value :',value,'K')
        result = value - 273.15
        print('result :',"{:.2f}".format(result),'C')
    else:
        print('wrong input')

convert_celcius_kelvin('K','C',273) #convert from K to C value of K is 273
convert_celcius_kelvin('C','K',32) #convert from C to K value of C is 32

def convert_to_fahrenheit (fr,value):
    '''
    this function is to convert from celcius or kelvin to fahrenheit
    :param fr can be C or K
    :param value is the value of fr
    '''
    if (fr == 'C'):
        print('---------Converting from Celsius to fahrenheit-------')
        print('value:',value,'C')
        result = (value * 9/5)+32
        print('result :',"{:.2f}".format(result),'F')
    elif(fr == 'K'):
        print('---------Converting from Kelvin to fahrenheit-------')
        print('value:',value,'K')
        result = (value-273.15)*9/5+32
        print('result :',"{:.2f}".format(result),'F')
    else:
        print('Invalid Input')

convert_to_fahrenheit('K',2) #convert from kelvin to fahrenheit, value of kelvin is 2
convert_to_fahrenheit('C',27) #convert from Celcius to Fahrenheit, value of Celcius is 27 

def convert_from_fahrenheit_to_celcius_and_kelvin (value):
    '''
    This function is to convert from fahrenheit to celcius and kevin
    :param value is the value of fahrenheit, it must be integer or float or number 
    '''
    kelvin = (value-32)*5/9+273.15
    celcius = (value-32)*5/9
    print('---------converting from fahrenheit to celcius and kelvin---------')
    print('value :',value)
    print('To Kelvin :',"{:.2f}".format(kelvin),'K')
    print('To Celcius',"{:.2f}".format(celcius),'C')

convert_from_fahrenheit_to_celcius_and_kelvin(2)

print(convert_celcius_kelvin.__doc__)
print(convert_to_fahrenheit.__doc__)
print(convert_from_fahrenheit_to_celcius_and_kelvin.__doc__)






