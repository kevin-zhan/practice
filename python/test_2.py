def namelist(names):
    #your code here
    if len(names) == 1:
    	return names[0]["name"]
    if len(names) == 2:
    	return names[0]["name"]+" & "+names[1]["name"]
    result = ""
    for i in range(0,len(names)):
    	if i == len(names)-2:
    		result += names[i]["name"]+" & "
    		continue
    	if i == len(names)-1:
    		result += names[i]["name"]
    		continue
    	result += names[i]["name"]+", "
    return result
names = [ {'name': 'Bart'}, {'name': 'Lisa'}]

print namelist(names)