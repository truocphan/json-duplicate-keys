# JSON Duplicate Keys
Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys

## Installation
```console
pip install json_duplicate_keys
```

## Basic Usage
### loads(`Jstr`, `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Deserialize a JSON format string to a class `JSON_DUPLICATE_KEYS`_
- `Jstr`: JSON format string
- `ordered_dict`: preserves the order in which the Keys are inserted
- `_isDebug_`: Show/Hide debug error messages
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(type(JDKSObject))

# OUTPUT: <class 'json_duplicate_keys.JSON_DUPLICATE_KEYS'>
```

### load(`Jfilepath`, `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Deserialize a JSON format string from a file to a class `JSON_DUPLICATE_KEYS`_
- `Jfilepath`: The path to the file containing the JSON format string
- `ordered_dict`: preserves the order in which the Keys are inserted
- `_isDebug_`: Show/Hide debug error messages
```python
# /path/to/file.json: {"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}

import json_duplicate_keys as jdks

Jfilepath = "/path/to/file.json"

JDKSObject = jdks.load(Jfilepath)

print(type(JDKSObject))

# OUTPUT: <class 'json_duplicate_keys.JSON_DUPLICATE_KEYS'>
```

### JSON_DUPLICATE_KEYS.getObject()
_Get the JSON object_
```python
import json_duplicate_keys as jdks

Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

JDKSObject = jdks.loads(Jstr)

print(JDKSObject.getObject())

# OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
```

### JSON_DUPLICATE_KEYS.get(`name`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
_Get value in JSON object by `name`_
```python
```

### JSON_DUPLICATE_KEYS.set(`name`, `value`, `separator`="||", `parse_index`="$", `dupSign_start`="{{{", `dupSign_end`="}}}", `ordered_dict`=False, `_isDebug_`=True)
_Set a new `name` and `value` for the JSON object_
```python
```

### JSON_DUPLICATE_KEYS.update(`name`, `value`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
_Update new `value` for existing `name` in the JSON object_
```python
```

### JSON_DUPLICATE_KEYS.delete(`name`, `separator`="||", `parse_index`="$", `_isDebug_`=True)
```python
```

### JSON_DUPLICATE_KEYS.dumps(`dupSign_start`="{{{", `dupSign_end`="}}}", `_isDebug_`=True, `skipkeys`=False, `ensure_ascii`=True, `check_circular`=True, `allow_nan`=True, `cls`=None, `indent`=None, `separators`=None, `default`=None, `sort_keys`=False)
_Serialize a JSON object to a JSON format string_
```python
```

### JSON_DUPLICATE_KEYS.dump(`Jfilepath`, `dupSign_start`="{{{", `dupSign_end`="}}}", `_isDebug_`=True, `skipkeys`=False, `ensure_ascii`=True, `check_circular`=True, `allow_nan`=True, `cls`=None, `indent`=None, `separators`=None, `default`=None, `sort_keys`=False)
_Serialize a JSON object to a JSON format string and write to a file_
```python
```

### JSON_DUPLICATE_KEYS.flatten(`separator`="||", `parse_index`="$", `ordered_dict`=False, `_isDebug_`=True)
_Flatten a JSON object to a single key-value pairs_
```python
```

### JSON_DUPLICATE_KEYS.unflatten(`separator`="||", `parse_index`="$", `ordered_dict`=False, `_isDebug_`=True)
_Unflatten a flattened JSON object back to a JSON object_
```python
```