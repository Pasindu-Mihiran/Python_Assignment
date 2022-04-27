import sys

r = 0;
linear = 0;
circular = 0;
a = sys.argv

for f in range(1,len(a),2):
    for b in range(0,len(a[f])):
        x = a[f][b]
        y = a[f+1][b]
        if(ord(y) > ord(x)):
            linear = linear + ord(y)-ord(x);
            circular = circular + min(ord(y)-ord(x),26-(ord(y)-96)+(ord(x)-96));
        else:
            linear = linear + ord(x)-ord(y);
            circular = circular + min(ord(x)-ord(y),26-(ord(x)-96)+(ord(y)-96));
    print(linear , "  " ,circular )
    linear = 0;
    circular = 0;

 




