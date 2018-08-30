#This function allows to fill in the Recipient Country Percentage column in the csv file


def percentage_recipient_country(countries,ID):
    #get an array of #of rows for each activities
    count_ID=[]
    for i in range(len(ID)):
        if(ID[i]!=''):
            j=1
            while(i+j<len(ID) and ID[i+j]==''):
                j=j+1
            count_ID.append(j)
    #setting the countries and the percentage for each activity
    k=0
    percentage=[]
    sorted_countries=[]
    for count in count_ID:
        tab = countries[k:k+count]
        k=k+count
        tab2=set(tab)
        for c in tab2:
            sorted_countries.append(c)
            percent = 0
            for c2 in tab:
                if (c==c2):
                    percent=percent+1
            percent = round(percent/count*100,2)
            percentage.append(percent)
        for i in range(count-len(tab2)):
            sorted_countries.append('')
            percentage.append('')
        #k=k+count
    return (sorted_countries,percentage)
