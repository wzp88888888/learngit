#创建一个简单数据库，可查询号码，地址
pepole={'wzp':{'phone':'888','add':'drive 1'},
        'ls':{'phone':'666','add':'drive 2'}
        }

name=input('名字:')

labels={'phone':'phone number',
        'add':'adderss'
        }

pa=input('phone(p),addreee(a)')
if pa=='p':key='phone'
if pa=='a':key='add'
#print(key)

if name in pepole:print(name,labels[key],'is',pepole[name][key])
