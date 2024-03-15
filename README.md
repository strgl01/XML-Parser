# XML-Parser <br>
This piece of code parse a number of XML file in a given dirctory and convert data collected from one xml file into one row of a dataframe and repeat the process till all xml file in directory is parsed.<br>
<br>
pre-requisite:<br>
  import os <br>
  from static import *  #importing static.py<br>
  from bs4 import BeautifulSoup as bs   #pip install beautifulsoup4 <br>
  import numpy as np   #pip install numpy<br>
  import pandas as pd   #pip install pandas <br>
<br>
static.py file:<br>
  This file has variable declared.<br>
  variable 'attr_chain' i have stored xml tags as list of strings<br>
  variable DATA is a dictionary which is used to create dataframe<br>

xml_parser.py file:<br>
  This file has the core logic for parsing the xml and is the main file to be run to get the output.<br>
  Added the comment before each code in the file<br>



