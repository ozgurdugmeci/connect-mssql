import pypyodbc
id=[]
id.append(1)
con= pypyodbc.connect("DRIVER={SQL Server};Server=BORNEO;UID=sa;PWD=alterego123;Database=testo2")
cur=con.cursor()
cur.execute("SELECT * FROM tablo1 where id = ?",id)
report=cur.fetchall()
print (report)
cur.close()
con.close()
