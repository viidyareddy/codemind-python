n=int(input())
c=''
while(n!=0):
    if(n>=1000):
        c+='M'
        n-=1000
    elif(n>=900):
        c+="CM"
        n-=900
    elif(n>=500):
        c+="D"
        n-=500
    elif(n>=400):
        c+="CD"
        n-=400
    elif(n>=100):
        c+="C"
        n-=100
    elif(n>=90):
        c+="XC"
        n-=90
    elif(n>=50):
        c+="IV"
        n-=50
    elif(n>=40):
        c+="XI"
        n-=40
    elif(n>=10):
        c+="X"
        n-=10
    elif(n>=9):
        c+="IX"
        n-=9
    elif(n>=5):
        c+="V"
        n-=5
    elif(n>=4):
        c+="IV"
        n-=4
    elif(n>=1):
        c+="I"
        n-=1
print(c)
