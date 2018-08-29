#This function allows to delete the replicated rows for any column compare to an array (in our case the ID column)

def delete_replicate(array1, array_replicated):
    for i in range(1,len(array1)):
        if(array1[i]==''):
            array_replicated[i]=''
