# JSON Duplicate Keys
Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys

<p align="center">
    <a href="https://github.com/truocphan/json_duplicate_keys/releases/"><img src="https://img.shields.io/github/release/truocphan/json_duplicate_keys" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/downloads/truocphan/json_duplicate_keys/total" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/stars/truocphan/json_duplicate_keys" height=30></a>
	<a href="https://pypi.org/project/json-duplicate-keys/" target="_blank"><img src="https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" height=30></a>
	<a href="https://www.facebook.com/292706121240740" target="_blank"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" height=30></a>
	<a href="https://twitter.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" height=30></a>
	<a href="https://github.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height=30></a>
	<a href="mailto:truocphan112017@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" height=30></a>
	<a href="https://www.buymeacoffee.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" height=30></a>
</p>

## Installation
```console
pip install json_duplicate_keys
```

## Basic Usage
### loads(`Jstr`, `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Deserialize a JSON format string to a class `JSON_DUPLICATE_KEYS`_
- `Jstr`: a JSON format string
- `dupSign_start`: 
- `dupSign_end`: 
- `ordered_dict`: preserves the order in which the Keys are inserted
- `_isDebug_`: Show/ Hide debug error messages
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject)

# OUTPUT: <json_duplicate_keys.JSON_DUPLICATE_KEYS object at 0x00000270AE987940>
```

### load(`Jfilepath`, `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Deserialize a JSON format string from a file to a class `JSON_DUPLICATE_KEYS`_
- `Jfilepath`: The path to the file containing the JSON format string
- `dupSign_start`: 
- `dupSign_end`: 
- `ordered_dict`: preserves the order in which the Keys are inserted
- `_isDebug_`: Show/ Hide debug error messages
```python
# /path/to/file.json: {"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}

import json_duplicate_keys as jdks

Jfilepath = "/path/to/file.json"

JDKSObject = jdks.load(Jfilepath)

print(JDKSObject)

# OUTPUT: <json_duplicate_keys.JSON_DUPLICATE_KEYS object at 0x00000270AE986D40>
```

### JSON_DUPLICATE_KEYS.getObject()
_Get the JSON object_
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())

# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
```

### JSON_DUPLICATE_KEYS.get(`name`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
_Get value in the JSON object by `name`_
- `name`: the key name of the JSON object. Supported flatten key name format
- `separator`: 
- `parse_index`:
- `_isDebug_`: Show/ Hide debug error messages
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.get("version{{{_2_}}}"))
# OUTPUT: latest

print(JDKSObject.get("release||$0$"))
# OUTPUT: {'version': 'latest'}

print(JDKSObject.get("snapshot||author"))
# OUTPUT: truocphan
```

### JSON_DUPLICATE_KEYS.set(`name`, `value`, `separator`="||", `parse_index`="$", `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Set a new `name` and `value` for the JSON object_
- `name`: 
- `value`: 
- `separator`: 
- `parse_index`: 
- `dupSign_start`: 
- `dupSign_end`: 
- `ordered_dict`: preserves the order in which the Keys are inserted
- `_isDebug_`: Show/Hide debug error messages
```python
import json_duplicate_keys as jdks

JDKSObject = jdks.loads('{}')
print(JDKSObject.getObject())
# OUTPUT: 

JDKSObject.set("author", "truocphan")
print(JDKSObject.getObject())
# OUTPUT: 

JDKSObject.set("version", "22.3.3")
JDKSObject.set("version", "latest")
print(JDKSObject.getObject())
# OUTPUT: 

JDKSObject.set("release||$0$||version", "latest")
print(JDKSObject.getObject())
# OUTPUT: 
```

### JSON_DUPLICATE_KEYS.update(`name`, `value`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
_Update new `value` for existing `name` in the JSON object_
- `name`: the key name of the JSON object. Supported flatten key name format
- `value`: new value for key `name`
- `separator`: 
- `parse_index`: 
- `_isDebug_`: Show/ Hide debug error messages
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

JDKSObject.update("version{{{_2_}}}", ["22.3.3", "latest"])
JDKSObject.update("snapshot||version", "latest")

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': ['22.3.3', 'latest'], 'release': [{'version': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': 'latest', 'release': [{'version': 'latest'}]}}
```

### JSON_DUPLICATE_KEYS.delete(`name`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
_Delete a key-value pair in a JSON object by key `name`_
- `name`: the key name of the JSON object. Supported flatten key name format
- `separator`: 
- `parse_index`: 
- `_isDebug_`: Show/ Hide debug error messages
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

JDKSObject.delete("version")
JDKSObject.delete("release||$0$")
JDKSObject.delete("snapshot")

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version{{{_2_}}}': 'latest', 'release': []}
```

### JSON_DUPLICATE_KEYS.dumps(`dupSign_start`="{{{", `dupSign_end`="}}}", `_isDebug_`=True, `skipkeys`=False, `ensure_ascii`=True, `check_circular`=True, `allow_nan`=True, `cls`=None, `indent`=None, `separators`=None, `default`=None, `sort_keys`=False)
_Serialize a JSON object to a JSON format string_
- `dupSign_start`: 
- `dupSign_end`: 
- `_isDebug_`: Show/ Hide debug error messages
- For remaining arguments, please refer to [json.dump()](https://docs.python.org/3/library/json.html#json.dump)
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

JDKSObject.delete("version")
JDKSObject.delete("release||$0$")
JDKSObject.delete("snapshot")

print(JDKSObject.dumps())
# OUTPUT: {"author": "truocphan", "version": "latest", "release": []}
```

### JSON_DUPLICATE_KEYS.dump(`Jfilepath`, `dupSign_start`="{{{", `dupSign_end`="}}}", `_isDebug_`=True, `skipkeys`=False, `ensure_ascii`=True, `check_circular`=True, `allow_nan`=True, `cls`=None, `indent`=None, `separators`=None, `default`=None, `sort_keys`=False)
_Serialize a JSON object to a JSON format string and write to a file_
- `Jfilepath`: the path to the file to save the JSON format string
- `dupSign_start`: 
- `dupSign_end`: 
- `_isDebug_`: Show/ Hide debug error messages
- For remaining arguments, please refer to [json.dump()](https://docs.python.org/3/library/json.html#json.dump)
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())
# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

JDKSObject.delete("version")
JDKSObject.delete("release||$0$")
JDKSObject.delete("snapshot")

Jfilepath = "/path/to/file.json"
JDKSObject.dump(Jfilepath)

JDKSObject_load = jdks.load(Jfilepath)
print(JDKSObject_load.getObject())
# OUTPUT: {'author': 'truocphan', 'version': 'latest', 'release': []}
```

### JSON_DUPLICATE_KEYS.flatten(`separator`="||", `parse_index`="$", `ordered_dict`=False, `_isDebug_`=True)
_Flatten a JSON object to a single key-value pairs_
```python
```

### JSON_DUPLICATE_KEYS.unflatten(`separator`="||", `parse_index`="$", `ordered_dict`=False, `_isDebug_`=True)
_Unflatten a flattened JSON object back to a JSON object_
```python
```