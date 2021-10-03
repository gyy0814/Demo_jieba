import logging

import pymysql


def ORDP_run(sql):
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


def mysql_run(sql):
    try:
        db = pymysql.connect(
            host="192.168.3.18",
            user="ORDP",
            password="ORDP",
            port=32771,
            database="TRAINS",
            charset="utf8"
        )
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
    except Exception as err:
        logging.error(err)


TRAINS_dict = dict()


def dict_add(type, id, boss, numb):
    if type not in TRAINS_dict:
        TRAINS_dict[type] = list()
    train_dict = dict()
    train_dict['type'] = type
    train_dict['id'] = id
    train_dict['boss'] = boss
    train_dict['numb'] = numb
    TRAINS_dict[type].append(train_dict)


# req = ORDP_run('SHOW TABLES')
# print(req)
def fenlei_1():
    req = ORDP_run('SELECT * FROM chekuang')
    for r in req:
        train_name = r[0]
        train_boss = r[1]
        train_numb = r[2]

        '''和谐电机车分类方法'''
        if train_name.startswith('HXD_') or train_name.startswith('HXN_'):
            # print(f'机车:{train_name} 配属:{train_boss} 整备率:{train_numb}')
            if train_name[-1].isdecimal():
                train_type = train_name[:-4]
                train_id = train_name[-4:]
                dict_add(train_type,train_id,train_boss,train_numb)
                # print(train_name, ' = ', train_type, ' + ', train_id)
            else:
                train_type = train_name[:-5]
                train_id = train_name[-5:]
                dict_add(train_type,train_id,train_boss,train_numb)
                # print(train_name, ' = ', train_type, ' + ', train_id)

        elif train_name.startswith('DF'):
            # print(f'机车:{train_name} 配属:{train_boss} 整备率:{train_numb}')
            if train_name.count('_') == 0:
                train_type = train_name[:3]
                train_id = train_name[3:]
                dict_add(train_type,train_id,train_boss,train_numb)
                # print(train_name, ' = ', train_type, ' + ', train_id)
            else:
                try:
                    train_type = train_name.split('_')[0]
                    train_id = train_name.split('_')[1]
                    dict_add(train_type,train_id,train_boss,train_numb)
                    # print(train_name, ' = ', train_type, ' + ', train_id)
                except Exception as e:
                    print('error:', train_name)

        elif train_name.startswith('SS'):
            if train_name.count('_') == 1:
                train_type = train_name.split('_')[0]
                train_id = train_name.split('_')[1]
                dict_add(train_type,train_id,train_boss,train_numb)
                # print(train_name, ' = ', train_type, ' + ', train_id)
        else:
            print('无法分类', train_name)
            pass
def fenlei_2():
    req = ORDP_run('SELECT * FROM chekuang')
    for r in req:
        train_name = r[0]
        train_boss = r[1]
        train_numb = r[2]
        if train_name.count('_') == 1:
            # print(train_name.split('_')[0],"--",train_name.split('_')[1])
            pass
        elif train_name.count('_') == 2:
            print(train_name,train_name.split('_')[0],"--",train_name.split('_')[1])
            pass
        else:
            # print("奇奇怪怪的车",train_name)
            pass


def tianjiajilu():
    print(TRAINS_dict)


    sql = "CREATE TABLE `HXD1` (" \
          "`TYPE` TEXT NULL," \
          "`ID` TEXT NULL," \
          "`BOSS` TEXT NULL," \
          "`NUMB` TEXT NULL" \
          ") " \
          "COLLATE='utf8mb4_0900_ai_ci'" \
          ";"

    sql = "SHOW TABLES;"
    print(mysql_run(sql))
    sql = """INSERT INTO HXD1(
             TYPE, ID, BOSS, NUMB)
             VALUES ('123','2','3','4')"""
    mysql_run(sql)
    sql = "select * from HXD1;"
    print(mysql_run(sql))
fenlei_2()