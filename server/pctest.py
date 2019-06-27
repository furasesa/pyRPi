import pymysql

# connect to the database
connection = pymysql.connect(
    host='localhost',
    db='test',
    user='root',
    password='ganteng',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor )
try:
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print(version)

    # with connection:
    #     cur = connection.cursor()
    #     cur.execute("INSERT INTO books (Title,SeriesID,AuthorID) VALUES ('Book of Jungle','2','2')")
    # connection.commit()
    with connection:
        cur = connection.cursor()
        sql="SELECT * FROM books WHERE BookID=%s"
        cur.execute(sql, (1, ))
        rows = cur.fetchall()
        print(rows)

finally:
    connection.close()
