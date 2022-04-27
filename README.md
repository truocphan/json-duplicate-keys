# JSON Duplicate Keys
Flatten / Unflatten and Loads / Dumps JSON object with Duplicate Keys

## Installation
```console
pip install json-duplicate-keys
```

## Usage
```python
>>> import json_duplicate_keys
>>>
>>> Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'
>>> Jobj = json_duplicate_keys.loads(Jstr)
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>>
>>> Jobj["version{{{_2_}}}"] = "22.3.14"
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>> json_duplicate_keys.dumps(Jobj)
'{"author": "truocphan", "version": "22.3.3", "version": "22.3.14", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'
>>>
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>> Jflat = json_duplicate_keys.flatten(Jobj)
>>> Jflat
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': 'latest'}
>>>
>>> Jflat['snapshot||release||$0$||version'] = "22.3.14"
>>> Jflat
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': '22.3.14'}
>>>
>>> json_duplicate_keys.unflatten(Jflat)
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': '22.3.14'}]}}
```