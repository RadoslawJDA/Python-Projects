import re
import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.youtube.com/c/Rozziofficial/about"
soup = BeautifulSoup(requests.get(URL).content, "html.parser")

# We locate the JSON data using a regular-expression pattern
data = re.search(r"var ytInitialData = ({.*});", str(soup))

# Uncomment to view all the data
# print(json.dumps(data))

# This converts the JSON data to a python dictionary (dict)
json_data = json.loads(data)

# This is the info from the webpage on the right-side under "stats", it contains the data you want
stats = json_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][5]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"]

print("Channel Views:", stats["viewCountText"]["simpleText"])
print("Joined:", stats["joinedDateText"]["runs"][1]["text"])
