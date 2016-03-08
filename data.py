#Generic Object Sequences (Lists and Dictionaries)

lst = ["dog", "cat", "mouse", "goat", "albatross"]

dic_lst = [{"animal": "dog", "street_cred": 5 }, {"animal": "cat", "street_cred": 9999 },
{"animal": "mouse", "street_cred": 4 }, {"animal": "TMNT", "street_cred": 10000 }]

add_lst = ["fish", "lepercoon", "shark"]


#Duck Typing Example
def calc(a,b,c):
	return (a+b)*c


#Mutable and Unmutable
def func_str(str):
	str += "add"
	return str

def func_lst(lst):
	lst+= [1,2,3]
	return lst

def func_dic(dic):
	dic["novo"] = ["INSERTED"]
	return dic

def func_int(n):
	n+=2
	return n