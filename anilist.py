import requests
import json
import objectpath 
from config import variables
# Here we define our query as a multi-line string
query = '''
query  {
Page {
    mediaList (userName: "InDoNax", status: CURRENT) {
      mediaId
      status
    }
  }
}  
'''

# Define our query variables and values that will be used in the query request


url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})

json_string = json.dumps(response.json())

print(json_string)

json_tree = objectpath.Tree(json_string['Page'])

result_tuple = tuple(json_tree.execute('$...mediaID'))

print(result_tuple)