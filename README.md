# Web-Scraping-and-Crawling

            I completed the coding challenge, which you assigned me and was able to parse all the 13F files from "sec.gov" website. In python, I had previous experiences working with data mining and data structures algorithm development, but this coding challenge was new to me and I learnt web crawling. 
Thanks for that.

For parsing the files, there are many commercially packages like sec-edgar, py-edgar, which I didn't use and designed my own algorithm to parse the 13F filling text files.

Please find below the summary of my algorithm: 

1) I found that the files are in the format of
https://www.sec.gov/Archives/edgar/data/1067983/000116655909000072/0001166559-09-000072.txt
which is,
https://www.sec.gov/Archives/edgar/data/’zero stripped CIK’/’account number’/’hyphen separated account number.txt’

2) Using my python codes, I navigated the sec site by using the following URL
'https: //www.sec.gov/cgi-bin/browse-'https://www.sec.gov/cgi-bin/browse-edgar?CIK='+x+'&type=&dateb=&owner=exclude&start='+f+'&count=100'
where, 
         'x' = variable that represents CIK and is given by the user.
         ‘f’  = This is the looping variable and I used it to represent the number of fillings to be extracted per document. The maximum is 1000 and it increases by 100 each time in a loop.
         
3) To get the html content of a particular page, I used a package called requests.

4) After loading the html text into a variable, I applied 'Beautiful Soup' package on top of that. By using this, I got all the tr elements that contains valid information for opening the link.

5)  I stripped all the tags of td elements in the tr element section and made them into a formatted list for representing it in a well-structured data frame. A sample of the dataframe is shown below:

a	b	c	d	e
0	13F-HR	000110465916139781	0001104659-16-139781.txt	1166559	https://www.sec.gov/Archives/edgar/data/116655...
1	13F-HR	000110465916120911	0001104659-16-120911.txt	1166559	https://www.sec.gov/Archives/edgar/data/116655...
2	SC 13G	000110465916106632	0001104659-16-106632.txt	1166559	https://www.sec.gov/Archives/edgar/data/116655...
3	13F-HR	000110465916096636	0001104659-16-096636.txt	1166559	https://www.sec.gov/Archives/edgar/data/116655...
4	SC 13G	000110465915086909	0001104659-15-086909.txt	1166559	https://www.sec.gov/Archives/edgar/data/116655...

6) As you can see from the above data frame, I had extracted pretty much all the information for opening the files.

7) In my code, I used filtering techniques to pull out only the 13F fillings report and the resultant links of the information files.

8) After getting all the links, I used beautiful soup  to filter out the necessary links from the requests.

9) So now after getting the files, I applied webpage parsing techniques and regular expressions to parse the  holdings.

The resultant dataframe which I parsed is shown below:

NameOfIssuer	TitleofClass	Cusip	value	sshprnamt	sshprnamtType	investmentdiscretion	sole	shared	None
0	ARCOS DORADOS HOLDINGS INC	SHS CLASS -A -	G0457F107	14599	3060500	SH	SOLE	3060500	0	0
1	AUTONATION INC	COM	05329W102	89202	1898717	SH	SOLE	1898717	0	0
2	BERKSHIRE HATHAWAY INC DEL	CL B NEW	084670702	9321804	64381548	SH	SOLE	64381548	0	0
3	CANADIAN NATL RY CO	COM	136375102	1011513	17126874	SH	SOLE	17126874	0	0
4	CATERPILLAR INC DEL	COM	149123101	853686	11260857	SH	SOLE	11260857	0	0


10) After this, all the output were written to the tab delimited file, which is named duck*_*.
       Here * represents the file name (0,100,200)

-------------------------------------------------------------------------------------------------------------------------- 
Given goals are below.
Goals:
•	Your code should be able to use any mutual fund ticker. Try morningstar.com or lipperweb.com to find valid tickers.
•	Be sure to check multiple tickers, since the format of the 13F reports can differ.
•	Let us know your thoughts on how to deal with different formats. 

I checked for multiple ciks and tickers from the link ‘https://www.sec.gov/edgar/NYU/cik.coleft.c’ and also from Morningstar.com andlipperweb.com.
As mentioned by you, the formats of 13F reports differed in some links. I saw some having their contents represented in xml and others represented as tables.
So, I had to write different procedures for retrieving the information from different formats by checking specific tags.

Challenges faced:

1.	Multiple pages in the web site.
2.	Reports were in different formats.
3.	Parsing the report of necessary information.

My Idea for parsing multiple formats:
The best way to deal with the problem of parsing multiple formats is by designing a method that can understand different formats by delimiters or regular expressions.
That method should contain several ifelse conditions to deal with problems.
We need to select the strings which conveys whether these strings can parse the incoming string.

Other Challenges I faced is that:
Big data technologies are required to handle large amount of data.
Sometimes system hangs while parsing huge amounts of data.

