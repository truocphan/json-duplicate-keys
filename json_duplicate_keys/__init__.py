import json

# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # Loads # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
"""
>>> INPUT: '{"author": "truocphan", "version": "22.3.3", "version": "latest", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'

<<< OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': 'latest', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}
"""
def loads(Jstr, dupSign_start="{", dupSign_end="}", _isDebug_=False):
	import re
	from collections import OrderedDict
	import traceback

	def __convert_Jloads_to_Jobj(Jloads, Jobj):
		if type(Jloads) == OrderedDict:
			for k in Jloads.keys():
				_key = re.split(dupSign_start_escape_regex*3+"_\d+_"+dupSign_end_escape_regex*3+"$", k)[0]

				if _key not in Jobj.keys():
					if type(Jloads[k]) not in [list, OrderedDict]:
						Jobj[_key] = Jloads[k]
					else:
						if type(Jloads[k]) == list:
							Jobj[_key] = list()
						else:
							Jobj[_key] = OrderedDict()

						__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key])
				else:
					countObj = len([i for i in Jobj.keys() if _key==re.split(dupSign_start_escape_regex*3+"_\d+_"+dupSign_end_escape_regex*3+"$", i)[0]])
					if type(Jloads[k]) not in [list, OrderedDict]:
						Jobj[_key+dupSign_start*3+"_"+str(countObj+1)+"_"+dupSign_end*3] = Jloads[k]
					else:
						if type(Jloads[k]) == list:
							Jobj[_key+dupSign_start*3+"_"+str(countObj+1)+"_"+dupSign_end*3] = list()
						else:
							Jobj[_key+dupSign_start*3+"_"+str(countObj+1)+"_"+dupSign_end*3] = OrderedDict()

						__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key+dupSign_start*3+"_"+str(countObj+1)+"_"+dupSign_end*3])
		elif type(Jloads) == list:
			for i in range(len(Jloads)):
				if type(Jloads[i]) not in [list, OrderedDict]:
					Jobj.append(Jloads[i])
				else:
					if type(Jloads[i]) == list:
						Jobj.append(list())
					else:
						Jobj.append(OrderedDict())

					__convert_Jloads_to_Jobj(Jloads[i], Jobj[i])

	try:
		Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

		if type(Jloads) in [list, OrderedDict] and len(Jloads) > 0:
			try:
				if type(dupSign_start) not in [str, unicode] or len(dupSign_start) == 0: dupSign_start = "{"
			except Exception as e:
				if type(dupSign_start) != str or len(dupSign_start) == 0: dupSign_start = "{"

			dupSign_start_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_start])

			dupSign_start_escape_regex = re.escape(dupSign_start)


			try:
				if type(dupSign_end) not in [str, unicode] or len(dupSign_end) == 0: dupSign_end = "}"
			except Exception as e:
				if type(dupSign_end) != str or len(dupSign_end) == 0: dupSign_end = "}"

			dupSign_end_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_end])

			dupSign_end_escape_regex = re.escape(dupSign_end)


			Jstr = re.sub(r'\\\\', '\x00\x01', Jstr)
			Jstr = re.sub(r'\\"', '\x02\x03', Jstr)
			Jstr = re.sub(r'"([^"]*)"[\s\t\r\n]*([,\]}])', '\x04\x05\\1\x04\x05\\2', Jstr)


			Jstr = re.sub(r'"([^"]+)"[\s\t\r\n]*:', r'"\1{dupSign_start}_dupSign_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape*3, dupSign_end=dupSign_end_escape*3), Jstr)

			Jstr = re.sub(r'""[\s\t\r\n]*:', '"{dupSign_start}_dupSign_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape*3, dupSign_end=dupSign_end_escape*3), Jstr)

			i = 0
			while re.search(r'{dupSign_start}_dupSign_{dupSign_end}"[\s\t\r\n]*:'.format(dupSign_start=dupSign_start_escape*3, dupSign_end=dupSign_end_escape*3), Jstr):
				Jstr = re.sub(r'{dupSign_start}_dupSign_{dupSign_end}"[\s\t\r\n]*:'.format(dupSign_start=dupSign_start_escape*3, dupSign_end=dupSign_end_escape*3), dupSign_start_escape*3+"_"+str(i)+"_"+dupSign_end_escape*3+'":', Jstr, 1)
				i += 1

			Jstr = re.sub('\x00\x01', r'\\\\', Jstr)
			Jstr = re.sub('\x02\x03', r'\\"', Jstr)
			Jstr = re.sub('\x04\x05', r'"', Jstr)

			Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

			if type(Jloads) == list:
				Jobj = list()
			else:
				Jobj = OrderedDict()

			__convert_Jloads_to_Jobj(Jloads, Jobj)

			return Jobj
		else:
			return Jloads
	except:
		if _isDebug_: traceback.print_exc()
		return None
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #





# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # Dumps # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
"""
>>> INPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

<<< OUTPUT: '{"author": "truocphan", "version": "22.3.3", "version": "22.3.14", "release": [{"version": "22.3.3", "version": "latest"}], "snapshot": {"author": "truocphan", "version": "22.3.3", "release": [{"version": "latest"}]}}'
"""
def dumps(Jobj, dupSign_start="{", dupSign_end="}", _isDebug_=False, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False):
	import re
	from collections import OrderedDict
	import traceback

	try:
		if type(Jobj) in [list, dict, tuple, OrderedDict] and len(Jobj) > 0:
			try:
				if type(dupSign_start) not in [str, unicode]: dupSign_start = "{"
			except Exception as e:
				if type(dupSign_start) != str: dupSign_start = "{"

			dupSign_start_escape_regex = re.escape(json.dumps({dupSign_start:""})[2:-6])


			try:
				if type(dupSign_end) not in [str, unicode]: dupSign_end = "}"
			except Exception as e:
				if type(dupSign_end) != str: dupSign_end = "}"

			dupSign_end_escape_regex = re.escape(json.dumps({dupSign_end:""})[2:-6])


			if len(dupSign_start) == 0 and len(dupSign_end) == 0:
				return json.dumps(Jobj, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys)
			else:
				return re.sub(r'{dupSign_start}_\d+_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape_regex*3, dupSign_end=dupSign_end_escape_regex*3), '":', json.dumps(Jobj, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys))
		else:
			return json.dumps(Jobj, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys)
	except:
		if _isDebug_: traceback.print_exc()
		return None
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #





# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # Flatten # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
"""
>>> INPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': 'latest'}]}}

<<< OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': 'latest'}
"""
def flatten(Jobj, separator="||", parse_index="$", _isDebug_=False):
	from collections import OrderedDict
	import traceback

	Jflat = OrderedDict()

	def __convert_Jobj_to_Jflat(Jobj, key=None):
		if type(Jobj) in [dict, OrderedDict]:
			if len(Jobj) == 0:
				Jflat[key] = OrderedDict()
			else:
				for k,v in Jobj.items():
					_Jobj = v
					_key = "{key}{separator}{k}".format(key=key,separator=separator,k=k) if key != None else "{k}".format(k=k)

					__convert_Jobj_to_Jflat(_Jobj, _key)
		elif type(Jobj) == list:
			if len(Jobj) == 0:
				Jflat[key] = list()
			else:
				for i,v in enumerate(Jobj):
					_Jobj = v
					_key = "{key}{separator}{parse_index}{i}{parse_index}".format(key=key, separator=separator, parse_index=parse_index, i=i) if key != None else "{parse_index}{i}{parse_index}".format(parse_index=parse_index, i=i)

					__convert_Jobj_to_Jflat(_Jobj, _key)
		else:
			Jflat[key] = Jobj

	try:
		if type(Jobj) in [list, dict, OrderedDict]:
			if len(Jobj) == 0:
				if type(Jobj) == list:
					if _isDebug_: print("+ [DEBUG::flatten] Unable to Flatten an empty List")
					return None
				else:
					return Jflat
			else:
				try:
					if type(separator) not in [str, unicode] or len(separator) == 0: separator = "||"
				except Exception as e:
					if type(separator) != str or len(separator) == 0: separator = "||"

				try:
					if type(parse_index) not in [str, unicode] or len(parse_index) == 0: parse_index = "$"
				except Exception as e:
					if type(parse_index) != str or len(parse_index) == 0: parse_index = "$"

				__convert_Jobj_to_Jflat(Jobj)

				return Jflat
		else:
			if _isDebug_: print("+ [DEBUG::flatten] Unable to Flatten the {datatype} Object: \"{value}\"".format(datatype=type(Jobj), value=Jobj))
			return None
	except:
		if _isDebug_: traceback.print_exc()
		return None
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #





# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # Unflatten # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
"""
>>> INPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release||$0$||version': '22.3.3', 'release||$0$||version{{{_2_}}}': 'latest', 'snapshot||author': 'truocphan', 'snapshot||version': '22.3.3', 'snapshot||release||$0$||version': '22.3.14'}

<<< OUTPUT: {'author': 'truocphan', 'version': '22.3.3', 'version{{{_2_}}}': '22.3.14', 'release': [{'version': '22.3.3', 'version{{{_2_}}}': 'latest'}], 'snapshot': {'author': 'truocphan', 'version': '22.3.3', 'release': [{'version': '22.3.14'}]}}
"""
def unflatten(Jflat, separator="||", parse_index="$", _isDebug_=False):
	import re
	from collections import OrderedDict
	import traceback

	try:
		if type(Jflat) in [dict, OrderedDict]:
			if len(Jflat) == 0:
				return OrderedDict()
			else:
				Jobj = list() if len([k for k in Jflat.keys() if re.compile("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$").match(str(k).split(separator)[0])]) == len(Jflat.keys()) else OrderedDict()

				for k, v in Jflat.items():
					Jtmp = Jobj
					Jkeys = k.split(separator)

					for count, (Jkey, next_Jkeys) in enumerate(zip(Jkeys, Jkeys[1:] + [v]), 1):
						v = next_Jkeys if count == len(Jkeys) else list() if re.compile("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$").match(next_Jkeys) else OrderedDict()

						if type(Jtmp) == list:
							Jkey = int(re.compile(re.escape(parse_index)+"(\d+)"+re.escape(parse_index)).match(Jkey).group(1))

							while Jkey >= len(Jtmp):
								Jtmp.append(v)

						elif Jkey not in Jtmp:
							Jtmp[Jkey] = v

						Jtmp = Jtmp[Jkey]

				return Jobj
		else:
			if _isDebug_: print("+ [DEBUG::unflatten] Unable to Unflatten the {datatype} Object: \"{value}\"".format(datatype=type(Jflat), value=Jflat))
			return None
	except:
		if _isDebug_: traceback.print_exc()
		return None
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #