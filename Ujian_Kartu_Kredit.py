import json

with open('ccNasabah.json','r') as x:
    out = json.load(x)

letter = ['a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z'
]
valid = []
invalidCC = []

for i in range(len(out)):
    no_CC = out[i]['noCreditCard']
    no_CC = no_CC.split('-')
    no_CC = ''.join(no_CC)
    
    if no_CC[0]=='4' and len(no_CC) == 16:
        
            
        if ' ' in no_CC:
            invalidCC.append(out[i])
        elif no_CC[i].isalpha():
            invalidCC.append(out[i])
        elif '-' in no_CC:
            invalidCC.append(out[i])
        elif '44444' in no_CC:
            invalidCC.append(out[i])
        else: 
            valid.append(out[i])
    elif no_CC[0] == '5' and len(no_CC) == 16:

        
        if ' ' in no_CC:
            invalidCC.append(out[i])
        elif no_CC[i].isalpha():
            invalidCC.append(out[i])
        elif '-' in no_CC:
            invalidCC.append(out[i])
        elif '9999' in no_CC:
            invalidCC.append(out[i])
        else:
            valid.append(out[i])
    elif no_CC[0] == '6' and len(no_CC) == 16:
        # for j in range(len(no_CC)):
        #     if no_CC[j].isalpha():
        #         invalidCC.append(out[i])
        if ' ' in no_CC:
            invalidCC.append(out[i])
        elif no_CC[i].isalpha():
            invalidCC.append(out[i])
        elif '-' in no_CC:
            invalidCC.append(out[i])
        elif '61234' in no_CC:
            invalidCC.append(out[i])
        else: 
            valid.append(out[i])
    else:
        invalidCC.append(out[i])

with open('ccValid.json','w') as y:
    json.dump(valid,y)
with open('ccInvalidCC.json','w') as yy:
    json.dump(invalidCC,yy)