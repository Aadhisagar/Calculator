import tkinter as tk

root=tk.Tk()
var={"decimal":False,"ValX":0.0,"ValY":0.0,'result':0.0,'front':[],'back':[],'operator':''}
root.title('calculator')
#color fuction
root.config(bg='sky blue')

display_text=tk.StringVar()
display_text.set('0.0000')

canvas=tk.Canvas(bg='sky blue',bd=0, highlightthickness=0)
canvas.pack(padx=15,pady=15)

def update_value(display_value):
    global display_text
    try:
        display_text.set('{,.4f}'.format(display_value))
    except:
        display_text.set(display_value)
        
def number_click_event(event):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    display_value=float(format_number())
    update_value(display_value)
    update_value

def format_number():
    return''.join(var['front'])+'.'+''.join(var['back'])


def Event_click(event):
    global var
    if event in ['CE','C']:
        clear_click()
        update_value(0.0)
        var['result']=0.0
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click_event(event)
    if event in ['+','-','/','*']:
        operator_click_event(event)
    if event=='.':
        var['decimal']=True
    if event=="%":
        update_value(var['result']/100.0)
    if event=='=':
        calculate_result()

        
def operator_click_event(event):
    global var
    var['operator']=event
    try:
        var['VarX']=float(format_number())
    except:
        var['VarX']=var['result']
    clear_click()

def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal']=False

def calculate_result():
    global var
    if not var['VarX']:
        return
    try:
        var['VarY']=float(format_number())
    except:
        var['VarY']=0.0

    try:
        var['result']=float(eval(str(var['VarX'])+var['operator']+str(var['VarY'])))
        update_value(var['result'])
    except ZeroDivisionError:
        error='ERROR!DIV/0'
        var['ValX']=0.0
        clear_click()
        updated_value(error)
    clear_click()
    

    
def update_value(display_value):
    global display_text
    try:
        display_text.set('{,.4f}'.format(display_value))
    except:
        display_text.set(display_value)
        
        
def number_click_event(event):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    display_value=float(format_number())
    update_value(display_value)
    update_value



def std_btn(text,bg,row,col,width=7,height=2,font=("Times of new roman",24)):
    btn=tk.Button(canvas,text=text,bg=bg,width=width,height=height ,
    font=font,command=lambda:Event_click(text))
    return btn.grid(row=row,column=col,padx=4,pady=4)
#btn=tk.Button()
tk.Label(canvas,textvariable=display_text,anchor='e',bg='white',fg='black',font=("Times of new roman",24)).grid(row=1,columnspan=4,sticky='ew',padx=4,pady=2)

std_btn("C","blue",2,0),std_btn("CE","blue",2,1),std_btn("%","blue",2,2),std_btn("/","blue",2,3)
std_btn("7","blue",3,0),std_btn("8","blue",3,1),std_btn("9","blue",3,2),std_btn("*","blue",3,3)
std_btn("4","blue",4,0),std_btn("5","blue",4,1),std_btn("6","blue",4,2),std_btn("-","blue",4,3)
std_btn("1","blue",5,0),std_btn("2","blue",5,1),std_btn("3","blue",5,2),std_btn("+","blue",5,3)
std_btn(".","blue",6,0),std_btn("0","blue",6,1),std_btn("=","blue",6,3)


    























root.mainloop()
