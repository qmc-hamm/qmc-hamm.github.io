import json

bibdb=json.load(open("my_papers.json"))

df={'title':[],'DOI':[],'volume':[],'pages':[],'author':[],'date':[],"publicationTitle":[], 'url':[]}

def get_name(creator):
    if 'firstName' in creator.keys() and 'lastName' in creator.keys():
        return  creator['firstName'] + " " + creator['lastName']
    if 'name' in creator.keys():
        return creator['name']
    return 'UNK'


for i in bibdb['items']:
  i['author'] = ", ".join([get_name(x) for x in i['creators'] ])
  for k in df.keys():
    if k in i.keys():
      df[k].append(i[k])
    else:
      df[k].append("")

import pandas as pd
df=pd.DataFrame(df)
df['datetime'] = pd.to_datetime(df['date'])

df=df.sort_values("datetime",ascending=False)
df['year'] = [x.year for  x in df['datetime']]
def fix_names(s):
    return s.replace("$","$").replace("\ensuremath","")

df['title'] = [fix_names(x) for x in df['title']]

with open("_index.md",'w') as f:
  f.write("""---
layout: page
title: Papers
---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

""")
  for row in df.iterrows():
    r=row[1]
    print(r)
    url = r['url']
    if len(r['DOI']) > 1: 
        url = "https://doi.org/"+r['DOI']
    f.write( "<b>["+r['title']+"](" + url + ")</b>  <br>" \
        + r['author'] +" <br>"\
        + r["publicationTitle"].replace(r"$",r"$$") +" "+\
        "<b>"+r['volume']+"</b> "+\
        r['pages'] + \
        " ("+str(r['year'])+") " + 
        "\n\n")

