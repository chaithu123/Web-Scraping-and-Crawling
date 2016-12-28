import webbrowser
import requests,bs4
import pandas as pd
import numpy as np
import re
#enter the CIK OR Ticker for which you want the mutual fund holdings
x=input("enter the cik number or ticker")
#filling string hardcoded as 13F
g="13F"
#running the loop for pages above 100 in websites if exists,limits upto 100 pages
for a in range(0,10000,100):
    f=str(a)
    #requesting html content for this page
    res=requests.get('https://www.sec.gov/cgi-bin/browse-edgar?CIK='+x+'&type=&dateb=&owner=include&start='+f+'&count=100')
    res.raise_for_status()
    noStarchSoup=bs4.BeautifulSoup(res.text)
    ross=noStarchSoup.find_all('tr')
    #creating a list containing table elements
    l=[td.text.strip() for row in ross for td in row.find_all('td')]
    #As formats are different ,to select the perfect break point
    if "Documents" not in l:
        break
    s=l.index("Documents")
    k=l[s-1:]
    chunks = [k[x:x+5] for x in range(0, len(k),5)]
    #creating necessary dataframe which contains raw elements that contain information
    df=pd.DataFrame(chunks)
    juk="Acc-no: "
    jok="("
    #checking for the existence of rows in dataframe
    if(len(df)!=0):
        #deleting the unnecessary columns
        del df[1]
        del df[3]
        del df[4]
        #dropping the rows that contain none values 
        df=df[df[2].str.contains("None") == False]
        #creating the dataframe with neccessary links to traverse
        #using neccessary splitter to get the perfect values
        hip=[]
        for i in range(len(df)):
            hip.append((df[2].iloc[i].split(juk))[1].split(jok)[0].split('\xa0')[0].split(" ")[0])
        df1=pd.DataFrame(hip)
        del df[2]
        df[3]=df1.values
        hep=[]
        #replacing all waste tags to spaces
        for i in range(len(df)):
            hep.append((df[3].iloc[i]).replace("-",""))
        kop=pd.DataFrame(hep)
        df[2]=kop.values
        hop=[]
        for i in range(len(df)):
            hop.append(df[3].iloc[i]+".txt")
        kep=pd.DataFrame(hop)
        del df[3]
        df[3]=kep.values
        y=str(x)
        z=y.strip("0")
        df[1]=z
        lg=[]
        #creation of valid http links that directs to the necessary locations of the files that are to be paresed
        for i in range(len(df)):
            lg.append("https://www.sec.gov/Archives/edgar/data/"+df[1].iloc[i]+"/"+df[2].iloc[i]+"/"+df[3].iloc[i])
        fun=pd.DataFrame(lg)
        df[4]=fun.values
        df.columns=['a','b','c','d','e']
        #Dataframe created with filling,accountnumber,link
        df_final=df[df['a'].str.contains(g)]
        if(len(df_final)!=0):
            tick1=[]
            tick2=[]
            for i in range(len(df_final)):
                res=requests.get(df_final['e'].iloc[i])
                noStarchSoup3=bs4.BeautifulSoup(res.text)
                #checking for the format of 13F,deciding what procedure to use to parse holdings
                if(len(noStarchSoup3.find_all('table'))==0):
                    q1=[]
                    #fetching the value of nameofissuer
                    for i in range(len(noStarchSoup3.find_all('nameofissuer'))):
                        q1.append(str(noStarchSoup3.find_all('nameofissuer')[i]).split(">")[1].split('<')[0])
                        gup1=pd.DataFrame(q1)
                    q2=[]
                    #fetching the value of title of class
                    for i in range(len(noStarchSoup3.find_all('titleofclass'))):
                        q2.append(str(noStarchSoup3.find_all('titleofclass')[i]).split(">")[1].split('<')[0])
                        gup2=pd.DataFrame(q2)
                    q3=[]
                    #fetching the value of Cusip
                    for i in range(len(noStarchSoup3.find_all('cusip'))):
                        q3.append(str(noStarchSoup3.find_all('cusip')[i]).split(">")[1].split('<')[0])
                        gup3=pd.DataFrame(q3) 
                    q4=[]
                    #fetching the value of value
                    for i in range(len(noStarchSoup3.find_all('value'))):
                        q4.append(str(noStarchSoup3.find_all('value')[i]).split(">")[1].split('<')[0])
                        gup4=pd.DataFrame(q4)
                    q5=[]
                    #fetching the value of sshprnamt
                    for i in range(len(noStarchSoup3.find_all('sshprnamt'))):
                        q5.append(str(noStarchSoup3.find_all('sshprnamt')[i]).split(">")[1].split('<')[0])
                        gup5=pd.DataFrame(q5)
                    q6=[]
                    #fetching the value of sshprnamt type
                    for i in range(len(noStarchSoup3.find_all('sshprnamttype'))):
                        q6.append(str(noStarchSoup3.find_all('sshprnamttype')[i]).split(">")[1].split('<')[0])
                        gup6=pd.DataFrame(q6) 
                    q7=[]
                    #fetching the value of investment discretion
                    for i in range(len(noStarchSoup3.find_all('investmentdiscretion'))):
                        q7.append(str(noStarchSoup3.find_all('investmentdiscretion')[i]).split(">")[1].split('<')[0])
                        gup7=pd.DataFrame(q7)  
                    q8=[]
                    #fetching the value of sole
                    for i in range(len(noStarchSoup3.find_all('sole'))):
                        q8.append(str(noStarchSoup3.find_all('sole')[i]).split(">")[1].split('<')[0])
                        gup8=pd.DataFrame(q8) 
                    q9=[]
                    #fetching the value of shared
                    for i in range(len(noStarchSoup3.find_all('shared'))):
                        q9.append(str(noStarchSoup3.find_all('shared')[i]).split(">")[1].split('<')[0])
                        gup9=pd.DataFrame(q9)
                    q10=[]
                    #fetching the value of none
                    for i in range(len(noStarchSoup3.find_all('none'))):
                        q10.append(str(noStarchSoup3.find_all('none')[i]).split(">")[1].split('<')[0])
                        gup10=pd.DataFrame(q10)
                    jik=[]
                    jik=[gup1,gup2,gup3,gup4,gup5,gup6,gup7,gup8,gup9,gup10]
                    #merging all necessary column in a single dataframe
                    for i in range(1,len(jik)):
                        jik[0]=jik[0].merge(jik[i], left_index=True, right_index=True)
                    gif=jik[0]
                    #Dataframe with holding values is created
                    gif.columns=['NameOfIssuer','TitleofClass','Cusip','value','sshprnamt','sshprnamtType','investmentdiscretion','sole','shared','None']
                    tick1.append(gif)

                else:
                    jo=str(noStarchSoup3.find_all('table'))
                    #chopping all the unnecessary strings using regular expressions
                    result1=re.sub("<.*?>","",jo)
                    tick2.append(result1)
            if(len(tick1)!=0):
                #creating multiple files for different pages
                kick=pd.concat(tick1)
                kick.to_csv(r'duck1_%a.txt' %a,sep='\t')
                print(kick)
            with open('duck2_%a.txt' %a, 'w') as f:
                f.writelines(tick2)
        else:
            #handling the exception if documents for that particular CIK not present
            print("No such report documents for that particular CIK")
    else:
        #handling the exception if there are not no entries 
        print("no entries for that cik")
