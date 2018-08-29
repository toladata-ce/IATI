import sys
import csv
import psycopg2
from country_code import country_code
from country_to_region import country_to_region
from compare_date import compare_date
from delete_replicate import delete_replicate
from percentage_recipient_country import percentage_recipient_country

if __name__ == '__main__':

    #Connection to the database
    conn = psycopg2.connect(host="localhost",database="demo", user="postgres", password="postgres")
    cur=conn.cursor()
    #IATI Identifier will need to be taken in input too as a string from the users
    #IATI_Identifier=sys.argv[2]
    IATI_Identifier = 'AA-AAA-123456789'
    #Getting the Org name and adding quotes so the queries can be done as a String
    org = "'"+sys.argv[1]+"'"




    #We query the database to get each column we need for the orgranization
    cur.execute("select a.id from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    ID = [row[0] for row in cur.fetchall()]
    ID2=[]
    #equals to Org Identifier + - + WFL2 ID
    for i in ID:
        ID2.append(IATI_Identifier+'-'+str(i))

    lgth=len(ID2)
    #remove replicated IDs
    for i in reversed(range(1,len(ID2))):
        if(ID2[i]==ID2[i-1]):
            ID2[i]=''


    #No Currencies in "workflow_currency" table
    cur.execute("select c.default_currency_id as currency from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name= {} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    currency = [row[0] for row in cur.fetchall()]

    cur.execute("select a.name as workflowlevel2 from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    WFL2 = [row[0] for row in cur.fetchall()]
    delete_replicate(ID2, WFL2)

    #Description is nearly empty in TolaData so I fill up with dummy data if it is empty as it is a required field
    cur.execute("select a.description as workflowlevel2 from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    description = [row[0] for row in cur.fetchall()]
    for i in range(len(ID2)):
        if(description[i]==''):
            description[i]='add description'+str(i)
    delete_replicate(ID2, description)

    cur.execute("select a.effect_or_impact as workflowlevel2 from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    objectives = [row[0] for row in cur.fetchall()]

    cur.execute("select a.status as workflowlevel2 from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    status = [row[0] for row in cur.fetchall()]


    cur.execute("select to_char(a.expected_start_date, 'YYYY/MM/DD') as actual_date from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    wfl2_start_date = [row[0] for row in cur.fetchall()]


    cur.execute("select to_char(a.expected_end_date, 'YYYY/MM/DD') as end_date from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    wfl2_end_date = [row[0] for row in cur.fetchall()]


    #Giving activity status code there are 6 in total but I tried to give a coherent status code
    status2 = []
    for i in range(len(wfl2_end_date)):
        if((wfl2_end_date[i]!=None) and compare_date(wfl2_end_date[i])):
            status2.append('3')
        elif(status[i]=='green'):
            status2.append('2')
        else:
            status2.append('1')
    delete_replicate(ID2, status2)

    #budget_start_date = wfl2_start_date.copy()
    #budget_end_date = wfl2_end_date.copy()
    budget_start_date = wfl2_start_date
    budget_end_date = wfl2_end_date
    delete_replicate(ID2, wfl2_start_date)
    delete_replicate(ID2, wfl2_end_date)

    cur.execute("select e.role as stakeholder_role from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis'order by a.id".format(org))
    stakeholder_role = [row[0] for row in cur.fetchall()]
    org_role='1'

    cur.execute("select f.name as stakeholder_type from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id left join workflow_stakeholder e on e.id=d.stakeholder_id left join workflow_stakeholdertype f on f.id=e.type_id  where c.name={} and b.name='Humanitarian Response to the Syrian Crisis'order by a.id".format(org))
    stakeholder_type = [row[0] for row in cur.fetchall()]

    cur.execute("select e.name as stakeholder from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id left join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id left join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis'order by a.id".format(org))
    stakeholder = [row[0] for row in cur.fetchall()]


    cur.execute("select f.country from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id join workflow_country f on f.id=e.country_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis'order by a.id".format(org))
    country = [row[0] for row in cur.fetchall()]
    countrycode=[]
    #regioncode=[]
    for c in country:
        countrycode.append(country_code(c))

    percentage_recipient_country = percentage_recipient_country(ID2)

     #for c in country:
    #    regioncode.append(country_to_region(c))


    #policy_marker_vocabulary = '99'
    policy_marker_vocabulary = ''
    #policy_marker_code = '99-RO'
    policy_marker_code = ''

    budget_status=[]
    for i in range(len(ID2)):
        budget_status.append('1')
    delete_replicate(ID2, budget_status)

    cur.execute("select a.total_estimated_budget as budget from workflow_workflowlevel2 a join workflow_workflowlevel1 b on b.id=a.workflowlevel1_id join workflow_organization c on b.organization_id=c.id join workflow_stakeholder_workflowlevel1 d on d.workflowlevel1_id=b.id join workflow_stakeholder e on e.id=d.stakeholder_id where c.name={} and b.name='Humanitarian Response to the Syrian Crisis' order by a.id".format(org))
    budget = [row[0] for row in cur.fetchall()]
    delete_replicate(ID2, budget)

    conn.close()

    #Write the CSV File with the name of the columns from IATI Standard
    counter = 0
    with open('IATI_CSV.csv', 'w') as csvfile:
        #filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter = csv.writer(csvfile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        filewriter.writerow(['Activity Identifier',	 'Activity Default Currency',	 'Activity Default Language',	 'Humanitarian',	 'Activity Title',	 'Activity Description (General)',	 'Activity Description (Objectives)',	 'Activity Description (Target Groups)',	 'Activity Description (Others)',	 'Activity Status',	 'Actual Start Date',	 'Actual End Date',	 'Planned Start Date',	 'Planned End Date',	 'Participating Organisation Role',	 'Participating Organisation Type',	 'Participating Organisation Name',	 'Participating Organisation Identifier',	 'Recipient Country Code',	 'Recipient Country Percentage',	 'Recipient Region Code',	 'Recipient Region Percentage',	 'Sector Vocabulary',	 'Sector Code',	 'Sector Percentage',	 'Policy Marker Vocabulary',	 'Policy Marker Code',	 'Policy Marker Significance',	 'Activity Scope',	 'Budget Type',	 'Budget Status',	 'Budget Period Start',	 'Budget Period End',	 'Budget Value',	 'Budget Value Date',	 'Budget Currency',	 'Related Activity Identifier',	 'Related Activity Type',	 'Contact Type',	 'Contact Organization',	 'Contact Department',	 'Contact Person Name',	 'Contact Job Title',	 'Contact Telephone',	 'Contact Email',	 'Contact Website',	 'Contact Mailing Address'
    ])
        #Fill up the CSV by adding each column
        max_counter = len(ID)
        while counter < max_counter:
            filewriter.writerow((ID2[counter], currency[counter],'','', WFL2[counter],description[counter],objectives[counter],'','',status2[counter],wfl2_start_date[counter],wfl2_end_date[counter],'','',org_role,stakeholder_type[counter],stakeholder[counter],'',countrycode[counter],percentage_recipient_country[counter],'','',policy_marker_vocabulary,policy_marker_code,'','','','','','',budget_status[counter],budget_start_date[counter],budget_end_date[counter],budget[counter],budget_start_date[counter] ))
            counter = counter +1
