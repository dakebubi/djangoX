import datetime

import MySQLdb

db = MySQLdb.connect(host="localhost", user="zwang", passwd="zwang", db="test");
c = db.cursor()



class demo(object):
    def test_query(self):
        hosp_id = "500bf1f4-48b9-407c-93de-ae3015fa282d";
        c.execute("""SELECT * FROM resource_permission_rule WHERE hosp_id = %s""", (hosp_id))
        print c.fetchone()

    def test_insert(self):
        n = c.executemany(
            """INSERT INTO resource_permission_rule (channel_id, hosp_id, include_or_exclude, is_delete, gmt_created,
            gmt_modified,
            staff_created, staff_modified)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            [
                (123, "12345", 0, 0, datetime.datetime.now(), datetime.datetime.now(), 10000, 10000),
                (124, "12345", 0, 0, datetime.datetime.now(), datetime.datetime.now(), 20000, 20000),
                (125, "12345", 0, 0, datetime.datetime.now(), datetime.datetime.now(), 30000, 30000)
            ])
        db.commit()
        print n


demo1 = demo()
demo1.test_query()
# demo1.test_insert()