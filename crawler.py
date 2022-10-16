# IMPORTING REQUIRED LIBRARIES

from urllib import response
import requests
from bs4 import BeautifulSoup

url =  'https://knowthychoice.in/blog'


# GETTING RAW RESPONCE FROM URL 

response = requests.get(url)


# PARSING THE HTML CONTENT WITH BEAUTIFULSOUP

soup = BeautifulSoup(response.content, 'html.parser')



# GETTING ALL PROGRAMS LIST FROM THE HOMEPAGE

programs = soup.find_all('div',attrs = {'class','blog-post-content'})


# CREATING A DICTIONARY TO STORE THE RESULT IN FORMAT : { "PROGRAM_NAME" : [ LIST OF CONCEPTS COVERED ] }
output_dict = {}



# ITERATING THROUGH LIST OF ALL PROGRAMS 

for program in programs :

    # EXTRACTING PROGRAM NAME
    program_name = program.find('a').text


    # EXTRACTING URL OF THE PROGRAM FOR MORE DETAILS
    program_url = program.find('a').get('href')

    # GETTING RAW-RESPONCE FOR A PROGRAM-URL
    program_response = requests.get(program_url)

    # PARSING HTTP RESPONCE
    soup = BeautifulSoup(program_response.content, 'html.parser')

    # GETTING ARTICLE COMPONENT IN PROGRAM PAGE
    article = soup.find('article',attrs = {'class','blog-single-post'})

    # GETTING LIST OF ALL CONEPTS-COVERED LIST COMPONENTS I.E. <li> concept </li>
    concept_covered = article.find_all('ul')[3]
    
    concept_list = []


    # ITERATING THROUGH CONCEPTS-COVERED LIST OF COMPONENTS TO CONVERT TO LIST OF STRINGS

    for  concept in concept_covered :

        # REMOVING EXTRA \n FROM LIST 
        if concept.text == '\n':
            continue

        # ADDING CONCEPTS-COVERED STRING IN concept_list
        
        concept_list.append(concept.text)


    # ADDING KEY-VALUE PAIR { PROGRAM NAME : CONCEPTS-COVERED LIST } IN OUTPUT DICTIONARY

    output_dict[program_name] = concept_list



print(output_dict)
    


    

    

