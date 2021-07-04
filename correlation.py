# Add the functions in this file

def load_journal(fname):
    data=open(fname).read()
    js = json.loads(data)
    return js

def compute_phi(js,event):
    a=0
    b=0
    c=0
    d=0
    w=0
    x=0
    y=0
    z=0
    for item in js:
        list=item['events']
        bool=item['squirrel']
        if event in list and bool==True:
            a=a+1
            w=w+1
            y=y+1
        if event not in list and bool==False:
            b=b+1
            x=x+1
            z=z+1
        if event in list and bool==False:
            c=c+1
            w=w+1
            z=z+1
        if event not in list and bool==True:
            d=d+1
            x=x+1
            y=y+1
    num=(a*b)-(c*d)
    den=math.sqrt(w*x*y*z)
    corr=num/den
    return corr
    #a,b,c,d;w,x,y,z

def compute_correlations(fname):
    js=load_journal(fname)
    eventlist=[]
    for item in js:
      list=item['events']
      for ev in list:
          if ev not in eventlist:
              eventlist.append(ev)
    corr_pair=dict()
    for event in eventlist:
        x=compute_phi(js,event)
        corr_pair[x]=event
    return corr_pair


def diagnose(fname):
    d=compute_correlations(fname)
    x=sorted(d.items())
    for k,v in x:
        e1=v
        break
    x=sorted(d.items(),reverse=True)
    for k,v in x:
        e2=v
        break
    return e2,e1
