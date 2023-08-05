# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # loads # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def loads(Jstr, dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, _isDebug_=True):
	import json, re
	from collections import OrderedDict

	if type(Jstr) in [str]:
		def __convert_Jloads_to_Jobj(Jloads, Jobj):
			if type(Jloads) in [dict, OrderedDict]:
				for k in Jloads.keys():
					_key = re.split(dupSign_start_escape_regex+"_\d+_"+dupSign_end_escape_regex+"$", k)[0]

					if _key not in Jobj.keys():
						if type(Jloads[k]) not in [list, dict, OrderedDict]:
							Jobj[_key] = Jloads[k]
						else:
							if type(Jloads[k]) == list:
								Jobj[_key] = list()
							elif type(Jloads[k]) == dict:
								Jobj[_key] = dict()
							else:
								Jobj[_key] = OrderedDict()

							__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key])
					else:
						countObj = len([i for i in Jobj.keys() if _key==re.split(dupSign_start_escape_regex+"_\d+_"+dupSign_end_escape_regex+"$", i)[0]])
						if type(Jloads[k]) not in [list, dict, OrderedDict]:
							Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = Jloads[k]
						else:
							if type(Jloads[k]) == list:
								Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = list()
							elif type(Jloads[k]) == dict:
								Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = dict()
							else:
								Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end] = OrderedDict()

							__convert_Jloads_to_Jobj(Jloads[k], Jobj[_key+dupSign_start+"_"+str(countObj+1)+"_"+dupSign_end])
			elif type(Jloads) == list:
				for i in range(len(Jloads)):
					if type(Jloads[i]) not in [list, dict, OrderedDict]:
						Jobj.append(Jloads[i])
					else:
						if type(Jloads[i]) == list:
							Jobj.append(list())
						elif type(Jloads[i]) == dict:
							Jobj.append(dict())
						else:
							Jobj.append(OrderedDict())

						__convert_Jloads_to_Jobj(Jloads[i], Jobj[i])

		try:
			Jloads = json.loads(Jstr)
			if ordered_dict:
				Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

			if type(Jloads) in [list, dict, OrderedDict]:
				try:
					if type(dupSign_start) not in [str, unicode] or len(dupSign_start) == 0: dupSign_start = "{{{"
				except Exception as e:
					if type(dupSign_start) != str or len(dupSign_start) == 0: dupSign_start = "{{{"

				dupSign_start_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_start])

				dupSign_start_escape_regex = re.escape(dupSign_start)


				try:
					if type(dupSign_end) not in [str, unicode] or len(dupSign_end) == 0: dupSign_end = "}}}"
				except Exception as e:
					if type(dupSign_end) != str or len(dupSign_end) == 0: dupSign_end = "}}}"

				dupSign_end_escape = "".join(["\\\\u"+hex(ord(c))[2:].zfill(4) for c in dupSign_end])

				dupSign_end_escape_regex = re.escape(dupSign_end)


				Jstr = re.sub(r'\\\\', '\x00\x01', Jstr)
				Jstr = re.sub(r'\\"', '\x02\x03', Jstr)
				Jstr = re.sub(r'"([^"]*)"[\s\t\r\n]*([,\]}])', '\x04\x05\\1\x04\x05\\2', Jstr)


				Jstr = re.sub(r'"([^"]+)"[\s\t\r\n]*:', r'"\1{dupSign_start}_dupSign_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape, dupSign_end=dupSign_end_escape), Jstr)

				Jstr = re.sub(r'""[\s\t\r\n]*:', '"{dupSign_start}_dupSign_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape, dupSign_end=dupSign_end_escape), Jstr)

				i = 0
				while re.search(r'{dupSign_start}_dupSign_{dupSign_end}"[\s\t\r\n]*:'.format(dupSign_start=dupSign_start_escape, dupSign_end=dupSign_end_escape), Jstr):
					Jstr = re.sub(r'{dupSign_start}_dupSign_{dupSign_end}"[\s\t\r\n]*:'.format(dupSign_start=dupSign_start_escape, dupSign_end=dupSign_end_escape), dupSign_start_escape+"_"+str(i)+"_"+dupSign_end_escape+'":', Jstr, 1)
					i += 1

				Jstr = re.sub('\x00\x01', r'\\\\', Jstr)
				Jstr = re.sub('\x02\x03', r'\\"', Jstr)
				Jstr = re.sub('\x04\x05', r'"', Jstr)

				Jloads = json.loads(Jstr)
				if ordered_dict:
					Jloads = json.loads(Jstr, object_pairs_hook=OrderedDict)

				if type(Jloads) == list:
					Jobj = list()
				elif type(Jloads) == dict:
					Jobj = dict()
				else:
					Jobj = OrderedDict()

				__convert_Jloads_to_Jobj(Jloads, Jobj)

				return JSON_DUPLICATE_KEYS(Jobj)
			else:
				if _isDebug_: print("\x1b[31m[-] DataError: Invalid JSON format\x1b[0m")
		except Exception as e:
			if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
	else:
		if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be str, not {}\x1b[0m".format(type(Jstr)))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # load # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def load(Jfilepath, dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, _isDebug_=True):
	try:
		Jfile = open(Jfilepath)
		Jstr = Jfile.read()
		Jfile.close()

		return loads(Jstr, dupSign_start=dupSign_start, dupSign_end=dupSign_end, ordered_dict=ordered_dict, _isDebug_=_isDebug_)
	except Exception as e:
		if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # JSON_DUPLICATE_KEYS # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class JSON_DUPLICATE_KEYS:
	def __init__(self, Jobj):
		from collections import OrderedDict
		self.__Jobj = dict()
		if type(Jobj) in [dict, OrderedDict, list]:
			self.__Jobj = Jobj

	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # getObject # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def getObject(self):
		return self.__Jobj
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # get # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def get(self, name, separator="||", parse_index="$", _isDebug_=True):
		import re
		from collections import OrderedDict

		if type(self.getObject()) in [list, dict, OrderedDict]:
			try:
				Jobj = self.__Jobj
				Jval = "JSON_DUPLICATE_KEYS_ERROR"
				name_split = name.split(separator)

				for i in range(len(name_split)):
					if type(Jobj) in [dict, OrderedDict] and name_split[i] in Jobj.keys():
						Jval = Jobj[name_split[i]]
						Jobj = Jobj[name_split[i]]
					elif type(Jobj) in [list] and re.search("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$", name_split[i]):
						Jval = Jobj[int(name_split[i].split(parse_index)[1])]
						Jobj = Jobj[int(name_split[i].split(parse_index)[1])]
					else:
						if _isDebug_: print("\x1b[31m[-] KeyNotFoundError: \x1b[0m"+separator.join(name_split[:i+1]))
						return "JSON_DUPLICATE_KEYS_ERROR"
				return Jval
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
				return "JSON_DUPLICATE_KEYS_ERROR"
		else:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return "JSON_DUPLICATE_KEYS_ERROR"
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # set # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# def set(self, name, value, separator="||", parse_index="$", dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False, _isDebug_=True):
	# 	import re, copy
	# 	from collections import OrderedDict

	# 	if type(self.getObject()) in [list, dict, OrderedDict]:
	# 		name_split = name.split(separator)
	# 		for i in range(len(name_split),0,-1):
	# 			name_split_first = separator.join(name_split[:i-1])
	# 			name_split_current = name_split[i-1]
	# 			name_split_last = separator.join(name_split[i:])

	# 			if self.get(separator.join([name_split_first, name_split_current]), separator=separator, parse_index=parse_index, _isDebug_=False) != "JSON_DUPLICATE_KEYS_ERROR":
	# 				if re.search("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$", name_split_current):
	# 					k = separator.join([ name_split_first, parse_index+str(len(self.get(name_split_first, separator=separator, parse_index=parse_index, _isDebug_=False)))+parse_index, separator.join([re.sub("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$",parse_index+"0"+parse_index, ns) for ns in name_split_last.split(separator)]) ])
	# 					self.flatten()
	# 					self.__Jobj[k] = value
	# 					self.unflatten()
	# 				else:
	# 					i = 2
	# 					while True:
	# 						if self.get(separator.join(name_split_first, name_split_current)+dupSign_start+"_"+str(i)+"_"+dupSign_end, separator=separator, parse_index=parse_index, _isDebug_=False) == "JSON_DUPLICATE_KEYS_ERROR":
	# 							self.flatten()
	# 							self.__Jobj[separator.join([separator.join(name_split_first, name_split_current)+dupSign_start+"_"+str(i)+"_"+dupSign_end]), separator.join([re.sub("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$",parse_index+"0"+parse_index, ns) for ns in name_split_last.split(separator)])] = value
	# 							self.unflatten()
	# 							break
	# 						i += 1
	# 				break
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # update # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def update(self, name, value, separator="||", parse_index="$", _isDebug_=True):
		import re

		if self.get(name, separator=separator, parse_index=parse_index, _isDebug_=_isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
			try:
				exec_expression = "self.getObject()"

				for k in name.split(separator):
					if re.search("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$", k):
						exec_expression += "["+k.split(parse_index)[1]+"]"
					else:
						exec_expression += "["+repr(k)+"]"

				exec(exec_expression+"="+repr(value))
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # #  delete   # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def delete(self, name, separator="||", parse_index="$", _isDebug_=True):
		import re

		if self.get(name, separator=separator, parse_index=parse_index, _isDebug_=_isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
			try:
				exec_expression = "del self.getObject()"

				for k in name.split(separator):
					if re.search("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$", k):
						exec_expression += "["+k.split(parse_index)[1]+"]"
					else:
						exec_expression += "["+repr(k)+"]"

				exec(exec_expression)
			except Exception as e:
				if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # # dumps # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def dumps(self, dupSign_start="{{{", dupSign_end="}}}", _isDebug_=True, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False):
		import json, re
		from collections import OrderedDict

		if type(self.getObject()) in [list, dict, OrderedDict]:
			try:
				if type(dupSign_start) not in [str, unicode]: dupSign_start = "{{{"
			except Exception as e:
				if type(dupSign_start) != str: dupSign_start = "{{{"

			dupSign_start_escape_regex = re.escape(json.dumps({dupSign_start:""})[2:-6])


			try:
				if type(dupSign_end) not in [str, unicode]: dupSign_end = "}}}"
			except Exception as e:
				if type(dupSign_end) != str: dupSign_end = "}}}"

			dupSign_end_escape_regex = re.escape(json.dumps({dupSign_end:""})[2:-6])


			return re.sub(r'{dupSign_start}_\d+_{dupSign_end}":'.format(dupSign_start=dupSign_start_escape_regex, dupSign_end=dupSign_end_escape_regex), '":', json.dumps(self.getObject(), skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys))
		else:
			if _isDebug_: print("\x1b[31m[-] DataTypeError: the JSON object must be list, dict or OrderedDict, not {}\x1b[0m".format(type(self.getObject())))
			return "JSON_DUPLICATE_KEYS_ERROR"
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	 # # # # # # # # # # # # # # dump  # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def dump(self, Jfilepath, dupSign_start="{{{", dupSign_end="}}}", _isDebug_=True, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False):
		Jstr = self.dumps(dupSign_start=dupSign_start, dupSign_end=dupSign_end, _isDebug_=_isDebug_, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default, sort_keys=sort_keys)

		try:
			Jfile = open(Jfilepath, "w")
			Jfile.write(Jstr)
			Jfile.close()
		except Exception as e:
			if _isDebug_: print("\x1b[31m[-] ExceptionError: {}\x1b[0m".format(e))
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	#  # # # # # # # # # # # # # flatten # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# def flatten(self, separator="||", parse_index="$", ordered_dict=False):
	# 	from collections import OrderedDict

	# 	if len(self.__Jobj) > 0:
	# 		Jflat = dict()
	# 		if ordered_dict:
	# 			Jflat = OrderedDict()

	# 		def __convert_Jobj_to_Jflat(Jobj, key=None):
	# 			if type(Jobj) in [dict, OrderedDict]:
	# 				if len(Jobj) == 0:
	# 					Jflat[key] = dict()
	# 					if ordered_dict:
	# 						Jflat[key] = OrderedDict()
	# 				else:
	# 					for k,v in Jobj.items():
	# 						_Jobj = v
	# 						_key = "{key}{separator}{k}".format(key=key,separator=separator,k=k) if key != None else "{k}".format(k=k)

	# 						__convert_Jobj_to_Jflat(_Jobj, _key)
	# 			elif type(Jobj) == list:
	# 				if len(Jobj) == 0:
	# 					Jflat[key] = list()
	# 				else:
	# 					for i,v in enumerate(Jobj):
	# 						_Jobj = v
	# 						_key = "{key}{separator}{parse_index}{i}{parse_index}".format(key=key, separator=separator, parse_index=parse_index, i=i) if key != None else "{parse_index}{i}{parse_index}".format(parse_index=parse_index, i=i)

	# 						__convert_Jobj_to_Jflat(_Jobj, _key)
	# 			else:
	# 				Jflat[key] = Jobj


	# 		try:
	# 			if type(separator) not in [str, unicode] or len(separator) == 0: separator = "||"
	# 		except Exception as e:
	# 			if type(separator) != str or len(separator) == 0: separator = "||"

	# 		try:
	# 			if type(parse_index) not in [str, unicode] or len(parse_index) == 0: parse_index = "$"
	# 		except Exception as e:
	# 			if type(parse_index) != str or len(parse_index) == 0: parse_index = "$"

	# 		__convert_Jobj_to_Jflat(self.__Jobj)

	# 		self.__Jobj = Jflat
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	#  # # # # # # # # # # # # # unflatten # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# def unflatten(self, separator="||", parse_index="$", ordered_dict=False):
	# 	import re
	# 	from collections import OrderedDict

	# 	if type(self.__Jobj) in [dict, OrderedDict] and len(self.__Jobj) > 0:
	# 		Jobj = list() if len([k for k in self.__Jobj.keys() if re.compile("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$").match(str(k).split(separator)[0])]) == len(self.__Jobj.keys()) else OrderedDict() if ordered_dict else dict()

	# 		for k, v in self.__Jobj.items():
	# 			Jtmp = Jobj
	# 			Jkeys = k.split(separator)

	# 			for count, (Jkey, next_Jkeys) in enumerate(zip(Jkeys, Jkeys[1:] + [v]), 1):
	# 				v = next_Jkeys if count == len(Jkeys) else list() if re.compile("^"+re.escape(parse_index)+"\d+"+re.escape(parse_index)+"$").match(next_Jkeys) else OrderedDict() if ordered_dict else dict()

	# 				if type(Jtmp) == list:
	# 					Jkey = int(re.compile(re.escape(parse_index)+"(\d+)"+re.escape(parse_index)).match(Jkey).group(1))

	# 					while Jkey >= len(Jtmp):
	# 						Jtmp.append(v)

	# 				elif Jkey not in Jtmp:
	# 					Jtmp[Jkey] = v

	# 				Jtmp = Jtmp[Jkey]

	# 		self.__Jobj = Jobj
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #