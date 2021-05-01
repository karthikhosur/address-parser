# Project Design:

# 1. Search for the pin code - re library, either in 5 digit format or 6 digit format. 560-102/560102
#     1. If we find pincode then:
#         1. Store the previous 10 tokens from the current pincode  tokens
#         2. Count the number of words in common_words_addres which are also in the previous 10 tokens
#     2. If we didn’t find a pincode:
#         1. Look For a state name or union term and States in USA-50
#         2. Search for states
#         3. If we don’t find states:
#             1. We look for district or city from city name
#         4. Once we find a district to r city. We will capture last 10 tokens 

import re

text ="When writing an address all on one line or in a sentence,use a comma before the following elements: the apartment or suite number, the city, and the state. It is not necessary to use a comma before the zip code.Her address is 3425 Stone Street, Apt. 2A, Los Angeles, CA 39404."
 
text =text.lower()
text = re.sub(":|\.|,|\/"," ",text)

tokens = text.split()
pincode = ""
us_pincode =""
count = 0
for token in tokens:
    
    if len(token)<8 and len(token)>5:
        if re.search(r"\b\d{3}\s{0,1}\d{3}\b",token):
            ind_pincode =str(re.search(r"\b\d{3}\s{0,1}\d{3}\b",token)[0])
            pincode = ind_pincode

    if len(token)<14 and len(token)>8:
        if re.search(r"\b\d{5}([-+]?\d{4})?\b",token):
            us_pincode=str(re.search(r"\b\d{5}([-+]?\d{4})?\b",token)[0])
            pincode =us_pincode

    if len(token)>4:
        if re.search(r"\b\d{5}\b",token):
            us_zipcode = re.search(r"\b\d{5}\b",token)[0]
            pincode =us_zipcode
    if pincode != "":
        break
    count +=1

common_words_addres = "st|nd|th|main|cross|ave|apt|ward|street|road|apartment"
state_name=""
match_count= 0
print("Pincode:",pincode)
if pincode != "":
    tokens = tokens[count-10:count+1]
    for token in tokens:
        if( re.search(common_words_addres,token)):
           match_count+=1

state_name_index = 0
print(tokens)
for token in tokens:
    if re.search("AL|AZ|AR|CA|CO|CT|DE|FL|GA|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",token.upper()):
        state_name= re.search("AL|AZ|AR|CA|CO|CT|DE|FL|GA|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",token.upper())[0]
    elif re.search("alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|district of columbia|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|maryland|massachusetts|michigan|minnesota|mississippi|missouri|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming",token.lower()):
        state_name =re.search("alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|district of columbia|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|maryland|massachusetts|michigan|minnesota|mississippi|missouri|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming",token.lower())[0]
    if state_name !="":
        break
    state_name_index +=1

try: 
    tokens = tokens[state_name_index-7:state_name_index+2]
except:
    tokens = tokens 

print(state_name)
