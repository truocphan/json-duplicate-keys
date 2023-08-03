# JSON Duplicate Keys
Flatten/ Unflatten and Load(s)/ Dump(s) JSON File/ Object with Duplicate Keys

## Installation
```console
pip install json-duplicate-keys
```

## Usage
```python
>>> import json_duplicate_keys as jdks
>>>
>>> Jstr = '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'
>>> Jobj = jdks.loads(Jstr)
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>>
>>> Jobj["version{{{_2_}}}"] = "22.3.14"
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>> jdks.dumps(Jobj)
'{"author": "truocphan", "version": "22.3.3", "version": "22.3.14", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'
>>>
>>> Jobj
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
>>> Jflat = jdks.flatten(Jobj)
>>> Jflat
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': 'latest'}
>>>
>>> Jflat['snapshot||release||$0$||version'] = "22.3.14"
>>> Jflat
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': '22.3.14'}
>>>
>>> jdks.unflatten(Jflat)
{'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': '22.3.14'}]}}
```
