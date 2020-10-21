#Some parts from documentation at https://pymapd.readthedocs.io/en/latest/usage.html
#(C)Tsubasa Kato (@_stingraze on Twitter)
from pymapd import connect
import pandas as pd

con = connect(user="admin", password="PasswordHere", host="localhost", dbname="omnisci")
df = pd.read_sql("SELECT * from flights_2008_7M limit 100", con)

print(df.to_string())

#Output to File
path = './omnisci-data.txt'

with open(path, 'w') as f:
        print(df.to_string(), file=f)