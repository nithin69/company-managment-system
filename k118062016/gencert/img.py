from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from time import gmtime, strftime
#import MySQLdb
#conn = MySQLdb.connect(user="bhanu", passwd="bhanu", db="sv01d3")
#cur = conn.cursor()

showtimein = strftime("%d %b,%Y", gmtime())
showtimeout = strftime("%d %b,%Y", gmtime())


#cur.execute("SELECT * FROM city_ping where id ="+str(a))
#row = cur.fetchone()


img = Image.open("memo.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("DancingScript-Regular.otf", 100)
draw.text((820, 1280),"Sibani Shankar",(255,255,255),font=font)
draw.text((740, 1490),"Sibani Babu",(255,255,255),font=font)
draw.text((540, 1700),"Puri, Odisha",(255,255,255),font=font)

draw.text((1580, 2100),showtimein,(255,255,255),font=font)
draw.text((300, 2300),showtimeout,(255,255,255),font=font)
img.save('sample-out.jpg')

#cur.close()
#conn.close()
