import re

class hodo:
	hodo = 'hodo'#編碼文字
	hodo_pattern = r'(?P<h>h+)(?P<o>o+)(?P<d>d+)(?P<o2>o+)'#匹配hodo編碼

	#編碼函數，將unicode文字編碼成hodo文串
	#@param String str 要編碼的unicode字串
	#@return String 編碼好的hodo字串
	def encode(str):
		hodo_str = ''
		for char in str:
			Hex = hex(ord(char))[2:]
			Hex = ('0' * (len(hodo.hodo) - len(Hex))) + Hex
			temp = ''
			for i in range(len(hodo.hodo)):
				temp += hodo.hodo[i]*(int(Hex[i],16) + 1)
			hodo_str += temp + ' '
		return hodo_str[:-1]

	#解函數，將hodo文串解碼回unicode文字
	#@param String hodo_str 要解碼的hodo字串
	#@return String 解碼好的unicode文字
	def decode(hodo_str):
		str = ''
		hodo_list = hodo_str.split(' ')
		for hodo_char in hodo_list:
			if re.match(r'^\s*$',hodo_char):
				continue
			match = re.match(hodo.hodo_pattern,hodo_char)
			value = hex(len(match.group('h'))-1)[2]+hex(len(match.group('o'))-1)[2]+hex(len(match.group('d'))-1)[2]+hex(len(match.group('o2'))-1)[2]
			str += chr(int(value,16))
		return str
		
