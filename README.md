# Live-Score-Cricket
Lets check out live cricket score using python.

### Pre-requisites

- pycricbuzz: Pycricbuzz is a python library which can be used to get live scores,<br> commentary and full scorecard for recent and live matches.
  
### Install Libraries

- pip install pycricbuzz 

### Import Libraries

         from pycricbuzz import Cricbuzz as cb
         
We specifically need 'Cricbuzz' database in the 'pycricbuzz' library which we are importing as 'cb'

### Lets dive into the code

         cric = cb()
         match = cric.matches()
         
'cric' is a object of cb. 'match' extracts the match details in the database  using matches() function.

### Printing match details

         for m in match:
             print(m)
             if(m['mchstate'] !=  'nextlive'):
                 print(cric.livescore(m['id']))
                 print(cric.scorecard(m['id']))
         
The first print statement 'print(m)' gives the basic match details.<br>
The conditional statement checks the match status.<br>
The second print statement 'print(cric.livescore(m['id']))' gives the live scores.<br>
The second print statement 'print(cric.scorecard(m['id']))' gives the complete scorecard.
