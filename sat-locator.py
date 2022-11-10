#Title: Satellite Locator [Norse]
import mysql.connector as ms
from math import sqrt,sin,cos
from time import strftime,gmtime,sleep
con=ms.connect(host='localhost', user='root', password ='123456', charset='utf8', database ='satellite')
cur = con.cursor()
G=6.673*10**-11
M=5.98*10**24
R=6.3781*10**6
pi=3.1415
def add_sat_id():
    tag=input('Enter the name of the SATELLITE')
    opr=input('Enter the name of the operator')
    alt=float(input('Enter the altitude of the satellite'))
    oinc=float(input('Enter the orbital inclination of the satellite'))
    lattitude=float(input('Enter lattitude'))
    longitude=float(input('Enter longitude'))
    DOL=input('Enter the date of launch')
    TAO=input('Enter the time at orbit')
    type=input('Enter the type')
    vel=(sqrt(G*M/(R+(alt*1000))))/1000
    avel=vel/(R*10**-3)
    T=sqrt((4*(pi**2)*((R+(alt*1000))**3))/(G * M))
    a=(tag,opr,vel,avel,alt,T,oinc,lattitude,longitude,DOL,TAO,type)
    q = "insert into satellite_identities values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,a)
    con.commit()
def mod_sat_id():
    print("\n\n")
    print("*************************************************************")
    print("operator - to modify the operator name of the satellite")
    print("vel_kmps - to modify the operator name of the satellite")
    print("avel - to modify the angular velocity of the satellite")
    print("altitude - to modify the altitude of the satellite")
    print("orb_tme - to modify the orbital time of the satellite")
    print("orb_inc - to modify the orbital inclination in degrees of the satellite")
    print("lattitude - to modify the lattitude at orbit of the satellite")
    print("longitude - to modify the longitude at orbit of the satellite")
    print("DOL - to modify the date of launch of the satellite")
    print("TAO - to modify the time at orbit of the satellite")
    print("type - to modify the type of orbit of the satellite")
    print("*************************************************************")
    print("\n\n")
    mod=input("Enter what to modify? ")
    if mod=='tag':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the new tag name")
                a=(j,h,)
                q="update satellite_identities set tag = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
                break
        else:
            print("Not Present")
    elif mod == 'operator':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the operator name")
                a=(j,h,)
                q="update satellite_identities set operator = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'altitude':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=int(input("Enter the altitude"))
                vel1=(sqrt(G*M/(R+(j*1000))))/1000
                avel1=vel1/(R*10**-3)
                T1=sqrt((4*(pi**2)*((R+(j*1000))**3))/(G * M))
                a=(j,h,)
                b=(vel1,h,)
                c=(avel1,h,)
                d=(T1,h,)
                q="update satellite_identities set altitude = %s where tag= %s"
                q1="update satellite_identities set vel_kmps = %s where tag= %s"
                q2="update satellite_identities set avel = %s where tag= %s"
                q3="update satellite_identities set orb_tme = %s where tag= %s"
                cur.execute(q,a)
                cur.execute(q1,b)
                cur.execute(q2,c)
                cur.execute(q3,d)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'orb_inc':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the orbital inclination")
                a=(j,h,)
                q="update satellite_identities set orb_inc = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'lattitude':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the lattitude")
                a=(j,h,)
                q="update satellite_identities set lattitude = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'longitude':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the longitude")
                a=(j,h,)
                q="update satellite_identities set longitude = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'DOL':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the Date of Launch")
                a=(j,h,)
                q="update satellite_identities set DOL = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'TAO':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the TAO")
                a=(j,h,)
                q="update satellite_identities set TAO = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
    elif mod == 'type':
        h=input("Enter the tag name to be changed")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                j=input("Enter the type")
                a=(j,h,)
                q="update satellite_identities set type = %s where tag= %s"
                cur.execute(q,a)
                con.commit()
        else:
            print("Not Present")
def view():
    print("\n\n*******************************")
    print('tag - to see the name tags\nsel - to view the detail of a specific tag ')
    print("\n\n*******************************")
    view=input("Enter any one of the options")
    if view=='tag':
        cur.execute("select tag from satellite_identities")
        c=cur.fetchall()
        for i in c:
            print("[Tag Name]",i[0])
    elif view=='sel':
        h=input("Enter the tag name")
        cur.execute("select tag from satellite_identities")
        b = cur.fetchall()
        for i in b:
            if h in i:
                print("\n\n")
                print("*************************************************************")
                print("operator - to view the operator name of the satellite")
                print("vel_kmps - to view the velocity in kmps of the satellite")
                print("avel - to view the angular velocity of the satellite")
                print("altitude - to view the altitude of the satellite")
                print("orb_tme - to view the orbital time of the satellite")
                print("orb_inc - to view the orbital inclination in degrees of the satellite")
                print("lattitude - to view the lattitude at orbit of the satellite")
                print("longitude - to view the longitude at orbit of the satellite")
                print("DOL - to view the date of launch of the satellite")
                print("TAO - to view the time at orbit of the satellite")
                print("type - to view the type of orbit of the satellite")
                print("*************************************************************")
                print("\n\n")
                j=input("Enter what to view")
                if j == "operator":
                    a=(h,)
                    q="select operator from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[operator]",r[0])
                    break
                elif j == "vel_kmps":
                    a=(h,)
                    q="select vel_kmps from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[velocity-kmps]",r[0])
                    break
                elif j == "avel":
                    a=(h,)
                    q="select avel from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[angular-velocity]",r[0])
                    break
                elif j == "altitude":
                    a=(h,)
                    q="select altitude from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[altitude-Kms]",r[0])
                    break
                elif j == "orb_tme":
                    a=(h,)
                    q="select orb_tme from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[orbital-time]",r[0])
                    break
                elif j == "orb_inc":
                    a=(h,)
                    q="select orb_inc from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[orbital-inclination]",r[0])
                    break
                elif j == "lattitude":
                    a=(h,)
                    q="select lattitude from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[lattitude]",r[0])
                    break
                elif j == "longitude":
                    a=(h,)
                    q="select longitude from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[longitude]",r[0])
                    break
                elif j == "DOL":
                    a=(h,)
                    q="select DOL from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[date-of-launch]",r[0])
                    break
                elif j == "TAO":
                    a=(h,)
                    q="select TAO from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchall()
                    print("[time-at-orbit]",r[0][0])
                    break
                elif j == "type":
                    a=(h,)
                    q="select type from satellite_identities where tag =%s"
                    cur.execute(q,a)
                    r=cur.fetchone()
                    print("[type]",r[0])
                    break
                else:
                    print("wrong choice")
        else:
            print("Not Present")
    else:
        print("wrong option")
            
def Del():
    h=input("Enter the tag name to be deleted")
    cur.execute("select tag from satellite_identities")
    b = cur.fetchall()
    for i in b:
        if h in i:
            a=(h,)
            q="delete from satellite_identities where tag= %s"
            cur.execute(q,a)
            con.commit()
    else:
        print("Not Present")
def date_time():
    t=strftime("%H:%M:%S",gmtime())
    d=strftime("%Y-%m-%d",gmtime())
    a=(int(t[0:2]),int(t[3:5]),int(t[6:]),int(d[0:4]),int(d[5:7]),int(d[9:]))
    d=str(D)
    sec=a[2]+ (a[1]*60) + (a[0]*3600) + (a[5]-1)* 86400
    for i in range(1,a[4]):
        if i in (1,3,5,7,8,10):
            sec=sec + (2678400)
        elif i in (4,6,9,11):
            sec=sec + (2592000)
        elif i == 2:
            if a[3]/4 == 0:
                sec = sec + (2505600)
            else:
                sec = sec + (2419200)
    global y3
    y3=strftime("%Y",gmtime())
    return sec
def date_time_stamp():
    t=strftime("[%H:%M:%S]",gmtime())
    d=strftime("[%Y-%m-%d]",gmtime())
    print(d,end='')
    print(t,end='')
def lattitude(t1):
    a=()
    lat=0
    u=0
    tp='d'
    Vy = ((vo*1000) * R)/(R + (alt*1000))
    Voy = Vy * sin(o*0.0174)
    dr = Voy/(to/4)
    y = (((Voy)*(to/4) - (0.5*dr*((to/4)**2))) * 1.5)/111000
    for i in range (1,t1):
        dr1= Voy/(i)
        y1 = (((Voy)*(i) - (0.5*dr1*((i)**2))) * 1.5)/111000
        if y1+1 < y:
            a=a+(y1,)
        else:
            break
    t2=0
    for i in range (0,999999999):
        if 4*len(a)*i > t1:
            t2=4*len(a)*i
            break
    t=t2-t1
    b=()
    for i in range (1,len(a)):
        b=b+(a[-i],)
    c=()
    for i in range (1,len(a)):
        c=c+(-a[i],)
    d=()
    for i in range (1,len(a)):
        d=d+(-a[-i],)
    tot=a+b+c+d
    ti=0
    a1=0
    for i in tot:
        if i >= l and l>0:
            ti=i
            a1=tot.index(i)
        elif i <= l and l <0:
            ti=i
            a1=tot.index(i)
    if tp=='d':
        if ti>0:
            a1=tot.index(ti,a1+1)
        elif ti<0:
            a1=tot.index(ti,a1+1)
    ln=len(tot)
    if a1 + t < ln:
        lat=(tot[a1+(t//1)])
    else:
        b=(a1 + t) - ln
        lat=(tot[(b//1)])
    return lat
def longitude(t1):
    Vx = ((vo*1000) * R)/(R + (alt*1000))
    Vox = (Vx * cos(o*0.0174))/111000
    log1 = Vox * t1
    log2=0
    for i in range (0,t1):
        if 360 * i > log1:
            log2 = 360 * i
            break
    log0 = log2 - log1
    log = 360 - log0 + lo
    if log < 180:
        return log
    else:
        return (log-360)
def country(t1):
    if lattitude(t1) < 83.766245 and longitude(t1) > -62.464923  and lattitude(t1) > 60.556355 and longitude(t1) < -13.913123:
        print("Greenland")
    elif lattitude(t1) < 69.787405 and lattitude(t1) >12.665303 and longitude(t1) > -162.272499 and longitude(t1) < -59.088904:
        print("North America")
    elif lattitude(t1) < 9.040570 and lattitude(t1) >-54.506228 and longitude(t1) > -98.463905 and longitude(t1) < -36.3237342:
        print("South America")
    elif lattitude(t1) < 36.123045 and lattitude(t1) >23.667959 and longitude(t1) > -12.506875 and longitude(t1) < 32.668908:
        print("North Africa")
    elif lattitude(t1) < 16.070400 and lattitude(t1) >-13.642476 and longitude(t1) > 11.223595 and longitude(t1) < 25.813439:
        print("Central Africa")
    elif lattitude(t1) < 9.560980 and lattitude(t1) > -17.535851  and longitude(t1) > 27.747033 and longitude(t1) < 51.653283:
        print("East Africa")
    elif lattitude(t1) < 20.079963 and lattitude(t1) > 5.553976 and longitude(t1) > -21.647499 and longitude(t1) < 9.465783:
        print("West Africa")
    elif lattitude(t1) < -22.651237 and lattitude(t1) >-34.358593 and longitude(t1) > 13.332970 and longitude(t1) < 35.305627:
        print("Southern Africa")
    elif lattitude(t1) < 69.696498 and lattitude(t1) > 41.197908 and longitude(t1) > -8.991249 and longitude(t1) < 30.383752:
        print("Europe")
    elif lattitude(t1) < 40.932844 and lattitude(t1) >16.744887 and longitude(t1) > 37.237221 and longitude(t1) < 61.236864:
        print("Middle East")
    elif lattitude(t1) < 50.673051 and lattitude(t1) >40.236661 and longitude(t1) > 52.272020 and longitude(t1) < 78.287645:
        print("Central Asia")
    elif lattitude(t1) < 32.200889 and lattitude(t1) >7.437504 and longitude(t1) > 62.379442 and longitude(t1) < 94.723192:
        print("South Asia")
    elif lattitude(t1) < 47.686746 and lattitude(t1) > 19.713836 and longitude(t1) > 86.285692 and longitude(t1) < 143.590380:
        print("East Asia")
    elif lattitude(t1) < 19.548272 and lattitude(t1) >-7.113022 and longitude(t1) > 94.283739 and longitude(t1) < 134.889208:
        print("South East Asia")
    elif lattitude(t1) < -14.701705 and lattitude(t1) >-42.367575 and longitude(t1) > 113.180223 and longitude(t1) < 153.522020:
        print("Australia")
    elif lattitude(t1) < -34.925111 and lattitude(t1) >-47.031735 and longitude(t1) > 166.433720 and longitude(t1) < 177.815384:
        print("New Zealand")
    elif lattitude(t1) < 73.627205 and lattitude(t1) >53.809283 and longitude(t1) > 44.487316 and longitude(t1) < 165.399023:
        print("Russia")
    elif lattitude(t1) < -68.440916 and lattitude(t1) >-84.969265 and longitude(t1) > -179.0000000 and longitude(t1) < 179.000000:
        print("Antartica")
    else:
        print("OCN / NOT - SPECIFIED / ISLAND")

w1="\t\t\t\t\t\t\t\t\t\t\tWelcome to Project Norse - Satellite Locator"
w2="\t\t\t\t\t\t\t\t\t\t\t Choose any one of the options given below"
w3="\t\t\t\t\t\t\t\t\t 1. Type `add` to add the details of a satellite"
w4="\t\t\t\t\t\t\t\t\t 2. Type `mod` to modify the details of a satellite"
w5="\t\t\t\t\t\t\t\t\t 3. Type `view` to view the details of a satellite"
w6="\t\t\t\t\t\t\t\t\t 4. Type `del` to delete the details of a satellite"
w7="\t\t\t\t\t\t\t\t\t 5. Type `curloctd` to display the current location of a satellite with time and date stamp"
w8="\t\t\t\t\t\t\t\t\t 6. Type `lcurloctd` to display the current location of a satellite with time and date stamp in loop"
for i in w1:
    print(i,end='')
    sleep(0.006525)
print()
for i in w2:
    print(i,end='')
    sleep(0.006525)
print()
for i in w3:
    print(i,end='')
    sleep(0.006525)
print()
for i in w4:
    print(i,end='')
    sleep(0.006525)
print()
for i in w5:
    print(i,end='')
    sleep(0.006525)
print()
for i in w6:
    print(i,end='')
    sleep(0.006525)
print()
for i in w7:
    print(i,end='')
    sleep(0.006525)
print()
for i in w8:
    print(i,end='')
    sleep(0.006525)
print()
i = 'y'
while i == "y":
    inp=input("Enter your choice :")
    if inp == 'add':
        i = 'y'
        while i == 'y':
            add_sat_id()
            y=input("Add another Satellite's details? <y/n>")
            if y == 'n':
                i == y
                break
            elif y == 'y':
                i == y
            else:
                print('Wrong option....Auto Reject')
    elif inp == 'mod':
        i = 'y'
        while i == 'y':
            mod_sat_id()
            y=input("Modify anymore Satellite's details? <y/n>")
            if y == 'n':
                break
            elif y == 'y':
                i == y
            else:
                print('Wrong option....Auto Reject')
    elif inp == 'del':
        i = 'y'
        while i == 'y':
            Del()
            y=input("Delete anymore Satellite's details? <y/n>")
            if y == 'n':
                break
            elif y == 'y':
                i == y
            else:
                print('Wrong option....Auto Reject')
    elif inp == 'view':
        i = 'y'
        while i == 'y':
            view()
            y=input("View anymore Satellite's details? <y/n>")
            if y == 'n':
                break
            elif y == 'y':
                i == y
            else:
                print('Wrong option....Auto Reject')
    elif inp == 'curloctd':
        sat=input('Enter the satellites name')
        o=t=l=lo=D=T=0
        a= cur.execute('select * from satellite_identities')
        b=cur.fetchall()
        for i in range(len(b)):
            if b[i][0]==sat:
                vo=b[i][2]
                alt=b[i][4]
                to=b[i][5]
                if b[i][6] > 90:
                    o=b[i][6]-90
                else:
                    o=b[i][6]
                l=b[i][7]
                lo=b[i][8]
                D=(b[i][9])
                T=(b[i][10])
        d=str(D)
        y2=int(d[0:4])
        t1=date_time()
        for i in range(y2,int(y3)):
            if i%4==0:
                t1 = t1 + 31622400
            else:
                t1 = t1 + 31536000
        date_time_stamp()
        print("Lattitude: ",lattitude(t1),end='  ')
        print("Longitude: ",longitude(t1), end='   ')
        print("Country: ",end='   ')
        country(t1)
    elif inp == 'lcurloctd':
        sat=input('Enter the satellites name')
        o=t=l=lo=D=T=0
        a= cur.execute('select * from satellite_identities')
        b=cur.fetchall()
        for i in range(len(b)):
            if b[i][0]==sat:
                vo=b[i][2]
                alt=b[i][4]
                to=b[i][5]
                if b[i][6] > 90:
                    o=b[i][6]-90
                else:
                    o=b[i][6]
                l=b[i][7]
                lo=b[i][8]
                D=(b[i][9])
                T=(b[i][10])
        d=str(D)
        y2=int(d[0:4])
        t1=date_time()
        for i in range(y2,int(y3)):
            if i%4==0:
                t1 = t1 + 31622400
            else:
                t1 = t1 + 31536000
        i=1
        while True:
            date_time_stamp()
            print("Lattitude: ",lattitude(t1+i),end='  ')
            print("Longitude: ",longitude(t1+i), end='   ')
            print("Region: ",end='   ')
            country(t1+i)
            sleep(1)
            i=i+1
    else:
        print("<Error> Wrong option")
    y=input("Run the programs again? <y/n>")
    if y == 'n':
        print('Program-Closed')
        i == y
        break
    elif y == 'y':
        i == y
    else:
        print('Wrong option....Auto Quit')
cur.close()
con.close()
