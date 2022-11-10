import mysql.connector as ms
con=ms.connect(host='localhost', user='root', password ='123456', charset='utf8')
cur = con.cursor()
cur.execute("create database if not satellite")
cur.execute("use satellite")
cur.execute("create table if not exist satellite_identities(operator varchar(20), vel_kmps numeric(20) avel numeric(20), altitude numeric(20), orb_tme numeric(20), orb_inc numeric(20), lattitude numeric(20), longitude numeric(20), DOL date, TAO datetime, type varchar(3))")
cur.close()
con.close()
