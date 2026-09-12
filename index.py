import uuid

header = []
ui = ""
while (True):
  isUI = input("UIを使用しますか？ y/n : ")
  if isUI == "y":
    ui = """{
            "module_name": "@minecraft/server-ui",
            "version": "2.1.0"
        },"""
    break
  elif isUI == "n":
    break
  else:
    pass

name = input("名前を入力してください : ")
description = input("説明を入力してください : ")
header.append(name)
header.append(description)
uuids = []
uuids.append(uuid.uuid4())
uuids.append(uuid.uuid4())

resource = ""
while (True):
  isResource = input("リソースパックを作成しますか？ y/n : ")
  if isResource == "y":
    uuids.append(uuid.uuid4())
    uuids.append(uuid.uuid4())
    resource = f"""{{
            "uuid": "{uuids[2]}",
            "version": [1, 0, 0]
        }},"""
    jsonResource = f"""{{
      "format_version": 2,
      "header": {{
        "name": "{header[0]}",
        "description": "{header[1]}",
        "uuid": "{uuids[2]}",
        "version": [1, 0, 0],
        "min_engine_version": [1, 21, 10]
      }},
      "modules": [
        {{
          "description": "{header[0]}のリソースパック",
          "type": "resources",
          "uuid": "{uuids[3]}",
          "version": [1, 0, 0]
        }}
      ]
    }}"""
    fileResource = open("Resource/manifest.json", "w", encoding="utf-8")
    fileResource.write(jsonResource)
    fileResource.close()
    break
  elif isResource == "n":
    break
  else:
    pass

json = f"""{{
    "format_version": 2,
    "header": {{
        "name": "{header[0]}",
        "description": "{header[1]}",
        "uuid": "{uuids[0]}",
        "version": [1, 0, 0],
        "min_engine_version": [1, 21, 0]
    }},
    "modules": [
        {{
            "description": " ",
            "type": "script",
            "entry": "scripts/index.js",
            "uuid": "{uuids[1]}",
            "version": [1, 0, 0]
        }}
    ],
    "dependencies": [
        {ui}
        {resource}
        {{
            "module_name": "@minecraft/server",
            "version": "2.9.0"
        }}
    ]
}}
"""

file = open("Behavior/manifest.json", "w", encoding="utf-8")
file.write(json)
file.close()
