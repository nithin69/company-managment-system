import datetime
import MySQLdb
import urllib
import urllib2


now = datetime.datetime.now()
today1 = str(now)[:10]
today = today1[5:]
tmon=today[1]
tday=today[2:]
#print tmon
conn = MySQLdb.connect("localhost","anil","anil","kcitsplc_ssms" )
sqlcursor = conn.cursor() 
sqlcursor.execute("SELECT firstname,mobile FROM kcitsplc_ssms.k1emp_employee")
row = sqlcursor.fetchall() 

authkey = "73233ADi7CjnTmOXH589d1fa2" # Your authentication key.

url = "http://sms.rpsms.in/api/sendhttp.php" # API URL


for message in row:
    

    mobiles = message[1]
    

    message = "hi " + message[0]+",\nyou had creadited your salary in account please check you account.\n\nfrom\nk1group."  

    sender = "MANASA" 

    route = 4 

    # Prepare you post parameters
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route
              }

    print mobiles



    postdata = urllib.urlencode(values) # URL encoding the data here.

    req = urllib2.Request(url, postdata)

    response = urllib2.urlopen(req)

    output = response.read()

    print output 
