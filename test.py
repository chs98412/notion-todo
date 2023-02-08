import requests, json
from json.decoder import JSONDecoder
import notion
from notion.client import NotionClient
from notion.block import *
from notion.collection import *
def readDatabase(pageId, headers):
    
    readUrl = f"https://api.notion.com/v1/databases/"

    
    postdata='''
    {
    "parent": {
        "type": "page_id",
        "page_id": "6f310e7e07a445b292c5635ed77b9984"
    },
  	"cover": {
  		"type": "external",
    	"external": {
    		"url": "https://website.domain/images/image.png"
    	}
  	},
    "is_inline":true,
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Issues",
                "link": null
            }
        }
    ],
    "properties": {
        "Title": {
            "title": {}
        },
        "Description": {
            "select": {
                "options": [
      {
        "name": "Close",
        "color": "red"
      },
      {
        "name": "Open",
        "color": "green"
      }
    ]
            }
        },
    "Issue Number": {
            "checkbox": {}
    },
    "Closed At": {
            "checkbox": {}
    },
    "Related Github Creator": {
            "checkbox": {}
    },
    "Issue Number": {
            "checkbox": {}
    },
    "Created At": {
            "checkbox": {}
    },
    "Assignees": {
            "checkbox": {}
    },
    "Creator": {
            "checkbox": {}
    },
    "Description": {
            "checkbox": {}
    },
    "Related Github Assignees": {
            "checkbox": {}
    },
    "Updated At": {
            "checkbox": {}
    },
    "check": {
            "checkbox": {}
    }
    }
}
    '''
    
    res = requests.post(readUrl, headers=headers ,data=postdata)
    print(res.status_code)
    print(res.content)

    resdata = res.json()
    with open("./db.json", "w", encoding="utf8") as f:
        json.dump(resdata, f, ensure_ascii=False)
        
token = "secret_ol7eQYzAGwz3jq9C7hLrMaPH8e0F7wmScQLnfmw4cZu"

pageId = "6f310e7e07a445b292c5635ed77b9984"

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-06-28",
    "Content-Type":"application/json"
}



#readDatabase(pageId, headers)



def createPage(databaseId, headers, page_values,idx):

    createdUrl = "https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": page_values[idx]
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)

    res = requests.post(createdUrl, headers=headers, data=data)

    print(res.status_code)


databaseId = "fe0474733b3940ab8696b567210e6baf"

# page_values = {
#     'Title': 'Hyuk',
#     'Assignees': True
# }

def getissues():
    headers = {
    "Authorization": "Bearer " + "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",
    "Notion-Version": "2022-06-28",
    "Content-Type":"application/json"
    }
    res=requests.get("https://api.github.com/issues", headers=headers)
    page_values=[]
    for i in res.json():
        page_values.append(i["title"])
    return page_values
page_values=getissues()

for i in range(len(page_values)):
    createPage(databaseId, headers, page_values,i)