"""
Write a simple program that reads a line from the keyboard and outputs the same line where 
every word is reversed. A word is defined as a continuous sequence of alphanumeric characters 
or hyphen ('')
"""
def reverse_word(string):
    import re
    str_list = string.split(' ')
    result = []
    for each in str_list:
        # checking if special character is present in each word
        if not set('[~!@#$%^&*()_+{}":;.\']+$').intersection(each):
            result.append(each[::-1])
        else:
            temp = []
            res = ''
            for index, char in enumerate(list(each)):
                if not temp:
                    temp.append(char)
                elif char in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', ';', '.','/', '[', ']', '$']:
                    temp.insert(index, char)
                    res += ''.join(temp)
                    temp = []
                else:
                    temp.insert(0, char)
            res += ''.join(temp)
            result.append(res)

    print 'Input: %s' %string
    print 'Output: %s' %(' '.join(result))

reverse_word("We are at Ignite Solutions! Their email-id is careers@ignitesol.com")