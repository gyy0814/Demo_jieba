import pymysql
import logging


def sql_run(sql):
    try:
        db = pymysql.connect(
            host="123.206.56.54",
            user="chaxun",
            password="cha13579",
            port=3306,
            database="yxb2",
            charset="utf8"
        )
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Exception as err:
        logging.error(err)


def scan():
    sql_run("SELECT * FROM sijixinxi WHERE =1")
    pass
