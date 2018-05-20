import sqlite3
import numpy as np
import math, time
from vectors import ptToLine2
import serial

ser = serial.Serial("COM3", baudrate = 9600, timeout = 1)
time.sleep(2)
def sendValues(text):
    ser.write(text.encode("utf-8"))

def check():
    conn = sqlite3.connect("fingerdata.db")
    c = conn.cursor()

    c.execute("""SELECT xcoord FROM fproximal1 WHERE id > 0""")
    xproximal1 = c.fetchall()
    c.execute("""SELECT xcoord FROM fproximal2 WHERE id > 0""")
    xproximal2 = c.fetchall()
    c.execute("""SELECT xcoord FROM fproximal3 WHERE id > 0""")
    xproximal3 = c.fetchall()
    c.execute("""SELECT xcoord FROM fproximal4 WHERE id > 0""")
    xproximal4 = c.fetchall()
    c.execute("""SELECT xcoord FROM fproximal5 WHERE id > 0""")
    xproximal5 = c.fetchall()
    c.execute("""SELECT xcoord FROM fdistal1 WHERE id > 0""")
    xdistal1 = c.fetchall()
    c.execute("""SELECT xcoord FROM fdistal2 WHERE id > 0""")
    xdistal2 = c.fetchall()
    c.execute("""SELECT xcoord FROM fdistal3 WHERE id > 0""")
    xdistal3 = c.fetchall()
    c.execute("""SELECT xcoord FROM fdistal4 WHERE id > 0""")
    xdistal4 = c.fetchall()
    c.execute("""SELECT xcoord FROM fdistal5 WHERE id > 0""")
    xdistal5 = c.fetchall()

    c.execute("""SELECT ycoord FROM fproximal1 WHERE id > 0""")
    yproximal1 = c.fetchall()
    c.execute("""SELECT ycoord FROM fproximal2 WHERE id > 0""")
    yproximal2 = c.fetchall()
    c.execute("""SELECT ycoord FROM fproximal3 WHERE id > 0""")
    yproximal3 = c.fetchall()
    c.execute("""SELECT ycoord FROM fproximal4 WHERE id > 0""")
    yproximal4 = c.fetchall()
    c.execute("""SELECT ycoord FROM fproximal5 WHERE id > 0""")
    yproximal5 = c.fetchall()
    c.execute("""SELECT ycoord FROM fdistal1 WHERE id > 0""")
    ydistal1 = c.fetchall()
    c.execute("""SELECT ycoord FROM fdistal2 WHERE id > 0""")
    ydistal2 = c.fetchall()
    c.execute("""SELECT ycoord FROM fdistal3 WHERE id > 0""")
    ydistal3 = c.fetchall()
    c.execute("""SELECT ycoord FROM fdistal4 WHERE id > 0""")
    ydistal4 = c.fetchall()
    c.execute("""SELECT ycoord FROM fdistal5 WHERE id > 0""")
    ydistal5 = c.fetchall()

    c.execute("""SELECT zcoord FROM fproximal1 WHERE id > 0""")
    zproximal1 = c.fetchall()
    c.execute("""SELECT zcoord FROM fproximal2 WHERE id > 0""")
    zproximal2 = c.fetchall()
    c.execute("""SELECT zcoord FROM fproximal3 WHERE id > 0""")
    zproximal3 = c.fetchall()
    c.execute("""SELECT zcoord FROM fproximal4 WHERE id > 0""")
    zproximal4 = c.fetchall()
    c.execute("""SELECT zcoord FROM fproximal5 WHERE id > 0""")
    zproximal5 = c.fetchall()
    c.execute("""SELECT zcoord FROM fdistal1 WHERE id > 0""")
    zdistal1 = c.fetchall()
    c.execute("""SELECT zcoord FROM fdistal2 WHERE id > 0""")
    zdistal2 = c.fetchall()
    c.execute("""SELECT zcoord FROM fdistal3 WHERE id > 0""")
    zdistal3 = c.fetchall()
    c.execute("""SELECT zcoord FROM fdistal4 WHERE id > 0""")
    zdistal4 = c.fetchall()
    c.execute("""SELECT zcoord FROM fdistal5 WHERE id > 0""")
    zdistal5 = c.fetchall()

    conn.commit()
    conn.close()

    xp1 = []
    xp2 = []
    xp3 = []
    xp4 = []
    xp5 = []
    xd1 = []
    xd2 = []
    xd3 = []
    xd4 = []
    xd5 = []

    yp1 = []
    yp2 = []
    yp3 = []
    yp4 = []
    yp5 = []
    yd1 = []
    yd2 = []
    yd3 = []
    yd4 = []
    yd5 = []

    zp1 = []
    zp2 = []
    zp3 = []
    zp4 = []
    zp5 = []
    zd1 = []
    zd2 = []
    zd3 = []
    zd4 = []
    zd5 = []

    xsections0 = [xproximal1, xproximal2, xproximal3, xproximal4, xproximal5, xdistal1, xdistal2, xdistal3, xdistal4, xdistal5]
    xsections = [xp1, xp2, xp3, xp4, xp5, xd1, xd2, xd3, xd4, xd5]
    ysections0 = [yproximal1, yproximal2, yproximal3, yproximal4, yproximal5, ydistal1, ydistal2, ydistal3, ydistal4, ydistal5]
    ysections = [yp1, yp2, yp3, yp4, yp5, yd1, yd2, yd3, yd4, yd5]
    zsections0 = [zproximal1, zproximal2, zproximal3, zproximal4, zproximal5, zdistal1, zdistal2, zdistal3, zdistal4, zdistal5]
    zsections = [zp1, zp2, zp3, zp4, zp5, zd1, zd2, zd3, zd4, zd5]


    for i in range(len(xsections0)):
        for j in xsections0[i]:
                e = str(j)
                xsections[i].append(float(e[1:len(j)-3]))

    for i in range(len(ysections0)):
        for j in ysections0[i]:
                e = str(j)
                ysections[i].append(float(e[1:len(j)-3]))

    for i in range(len(zsections0)):
        for j in zsections0[i]:
                e = str(j)
                zsections[i].append(float(e[1:len(j)-3]))

    #getuserinput
    conn = sqlite3.connect("userfingerdata.db")
    c = conn.cursor()

    c.execute("""SELECT xcoord FROM proximal1 WHERE id > 0""")
    xproximal1 = c.fetchall()
    c.execute("""SELECT xcoord FROM proximal2 WHERE id > 0""")
    xproximal2 = c.fetchall()
    c.execute("""SELECT xcoord FROM proximal3 WHERE id > 0""")
    xproximal3 = c.fetchall()
    c.execute("""SELECT xcoord FROM proximal4 WHERE id > 0""")
    xproximal4 = c.fetchall()
    c.execute("""SELECT xcoord FROM proximal5 WHERE id > 0""")
    xproximal5 = c.fetchall()
    c.execute("""SELECT xcoord FROM distal1 WHERE id > 0""")
    xdistal1 = c.fetchall()
    c.execute("""SELECT xcoord FROM distal2 WHERE id > 0""")
    xdistal2 = c.fetchall()
    c.execute("""SELECT xcoord FROM distal3 WHERE id > 0""")
    xdistal3 = c.fetchall()
    c.execute("""SELECT xcoord FROM distal4 WHERE id > 0""")
    xdistal4 = c.fetchall()
    c.execute("""SELECT xcoord FROM distal5 WHERE id > 0""")
    xdistal5 = c.fetchall()

    c.execute("""SELECT ycoord FROM proximal1 WHERE id > 0""")
    yproximal1 = c.fetchall()
    c.execute("""SELECT ycoord FROM proximal2 WHERE id > 0""")
    yproximal2 = c.fetchall()
    c.execute("""SELECT ycoord FROM proximal3 WHERE id > 0""")
    yproximal3 = c.fetchall()
    c.execute("""SELECT ycoord FROM proximal4 WHERE id > 0""")
    yproximal4 = c.fetchall()
    c.execute("""SELECT ycoord FROM proximal5 WHERE id > 0""")
    yproximal5 = c.fetchall()
    c.execute("""SELECT ycoord FROM distal1 WHERE id > 0""")
    ydistal1 = c.fetchall()
    c.execute("""SELECT ycoord FROM distal2 WHERE id > 0""")
    ydistal2 = c.fetchall()
    c.execute("""SELECT ycoord FROM distal3 WHERE id > 0""")
    ydistal3 = c.fetchall()
    c.execute("""SELECT ycoord FROM distal4 WHERE id > 0""")
    ydistal4 = c.fetchall()
    c.execute("""SELECT ycoord FROM distal5 WHERE id > 0""")
    ydistal5 = c.fetchall()

    c.execute("""SELECT zcoord FROM proximal1 WHERE id > 0""")
    zproximal1 = c.fetchall()
    c.execute("""SELECT zcoord FROM proximal2 WHERE id > 0""")
    zproximal2 = c.fetchall()
    c.execute("""SELECT zcoord FROM proximal3 WHERE id > 0""")
    zproximal3 = c.fetchall()
    c.execute("""SELECT zcoord FROM proximal4 WHERE id > 0""")
    zproximal4 = c.fetchall()
    c.execute("""SELECT zcoord FROM proximal5 WHERE id > 0""")
    zproximal5 = c.fetchall()
    c.execute("""SELECT zcoord FROM distal1 WHERE id > 0""")
    zdistal1 = c.fetchall()
    c.execute("""SELECT zcoord FROM distal2 WHERE id > 0""")
    zdistal2 = c.fetchall()
    c.execute("""SELECT zcoord FROM distal3 WHERE id > 0""")
    zdistal3 = c.fetchall()
    c.execute("""SELECT zcoord FROM distal4 WHERE id > 0""")
    zdistal4 = c.fetchall()
    c.execute("""SELECT zcoord FROM distal5 WHERE id > 0""")
    zdistal5 = c.fetchall()


    conn.commit()
    conn.close()

    xp12 = []
    xp22 = []
    xp32 = []
    xp42 = []
    xp52 = []
    xd12 = []
    xd22 = []
    xd32 = []
    xd42 = []
    xd52 = []

    yp12 = []
    yp22 = []
    yp32 = []
    yp42 = []
    yp52 = []
    yd12 = []
    yd22 = []
    yd32 = []
    yd42 = []
    yd52 = []

    zp12 = []
    zp22 = []
    zp32 = []
    zp42 = []
    zp52 = []
    zd12 = []
    zd22 = []
    zd32 = []
    zd42 = []
    zd52 = []

    xsections02 = [xproximal1, xproximal2, xproximal3, xproximal4, xproximal5, xdistal1, xdistal2, xdistal3, xdistal4, xdistal5]
    xsections2 = [xp12, xp22, xp32, xp42, xp52, xd12, xd22, xd32, xd42, xd52]
    ysections02 = [yproximal1, yproximal2, yproximal3, yproximal4, yproximal5, ydistal1, ydistal2, ydistal3, ydistal4, ydistal5]
    ysections2 = [yp12, yp22, yp32, yp42, yp52, yd12, yd22, yd32, yd42, yd52]
    zsections02 = [zproximal1, zproximal2, zproximal3, zproximal4, zproximal5, zdistal1, zdistal2, zdistal3, zdistal4, zdistal5]
    zsections2 = [zp12, zp22, zp32, zp42, zp52, zd12, zd22, zd32, zd42, zd52]

              
    for i in range(len(xsections02)):
        for j in xsections02[i]:
                e = str(j)
                xsections2[i].append(float(e[1:len(j)-3]))

    for i in range(len(ysections02)):
        for j in ysections02[i]:
                e = str(j)
                ysections2[i].append(float(e[1:len(j)-3]))

    for i in range(len(zsections02)):
        for j in zsections02[i]:
                e = str(j)
                zsections2[i].append(float(e[1:len(j)-3]))

    transposex = 0
    transposey = 0
    transposez = 0

    for i in range(10):
        transposex += xsections[i][0] - xsections2[i][0]
    transposex/=10    
    for i in range(10):
        transposey += ysections[i][0] - ysections2[i][0]
    transposey/=10
    for i in range(10):
        transposez += zsections[i][0] - zsections2[i][0]
    transposez/=10

    for i in xsections2:
        for j in range(len(i)):
            i[j] = i[j] + transposex

    for i in ysections2:
        for j in range(len(i)):
            i[j] = i[j] + transposey

    for i in zsections2:
        for j in range(len(i)):
            i[j] = i[j] + transposez

    tot = 0

    if min(len(xp1), len(xp2), len(xp3), len(xp4), len(xp5)) > min(len(xp12), len(xp22), len(xp32), len(xp42), len(xp52)):
        ci = 0
        for i in range(min(len(xp12), len(xp22), len(xp32), len(xp42), len(xp52))):
            s1 = 0
            s2 = 0
            max1 = min(len(xp1), len(xp2), len(xp3), len(xp4), len(xp5))
            for j in range(10):
                cd = ptToLine2([xsections[j][ci], ysections[j][ci], zsections[j][ci]], [xsections[j][ci+1], ysections[j][ci+1], zsections[j][ci+1]], [xsections2[j][i], ysections2[j][i], zsections2[j][i]])
                s1 += cd
                if max1 > ci + 2:
                    nd = ptToLine2([xsections[j][ci+1], ysections[j][ci+1], zsections[j][ci+1]], [xsections[j][ci+2], ysections[j][ci+2], zsections[j][ci+2]], [xsections2[j][i], ysections2[j][i], zsections2[j][i]])
                    s2+=nd
            if s1 > s2:
                ci += 1
                tot += s2
            tot += s1
        average = tot/min(len(xp1), len(xp2), len(xp3), len(xp4), len(xp5))
    else:
        ci = 0
        for i in range(min(len(xp1), len(xp2), len(xp3), len(xp4), len(xp5))):
            s1 = 0
            s2 = 0
            max1 = min(len(xp12), len(xp22), len(xp32), len(xp42), len(xp52))
            for j in range(10):
                cd = ptToLine2([xsections2[j][ci], ysections2[j][ci], zsections2[j][ci]], [xsections2[j][ci+1], ysections2[j][ci+1], zsections2[j][ci+1]], [xsections[j][i], ysections[j][i], zsections[j][i]])
                s1 += cd
                if max1 > ci + 2:
                    nd = ptToLine2([xsections2[j][ci+1], ysections2[j][ci+1], zsections2[j][ci+1]], [xsections2[j][ci+2], ysections2[j][ci+2], zsections2[j][ci+2]], [xsections[j][i], ysections[j][i], zsections[j][i]])
                    s2+=nd
            if s1 > s2:
                ci += 1
                tot += s2
            tot += s1
        average = tot/min(len(xp12), len(xp22), len(xp32), len(xp42), len(xp52))

    print average
    if 1000-average < 400 and average < 1000:
        print "pass"
        sendValues("1")
        sendValues("3")
        sendValues("5")
    else:
        print "fail"
        sendValues("2")
        sendValues("4")
        sendValues("6")

check()
a = raw_input()
ser.close()




