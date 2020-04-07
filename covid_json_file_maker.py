#Okay this is it broooooooo
import bs4, requests, json


res=requests.get('https://www.mygov.in/corona-data/covid19-statewise-status')
var  = bs4.BeautifulSoup(res.text, 'html.parser')

list1 = var.select('.entity.entity-field-collection-item.field-collection-item-field-covid-statewise-data.clearfix')

#.field-item
 
data = {}


for stateNo in range(30):
    state = ((list1[stateNo].select('.field-item'))[0]).text
    total = ((list1[stateNo].select('.field-item'))[1]).text
    cured = ((list1[stateNo].select('.field-item'))[2]).text
    deaths = ((list1[stateNo].select('.field-item'))[3]).text
    
    data[state] = [total, cured, deaths]
    
#print(data)
    
    #print("State - " + (list1[stateNo].select('.field-item'))[0].text)
    
json_content = json.dumps(data)

local_file =open(r"all_data.json", "w")
local_file.write(json_content)
local_file.close()

