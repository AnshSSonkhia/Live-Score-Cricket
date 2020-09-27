from pycricbuzz import Cricbuzz as cb
cric = cb()
match = cric.matches()
for m in match:
    print(m)
    if(m['mchstate'] !=  'nextlive'):
        print(cric.livescore(m['id']))
        print(cric.scorecard(m['id']))
