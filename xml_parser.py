import os 
from static import *
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

 
# Folder Path 
path = r"C:/Users/dell/Downloads/2024"
  
# Change the directory 
os.chdir(path) 


# Read xml File 
def read_xml_file(file_path): 
    with open(file_path, 'r',encoding='utf-8-sig') as f: 
        file=f.read()
        return(file)


# generator creation
itr=list(DATA.keys())
def gene():
    for i in itr:
        yield i


# xml parsing function       
def xml_parser(file,fn):
        soup = bs(file,"xml")
        if (soup.ReturnTypeCd.text == '990'):
            # iterates over every attr chaining in attr_chain
            for single_tag in attr_chain:
                #splits each chain in unit attr
                attrs=single_tag.split('.')
                #assign soup object
                currentobj=soup
                #loop for every unit attr in one item of attr_chain
                for attr in attrs:
                    # check if obj is not None type and get the text value if obj not none
                    if currentobj!=None:
                        currentobj=getattr(currentobj,attr,None)
                    # if obj none than value=NAN and we break out of loop
                    else:
                        currentobj=np.NAN
                        result=str(currentobj)
                        break
                # each item's respective value
                result=str(currentobj)
                #using generator to map each vale to respective key of dictionary
                for i in fn:
                    DATA[i].append(result)
                    break
        
        

# iterate through all file            
for file in os.listdir():
    # Check whether file is in text format or not 
    if file.endswith(".xml"): 
        file_path = f"{path}\{file}"
        #call read text file function 
        file=read_xml_file(file_path)
        #initialise generator object for every file
        fn=gene()
        # xml parser fn call for each file
        xml_parser(file,fn)

# dataframe to csv conversion
df=pd.DataFrame(DATA)
df.to_csv('new2024.csv')
        