def getBrand(smth):
	if len(smth) == 1:
		return smth[0]['brand']
	if len(smth[0]['owners'])>len(smth[1]['owners']):
		del smth[1]
	else:
		del smth[0]
	return getBrand(smth)
def addOwner(smth, name, brand):
	for brands in smth:
		if brands['brand'] == brand:
			brands['owners'] = {name}
			print(smth)
def getNames(smth):
	names = set()
	for peop in smth:
		names.update(peop['owners'])
	return names
smth = [
		{
			"brand":"Ford",
			"model":"Mustang",
			"year":1964,
			'owners':{
						"Bob",
						"Boba"
					}
		},
		{
			"brand":"Mers",
			"model":"C500",
			"year":2000,
			'owners':{
						"Bob"
					}
		},
		{	"brand":"Wolksvagen",
			"model":"Polo",
			"year":2002,
			"owners":{}
		}
]
print(getBrand(smth.copy()))
addOwner(smth, 'Bibo', 'Wolksvagen')
print(getNames(smth))