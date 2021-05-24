def stroki (str1,str2):
    a = str1
    b = str2
    if (type(a)==str and type(b)==str):
        #print('Строка1 и Строка2 является строкой')
        if (str1.lower() == str2.lower()) :
            print('1')
        elif (len(str1) > len(str2) ):
            print('2')
        elif (str2=='learn'):
            print('3')

    else:
        print('0')   
    

stroki('cdef','learn')