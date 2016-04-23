# COS720-Securities
A data science experiment to detect identity deception of online profiles.

## Contributors (Group 14)
Jason Richard Evans - 13032608
Vivian Venter - 13238435

## Technologies
1. Python Backend
2. MongoDB Document Database

## Dependancies
1. pymongo - https://api.mongodb.org/python/current/ 
2. HTMLParser - https://docs.python.org/2/library/htmlparser.html
3. re - https://docs.python.org/2/library/re.html
4. pytagcloud - https://pypi.python.org/pypi/pytagcloud

## Data Import
The following techniques were used to extract the given data from a csv file into MongoDB:
1. Changing the encoding of the file from Latin1 to UTF-8
2. Properly escaping quotation marks ("" instead of \")

## Data Cleaning Techniques
1. Removal of URLs
2. Escaping of HTML Characters
3. Removal of unprintable characters
4. Removal of usernames (mentions)
5. Removal of stopping words
6. Converted all to lowercase

## Possible Removal of Data Columbs
1. Latitude
2. Longitude
3. Retweets
4. Translator
5. isFriend/isFollower

