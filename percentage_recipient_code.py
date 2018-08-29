def percentage_recipient_country(array):
    array1=[]
    array2=[]
    for i in range(len(array)):
        if(array[i]!=''):
            j=1
            while(i+j<len(array) and array[i+j]==''):
                j=j+1
            array1.append(j)
    for i in range(len(array1)):
        n=100/float(int(array1[i]))
        print(n)
        for j in range(array1[i]):
            array2.append(str(round(n,4)))
    return array2
