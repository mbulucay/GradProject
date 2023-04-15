import pyodbc 
import time

def convertSQLDateTimeToTimestamp(value):
    print(value)

    return time.mktime(time.strptime(value, '%Y-%m-%d %H:%M:%S'))


cnxn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-ULV9D0K\MSSQLSERVER03;"
    "Database=EQ;"
    "Trusted_Connection=yes;"
)


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM EQ.dbo.EQ')
# ret = cursor.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'EQ'")

# file = open("./dataset.txt", "w", encoding="utf-8")
# file.write("id,timestamp,location,latitude,longitude,magnitude,depth\n")
count = 0

for row in cursor:

    l = list(row)
    
    id = int(l[0])
    timestamp = l[1].strftime("%x %X")
    location = l[2]
    
    latitude = float(l[3])
    longitude = float(l[4])
    magnitude = float(l[5])
    depth = float(l[6])

    # file.write(str(id)+","+timestamp+","+location+","+str(latitude)+","+str(longitude)+","+str(magnitude)+","+str(depth)+"\n")
    if(magnitude >= 5.0):
        print(row)
        count += 1
        # str = str(id)+","+timestamp+","+location+","+str(latitude)+","+str(longitude)+","+str(magnitude)+","+str(depth)+"\n"
        # print(str)
    # file.write(str)

print(count)
