from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector

from PIL import Image, ImageChops,ImageStat
import sys, fsdk, math, ctypes, time
from fsdk import FSDK
import mysql.connector
import datetime
import time



#from __future__ import print_function
import sys, fsdk, math, ctypes, time
from fsdk import FSDK

import mysql.connector
import sys, fsdk, math, ctypes, time
import datetime
from datetime import date
start_date=date.today()
date_1 = datetime.datetime.now().strftime('%d-%b-%Y')
plus_one_hour = datetime.datetime.strptime(date_1,'%d-%b-%Y') + datetime.timedelta(days=2)
print(plus_one_hour.strftime("%d-%b-%Y"))



import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')
@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')
@app.route("/NewUser1")
def NewUser1():
    return render_template('NewUser.html')
@app.route("/AdminHome")
def AdminHome():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)

@app.route("/UserHome")
def UserHome():
    uname=session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where UserName='"+uname+"' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)

@app.route("/NewProduct")
def NewProduct():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    return render_template('NewProduct.html', data=data)


@app.route("/AProductInfo")
def AProductInfo():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    return render_template('AProductInfo.html', data=data)

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
           conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM regtb ")
           data = cur.fetchall()
           return render_template('AdminHome.html', data=data)
       else:
           alert = 'Username or Password is wrong'
           return render_template('goback.html', data=alert)


@app.route("/newproduct1", methods=['GET', 'POST'])
def newproduct1():
    if request.method == 'POST':
        #cname = session['Cname']

        Cname = request.form['Cname']
        Ptype = request.form['Ptype']
        Pname = request.form['Pname']
        color = request.form['color']
        price = request.form['price']
        Uvideo = request.form['Uvideo']
        spec = request.form['spec']

        file = request.files['file']
        file.save("static/upload/" + secure_filename(file.filename))


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO protb VALUES ('','"+ Cname +"','" + Ptype + "','" + Pname + "','" + color + "','" + price  + "','" + Uvideo + "','" + spec + "','" + file.filename + "')")
        conn.commit()
        conn.close()
        alert = 'Product register successfully'

    return render_template('goback.html',data=alert)

@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        if request.form["submit"] == "Submit":
            Cname = request.form['Cname']
            Ptype = request.form['Ptype']
            Pname = request.form['Pname']
            color = request.form['color']
            price = request.form['price']
            Uvideo = request.form['Uvideo']
            spec = request.form['spec']

            file = request.files['file']
            file.save("static/upload/" + file.filename)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO protb VALUES ('','" + Cname + "','" + Ptype + "','" + Pname + "','" + color + "','" + price + "','" + Uvideo + "','" + spec + "','" + file.filename + "')")
            conn.commit()
            conn.close()
            alert = 'Product register successfully'
            return render_template('goback.html', data=alert)

        elif request.form["submit"] == "Update":

            Pid = request.form['Pid']
            Cname = request.form['Cname']
            Ptype = request.form['Ptype']
            Pname = request.form['Pname']
            color = request.form['color']
            price = request.form['price']
            Uvideo = request.form['Uvideo']
            spec = request.form['spec']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
            cursor = conn.cursor()
            cursor.execute(
                "update  protb set CompanyName ='" + Cname + "',ProductType='" + Ptype + "',ProductName='" + Pname + "',Color='" + color + "',Price='" + price + "',VideoUrl='" + Uvideo + "',Specifications='" + spec + "' where id='"+Pid+"' ")
            conn.commit()
            conn.close()
            alert = 'Record Updated!'
            return render_template('goback.html', data=alert)

        elif request.form["submit"] == "Search":
            Pid = request.form['Pid']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb where id='"+ Pid +"' ")
            data = cur.fetchone()

            if data:
                pid=data[0]
                Cname = data[1]
                Ptype = data[2]
                Pname = data[3]
                color = data[4]
                price = data[5]
                Uvideo = data[6]
                spec = data[7]

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
                # cursor = conn.cursor()
                cur = conn.cursor()
                cur.execute("SELECT * FROM protb ")
                data = cur.fetchall()

                return render_template('Newproduct.html', Pid=pid,Cname=Cname,Ptype=Ptype,Pname=Pname,color=color,price=price,Uvideo=Uvideo,spec=spec)

            else:
                return 'Incorrect username / password !'



@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uid = request.form['uid']

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "','"+uid+"')")
        conn.commit()
        conn.close()
        # return 'file register successfully'


    return render_template('UserLogin.html')

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is error:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )



@app.route("/Search")
def Search():



    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    return render_template('Search.html',data=data)

@app.route("/typesearch", methods=['GET', 'POST'])
def typesearch():

    cname = request.form['Cname']
    ptype = request.form['Ptype']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from protb where CompanyName='" + cname + "' and ProductType='" + ptype + "'")
    data = cursor.fetchone()
    if data is None:
        alert = 'Product Not Found!'
        return render_template('goback.html', data=alert)
    else:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
        data = cur.fetchall()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cur = conn.cursor()
        cur.execute("SELECT ProductId,Image,ProductName,Price FROM temptb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
        data1 = cur.fetchall()
        return render_template('Search.html', data=data, data1=data1)



@app.route("/Book", methods=['GET', 'POST'])
def Book():
    if request.method == 'POST':
        from uuid import getnode as get_mac
        #mac = get_mac()
        import LiveRecognition1  as liv1
        liv1.examvales()

        # liv1.att()

        # print(ExamName)

        del sys.modules["LiveRecognition1"]


        uname = session['uname']
        pid = session['pid']

        qty = request.form['qty']
        ctype = request.form['ctype']
        cardno = request.form['cardno']
        cvno = request.form['cvno']

        Bookingid = ''
        ProductName =''
        UserName= uname
        Mobile=''
        Email=''
        Qty = qty
        Amount=''
        Mac=get_mac()

        CardType= ctype
        CardNo=cardno
        CvNo=cvno
        date = datetime.datetime.now().strftime('%d-%b-%Y')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[3]
            price = data[5]

            Amount= float(price) *float(Qty)

            print(Amount)

        else:
            return 'Incorrect username / password !'



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  regtb where  UserName='" + uname + "'")
        data = cursor.fetchone()

        if data:
            Mobile = data[4]
            Email= data[3]


        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
        cursor = conn.cursor()
        cursor.execute("SELECT  count(*) as count  FROM  booktb  ")
        data = cursor.fetchone()

        if data:
            count = data[0]

            if count == 0:
                count =1;
            else:
                count+=1




        else:
            return 'Incorrect username / password !'
        print(count)

        Bookingid="BOOKID00" + str(count)

        def examvales():
            global ExamName1
            global SubjectName1
            global Date1
            global Degree1
            global Department1
            global Year1

        # ExamName1 = ExamName
        # SubjectName1 = SubjectName
        # Date1 = Date
        # Degree1 = Degree
        # Department1 = Department
        # Year1 = Year11

        # print(ExamName1)
        # print(SubjectName1)
        # print(Date1)
        # print(Degree1)
        # print(Department1)
        # print(Year1)

        license_key = "fVrFCzYC5wOtEVspKM/zfLWVcSIZA4RNqx74s+QngdvRiCC7z7MHlSf2w3+OUyAZkTFeD4kSpfVPcRVIqAKWUZzJG975b/P4HNNzpl11edXGIyGrTO/DImoZksDSRs6wktvgr8lnNCB5IukIPV5j/jBKlgL5aqiwSfyCR8UdC9s="

        if not fsdk.windows:
            print('The program is for Microsoft Windows.');
            exit(1)
        import win

        trackerMemoryFile = "tracker70.dat"

        FONT_SIZE = 30

        print("Initializing FSDK... ", end='')
        FSDK.ActivateLibrary(license_key);
        FSDK.Initialize()
        print("OK\nLicense info:", FSDK.GetLicenseInfo())

        FSDK.InitializeCapturing()
        print('Looking for video cameras... ', end='')
        camList = FSDK.ListCameraNames()

        if not camList: print("Please attach a camera.");
        print(camList[0])  # camList[0].devicePath

        camera = camList[0]  # choose the first camera (0)
        print("using '%s'" % camera)
        formatList = FSDK.ListVideoFormats(camera)
        # print(*zip(range(len(formatList)), formatList), sep='\n')
        print(*formatList[0:5], sep='\n')
        if len(formatList) > 5: print('...', len(formatList) - 5, 'more formats (skipped)...')

        vfmt = formatList[0]  # choose the first format: vfmt.Width, vfmt.Height, vfmt.BPP
        print('Selected camera format:', vfmt)
        FSDK.SetVideoFormat(camera, vfmt)

        print("Trying to open '%s'... " % camera, end='')
        camera = FSDK.OpenVideoCamera(camera)
        print("OK", camera.handle)

        try:
            fsdkTracker = FSDK.Tracker.FromFile(trackerMemoryFile)
        except:
            fsdkTracker = FSDK.Tracker()  # creating a FSDK Tracker

        fsdkTracker.SetParameters(  # set realtime face detection parameters
            RecognizeFaces=True, DetectFacialFeatures=True,
            HandleArbitraryRotations=True, DetermineFaceRotationAngle=False,
            InternalResizeWidth=256, FaceDetectionThreshold=5
        )

        need_to_exit = False

        def WndProc(hWnd, message, wParam, lParam):
            global capturedFace
            if message == win.WM_CTLCOLOREDIT:
                fsdkTracker.SetName(capturedFace, win.GetWindowText(inpBox))
            if message == win.WM_DESTROY:
                global need_to_exit
                need_to_exit = True
            else:
                if message == win.WM_MOUSEMOVE:
                    updateActiveFace()
                    return 1
                if message == win.WM_LBUTTONDOWN:
                    if activeFace and capturedFace != activeFace:
                        capturedFace = activeFace
                        win.SetWindowText(inpBox, fsdkTracker.GetName(capturedFace))
                        win.ShowWindow(inpBox, win.SW_SHOW)
                        win.SetFocus(inpBox)
                    else:
                        capturedFace = None
                        win.ShowWindow(inpBox, win.SW_HIDE)
                    return 1
            return win.DefWindowProc(hWnd, message, win.WPARAM(wParam), win.LPARAM(lParam))

        wcex = win.WNDCLASSEX(cbSize=ctypes.sizeof(win.WNDCLASSEX), style=0, lpfnWndProc=win.WNDPROC(WndProc),
                              cbClsExtra=0, cbWndExtra=0, hInstance=0, hIcon=0,
                              hCursor=win.LoadCursor(0, win.IDC_ARROW), hbrBackground=0,
                              lpszMenuName=0, lpszClassName=win.L("My Window Class"), hIconSm=0)
        win.RegisterClassEx(wcex)

        hwnd = win.CreateWindowEx(win.WS_EX_CLIENTEDGE, win.L("My Window Class"), win.L("Live Recognition"),
                                  win.WS_SYSMENU | win.WS_CAPTION | win.WS_CLIPCHILDREN,
                                  100, 100, vfmt.Width, vfmt.Height, *[0] * 4)
        win.ShowWindow(hwnd, win.SW_SHOW)

        # textBox = win.CreateWindow(win.L("STATIC"), win.L("Click face to name it"), win.SS_CENTER | win.WS_CHILD, 0, 0, 0, 0, hwnd, 0, 0, 0)
        # myFont = win.CreateFont(30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, win.L("Microsoft Sans Serif"))
        # win.SendMessage(textBox, win.WM_SETFONT, myFont, True);
        # win.SetWindowPos(textBox, 0, 0, vfmt.Height, vfmt.Width, 80, win.SWP_NOZORDER)
        # win.ShowWindow(textBox, win.SW_SHOW)

        inpBox = win.CreateWindow(win.L("EDIT"), win.L(""), win.SS_CENTER | win.WS_CHILD, 0, 0, 0, 0, hwnd, 0, 0, 0)
        myFont = win.CreateFont(30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, win.L("Microsoft Sans Serif"))
        win.SendMessage(inpBox, win.WM_SETFONT, myFont, True);
        win.SetWindowPos(inpBox, 0, 0, vfmt.Height - 80, vfmt.Width, 80, win.SWP_NOZORDER)
        win.UpdateWindow(hwnd)

        def dot_center(dots):  # calc geometric center of dots
            return sum(p.x for p in dots) / len(dots), sum(p.y for p in dots) / len(dots)

        class LowPassFilter:  # low pass filter to stabilize frame size
            def __init__(self, a=0.35): self.a, self.y = a, None

            def __call__(self, x): self.y = self.a * x + (1 - self.a) * (self.y or x); return self.y

        class FaceLocator:
            def __init__(self, fid):
                self.lpf = None
                self.center = self.angle = self.frame = None
                self.fid = fid

            def isIntersect(self, state):
                (x1, y1, x2, y2), (xx1, yy1, xx2, yy2) = self.frame, state.frame
                return not (x1 >= xx2 or x2 < xx1 or y1 >= yy2 or y2 < yy1)

            def isActive(self):
                return self.lpf is not None

            def is_inside(self, x, y):
                x -= self.center[0];
                y -= self.center[1]
                a = self.angle * math.pi / 180
                x, y = x * math.cos(a) + y * math.sin(a), x * math.sin(a) - y * math.cos(a)
                return (x / self.frame[0]) ** 2 + (y / self.frame[1]) ** 2 <= 1

            def draw_shape(self, surf):
                container = surf.beginContainer()
                surf.translateTransform(*self.center).rotateTransform(self.angle).ellipse(facePen,
                                                                                          *self.frame)  # draw frame
                if activeFace == self.fid:
                    surf.ellipse(faceActivePen, *self.frame)  # draw active frame
                if capturedFace == self.fid:
                    surf.ellipse(faceCapturedPen, *self.frame)  # draw captured frame
                surf.endContainer(container)

            def draw(self, surf, path, face_id=None):
                if face_id is not None:
                    ff = fsdkTracker.GetFacialFeatures(0, face_id)
                    if self.lpf is None: self.lpf = LowPassFilter()
                    xl, yl = dot_center([ff[k] for k in FSDK.FSDKP_LEFT_EYE_SET])
                    xr, yr = dot_center([ff[k] for k in FSDK.FSDKP_RIGHT_EYE_SET])
                    w = self.lpf((xr - xl) * 2.8)
                    h = w * 1.4
                    self.center = (xr + xl) / 2, (yr + yl) / 2 + w * 0.05
                    self.angle = math.atan2(yr - yl, xr - xl) * 180 / math.pi
                    self.frame = -w / 2, -h / 2, w / 2, h / 2

                    self.draw_shape(surf)

                    name = fsdkTracker.GetName(self.fid)
                    # print(name)
                    surf.drawString(name, font, self.center[0] - w / 2 + 2, self.center[1] - h / 2 + 2, text_shadow)
                    surf.drawString(name, font, self.center[0] - w / 2, self.center[1] - h / 2, text_color)
                else:
                    if self.lpf is not None\
                            : self.lpf, self.countdown = None, 35
                    self.countdown -= 1
                    if self.countdown <= 8:
                        self.frame = [v * 0.95 for v in self.frame]
                    else:
                        self.draw_shape(surf)
                    name = 'Unkown User!';
                # print(name)

                path.ellipse(*self.frame)  # frame background
                return self.lpf or self.countdown > 0

        activeFace = capturedFace = None

        def updateActiveFace():
            global activeFace
            p = win.ScreenToClient(hwnd, win.GetCursorPos())
            for fid, tr in trackers.items():
                if tr.is_inside(p.x, p.y):
                    activeFace = fid
                    break
            else:
                activeFace = None

        gdiplus = win.GDIPlus()  # initialize GDI+
        graphics = win.Graphics(hwnd=hwnd)
        backsurf = win.Bitmap.FromGraphics(vfmt.Width, vfmt.Height, graphics)
        surfGr = win.Graphics(bmp=backsurf).setSmoothing(True)  # graphics object for back surface with antialiasing
        facePen, featurePen, brush = win.Pen(0x60ffffff, 5), win.Pen(0xa060ff60, 1.8), win.Brush(0x28ffffff)
        faceActivePen, faceCapturedPen = win.Pen(0xFF00ff00, 2), win.Pen(0xFFff0000, 3)
        font = win.Font(win.FontFamily("Tahoma"), FONT_SIZE)
        text_color, text_shadow = win.Brush(0xffffffff), win.Brush(0xff808080)

        trackers = {}
        # def att():
        # pass

        sampleNum = 0
        while 1:
            sampleNum = sampleNum + 1
            img = camera.GrabFrame()
            surfGr.resetClip().drawImage(win.Bitmap.FromHBITMAP(img.GetHBitmap()))  # fill backsurface with image

            faces = frozenset(fsdkTracker.FeedFrame(0, img))  # recognize all faces in the image
            for face_id in faces.difference(trackers): trackers[face_id] = FaceLocator(face_id)  # create new trackers

            missed, gpath = [], win.GraphicsPath()
            for face_id, tracker in trackers.items():  # iterate over current trackers
                ss = fsdkTracker.GetName(face_id)
                if sampleNum > 100:
                    # ExamName1,SubjectName1,Date1,Degree1,Department1,Year1=fs.examvales1()

                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1productrecomdb')
                    cursor = conn.cursor()
                    cursor.execute("select * from regtb where UserId='" + str(ss) + "'")
                    data = cursor.fetchone()
                    if data is None:
                        print("Fake Face")
                        return "Fake Face"
                    else:
                        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                       database='1productrecomdb')
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO booktb VALUES ('','" + Bookingid + "','" + pid + "','" + ProductName + "','" + uname + "','" + Mobile + "','" + Email + "','" + Qty + "','" + str(
                                Amount) + "','" + str(
                                Mac) + "','" + CardType + "','" + CardNo + "','" + CvNo + "','" + date + "')")
                        conn.commit()
                        conn.close()
                        # return 'file register successfully'

                        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                       database='1productrecomdb')
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM booktb where  UserName= '" + uname + "' ")
                        data = cur.fetchall()

                        return render_template('UbookInfo.html', data=data)

                    print("Amount Transfor Success")

                if face_id in faces:
                    tracker.draw(surfGr, gpath,
                                 face_id)  # fsdkTracker.GetFacialFeatures(face_id)) # draw existing tracker
                else:
                    missed.append(face_id)
            for mt in missed:  # find and remove trackers that are not active anymore
                st = trackers[mt]
                if any(st.isIntersect(trackers[tr]) for tr in faces) or not st.draw(surfGr, gpath): del trackers[mt]

            if capturedFace not in trackers:
                capturedFace = None
                win.ShowWindow(inpBox, win.SW_HIDE)
            updateActiveFace()

            # surfGr.clipPath(gpath, win.CombineModeExclude).fillRect(brush, 0, 0, vfmt.Width, vfmt.Height) # clip frames
            graphics.drawImage(backsurf, 0, 0)  # show backsurface
            if sampleNum > 100:
                break

            msg = win.MSG()
            if win.PeekMessage(win.byref(msg), 0, 0, 0, win.PM_REMOVE):
                win.TranslateMessage(win.byref(msg))
                win.DispatchMessage(win.byref(msg))
                if msg.message == win.WM_KEYDOWN and msg.wParam == win.VK_ESCAPE or need_to_exit: break

        print("Please wait while saving Tracker memory... ", end='', flush=True)
        fsdkTracker.SaveToFile(trackerMemoryFile)
        win.ShowWindow(hwnd, win.SW_HIDE)

        img.Free()
        fsdkTracker.Free()
        camera.Close()

        FSDK.FinalizeCapturing()

        FSDK.Finalize()

@app.route("/fullInfo")
def fullInfo():
    pid = request.args.get('pid')
    session['pid'] = pid

    rat1 = ''
    rat2 = ''
    rat3 = ''
    rat4 = ''
    rat5 = ''

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  ROUND(AVG(Rate), 1) as numRating FROM reviewtb WHERE ProductId  ='" + pid + "' ")
    data2 = cursor.fetchone()
    print(data2[0])
    if data2 is None:
        avgrat = 0

    else:

        if data2[0] == 'None':
            avgrat = 0
            if (int(avgrat) == 1):
                rat1 = 'checked'
            if (int(avgrat) == 2):
                rat2 = 'checked'
            if (int(avgrat) == 3):
                rat3 = 'checked'
            if (int(avgrat) == 4):
                rat4 = 'checked'
            if (int(avgrat) == 5):
                rat5 = 'checked'
        else:
            avgrat = data2[0]

            if (avgrat == 1):
                rat1 = 'checked'
            if (avgrat == 2):
                rat2 = 'checked'
            if (avgrat == 3):
                rat3 = 'checked'
            if (avgrat == 4):
                rat4 = 'checked'
            if (avgrat == 5):
                rat5 = 'checked'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  count(Rate)  as numRating FROM reviewtb WHERE ProductId  ='" + pid + "' ")
    data3 = cursor.fetchone()
    if data3:
        avgrat = data3[0]

    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cursor = conn.cursor()
    cursor.execute("SELECT  sum(Smile1) as count1,sum(Smile2) as count2, sum(Smile3) as count3, sum(Smile4) as count4, sum(Smile5) as count5, sum(Smile6) as count6 FROM  reviewtb where ProductId='"+ pid +"' ")
    data = cursor.fetchone()
    if data:
        smile1 = data[0]
        smile2 = data[1]
        smile3 =  data[2]
        smile4 =  data[3]
        smile5 =  data[4]
        smile6 =  data[5]
    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cur = conn.cursor()
    cur.execute("SELECT UserName,Review FROM reviewtb where ProductId='" + pid + "' ")
    reviewdata = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where id='" + pid + "' ")
    data1 = cur.fetchall()
    return render_template('ProductFullInfo.html',data=data1 ,avgrat=avgrat, rat1=rat1, rat2=rat2, rat3=rat3, rat4=rat4, rat5=rat5,smile1=smile1,smile2=smile2,smile3=smile3, smile4=smile4, smile5=smile5 ,smile6=smile6, reviewdata=reviewdata )

@app.route("/UBookInfo")
def UBookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb  where UserName='" + uname +"'  ")
    data = cur.fetchall()
    return render_template('UBookInfo.html', data=data)

@app.route("/ABookInfo")
def ABookInfo():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb  ")
    data = cur.fetchall()
    return render_template('ABookInfo.html', data=data)
@app.route("/viewstatus")
def viewstatus():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb")
    data = cur.fetchall()
    return render_template('viewstatus.html', data=data)

@app.route("/UReviewInfo")
def UReviewInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb  where UserName='" + uname +"'  ")
    data = cur.fetchall()
    return render_template('UReviewInfo.html', data=data)


@app.route("/AReviewInfo")
def AReviewInfo():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1productrecomdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb   ")
    data = cur.fetchall()
    return render_template('AReviewInfo.html', data=data)
@app.route("/NewUser")
def NewUser():
    import LiveRecognition

    return render_template('NewUser.html')
@app.route("/daction")
def daction():
    id=request.args.get('id')


    return render_template('viewstatus.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)