import os

devicename = 'silver'

from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

try:
    import pymysql
except ImportError:
    pymysql = None
    os.system("pip3 install pymysql")
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None
    os.system("sudo apt install python-rpi.gpio python3-rpi.gpio")


class GPIORemote:
    def __init__(self):
        # f = open('/proc/cpuinfo', 'r')
        for line in open('/proc/cpuinfo', 'r'):
            if line[0:6] == 'Serial':
                self.serial = line[10:26]
            break
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setwarnings(False)
        # database setup
        self.connection = pymysql.connect(
            host='localhost',
            db='remote',
            user='root',
            password='ganteng',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.sql = None
        self.state = 0
        self.cursor = self.connection.cursor()
        try:
            with self.connection:
                self.cursor.execute("SELECT VERSION()")
                print(self.cursor.fetchone())
        except:
            print("Error when getting database version")

        try:
            with self.connection:
                self.sql = """CREATE TABLE IF NOT EXISTS raspberry (
                                serial CHAR(16) NOT NULL PRIMARY KEY,
                                name CHAR(10), 
                                setmode TINYINT NOT NULL,
                                state TINYINT NOT NULL ) """
                self.cursor.execute(self.sql)

                self.sql = """CREATE TABLE IF NOT EXISTS setting (
                                serial CHAR(16) NOT NULL,
                                channel TINYINT NOT NULL,
                                setup TINYINT NOT NULL,
                                val TINYINT ) """
                self.cursor.execute(self.sql)

                # read service state to run service
                self.sql = "SELECT state FROM raspberry WHERE serial=%s"

                if self.cursor.execute(self.sql, self.serial) == 0:
                    print("raspberry not found, registering.....")
                    self.sql = "INSERT INTO raspberry (serial, name, setmode, state) VALUES (%s, %s, %s, %s)"
                    print(self.sql)
                    registering = self.cursor.execute(self.sql, (self.serial, devicename, 11, 0))
                    if registering == 1:
                        print(self.serial, "is registered")

                self.state = self.cursor.fetchone()
                self.connection.commit()

                while self.state['state'] == 1:
                    # get raspberry setup
                    self.sql = "SELECT * FROM setting WHERE serial=%s"
                    self.cursor.execute(self.sql, self.serial)
                    res = self.cursor.fetchall()

                    for rpisetting in res:
                        ch = rpisetting['channel']
                        setup = rpisetting['setup']
                        val = rpisetting['val']
                        print("channel :", ch, "setup :", setup, "ch value :", val)
                        self.GPIO.setup(int(ch), int(setup))

                        if setup == 0:
                            self.GPIO.output(ch, val)
                        self.connection.commit()

        finally:
            self.connection.close()


if __name__ == '__main__':
    GPIORemote()

# try:
#     # test connection and show version
#
#     with connection:
#         cur = connection.cursor()
#         sql = "SELECT * FROM channel"
#         cur.execute(sql)
#         rpiset = cur.fetchall()
#         for mych in rpiset:
#             ch = mych["ch"]
#             chval = mych['val']
#             print("channel :", ch, "with values :", chval)
#             GPIO.setup(ch, GPIO.OUT)
#             GPIO.output(ch, chval)
#
# finally:
#     connection.close()
