import os
layer = iface.activeLayer()
countries = "EUROPE,Austria,Belgium,France,Germany,Italy,Netherlands,Spain,Sweden,Switzerland,United Kingdom,CIS,CIS-Russian Federation,CIS-Other European,AFRICA,Comoros,Kenya,Malagasy Rep.,Reunion Island,Seychelles,South Africa,Zimbabwe,Other African,ASIA,Hong Kong SAR,India,Japan,Malaysia,Peoples' Rep. of China,Singapore,United Arab Emirates,Other Asian,OCEANIA,Australia,Other Oceanian,AMERICA,USA,Canada,Other American,Other & Not Stated,All Countries"
countries = countries.split(',')
path = layer.source()
out_file = os.path.join(os.path.dirname(path), 'tourism_cleaned.csv')
out_file = out_file.replace('file://','')
output = open(out_file, 'wt')
output.write('year,country,visitors' + os.linesep)
for feature in layer.getFeatures():
    year = feature["Year"]
    for country in countries:
        output.write('%s,%s,%s%s' % (
        feature['Year'], country, feature[country], os.linesep))
output.close()
print ('Data cleanup complete')
  

