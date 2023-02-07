import requests, json
from json.decoder import JSONDecoder
def readDatabase(pageId, headers):
    
    readUrl = f"https://api.notion.com/v1/databases/"
    data={}
    data["parent"]={
        "type": "page_id",
        "page_id": "6f310e7e07a445b292c5635ed77b9984"
    }
    data["icon"]={
    	"type": "emoji",
			"emoji": "📝"
  	}
    data["cover"]={
  		"type": "external",
    	"external": {
    		"url": "https://website.domain/images/image.png"
    	}
  	}
    data["is_inline"]=True
    data["title"]=[]
    data["title"].append({
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": None
            }
        })
    data["properties"]={
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        }
    }
    print(data)
    
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
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
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

readDatabase(pageId, headers)