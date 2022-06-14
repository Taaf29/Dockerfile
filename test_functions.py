from unittest import result
from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result

def test1_maj ():
    input1="hi" 
    input2="yo"

    expected1=True
    expected2=False

    result1=check_if_maj(input1)
    result2=check_if_maj(input2)
    
    assert expected1==result1
    assert expected2==result2

def test2_special():
    input1="hi sir" 
    input2="yohoho"

    expected1=True
    expected2=False

    result1=check_if_special(input1)
    result2=check_if_special(input2)

    assert expected1==result1
    assert expected2==result2