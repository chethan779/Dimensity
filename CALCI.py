import tkinter as tk
import math
import random
from tkinter import simpledialog,messagebox
from math import factorial
from collections import Counter
from tkinter import ttk
from tkinter import*


calculation = ""
display_calculation = ""
mode='DEG'
memory_value=0

# --- CORE FUNCTIONS ---
def add_to_calculation(symbol, display_symbol=None):
    global calculation, display_calculation
    if symbol == '(':
        if calculation and (calculation[-1].isdigit() or calculation[-1] == ')'):
            calculation += '*' + symbol
            display_calculation += '*' + (display_symbol if display_symbol else symbol)
            update_display()
            return
    calculation += str(symbol)
    display_calculation += str(display_symbol if display_symbol else symbol)
    update_display()

def update_display():
    text_result.delete(0, tk.END)
    text_result.insert(0, display_calculation)

def evaluate_calculation():
    global calculation, display_calculation
    try:
        result = str(eval(calculation, {"math": math}))
        calculation = result
        display_calculation = result
        update_display()
    except:
        clear_field()
        text_result.insert(0, "Error")

def clear_field():
    global calculation, display_calculation
    calculation = ""
    display_calculation = ""
    update_display()

def delete_last():
    global calculation, display_calculation
    calculation = calculation[:-1]
    display_calculation = display_calculation[:-1]
    update_display()

def add_sqrt():
    add_to_calculation('math.sqrt(', '√(')

def add_cbrt():
    add_to_calculation('**(1/3)', '∛')

def add_pow():
    add_to_calculation('**', '^')

# --- MODE SWITCHING ---
def show_mode(mode):
    standard_frame.pack_forget()
    scientific_frame.pack_forget()
    matrix_frame.pack_forget()
    Determinant_frame.pack_forget() 
    progression_frame.pack_forget()
    programming_frame.pack_forget()
    permutations_frame.pack_forget()
    
    if mode == 'standard':
        text_result.pack(padx=10, pady=10, ipadx=8, ipady=15, fill='x')
        standard_frame.pack()
    elif mode == 'scientific':
        text_result.pack(padx=10, pady=10, ipadx=8, ipady=15, fill='x')
        scientific_frame.pack()
    elif mode == 'matrices':
        text_result.pack_forget()
        matrix_frame.pack()
    elif mode == 'determinants':
        text_result.pack_forget()
        Determinant_frame.pack()
    elif mode == 'progression':
        text_result.pack_forget()
        progression_frame.pack()
    elif mode=='programming':
       text_result.pack_forget()
       programming_frame.pack() 
    elif mode == 'permutations':
        text_result.pack_forget()
        permutations_frame.pack()
   

    
def sine_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = math.sin(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def cos_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = math.cos(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def tan_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = math.tan(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def cot_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = 1 / math.tan(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def cosec_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = 1 / math.sin(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def sec_function():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 0
        else:
            value = eval(calculation, {"math": math})
        if mode == 'DEG':
            value = math.radians(value)
        result = 1 / math.cos(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0,'Error')

def calculate_log():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 1
        else:
            value = eval(calculation, {'math': math})
        result = math.log10(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')

def calculate_ln():
    global calculation, display_calculation
    try:
        if calculation.strip() == "":
            value = 1
        else:
            value = eval(calculation, {'math': math})
        result = math.log(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')

def addpi():
     add_to_calculation('math.pi','π')

def adde():
    add_to_calculation('math.e', 'e')

def calculate_factorial():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.factorial(int(value))
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_power10():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.pow(10, value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_power2():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.pow(2, value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error') 
def calculate_abs():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = abs(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_floor():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.floor(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_signum():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        if value > 0:
            result = 1
        elif value < 0:
            result = -1
        else:
            result = 0
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error') 
def calculate_frac_part():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = value - math.floor(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def deg_to_rad():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.radians(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')

def rad_to_deg():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = math.degrees(value)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')

def generate_random():
    global calculation, display_calculation
    try:
        result = random.random()
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_reciprocal():
    global calculation, display_calculation
    try:
        value = eval(calculation, {'math': math})
        result = 1 / value
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def calculate_nth_root():
    global calculation, display_calculation
    try:
        n = simpledialog.askinteger("Nth Root", "Enter n (root degree):")
        if n is None or n == 0:
            return
        value = eval(calculation, {'math': math})
        result = value ** (1/n)
        calculation = str(result)
        display_calculation = str(result)
        update_display()
    except:
        clear_field()
        text_result.insert(0, 'Error')
def memory_add():
    global calculation, memory_value
    try:
        value = eval(calculation, {'math': math})
        memory_value += value
    except:
        clear_field()
        text_result.insert(0, 'Error')

def memory_subtract():
    global calculation, memory_value
    try:
        value = eval(calculation, {'math': math})
        memory_value -= value
    except:
        clear_field()
        text_result.insert(0, 'Error')

def memory_recall():
    global calculation, display_calculation, memory_value
    calculation = str(memory_value)
    display_calculation = str(memory_value)
    update_display()

def memory_clear():
    global memory_value
    memory_value = 0

# --- MAIN WINDOW SETUP ---
root = tk.Tk()
try:
    _sw = root.winfo_screenwidth()
    _sh = root.winfo_screenheight()
    root.geometry(f"{_sw}x{_sh}+0+0")
    root.attributes("-fullscreen", True)
except Exception:
    root.geometry('800x875')
root.title('E-Calci — Calculator')
root.configure(bg="#000000")

# --- JETBRAINS MONO SYSTEM FONT DETECTION ---
import tkinter.font as tkfont
def _detect_calc_font():
    try:
        fams = set(tkfont.families())
        for f in ["JetBrains Mono ExtraBold", "JetBrains Mono", "Noto Sans Mono", "Noto Sans", FONT_MAIN]:
            if f in fams:
                return f
    except Exception:
        pass
    return "JetBrains Mono"

FONT_MAIN = _detect_calc_font()
try:
    _fams = set(tkfont.families())
    FONT_EXTRABOLD = "JetBrains Mono ExtraBold" if "JetBrains Mono ExtraBold" in _fams else FONT_MAIN
except Exception:
    FONT_EXTRABOLD = FONT_MAIN

# --- PURE BLACK THEME DEFAULTS ---
try:
    root.tk_setPalette(background="#121212", foreground="#FFFFFF",
                       activeBackground="#1E1E1E", activeForeground="#FBBF24")
except Exception:
    pass

root.option_add("*Background", "#121212")
root.option_add("*Foreground", "#FFFFFF")
root.option_add("*Button.background", "#1E1E1E")
root.option_add("*Button.foreground", "#FFFFFF")
root.option_add("*Button.activeBackground", "#2A2A2A")
root.option_add("*Button.activeForeground", "#FBBF24")
root.option_add("*Button.relief", "flat")
root.option_add("*Button.borderWidth", 1)
root.option_add("*Entry.background", "#000000")
root.option_add("*Entry.foreground", "#FBBF24")
root.option_add("*Entry.insertBackground", "#FFFFFF")
root.option_add("*Frame.background", "#121212")
root.option_add("*Label.background", "#121212")
root.option_add("*Label.foreground", "#FFFFFF")
root.option_add("*Menu.background", "#121212")
root.option_add("*Menu.foreground", "#FFFFFF")
root.option_add("*Menu.activeBackground", "#2A2A2A")
root.option_add("*Menu.activeForeground", "#FBBF24")

root.bind("<Escape>", lambda e: root.destroy())

# --- TOP CONTROL BAR ---
top_bar = tk.Frame(root, bg="#0D0D0D", height=50)
top_bar.pack(side="top", fill="x")
top_bar.pack_propagate(False)

tk.Label(top_bar, text="🧮 E-Calci — Scientific Calculator", font=(FONT_EXTRABOLD, 15, "bold"),
         fg="#FBBF24", bg="#0D0D0D").pack(side="left", padx=20)

tk.Button(top_bar, text="✕ Close (Esc)", font=(FONT_EXTRABOLD, 11, "bold"),
          bg="#1E1E1E", fg="#FFFFFF", activebackground="#2A2A2A", activeforeground="#FBBF24",
          bd=0, padx=14, pady=5, cursor="hand2",
          command=root.destroy).pack(side="right", padx=16)

# --- MENU ---
menu = tk.Menu(root)
root.config(menu=menu)
mode_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Mode", menu=mode_menu)
mode_menu.add_command(label="Standard", command=lambda: show_mode('standard'))
mode_menu.add_command(label="Scientific", command=lambda: show_mode('scientific'))
mode_menu.add_command(label="Matrices", command=lambda: show_mode('matrices'))
mode_menu.add_command(label='Determinants',command=lambda:show_mode('determinants'))

mode_menu.add_command(label='Progression',command=lambda:show_mode('progression'))
mode_menu.add_command(label="Programming", command=lambda: show_mode('programming'))
mode_menu.add_command(label="Permutations & Combinations", command=lambda: show_mode('permutations'))
# --- DISPLAY ---
text_result = tk.Entry(root, font=(FONT_MAIN, 24), width=30, justify='right',
                       bg="#000000", fg="#FBBF24", insertbackground="#FFFFFF")
text_result.pack(padx=10, pady=10, ipadx=8, ipady=15, fill='x')

# --- FRAMES ---
standard_frame = tk.Frame(root, bg="#000000")
scientific_frame = tk.Frame(root, bg="#000000")
matrix_frame = tk.Frame(root, bg="#000000")
Determinant_frame = tk.Frame(root, bg="#000000")
progression_frame = tk.Frame(root, bg="#000000")

programming_frame = tk.Frame(root, bg="#000000")
permutations_frame = tk.Frame(root, bg="#000000")


# --- STANDARD MODE BUTTONS (your exact style) ---
btn1=tk.Button(standard_frame,text='1',command=lambda:add_to_calculation(1),width=5,font=(FONT_MAIN,24))
btn1.grid(row=2,column=1)
btn2=tk.Button(standard_frame,text='2',command=lambda:add_to_calculation(2),width=5,font=(FONT_MAIN,24))
btn2.grid(row=2,column=2)
btn3=tk.Button(standard_frame,text='3',command=lambda:add_to_calculation(3),width=5,font=(FONT_MAIN,24))
btn3.grid(row=2,column=3)
btn4=tk.Button(standard_frame,text='4',command=lambda:add_to_calculation(4),width=5,font=(FONT_MAIN,24))
btn4.grid(row=3,column=1)
btn5=tk.Button(standard_frame,text='5',command=lambda:add_to_calculation(5),width=5,font=(FONT_MAIN,24))
btn5.grid(row=3,column=2)
btn6=tk.Button(standard_frame,text='6',command=lambda:add_to_calculation(6),width=5,font=(FONT_MAIN,24))
btn6.grid(row=3,column=3)
btn7=tk.Button(standard_frame,text='7',command=lambda:add_to_calculation(7),width=5,font=(FONT_MAIN,24))
btn7.grid(row=4,column=1)
btn8=tk.Button(standard_frame,text='8',command=lambda:add_to_calculation(8),width=5,font=(FONT_MAIN,24))
btn8.grid(row=4,column=2)
btn9=tk.Button(standard_frame,text='9',command=lambda:add_to_calculation(9),width=5,font=(FONT_MAIN,24))
btn9.grid(row=4,column=3)
btn0=tk.Button(standard_frame,text='0',command=lambda:add_to_calculation(0),width=5,font=(FONT_MAIN,24))
btn0.grid(row=5,column=2)

btnplus=tk.Button(standard_frame,text='+',command=lambda:add_to_calculation('+'),width=5,font=(FONT_MAIN,24))
btnplus.grid(row=2,column=4)
btnminus=tk.Button(standard_frame,text='-',command=lambda:add_to_calculation('-'),width=5,font=(FONT_MAIN,24))
btnminus.grid(row=3,column=4)
btnmulti=tk.Button(standard_frame,text='*',command=lambda:add_to_calculation('*'),width=5,font=(FONT_MAIN,24))
btnmulti.grid(row=4,column=4)
btndivision=tk.Button(standard_frame,text='/',command=lambda:add_to_calculation('/'),width=5,font=(FONT_MAIN,24))
btndivision.grid(row=5,column=4)

btnopen=tk.Button(standard_frame,text='(',command=lambda:add_to_calculation('('),width=5,font=(FONT_MAIN,24))
btnopen.grid(row=5,column=1)
btnclose=tk.Button(standard_frame,text=')',command=lambda:add_to_calculation(')'),width=5,font=(FONT_MAIN,24))
btnclose.grid(row=5,column=3)

btnclear=tk.Button(standard_frame,text='C',command=clear_field,width=11,font=(FONT_MAIN,24))
btnclear.grid(row=6,column=0,columnspan=3)
btnequals=tk.Button(standard_frame,text='=',command=evaluate_calculation,width=11,font=(FONT_MAIN,24))
btnequals.grid(row=6,column=3,columnspan=2)

btndot = tk.Button(standard_frame, text='.', command=lambda: add_to_calculation('.'), width=5, font=(FONT_MAIN,24))
btndot.grid(row=5, column=5)
btndel = tk.Button(standard_frame, text='⌫', command=delete_last, width=5, font=(FONT_MAIN,24))
btndel.grid(row=6, column=5)
btnsqrt = tk.Button(standard_frame, text='√', command=add_sqrt, width=5, font=(FONT_MAIN,24))
btnsqrt.grid(row=2, column=5)
btncbrt = tk.Button(standard_frame, text='∛', command=add_cbrt, width=5, font=(FONT_MAIN,24))
btncbrt.grid(row=3, column=5)
btnpow = tk.Button(standard_frame, text='^', command=add_pow, width=5, font=(FONT_MAIN,24))
btnpow.grid(row=4, column=5)

# --- SCIENTIFIC MODE PLACEHOLDER ---

btnsin=tk.Button(scientific_frame,text='sin',command=sine_function,width=5,font=(FONT_MAIN,24))
btnsin.grid(row=0,column=0)
btncos=tk.Button(scientific_frame,text='cos',command=cos_function,width=5,font=(FONT_MAIN,24))
btncos.grid(row=0,column=1)
btntan=tk.Button(scientific_frame,text='tan',command=tan_function,width=5,font=(FONT_MAIN,24))
btntan.grid(row=0,column=2)
btncot=tk.Button(scientific_frame,text='cot',command=cot_function,width=5,font=(FONT_MAIN,24))
btncot.grid(row=0,column=3)
btncosec=tk.Button(scientific_frame,text='cosec',command=cosec_function,width=5,font=(FONT_MAIN,24))
btncosec.grid(row=0,column=4)
btnsec=tk.Button(scientific_frame,text='sec',command=sec_function,width=5,font=(FONT_MAIN,24))
btnsec.grid(row=0,column=5)
btnsqrt = tk.Button(scientific_frame, text='√', command=add_sqrt, width=5, font=(FONT_MAIN,24))
btnsqrt.grid(row=1, column=0)
btncbrt = tk.Button(scientific_frame, text='∛', command=add_cbrt, width=5, font=(FONT_MAIN,24))
btncbrt.grid(row=1, column=1)
btnpow = tk.Button(scientific_frame, text='^', command=add_pow, width=5, font=(FONT_MAIN,24))
btnpow.grid(row=1, column=2)
btndel = tk.Button(scientific_frame, text='⌫', command=delete_last, width=5, font=(FONT_MAIN,24))
btndel.grid(row=1, column=3)
btnclear=tk.Button(scientific_frame,text='C',command=clear_field,width=5,font=(FONT_MAIN,24))
btnclear.grid(row=1,column=4)
btnopen=tk.Button(scientific_frame,text='(',command=lambda:add_to_calculation('('),width=5,font=(FONT_MAIN,24))
btnopen.grid(row=1,column=5)
btnclose=tk.Button(scientific_frame,text=')',command=lambda:add_to_calculation(')'),width=5,font=(FONT_MAIN,24))
btnclose.grid(row=1,column=6)
btnpi = tk.Button(scientific_frame, text='π', command=addpi, width=5, font=(FONT_MAIN,24))
btnpi.grid(row=2, column=6)
btn7=tk.Button(scientific_frame,text='7',command=lambda:add_to_calculation(7),width=5,font=(FONT_MAIN,24))
btn7.grid(row=2,column=0)
btn8=tk.Button(scientific_frame,text='8',command=lambda:add_to_calculation(8),width=5,font=(FONT_MAIN,24))
btn8.grid(row=2,column=1)
btn9=tk.Button(scientific_frame,text='9',command=lambda:add_to_calculation(9),width=5,font=(FONT_MAIN,24))
btn9.grid(row=2,column=2)
btn4=tk.Button(scientific_frame,text='4',command=lambda:add_to_calculation(4),width=5,font=(FONT_MAIN,24))
btn4.grid(row=3,column=0)
btn5=tk.Button(scientific_frame,text='5',command=lambda:add_to_calculation(5),width=5,font=(FONT_MAIN,24))
btn5.grid(row=3,column=1)
btn6=tk.Button(scientific_frame,text='6',command=lambda:add_to_calculation(6),width=5,font=(FONT_MAIN,24))
btn6.grid(row=3,column=2)
btn1=tk.Button(scientific_frame,text='1',command=lambda:add_to_calculation(1),width=5,font=(FONT_MAIN,24))
btn1.grid(row=4,column=0)
btn2=tk.Button(scientific_frame,text='2',command=lambda:add_to_calculation(2),width=5,font=(FONT_MAIN,24))
btn2.grid(row=4,column=1)
btn3=tk.Button(scientific_frame,text='3',command=lambda:add_to_calculation(3),width=5,font=(FONT_MAIN,24))
btn3.grid(row=4,column=2)
btnlog = tk.Button(scientific_frame, text='log', command=calculate_log, width=5, font=(FONT_MAIN,24))
btnlog.grid(row=2, column=3)
btnequals=tk.Button(scientific_frame,text='=',command=evaluate_calculation,width=11,font=(FONT_MAIN,24))
btnequals.grid(row=5,column=6,columnspan=3)
btnplus=tk.Button(scientific_frame,text='+',command=lambda:add_to_calculation('+'),width=5,font=(FONT_MAIN,24))
btnplus.grid(row=4,column=3)
btnminus=tk.Button(scientific_frame,text='-',command=lambda:add_to_calculation('-'),width=5,font=(FONT_MAIN,24))
btnminus.grid(row=4,column=4)
btnmulti=tk.Button(scientific_frame,text='*',command=lambda:add_to_calculation('*'),width=5,font=(FONT_MAIN,24))
btnmulti.grid(row=4,column=5)
btndivision=tk.Button(scientific_frame,text='/',command=lambda:add_to_calculation('/'),width=5,font=(FONT_MAIN,24))
btndivision.grid(row=4,column=6)
btnln = tk.Button(scientific_frame, text='ln', command=calculate_ln, width=5, font=(FONT_MAIN,24))
btnln.grid(row=2, column=4)
btn0=tk.Button(scientific_frame,text='0',command=lambda:add_to_calculation(0),width=5,font=(FONT_MAIN,24))
btn0.grid(row=5,column=0)
btne = tk.Button(scientific_frame, text='e', command=adde, width=5, font=(FONT_MAIN,24))
btne.grid(row=2, column=5)
btnfact = tk.Button(scientific_frame, text='n!', command=calculate_factorial, width=5, font=(FONT_MAIN,24))
btnfact.grid(row=0, column=6)
btn10pow = tk.Button(scientific_frame, text='10^x', command=calculate_power10, width=5, font=(FONT_MAIN,24))
btn10pow.grid(row=0, column=7)
btn2pow = tk.Button(scientific_frame, text='2^x', command=calculate_power2, width=5, font=(FONT_MAIN,24))
btn2pow.grid(row=1, column=7)
btnabs = tk.Button(scientific_frame, text='|x|', command=calculate_abs, width=5, font=(FONT_MAIN,24))
btnabs.grid(row=3 ,column=3)
btnfloor = tk.Button(scientific_frame, text='⌊x⌋', command=calculate_floor, width=5, font=(FONT_MAIN,24))
btnfloor.grid(row=3, column=4)
btnsign = tk.Button(scientific_frame, text='sgn', command=calculate_signum, width=5, font=(FONT_MAIN,24))
btnsign.grid(row=3, column=5)
btnfrac = tk.Button(scientific_frame, text='frac', command=calculate_frac_part, width=5, font=(FONT_MAIN,24))
btnfrac.grid(row=3, column=6)
btnd2r = tk.Button(scientific_frame, text='Deg→Rad', command=deg_to_rad, width=11, font=(FONT_MAIN,24))
btnd2r.grid(row=5, column=2,columnspan=2)

btnr2d = tk.Button(scientific_frame, text='Rad→Deg', command=rad_to_deg, width=11, font=(FONT_MAIN,24))
btnr2d.grid(row=5, column=4,columnspan=2)
btndot = tk.Button(scientific_frame, text='.', command=lambda: add_to_calculation('.'), width=5, font=(FONT_MAIN,24))
btndot.grid(row=5, column=1)
btnrand = tk.Button(scientific_frame, text='Rand', command=generate_random, width=5, font=(FONT_MAIN,24))
btnrand.grid(row=3, column=7)

btnrecip = tk.Button(scientific_frame, text='1/x', command=calculate_reciprocal, width=5, font=(FONT_MAIN,24))
btnrecip.grid(row=2, column=7)
btnmplus = tk.Button(scientific_frame, text='M+', command=memory_add, width=5, font=(FONT_MAIN,24))
btnmplus.grid(row=6, column=0)

btnmminus = tk.Button(scientific_frame, text='M-', command=memory_subtract, width=5, font=(FONT_MAIN,24))
btnmminus.grid(row=6, column=1)

btnmr = tk.Button(scientific_frame, text='MR', command=memory_recall, width=5, font=(FONT_MAIN,24))
btnmr.grid(row=6, column=2)

btnmc = tk.Button(scientific_frame, text='MC', command=memory_clear, width=5, font=(FONT_MAIN,24))
btnmc.grid(row=6, column=3)
btnnroot = tk.Button(scientific_frame, text='n√x', command=calculate_nth_root, width=5, font=(FONT_MAIN,24))
btnnroot.grid(row=4, column=7)


show_mode('standard')
#matrix mode ui start
#add
matrix_entries = []

def add_matrices_mode():
    global matrix_entries
    matrix_entries.clear()

    # Clear old entries
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Show config dialog
    class MatrixConfigDialog(simpledialog.Dialog):
        def body(self, master):
            tk.Label(master, text="Number of matrices:").grid(row=0, column=0, sticky='e')
            tk.Label(master, text="Number of rows:").grid(row=1, column=0, sticky='e')
            tk.Label(master, text="Number of columns:").grid(row=2, column=0, sticky='e')

            self.num_matrices_entry = tk.Entry(master)
            self.rows_entry = tk.Entry(master)
            self.cols_entry = tk.Entry(master)

            self.num_matrices_entry.grid(row=0, column=1)
            self.rows_entry.grid(row=1, column=1)
            self.cols_entry.grid(row=2, column=1)

            return self.num_matrices_entry

        def apply(self):
            try:
                self.num_matrices = int(self.num_matrices_entry.get())
                self.rows = int(self.rows_entry.get())
                self.cols = int(self.cols_entry.get())
            except:
                self.num_matrices = self.rows = self.cols = None

    dialog = MatrixConfigDialog(root, title="Matrix Addition Config")

    num_matrices = dialog.num_matrices
    rows = dialog.rows
    cols = dialog.cols

    if not num_matrices or num_matrices < 2 or not rows or not cols or rows < 1 or cols < 1:
        return

    # Create entry grids
    for m in range(num_matrices):
        lf = tk.LabelFrame(matrix_input_frame, text=f"Matrix {m+1}")
        lf.pack(padx=5, pady=5)
        entries = []
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
                e.grid(row=r, column=c, padx=2, pady=2)

                # Arrow keys support
                def move(event, row=r, col=c, entries=entries):
                    if event.keysym == 'Up' and row > 0:
                        entries[row-1][col].focus_set()
                    elif event.keysym == 'Down' and row < len(entries)-1:
                        entries[row+1][col].focus_set()
                    elif event.keysym == 'Left' and col > 0:
                        entries[row][col-1].focus_set()
                    elif event.keysym == 'Right' and col < len(entries[row])-1:
                        entries[row][col+1].focus_set()
                e.bind('<KeyPress>', move)

                row_entries.append(e)
            entries.append(row_entries)
        matrix_entries.append(entries)

    # Evaluate button
    eval_btn = tk.Button(matrix_input_frame, text="Evaluate Addition", font=(FONT_MAIN,16),
                         command=lambda: evaluate_addition(num_matrices, rows, cols))
    eval_btn.pack(pady=10)
saved_result=None
def evaluate_addition(num_matrices, rows, cols):
    global matrix_entries, saved_result_matrix
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Validate and collect data
    matrices = []
    has_error = False
    for entries in matrix_entries:
        mat = []
        for row in entries:
            row_data = []
            for e in row:
                value = e.get()
                try:
                    num = float(value)
                    e.config(bg='white')
                    row_data.append(num)
                except:
                    e.config(bg='red')
                    has_error = True
            mat.append(row_data)
        matrices.append(mat)

    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields (invalid numbers).")
        return

    # Calculate sum
    result = [[0]*cols for _ in range(rows)]
    for mat in matrices:
        for r in range(rows):
            for c in range(cols):
                result[r][c] += mat[r][c]

    # Save the result
    saved_result_matrix = result

    # Show result
    lf = tk.LabelFrame(result_frame, text="Result")
    lf.pack()
    for r in range(rows):
        for c in range(cols):
            e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(result[r][c]))
            e.config(state='readonly')

# --- Sample minimal setup ---


matrix_input_frame = tk.Frame(matrix_frame)
matrix_input_frame.pack()
result_frame = tk.Frame(matrix_frame)
result_frame.pack()

operations_frame = tk.Frame(matrix_frame)
operations_frame.pack()
btn_add = tk.Button(operations_frame, text="Add", width=12, font=(FONT_MAIN,16), command=add_matrices_mode)
btn_add.grid(row=0, column=0, padx=5)

#subtract
matrix_entries = []
matrix_input_frame = tk.Frame(matrix_frame)
matrix_input_frame.pack(pady=10)

result_frame = tk.Frame(matrix_frame)
result_frame.pack(pady=10)

def validate_entry(event):
    entry = event.widget
    value = entry.get()
    try:
        float(value)
        entry.config(bg='white')
    except:
        entry.config(bg='salmon')

def bind_entry_events(entry, entries, r, c, rows, cols):
    entry.bind("<KeyRelease>", validate_entry)
    
    def move_focus(dr, dc):
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            entries[nr][nc].focus_set()

    entry.bind("<Up>", lambda e: move_focus(-1, 0))
    entry.bind("<Down>", lambda e: move_focus(1, 0))
    entry.bind("<Left>", lambda e: move_focus(0, -1))
    entry.bind("<Right>", lambda e: move_focus(0, 1))

class MatrixConfigDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Number of rows:").grid(row=0, column=0, sticky='e')
        tk.Label(master, text="Number of columns:").grid(row=1, column=0, sticky='e')

        self.rows_entry = tk.Entry(master)
        self.cols_entry = tk.Entry(master)

        self.rows_entry.grid(row=0, column=1)
        self.cols_entry.grid(row=1, column=1)

        return self.rows_entry

    def apply(self):
        try:
            self.rows = int(self.rows_entry.get())
            self.cols = int(self.cols_entry.get())
        except:
            self.rows = self.cols = None

def subtract_matrices_mode():
    global matrix_entries
    matrix_entries.clear()

    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

    dialog = MatrixConfigDialog(root, title="Matrix Subtraction Config")
    rows, cols = dialog.rows, dialog.cols

    if not rows or not cols or rows < 1 or cols < 1:
        return

    num_matrices = 2

    for m in range(num_matrices):
        lf = tk.LabelFrame(matrix_input_frame, text=f"Matrix {m+1}")
        lf.pack(padx=5, pady=5)
        entries = []
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
                e.grid(row=r, column=c, padx=2, pady=2)
                bind_entry_events(e, entries, r, c, rows, cols)
                row_entries.append(e)
            entries.append(row_entries)
        matrix_entries.append(entries)

    eval_btn = tk.Button(matrix_input_frame, text="Evaluate Subtraction", font=(FONT_MAIN,16),
                         command=lambda: evaluate_subtraction(rows, cols))
    eval_btn.pack(pady=10)
def evaluate_subtraction(rows, cols):
    global matrix_entries, saved_result_matrix
    try:
        # Validate and get values
        m1 = []
        m2 = []
        has_error = False

        for i, entries in enumerate(matrix_entries):
            mat = []
            for row in entries:
                row_data = []
                for e in row:
                    value = e.get()
                    try:
                        num = float(value)
                        e.config(bg='white')
                        row_data.append(num)
                    except:
                        e.config(bg='red')
                        has_error = True
                mat.append(row_data)
            if i == 0:
                m1 = mat
            else:
                m2 = mat

        if has_error:
            messagebox.showerror("Input Error", "Please correct red fields (invalid numbers).")
            return

        result = [[m1[r][c] - m2[r][c] for c in range(cols)] for r in range(rows)]

        # Save result
        saved_result_matrix = result

        # Show result
        for widget in result_frame.winfo_children():
            widget.destroy()

        lf = tk.LabelFrame(result_frame, text="Result")
        lf.pack()
        for r in range(rows):
            for c in range(cols):
                e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
                e.grid(row=r, column=c, padx=2, pady=2)
                e.insert(0, str(result[r][c]))
                e.config(state='readonly')

    except Exception as e:
        messagebox.showerror("Error", str(e))


# --- ADD BUTTONS ---
btn_subtract = tk.Button(operations_frame, text="Subtract", width=12, font=(FONT_MAIN,16), command=subtract_matrices_mode)
btn_subtract.grid(row=0, column=1, padx=5)
def load_saved_result_as_input():
    global saved_result_matrix, matrix_entries

    if saved_result_matrix is None:
        messagebox.showinfo("No Saved Result", "There is no saved result to load.")
        return

    # Clear current inputs
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()

    rows = len(saved_result_matrix)
    cols = len(saved_result_matrix[0])

    entries = []
    lf = tk.LabelFrame(matrix_input_frame, text="Loaded Matrix")
    lf.pack(padx=5, pady=5)
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(saved_result_matrix[r][c]))
            row_entries.append(e)
        entries.append(row_entries)

    matrix_entries.clear()

saved_result_matrix = None
def use_result_with_new_matrix():
    global saved_result_matrix, matrix_entries

    if saved_result_matrix is None:
        messagebox.showinfo("No Saved Result", "There is no saved result to load.")
        return

    # Clear current inputs and result
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

    rows = len(saved_result_matrix)
    cols = len(saved_result_matrix[0])

    matrix_entries.clear()

    # Matrix 1: saved result (readonly)
    lf1 = tk.LabelFrame(matrix_input_frame, text="Matrix 1 (Saved Result)")
    lf1.pack(padx=5, pady=5)
    entries1 = []
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(lf1, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(saved_result_matrix[r][c]))
            e.config(state='readonly')
            row_entries.append(e)
        entries1.append(row_entries)
    matrix_entries.append(entries1)

    # Matrix 2: new input
    lf2 = tk.LabelFrame(matrix_input_frame, text="Matrix 2 (New Input)")
    lf2.pack(padx=5, pady=5)
    entries2 = []
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(lf2, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            bind_entry_events(e, entries2, r, c, rows, cols)
            row_entries.append(e)
        entries2.append(row_entries)
    matrix_entries.append(entries2)

    # Buttons to do addition or subtraction
    btn_frame = tk.Frame(matrix_input_frame)
    btn_frame.pack(pady=10)

    btn_add_new = tk.Button(btn_frame, text="Add", font=(FONT_MAIN,16),
                            command=lambda: evaluate_saved_plus_input(rows, cols))
    btn_add_new.pack(side='left', padx=5)

    btn_sub_new = tk.Button(btn_frame, text="Subtract", font=(FONT_MAIN,16),
                            command=lambda: evaluate_saved_minus_input(rows, cols))
    btn_sub_new.pack(side='left', padx=5)
def evaluate_saved_plus_input(rows, cols):
    global matrix_entries, saved_result_matrix
    new_matrix_entries = matrix_entries[1]
    has_error = False

    new_matrix = []
    for row in new_matrix_entries:
        row_data = []
        for e in row:
            value = e.get()
            try:
                num = float(value)
                e.config(bg='white')
                row_data.append(num)
            except:
                e.config(bg='red')
                has_error = True
        new_matrix.append(row_data)

    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return

    result = [[saved_result_matrix[r][c] + new_matrix[r][c] for c in range(cols)] for r in range(rows)]
    saved_result_matrix = result

    show_result_matrix(result)
def evaluate_saved_minus_input(rows, cols):
    global matrix_entries, saved_result_matrix
    new_matrix_entries = matrix_entries[1]
    has_error = False

    new_matrix = []
    for row in new_matrix_entries:
        row_data = []
        for e in row:
            value = e.get()
            try:
                num = float(value)
                e.config(bg='white')
                row_data.append(num)
            except:
                e.config(bg='red')
                has_error = True
        new_matrix.append(row_data)

    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return

    result = [[saved_result_matrix[r][c] - new_matrix[r][c] for c in range(cols)] for r in range(rows)]
    saved_result_matrix = result

    show_result_matrix(result)
def show_result_matrix(result):
    for widget in result_frame.winfo_children():
        widget.destroy()

    rows = len(result)
    cols = len(result[0])

    lf = tk.LabelFrame(result_frame, text="Result")
    lf.pack()
    for r in range(rows):
        for c in range(cols):
            e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(result[r][c]))
            e.config(state='readonly')
btn_use_result = tk.Button(operations_frame, text="Use Result as Input", width=18, font=(FONT_MAIN,16),
                           command=use_result_with_new_matrix)
btn_use_result.grid(row=0, column=2, padx=5)

#multiply

def multiply_matrices_mode():
    global matrix_entries
    matrix_entries.clear()

    # Clear UI
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Ask dimensions (Matrix A: rows_A x cols_A, Matrix B: cols_A x cols_B)
    class MatrixMultiplyConfig(simpledialog.Dialog):
        def body(self, master):
            tk.Label(master, text="Matrix A rows:").grid(row=0, column=0, sticky='e')
            tk.Label(master, text="Matrix A columns / Matrix B rows:").grid(row=1, column=0, sticky='e')
            tk.Label(master, text="Matrix B columns:").grid(row=2, column=0, sticky='e')

            self.rows_a_entry = tk.Entry(master)
            self.cols_a_entry = tk.Entry(master)
            self.cols_b_entry = tk.Entry(master)

            self.rows_a_entry.grid(row=0, column=1)
            self.cols_a_entry.grid(row=1, column=1)
            self.cols_b_entry.grid(row=2, column=1)
            return self.rows_a_entry

        def apply(self):
            try:
                self.rows_a = int(self.rows_a_entry.get())
                self.cols_a = int(self.cols_a_entry.get())
                self.cols_b = int(self.cols_b_entry.get())
            except:
                self.rows_a = self.cols_a = self.cols_b = None

    dialog = MatrixMultiplyConfig(root, title="Matrix Multiplication Config")

    rows_a, cols_a, cols_b = dialog.rows_a, dialog.cols_a, dialog.cols_b
    if not rows_a or not cols_a or not cols_b or rows_a < 1 or cols_a < 1 or cols_b < 1:
        return

    num_matrices = 2  # Matrix A and Matrix B

    # Create entry fields
    shapes = [(rows_a, cols_a), (cols_a, cols_b)]
    for m in range(num_matrices):
        lf = tk.LabelFrame(matrix_input_frame, text=f"Matrix {m+1}")
        lf.pack(padx=5, pady=5)
        entries = []
        rows, cols = shapes[m]
        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
                e.grid(row=r, column=c, padx=2, pady=2)
                bind_entry_events(e, entries, r, c, rows, cols)
                row_entries.append(e)
            entries.append(row_entries)
        matrix_entries.append(entries)

    eval_btn = tk.Button(matrix_input_frame, text="Evaluate Multiplication", font=(FONT_MAIN,16),
                         command=lambda: evaluate_multiplication(rows_a, cols_a, cols_b))
    eval_btn.pack(pady=10)
def evaluate_multiplication(rows_a, cols_a, cols_b):
    global matrix_entries, last_result_matrix
    try:
        # Validate entries and highlight errors
        matrices = []
        has_error = False
        for entries in matrix_entries:
            mat = []
            for row in entries:
                row_data = []
                for e in row:
                    value = e.get()
                    try:
                        num = float(value)
                        e.config(bg='white')
                        row_data.append(num)
                    except:
                        e.config(bg='red')
                        has_error = True
                mat.append(row_data)
            matrices.append(mat)
        if has_error:
            messagebox.showerror("Input Error", "Please correct red fields.")
            return

        m1, m2 = matrices
        # Multiply m1 (rows_a x cols_a) * m2 (cols_a x cols_b)
        result = [[0]*cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += m1[i][k] * m2[k][j]

        last_result_matrix = result  # Save for next operation

        # Display result
        for widget in result_frame.winfo_children():
            widget.destroy()

        lf = tk.LabelFrame(result_frame, text="Result")
        lf.pack()
        for r in range(rows_a):
            for c in range(cols_b):
                e = tk.Entry(lf, width=9,font=(FONT_MAIN,16) ,justify='center')
                e.grid(row=r, column=c, padx=2, pady=2)
                e.insert(0, str(result[r][c]))
                e.config(state='readonly')

        # Add button to use result
        use_btn = tk.Button(result_frame, text="Use Result as Input", font=(FONT_MAIN,14),
                            command=lambda: use_result_in_multiplication(result))
        use_btn.pack(pady=5)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def use_result_in_multiplication(result_matrix):
    global matrix_entries
    matrix_entries.clear()
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()

    rows = len(result_matrix)
    cols = len(result_matrix[0])

    # Use result as Matrix A; ask user for Matrix B columns
    cols_b = simpledialog.askinteger("Matrix B columns", "Enter number of columns for new Matrix B:")
    if not cols_b or cols_b < 1:
        return

    # Matrix A (result) entries
    lf1 = tk.LabelFrame(matrix_input_frame, text="Matrix A (Previous Result)")
    lf1.pack(padx=5, pady=5)
    entries_a = []
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(lf1, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(result_matrix[r][c]))
            e.config(state='readonly')
            row_entries.append(e)
        entries_a.append(row_entries)
    matrix_entries.append(entries_a)

    # Matrix B (user input)
    lf2 = tk.LabelFrame(matrix_input_frame, text="Matrix B")
    lf2.pack(padx=5, pady=5)
    entries_b = []
    for r in range(cols):  # rows=cols of A
        row_entries = []
        for c in range(cols_b):
            e = tk.Entry(lf2, width=9,font=(FONT_MAIN,16) ,justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            bind_entry_events(e, entries_b, r, c, cols, cols_b)
            row_entries.append(e)
        entries_b.append(row_entries)
    matrix_entries.append(entries_b)

    eval_btn = tk.Button(matrix_input_frame, text="Evaluate Multiplication", font=(FONT_MAIN,16),
                         command=lambda: evaluate_multiplication(rows, cols, cols_b))
    eval_btn.pack(pady=10)
btn_multiply = tk.Button(operations_frame, text="Multiply", width=12, font=(FONT_MAIN,16), command=multiply_matrices_mode)
btn_multiply.grid(row=0, column=3, padx=5)
last_result_matrix = None  
#determinant mode
# Frame for determinaNTS
operations_frame = tk.Frame(Determinant_frame)
operations_frame.pack(pady=10)

det_input_frame = tk.Frame(Determinant_frame)
det_input_frame.pack(pady=10)

det_buttons_frame = tk.Frame(Determinant_frame)
det_buttons_frame.pack(pady=10)

det_result_frame = tk.Frame(Determinant_frame)
det_result_frame.pack(pady=10)

# --- HELPERS ---
def bind_entry_events(e, entries, r, c, rows, cols):
    def on_key(event):
        if event.keysym == 'Up' and r > 0:
            entries[r-1][c].focus_set()
            return 'break'
        elif event.keysym == 'Down' and r < rows-1:
            entries[r+1][c].focus_set()
            return 'break'
        elif event.keysym == 'Left' and c > 0:
            entries[r][c-1].focus_set()
            return 'break'
        elif event.keysym == 'Right' and c < cols-1:
            entries[r][c+1].focus_set()
            return 'break'
        elif event.keysym in ('Return', 'Tab'):
            next_r, next_c = r, c+1
            if next_c >= cols:
                next_c = 0
                next_r += 1
            if next_r < rows:
                entries[next_r][next_c].focus_set()
            return 'break'
        return None

    def on_validate(event):
        value = e.get()
        if value.strip() == '':
            e.config(bg='white')
            return
        try:
            float(value)
            e.config(bg='white')
        except:
            e.config(bg='red')

    e.bind('<KeyPress>', on_key)
    e.bind('<KeyRelease>', on_validate)
    e.bind('<FocusOut>', on_validate)

def get_matrix_from_entries(entries):
    has_error = False
    matrix = []
    for row in entries:
        row_data = []
        for e in row:
            try:
                num = float(e.get())
                e.config(bg='white')
                row_data.append(num)
            except:
                e.config(bg='red')
                has_error = True
        matrix.append(row_data)
    return matrix, has_error

def show_result_matrix(result):
    for widget in det_result_frame.winfo_children():
        widget.destroy()
    rows = len(result)
    cols = len(result[0])
    lf = tk.LabelFrame(det_result_frame, text="Result")
    lf.pack()
    for r in range(rows):
        for c in range(cols):
            e = tk.Entry(lf, width=9, font=(FONT_MAIN,16), justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            e.insert(0, str(result[r][c]))
            e.config(state='readonly')

def compute_determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(size):
        minor = [row[:c]+row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * compute_determinant(minor)
    return det

def compute_adjoint(matrix):
    size = len(matrix)
    adj = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            minor = [row[:j]+row[j+1:] for k,row in enumerate(matrix) if k != i]
            sign = (-1) ** (i + j)
            adj[j][i] = sign * compute_determinant(minor)
    return adj

# --- MAIN MODE ---
def determinant_mode():
    global matrix_entries
    matrix_entries.clear()

    # clear old widgets
    for frame in (det_input_frame, det_buttons_frame, det_result_frame):
        for w in frame.winfo_children():
            w.destroy()

    # ask size
    size = simpledialog.askinteger("Matrix Size", "Enter size of square matrix (2,3,4...):", parent=root)
    if not size or size < 1:
        return

    # build matrix input grid
    lf = tk.LabelFrame(det_input_frame, text="Matrix")
    lf.pack(padx=5, pady=5)
    entries = []
    for r in range(size):
        row_entries = []
        for c in range(size):
            e = tk.Entry(lf, width=9, font=(FONT_MAIN,16), justify='center')
            e.grid(row=r, column=c, padx=2, pady=2)
            bind_entry_events(e, entries, r, c, size, size)
            row_entries.append(e)
        entries.append(row_entries)
    matrix_entries.append(entries)

    # build buttons (once)
    btn_specs = [
        ("Determinant", lambda: evaluate_determinant(size)),
        ("Adjoint", lambda: evaluate_adjoint(size)),
        ("Inverse", lambda: evaluate_inverse(size)),
        ("Transpose", lambda: evaluate_transpose(size, size)),
    ]
    for text, cmd in btn_specs:
        tk.Button(det_buttons_frame, text=text, font=(FONT_MAIN,14), command=cmd)\
            .pack(side='left', padx=5, pady=5)

# --- EVALUATE FUNCTIONS ---
def evaluate_determinant(size):
    entries = matrix_entries[0]
    matrix, has_error = get_matrix_from_entries(entries)
    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return
    det = compute_determinant(matrix)
    show_result_matrix([[det]])

def evaluate_adjoint(size):
    entries = matrix_entries[0]
    matrix, has_error = get_matrix_from_entries(entries)
    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return
    adj = compute_adjoint(matrix)
    show_result_matrix(adj)

def evaluate_inverse(size):
    entries = matrix_entries[0]
    matrix, has_error = get_matrix_from_entries(entries)
    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return
    det = compute_determinant(matrix)
    if det == 0:
        messagebox.showerror("Math Error", "Matrix is singular, cannot compute inverse.")
        return
    adj = compute_adjoint(matrix)
    inverse = [[adj[r][c]/det for c in range(size)] for r in range(size)]
    show_result_matrix(inverse)

def evaluate_transpose(rows, cols):
    entries = matrix_entries[0]
    matrix, has_error = get_matrix_from_entries(entries)
    if has_error:
        messagebox.showerror("Input Error", "Please correct red fields.")
        return
    transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    show_result_matrix(transposed)

# --- OPEN MODE BUTTON ---
btn_open_mode = tk.Button(operations_frame, text="ENTER THE CONFIGURATION OF THE MATRIX", width=40, font=(FONT_MAIN,16),
                          command=determinant_mode)
btn_open_mode.pack(pady=10)

# ==============================================================================
# PROGRESSION & SERIES MODE (MATCHING DIMENSITY JETBRAINS MONO UI)
# ==============================================================================
class BaseProgressionTool(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#121212", padx=20, pady=16,
                         highlightbackground="#282828", highlightthickness=1)

    def add_labeled_entry(self, parent, label_text, row):
        tk.Label(parent, text=label_text, font=("JetBrains Mono", 11, "bold"),
                 fg="#FFFFFF", bg="#181818").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(parent, width=16, font=("JetBrains Mono", 12),
                         bg="#0A0A0A", fg="#FBBF24", insertbackground="#FFFFFF",
                         bd=1, relief="solid", highlightbackground="#282828")
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def create_action_button(self, parent, text, cmd):
        return tk.Button(parent, text=text, command=cmd, font=("JetBrains Mono", 11, "bold"),
                         bg="#10B981", fg="#000000", activebackground="#34D399",
                         bd=0, padx=16, pady=4, cursor="hand2")

    def create_section_frame(self, text):
        f = tk.LabelFrame(self, text=f" {text} ", font=("JetBrains Mono", 11, "bold"),
                          fg="#FBBF24", bg="#181818", bd=1, relief="solid",
                          padx=12, pady=8)
        f.pack(padx=8, pady=6, fill='x')
        return f

    def create_output_widget(self, height=7):
        tk.Label(self, text="⚡ Output Console:", font=("JetBrains Mono", 11, "bold"),
                 fg="#38BDF8", bg="#121212").pack(anchor='w', pady=(8, 2))
        self.output_text = tk.Text(self, height=height, width=58, wrap='word',
                                   font=("JetBrains Mono", 12, "bold"),
                                   bg="#050505", fg="#00E5FF", insertbackground="#FFFFFF",
                                   bd=1, relief="solid", highlightbackground="#282828")
        self.output_text.pack(pady=4)

    def get_float(self, entry, default=0):
        try: return float(entry.get())
        except: return default

    def get_int(self, entry, default=0):
        try: return int(entry.get())
        except: return default

    def show_output(self, text):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, text)

# --- AP Tool ---
class APTool(BaseProgressionTool):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Arithmetic Progression (AP)", font=("JetBrains Mono", 14, 'bold'),
                 fg="#00E5FF", bg="#121212").pack(pady=(0, 6))

        # Part 1: Missing Parameter
        part1 = self.create_section_frame("Find Missing Parameter (leave 1 blank)")
        self.a_entry = self.add_labeled_entry(part1, "First Term (a):", 0)
        self.l_entry = self.add_labeled_entry(part1, "Last Term (l):", 1)
        self.d_entry = self.add_labeled_entry(part1, "Common Diff (d):", 2)
        self.n_entry = self.add_labeled_entry(part1, "Num Terms (n):", 3)
        self.create_action_button(part1, "Find Parameter", self.find_missing_param).grid(row=4, column=0, columnspan=2, pady=6)

        # Part 2: Sum
        part_sum = self.create_section_frame("Find Sum of Series")
        self.sum_a_entry = self.add_labeled_entry(part_sum, "First Term (a):", 0)
        self.sum_d_entry = self.add_labeled_entry(part_sum, "Common Diff (d):", 1)
        self.sum_n_entry = self.add_labeled_entry(part_sum, "Num Terms (n):", 2)
        self.create_action_button(part_sum, "Calculate Sum", self.find_sum).grid(row=3, column=0, columnspan=2, pady=6)

        # Part 3: Generate
        part2 = self.create_section_frame("Generate AP Series")
        self.gen_a_entry = self.add_labeled_entry(part2, "First Term (a):", 0)
        self.gen_d_entry = self.add_labeled_entry(part2, "Common Diff (d):", 1)
        self.gen_n_entry = self.add_labeled_entry(part2, "Num Terms (n):", 2)
        self.create_action_button(part2, "Generate Series", self.generate_series).grid(row=3, column=0, columnspan=2, pady=6)

        self.create_output_widget(height=6)

    def find_missing_param(self):
        fields = [self.a_entry.get(), self.l_entry.get(), self.d_entry.get(), self.n_entry.get()]
        empty_indices = [i for i, val in enumerate(fields) if val.strip() == '']
        if len(empty_indices) != 1:
            self.show_output("Please leave exactly ONE field empty to find it.")
            return

        missing = empty_indices[0]
        a = self.get_float(self.a_entry)
        l = self.get_float(self.l_entry)
        d = self.get_float(self.d_entry)
        n = self.get_float(self.n_entry)

        try:
            if missing == 0:
                self.show_output(f"First term (a) = {l - (n - 1) * d}")
            elif missing == 1:
                self.show_output(f"Last term (l) = {a + (n - 1) * d}")
            elif missing == 2:
                if n > 1:
                    self.show_output(f"Common difference (d) = {(l - a) / (n - 1)}")
                else:
                    self.show_output("Number of terms must be >1 to find d.")
            elif missing == 3:
                if d != 0:
                    self.show_output(f"Number of terms (n) = {int(((l - a) / d) + 1)}")
                else:
                    self.show_output("Common difference cannot be zero.")
        except Exception as e:
            self.show_output(f"Calculation Error: {e}")

    def find_sum(self):
        a = self.get_float(self.sum_a_entry)
        d = self.get_float(self.sum_d_entry)
        n = self.get_float(self.sum_n_entry)
        if n > 0:
            S = n / 2 * (2 * a + (n - 1) * d)
            self.show_output(f"Sum of AP Series (S_{int(n)}) = {S}")
        else:
            self.show_output("Number of terms must be > 0.")

    def generate_series(self):
        a = self.get_float(self.gen_a_entry)
        d = self.get_float(self.gen_d_entry)
        n = self.get_int(self.gen_n_entry)
        try:
            series = [a + i * d for i in range(n)]
            self.show_output("AP Series:\n" + ', '.join(map(str, series)))
        except Exception as e:
            self.show_output(f"Error generating series: {e}")

# --- GP Tool ---
class GPTool(BaseProgressionTool):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Geometric Progression (GP)", font=("JetBrains Mono", 14, 'bold'),
                 fg="#00E5FF", bg="#121212").pack(pady=(0, 6))

        part1 = self.create_section_frame("Find Missing Parameter (leave 1 blank)")
        self.a_entry = self.add_labeled_entry(part1, "First Term (a):", 0)
        self.l_entry = self.add_labeled_entry(part1, "Last Term (l):", 1)
        self.r_entry = self.add_labeled_entry(part1, "Common Ratio (r):", 2)
        self.n_entry = self.add_labeled_entry(part1, "Num Terms (n):", 3)
        self.create_action_button(part1, "Find Parameter", self.find_missing_param).grid(row=4, column=0, columnspan=2, pady=6)

        part_sum = self.create_section_frame("Find Sum of Series")
        self.sum_a_entry = self.add_labeled_entry(part_sum, "First Term (a):", 0)
        self.sum_r_entry = self.add_labeled_entry(part_sum, "Common Ratio (r):", 1)
        self.sum_n_entry = self.add_labeled_entry(part_sum, "Num Terms (n):", 2)
        self.create_action_button(part_sum, "Calculate Sum", self.find_sum).grid(row=3, column=0, columnspan=2, pady=6)

        part2 = self.create_section_frame("Generate GP Series")
        self.gen_a_entry = self.add_labeled_entry(part2, "First Term (a):", 0)
        self.gen_r_entry = self.add_labeled_entry(part2, "Common Ratio (r):", 1)
        self.gen_n_entry = self.add_labeled_entry(part2, "Num Terms (n):", 2)
        self.create_action_button(part2, "Generate Series", self.generate_series).grid(row=3, column=0, columnspan=2, pady=6)

        self.create_output_widget(height=6)

    def find_missing_param(self):
        fields = [self.a_entry.get(), self.l_entry.get(), self.r_entry.get(), self.n_entry.get()]
        empty_indices = [i for i, val in enumerate(fields) if val.strip() == '']
        if len(empty_indices) != 1:
            self.show_output("Please leave exactly ONE field empty to find it.")
            return

        missing = empty_indices[0]
        a = self.get_float(self.a_entry)
        l = self.get_float(self.l_entry)
        r = self.get_float(self.r_entry)
        n = self.get_float(self.n_entry)

        try:
            if missing == 0:
                if r != 0: self.show_output(f"First term (a) = {l / (r ** (n - 1))}")
                else: self.show_output("Common ratio cannot be zero.")
            elif missing == 1:
                self.show_output(f"Last term (l) = {a * (r ** (n - 1))}")
            elif missing == 2:
                if a != 0 and n > 1: self.show_output(f"Common ratio (r) = {(l / a) ** (1 / (n - 1))}")
                else: self.show_output("Check a≠0 and n>1.")
            elif missing == 3:
                if a != 0 and r != 0:
                    import math
                    self.show_output(f"Number of terms (n) ≈ {int(round(math.log(l / a, r) + 1))}")
                else: self.show_output("Check a≠0 and r≠0.")
        except Exception as e:
            self.show_output(f"Calculation Error: {e}")

    def find_sum(self):
        a = self.get_float(self.sum_a_entry)
        r = self.get_float(self.sum_r_entry)
        n = self.get_float(self.sum_n_entry)
        try:
            S = a * n if r == 1 else a * (1 - r ** n) / (1 - r)
            self.show_output(f"Sum of GP Series (S) = {S}")
        except Exception as e:
            self.show_output(f"Error calculating sum: {e}")

    def generate_series(self):
        a = self.get_float(self.gen_a_entry)
        r = self.get_float(self.gen_r_entry)
        n = self.get_int(self.gen_n_entry)
        try:
            series = [a * (r ** i) for i in range(n)]
            self.show_output("GP Series:\n" + ', '.join(map(str, series)))
        except Exception as e:
            self.show_output(f"Error generating series: {e}")

# --- HP Tool ---
class HPTool(BaseProgressionTool):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Harmonic Progression (HP)", font=("JetBrains Mono", 14, 'bold'),
                 fg="#00E5FF", bg="#121212").pack(pady=(0, 6))

        part1 = self.create_section_frame("Find Missing Parameter (leave 1 blank)")
        self.a_entry = self.add_labeled_entry(part1, "First Term (a):", 0)
        self.l_entry = self.add_labeled_entry(part1, "Last Term (l):", 1)
        self.d_entry = self.add_labeled_entry(part1, "Common Diff (d):", 2)
        self.n_entry = self.add_labeled_entry(part1, "Num Terms (n):", 3)
        self.create_action_button(part1, "Find Parameter", self.find_missing_param).grid(row=4, column=0, columnspan=2, pady=6)

        part_sum = self.create_section_frame("Find HP Sum (Approximate)")
        self.sum_a_entry = self.add_labeled_entry(part_sum, "First Term (a):", 0)
        self.sum_d_entry = self.add_labeled_entry(part_sum, "Common Diff (d):", 1)
        self.sum_n_entry = self.add_labeled_entry(part_sum, "Num Terms (n):", 2)
        self.create_action_button(part_sum, "Calculate Sum", self.find_sum).grid(row=3, column=0, columnspan=2, pady=6)

        part2 = self.create_section_frame("Generate HP Series")
        self.gen_a_entry = self.add_labeled_entry(part2, "First Term (a):", 0)
        self.gen_d_entry = self.add_labeled_entry(part2, "Common Diff (d):", 1)
        self.gen_n_entry = self.add_labeled_entry(part2, "Num Terms (n):", 2)
        self.create_action_button(part2, "Generate Series", self.generate_series).grid(row=3, column=0, columnspan=2, pady=6)

        self.create_output_widget(height=6)

    def find_missing_param(self):
        fields = [self.a_entry.get(), self.l_entry.get(), self.d_entry.get(), self.n_entry.get()]
        empty_indices = [i for i, val in enumerate(fields) if val.strip() == '']
        if len(empty_indices) != 1:
            self.show_output("Please leave exactly ONE field empty to find it.")
            return
        missing = empty_indices[0]
        a = self.get_float(self.a_entry)
        l = self.get_float(self.l_entry)
        d = self.get_float(self.d_entry)
        n = self.get_float(self.n_entry)
        try:
            if missing == 0: self.show_output(f"First term (a) = {l - (n - 1) * d}")
            elif missing == 1: self.show_output(f"Last term (l) = {a + (n - 1) * d}")
            elif missing == 2:
                if n > 1: self.show_output(f"Common difference (d) = {(l - a) / (n - 1)}")
                else: self.show_output("n must be > 1 to find d.")
            elif missing == 3:
                if d != 0: self.show_output(f"Number of terms (n) = {int(((l - a) / d) + 1)}")
                else: self.show_output("d cannot be zero.")
        except Exception as e:
            self.show_output(f"Error calculating: {e}")

    def find_sum(self):
        a = self.get_float(self.sum_a_entry)
        d = self.get_float(self.sum_d_entry)
        n = self.get_int(self.sum_n_entry)
        try:
            terms = [a + i * d for i in range(n)]
            hp_terms = [1 / t for t in terms if t != 0]
            self.show_output(f"Approximate sum of HP series = {sum(hp_terms)}")
        except Exception as e:
            self.show_output(f"Error calculating sum: {e}")

    def generate_series(self):
        a = self.get_float(self.gen_a_entry)
        d = self.get_float(self.gen_d_entry)
        n = self.get_int(self.gen_n_entry)
        try:
            terms = [a + i * d for i in range(n)]
            hp_terms = [1 / t if t != 0 else 'inf' for t in terms]
            self.show_output("HP Series:\n" + ', '.join(map(str, hp_terms)))
        except Exception as e:
            self.show_output(f"Error generating series: {e}")

# --- Special Series Tool ---
class SpecialSeriesTool(BaseProgressionTool):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Special Mathematical Series", font=("JetBrains Mono", 14, 'bold'),
                 fg="#00E5FF", bg="#121212").pack(pady=(0, 6))

        btn_frame = tk.Frame(self, bg="#121212")
        btn_frame.pack(pady=4)

        self.series_type = "fibonacci"
        self.series_btns = {}

        types = [("Fibonacci", "fibonacci"), ("Squares", "squares"), ("Cubes", "cubes"),
                 ("Primes", "primes"), ("Factorials", "factorials")]
        for idx, (lbl, stype) in enumerate(types):
            b = tk.Button(btn_frame, text=lbl, font=("JetBrains Mono", 11, "bold"), width=11,
                          bd=0, padx=6, pady=4, cursor="hand2",
                          command=lambda s=stype: self.load_series(s))
            b.grid(row=0 if idx < 3 else 1, column=idx if idx < 3 else idx - 3, padx=4, pady=3)
            self.series_btns[stype] = b

        self.sub_frame = tk.Frame(self, bg="#181818", padx=10, pady=8, highlightbackground="#282828", highlightthickness=1)
        self.sub_frame.pack(pady=8, fill='x')

        self.create_output_widget(height=6)
        self.load_series("fibonacci")

    def load_series(self, series_type):
        self.series_type = series_type
        for st, b in self.series_btns.items():
            if st == series_type:
                b.config(bg="#FBBF24", fg="#000000", activebackground="#F59E0B")
            else:
                b.config(bg="#1E1E1E", fg="#A0A0A0", activebackground="#2A2A2A")

        for widget in self.sub_frame.winfo_children():
            widget.destroy()

        def make_row(row, lbl_text, btn_text, cmd_fn):
            tk.Label(self.sub_frame, text=lbl_text, font=("JetBrains Mono", 11, "bold"),
                     fg="#FFFFFF", bg="#181818").grid(row=row, column=0, sticky='w', padx=6, pady=3)
            entry = tk.Entry(self.sub_frame, width=10, font=("JetBrains Mono", 12),
                             bg="#0A0A0A", fg="#FBBF24", insertbackground="#FFFFFF",
                             bd=1, relief="solid", highlightbackground="#282828")
            entry.grid(row=row, column=1, padx=6, pady=3)
            self.create_action_button(self.sub_frame, btn_text, lambda: cmd_fn(entry)).grid(row=row, column=2, padx=6, pady=3)

        make_row(0, "Generate first n terms:", "Generate", self.generate_series)
        make_row(1, "Find nth term of series:", "Find Term", self.find_nth_term)
        make_row(2, "Sum of first m terms:", "Sum", self.sum_of_terms)
        make_row(3, "Check membership of num:", "Verify", self.check_term)

    def generate_series(self, n_entry):
        n = self.get_int(n_entry)
        if n <= 0:
            self.show_output("Enter a valid integer > 0.")
            return
        series = self.build_series(n)
        self.show_output(f"{self.series_type.title()} Series (first {n} terms):\n" + ', '.join(map(str, series)))

    def build_series(self, n):
        if self.series_type == "fibonacci":
            fib = [0, 1]
            while len(fib) < n: fib.append(fib[-1] + fib[-2])
            return fib[:n]
        elif self.series_type == "squares": return [i * i for i in range(1, n + 1)]
        elif self.series_type == "cubes": return [i ** 3 for i in range(1, n + 1)]
        elif self.series_type == "primes":
            primes, num = [], 2
            while len(primes) < n:
                if all(num % p != 0 for p in primes if p * p <= num): primes.append(num)
                num += 1
            return primes
        elif self.series_type == "factorials": return [math.factorial(i) for i in range(1, n + 1)]
        return []

    def find_nth_term(self, nth_entry):
        n = self.get_int(nth_entry)
        if n <= 0: return self.show_output("Enter valid n > 0.")
        try:
            if self.series_type == "fibonacci":
                a, b = 0, 1
                for _ in range(n - 1): a, b = b, a + b
                res = a
            elif self.series_type == "squares": res = n * n
            elif self.series_type == "cubes": res = n ** 3
            elif self.series_type == "primes":
                count, num, last = 0, 2, None
                while count < n:
                    if all(num % p != 0 for p in range(2, int(num ** 0.5) + 1)):
                        last, count = num, count + 1
                    num += 1
                res = last
            elif self.series_type == "factorials": res = math.factorial(n)
            else: res = "Unknown"
            self.show_output(f"{n}th term of {self.series_type.title()} = {res}")
        except Exception as e:
            self.show_output(f"Error: {e}")

    def sum_of_terms(self, sum_entry):
        m = self.get_int(sum_entry)
        if m <= 0: return self.show_output("Enter valid m > 0.")
        try:
            if self.series_type == "fibonacci":
                fib = [0, 1]
                while len(fib) < m: fib.append(fib[-1] + fib[-2])
                res = sum(fib[:m])
            elif self.series_type == "squares": res = m * (m + 1) * (2 * m + 1) // 6
            elif self.series_type == "cubes":
                s = m * (m + 1) // 2
                res = s * s
            elif self.series_type == "primes":
                primes, num = [], 2
                while len(primes) < m:
                    if all(num % p != 0 for p in primes if p * p <= num): primes.append(num)
                    num += 1
                res = sum(primes)
            elif self.series_type == "factorials": res = sum(math.factorial(i) for i in range(1, m + 1))
            else: res = "Unknown"
            self.show_output(f"Sum of first {m} terms = {res}")
        except Exception as e:
            self.show_output(f"Error: {e}")

    def check_term(self, check_entry):
        t = self.get_int(check_entry)
        if t <= 0: return self.show_output("Enter positive integer.")
        try:
            if self.series_type == "fibonacci":
                x = 5 * t * t
                is_fib = (int(math.isqrt(x + 4)) ** 2 == x + 4) or (int(math.isqrt(x - 4)) ** 2 == x - 4)
                msg = f"{t} {'BELONGS' if is_fib else 'does NOT belong'} to Fibonacci."
            elif self.series_type == "squares":
                is_sq = int(math.isqrt(t)) ** 2 == t
                msg = f"{t} {'IS' if is_sq else 'is NOT'} a square."
            elif self.series_type == "cubes":
                is_cb = round(t ** (1 / 3)) ** 3 == t
                msg = f"{t} {'IS' if is_cb else 'is NOT'} a cube."
            elif self.series_type == "primes":
                is_pr = t > 1 and all(t % i != 0 for i in range(2, int(t ** 0.5) + 1))
                msg = f"{t} {'IS' if is_pr else 'is NOT'} a prime number."
            elif self.series_type == "factorials":
                i, f = 1, 1
                while f < t: i += 1; f *= i
                msg = f"{t} {'IS' if f == t else 'is NOT'} a factorial number ({i}!)."
            else: msg = "Unknown"
            self.show_output(msg)
        except Exception as e:
            self.show_output(f"Error: {e}")

# --- Progression Main Wrapper ---
class ProgressionMode(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#000000", padx=10, pady=8)

        tk.Label(self, text="📈 Progression & Series Mode", font=("JetBrains Mono", 16, 'bold'),
                 fg="#FBBF24", bg="#000000").pack(pady=(2, 8))

        btn_frame = tk.Frame(self, bg="#000000")
        btn_frame.pack(pady=4)

        self.nav_btns = {}
        for idx, (title, cmd) in enumerate([
            ("AP", self.load_ap),
            ("GP", self.load_gp),
            ("HP", self.load_hp),
            ("Special Series", self.load_special)
        ]):
            btn = tk.Button(btn_frame, text=title, font=("JetBrains Mono", 12, "bold"),
                            width=14, bd=0, padx=8, pady=6, cursor="hand2", command=cmd)
            btn.grid(row=0, column=idx, padx=6)
            self.nav_btns[title] = btn

        self.sub_frame = tk.Frame(self, bg="#000000")
        self.sub_frame.pack(pady=8)

        self.load_ap()

    def set_active_tab(self, active_title):
        for t, b in self.nav_btns.items():
            if t == active_title:
                b.config(bg="#FBBF24", fg="#000000", activebackground="#F59E0B")
            else:
                b.config(bg="#1E1E1E", fg="#A0A0A0", activebackground="#2A2A2A")

    def clear_sub_frame(self):
        for widget in self.sub_frame.winfo_children():
            widget.destroy()

    def load_ap(self):
        self.set_active_tab("AP")
        self.clear_sub_frame()
        APTool(self.sub_frame).pack()

    def load_gp(self):
        self.set_active_tab("GP")
        self.clear_sub_frame()
        GPTool(self.sub_frame).pack()

    def load_hp(self):
        self.set_active_tab("HP")
        self.clear_sub_frame()
        HPTool(self.sub_frame).pack()

    def load_special(self):
        self.set_active_tab("Special Series")
        self.clear_sub_frame()
        SpecialSeriesTool(self.sub_frame).pack()

progression_widget = ProgressionMode(progression_frame)
progression_widget.pack(padx=10, pady=10)




#programming frame


class ProgrammingMode(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.input_base = 'DEC'  # default input base
        self.create_widgets()

    def create_widgets(self):
        # --- Title ---
        tk.Label(self, text="Programming Mode", font=(FONT_MAIN, 18, "bold")).pack(pady=10)

        # --- Base selection buttons ---
        base_frame = tk.Frame(self)
        base_frame.pack(pady=5)
        for base in ['BIN', 'OCT', 'DEC', 'HEX']:
            btn = tk.Button(base_frame, text=base, width=6, font=(FONT_MAIN, 12, "bold"),
                            command=lambda b=base: self.set_base(b))
            btn.pack(side='left', padx=3)
        self.base_label = tk.Label(self, text="Current Base: DEC", font=(FONT_MAIN, 12, "italic"))
        self.base_label.pack(pady=5)

        # --- Input Entry ---
        self.input_var = tk.StringVar()
        input_entry = tk.Entry(self, textvariable=self.input_var, font=("Consolas", 16), width=25, justify='center')
        input_entry.pack(pady=5)
        self.input_var.trace_add('write', self.update_conversions)

        # --- Conversion labels ---
        self.bin_label = tk.Label(self, text="BIN: -", font=("Consolas", 14))
        self.bin_label.pack(anchor='w', padx=20)
        self.oct_label = tk.Label(self, text="OCT: -", font=("Consolas", 14))
        self.oct_label.pack(anchor='w', padx=20)
        self.dec_label = tk.Label(self, text="DEC: -", font=("Consolas", 14))
        self.dec_label.pack(anchor='w', padx=20)
        self.hex_label = tk.Label(self, text="HEX: -", font=("Consolas", 14))
        self.hex_label.pack(anchor='w', padx=20)

        # --- Bitwise operations ---
        tk.Label(self, text="Bitwise Operations", font=(FONT_MAIN, 16, "bold")).pack(pady=(15,5))
        bit_frame = tk.Frame(self)
        bit_frame.pack(pady=5)

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()

        tk.Entry(bit_frame, textvariable=self.num1_var, font=("Consolas", 14), width=10).pack(side='left', padx=3)
        tk.Entry(bit_frame, textvariable=self.num2_var, font=("Consolas", 14), width=10).pack(side='left', padx=3)

        op_frame = tk.Frame(self)
        op_frame.pack(pady=5)
        tk.Button(op_frame, text="AND", width=8, command=self.bitwise_and).pack(side='left', padx=2)
        tk.Button(op_frame, text="OR", width=8, command=self.bitwise_or).pack(side='left', padx=2)
        tk.Button(op_frame, text="XOR", width=8, command=self.bitwise_xor).pack(side='left', padx=2)
        tk.Button(op_frame, text="NOT (1st)", width=8, command=self.bitwise_not).pack(side='left', padx=2)

        # --- Bit shifts ---
        tk.Label(self, text="Bit Shifts", font=(FONT_MAIN, 16, "bold")).pack(pady=(10,5))
        shift_frame = tk.Frame(self)
        shift_frame.pack(pady=5)
        self.shift_num_var = tk.StringVar()
        self.shift_places_var = tk.StringVar()
        tk.Entry(shift_frame, textvariable=self.shift_num_var, font=("Consolas", 14), width=10).pack(side='left', padx=3)
        tk.Entry(shift_frame, textvariable=self.shift_places_var, font=("Consolas", 14), width=5).pack(side='left', padx=3)
        shift_btn_frame = tk.Frame(self)
        shift_btn_frame.pack(pady=5)
        tk.Button(shift_btn_frame, text="<< Left", width=10, command=self.shift_left).pack(side='left', padx=2)
        tk.Button(shift_btn_frame, text=">> Right", width=10, command=self.shift_right).pack(side='left', padx=2)

        # --- Result bar ---
        self.result_var = tk.StringVar(value="Result will appear here")
        tk.Entry(self, textvariable=self.result_var, font=("Consolas", 16), width=35, justify='center', bg="#f0f0f0").pack(pady=10, padx=10, ipady=4)

    def set_base(self, base):
        self.input_base = base
        self.base_label.config(text=f"Current Base: {base}")
        self.update_conversions()

    def update_conversions(self, *args):
        val = self.input_var.get().strip()
        try:
            n = int(val, {'BIN':2, 'OCT':8, 'DEC':10, 'HEX':16}[self.input_base])
            self.bin_label.config(text=f"BIN: {bin(n)[2:]}")
            self.oct_label.config(text=f"OCT: {oct(n)[2:]}")
            self.dec_label.config(text=f"DEC: {n}")
            self.hex_label.config(text=f"HEX: {hex(n)[2:].upper()}")
        except:
            self.bin_label.config(text="BIN: -")
            self.oct_label.config(text="OCT: -")
            self.dec_label.config(text="DEC: -")
            self.hex_label.config(text="HEX: -")

    # Bitwise
    def bitwise_and(self):
        self.do_bitwise_op(lambda a,b: a & b, "AND")

    def bitwise_or(self):
        self.do_bitwise_op(lambda a,b: a | b, "OR")

    def bitwise_xor(self):
        self.do_bitwise_op(lambda a,b: a ^ b, "XOR")

    def bitwise_not(self):
        try:
            a = int(self.num1_var.get())
            res = ~a
            self.result_var.set(f"NOT {a} = {res}")
        except:
            self.result_var.set("Invalid Input")

    def do_bitwise_op(self, func, op_name):
        try:
            a = int(self.num1_var.get())
            b = int(self.num2_var.get())
            res = func(a,b)
            self.result_var.set(f"{a} {op_name} {b} = {res}")
        except:
            self.result_var.set("Invalid Input")

    # Shift
    def shift_left(self):
        self.do_shift_op(lambda n,p: n << p, "<<")

    def shift_right(self):
        self.do_shift_op(lambda n,p: n >> p, ">>")

    def do_shift_op(self, func, op_name):
        try:
            n = int(self.shift_num_var.get())
            p = int(self.shift_places_var.get())
            res = func(n,p)
            self.result_var.set(f"{n} {op_name} {p} = {res}")
        except:
            self.result_var.set("Invalid Input")

programming_widget = ProgrammingMode(programming_frame)
programming_widget.pack(padx=10, pady=10)
#pandc
# --- PERMUTATIONS & COMBINATIONS (MATCHING DIMENSITY UI) ---
perm_comb_frame = tk.Frame(permutations_frame, bg="#000000")
perm_comb_frame.pack(pady=12)

perm_content_frame = tk.Frame(permutations_frame, bg="#000000")
perm_content_frame.pack(pady=10)

# Configure dark theme for ttk Comboboxes
comb_style = ttk.Style()
try:
    comb_style.theme_use('clam')
except Exception:
    pass
comb_style.configure('Dark.TCombobox',
                     fieldbackground='#1E1E1E',
                     background='#282828',
                     foreground='#FFFFFF',
                     arrowcolor='#FBBF24',
                     selectbackground='#1E1E1E',
                     selectforeground='#FFFFFF',
                     bordercolor='#282828')

# Toggle buttons
def highlight_active(active):
    if active == 'perm':
        perm_button.config(bg="#FBBF24", fg="#000000", activebackground="#F59E0B")
        comb_button.config(bg="#1E1E1E", fg="#A0A0A0", activebackground="#2A2A2A")
    else:
        comb_button.config(bg="#FBBF24", fg="#000000", activebackground="#F59E0B")
        perm_button.config(bg="#1E1E1E", fg="#A0A0A0", activebackground="#2A2A2A")

perm_button = tk.Button(perm_comb_frame, text="Permutations (nPr)", font=(FONT_MAIN, 13, "bold"),
                        width=20, bd=0, padx=12, pady=8, cursor="hand2", command=lambda: show_permutations())
perm_button.grid(row=0, column=0, padx=12)

comb_button = tk.Button(perm_comb_frame, text="Combinations (nCr)", font=(FONT_MAIN, 13, "bold"),
                        width=20, bd=0, padx=12, pady=8, cursor="hand2", command=lambda: show_combinations())
comb_button.grid(row=0, column=1, padx=12)

def show_permutations():
    highlight_active('perm')
    for widget in perm_content_frame.winfo_children():
        widget.destroy()
    build_permutations_content()

def show_combinations():
    highlight_active('comb')
    for widget in perm_content_frame.winfo_children():
        widget.destroy()
    build_combinations_content()

def build_permutations_content():
    card = tk.Frame(perm_content_frame, bg="#121212", highlightbackground="#282828", highlightthickness=1, padx=32, pady=20)
    card.pack(pady=4)

    tk.Label(card, text="Select Problem Type:", font=(FONT_MAIN, 14, "bold"), fg="#FFFFFF", bg="#121212").pack(anchor='w', pady=(0, 6))

    problem_var = tk.StringVar(value="nPr")
    problem_combo = ttk.Combobox(card, textvariable=problem_var, font=(FONT_MAIN, 13), width=34,
                                 state="readonly", style="Dark.TCombobox")
    problem_combo['values'] = [
        "nPr",
        "With repetition",
        "Without repetition",
        "Circular permutations",
        "Dictionary rank",
        "Letters together"
    ]
    problem_combo.pack(pady=8)

    input_frame = tk.Frame(card, bg="#121212")
    input_frame.pack(pady=12)

    word_var = tk.StringVar()
    r_var = tk.StringVar()
    extra_var = tk.StringVar()
    result_var = tk.StringVar(value="Result will appear here")

    example_var = tk.StringVar(value="Example: n=5, r=3 ⇒ Number of permutations 5P3")
    tk.Label(card, textvariable=example_var, font=(FONT_MAIN, 12, "italic"), fg="#A0A0A0", bg="#121212").pack(pady=4)

    def evaluate():
        sel = problem_var.get()
        try:
            if sel == "nPr":
                n = int(word_var.get())
                r = int(r_var.get())
                res = factorial(n) // factorial(n - r)
                result_var.set(f"{n}P{r} = {res}")
            elif sel == "With repetition":
                word = word_var.get()
                r = int(r_var.get())
                res = len(word) ** r
                result_var.set(f"{len(word)}^{r} = {res}")
            elif sel == "Without repetition":
                word = word_var.get()
                r = int(r_var.get())
                n = len(word)
                res = factorial(n) // factorial(n - r)
                result_var.set(f"{n}P{r} = {res}")
            elif sel == "Circular permutations":
                n = int(word_var.get())
                res = factorial(n - 1)
                result_var.set(f"({n}-1)! = {res}")
            elif sel == "Dictionary rank":
                word = word_var.get().upper()
                rank = 1
                sorted_letters = sorted(word)
                for i, c in enumerate(word):
                    for smaller in filter(lambda x: x < c, sorted_letters):
                        temp = sorted_letters.copy()
                        temp.remove(smaller)
                        rank += factorial(len(temp))
                    sorted_letters.remove(c)
                result_var.set(f"Rank of '{word}' = {rank}")
            elif sel == "Letters together":
                word = word_var.get()
                group = extra_var.get()
                if not group or group not in word:
                    result_var.set("Invalid group or not in word")
                else:
                    n = len(word)
                    k = len(group)
                    remaining = n - k + 1
                    res = factorial(remaining)
                    result_var.set(f"Treat group as block: arrangements = {res}")
            else:
                result_var.set("Please select a problem type.")
        except Exception:
            result_var.set("Invalid input!")

    eval_btn = tk.Button(card, text="⚡ EVALUATE", font=(FONT_MAIN, 13, "bold"),
                         bg="#10B981", fg="#000000", activebackground="#34D399",
                         bd=0, padx=28, pady=8, cursor="hand2", command=evaluate)
    eval_btn.pack(pady=12)

    result_entry = tk.Entry(card, textvariable=result_var, font=(FONT_MAIN, 16, "bold"),
                            justify='center', width=36, bg="#050505", fg="#00E5FF",
                            bd=1, relief="solid", highlightbackground="#282828")
    result_entry.pack(pady=10, ipady=6)

    def update_inputs(event=None):
        for widget in input_frame.winfo_children():
            widget.destroy()
        sel = problem_var.get()

        def make_entry(row, label_text, var):
            tk.Label(input_frame, text=label_text, font=(FONT_MAIN, 13, "bold"), fg="#FFFFFF", bg="#121212").grid(row=row, column=0, sticky='w', padx=8, pady=6)
            ent = tk.Entry(input_frame, textvariable=var, font=(FONT_MAIN, 13), width=18,
                           bg="#1E1E1E", fg="#FBBF24", insertbackground="#FFFFFF", bd=1, relief="solid", highlightbackground="#282828")
            ent.grid(row=row, column=1, padx=8, pady=6)
            return ent

        if sel == "nPr":
            make_entry(0, "Enter n:", word_var)
            make_entry(1, "Enter r:", r_var)
            example_var.set("Example: n=5, r=3 ⇒ Number of permutations 5P3")
        elif sel in ["With repetition", "Without repetition"]:
            make_entry(0, "Enter word:", word_var)
            make_entry(1, "Length to form (r):", r_var)
            if sel == "With repetition":
                example_var.set("Example: word='ABC', r=2 ⇒ 3^2=9")
            else:
                example_var.set("Example: word='ABC', r=2 ⇒ 3P2=6")
        elif sel == "Circular permutations":
            make_entry(0, "Enter number of items (n):", word_var)
            example_var.set("Example: n=4 ⇒ Circular permutations=(4-1)!=6")
        elif sel == "Dictionary rank":
            make_entry(0, "Enter the word:", word_var)
            example_var.set("Example: Find rank of 'SMART' in all permutations")
        elif sel == "Letters together":
            make_entry(0, "Enter word:", word_var)
            make_entry(1, "Letter(s) to keep together:", extra_var)
            example_var.set("Example: word='APPLE', keep='PP' ⇒ treat as one block")

    problem_combo.bind("<<ComboboxSelected>>", update_inputs)
    update_inputs()

# Combinations State Variables
comb_problem_var = tk.StringVar(value="nCr")
comb_example_var = tk.StringVar(value="Example: n=5, r=2 ⇒ 5C2=10")
comb_word_var = tk.StringVar()
comb_r_var = tk.StringVar()
comb_n_var = tk.StringVar()
comb_result_var = tk.StringVar(value="Result will appear here")

def build_combinations_content():
    card = tk.Frame(perm_content_frame, bg="#121212", highlightbackground="#282828", highlightthickness=1, padx=32, pady=20)
    card.pack(pady=4)

    tk.Label(card, text="Select Problem Type:", font=(FONT_MAIN, 14, "bold"), fg="#FFFFFF", bg="#121212").pack(anchor='w', pady=(0, 6))

    comb_problem_combo = ttk.Combobox(card, textvariable=comb_problem_var,
                                      font=(FONT_MAIN, 13), width=34, state="readonly", style="Dark.TCombobox")
    comb_problem_combo['values'] = [
        "nCr",
        "With repetition",
        "Word selection",
        "Committees",
        "Identical items"
    ]
    comb_problem_combo.pack(pady=8)

    input_frame = tk.Frame(card, bg="#121212")
    input_frame.pack(pady=12)

    tk.Label(card, textvariable=comb_example_var, font=(FONT_MAIN, 12, "italic"), fg="#A0A0A0", bg="#121212").pack(pady=4)

    def evaluate_comb():
        sel = comb_problem_var.get()
        try:
            if sel == "nCr":
                n = int(comb_n_var.get())
                r = int(comb_r_var.get())
                res = factorial(n) // (factorial(r) * factorial(n - r))
                comb_result_var.set(f"{n}C{r} = {res}")
            elif sel == "With repetition":
                n = int(comb_n_var.get())
                r = int(comb_r_var.get())
                res = factorial(n + r - 1) // (factorial(r) * factorial(n - 1))
                comb_result_var.set(f"({n}+{r}-1)C{r} = {res}")
            elif sel == "Word selection":
                word = comb_word_var.get()
                r = int(comb_r_var.get())
                n = len(word)
                res = factorial(n) // (factorial(r) * factorial(n - r))
                comb_result_var.set(f"Select {r} from {word}: {n}C{r} = {res}")
            elif sel == "Committees":
                n = int(comb_n_var.get())
                r = int(comb_r_var.get())
                res = factorial(n) // (factorial(r) * factorial(n - r))
                comb_result_var.set(f"Choose {r} out of {n}: {n}C{r} = {res}")
            elif sel == "Identical items":
                word = comb_word_var.get().upper()
                letters = list(word)
                total = len(letters)
                counts = {}
                for c in letters:
                    counts[c] = counts.get(c, 0) + 1
                denom = 1
                for count in counts.values():
                    denom *= factorial(count)
                res = factorial(total) // denom
                comb_result_var.set(f"Unique combinations = {res}")
            else:
                comb_result_var.set("Please select a problem type.")
        except Exception:
            comb_result_var.set("Invalid input!")

    eval_btn = tk.Button(card, text="⚡ EVALUATE", font=(FONT_MAIN, 13, "bold"),
                         bg="#10B981", fg="#000000", activebackground="#34D399",
                         bd=0, padx=28, pady=8, cursor="hand2", command=evaluate_comb)
    eval_btn.pack(pady=12)

    res_entry = tk.Entry(card, textvariable=comb_result_var, font=(FONT_MAIN, 16, "bold"),
                         justify='center', width=36, bg="#050505", fg="#00E5FF",
                         bd=1, relief="solid", highlightbackground="#282828")
    res_entry.pack(pady=10, ipady=6)

    def update_comb_inputs(event=None):
        for widget in input_frame.winfo_children():
            widget.destroy()
        sel = comb_problem_var.get()

        def make_entry(row, label_text, var):
            tk.Label(input_frame, text=label_text, font=(FONT_MAIN, 13, "bold"), fg="#FFFFFF", bg="#121212").grid(row=row, column=0, sticky='w', padx=8, pady=6)
            ent = tk.Entry(input_frame, textvariable=var, font=(FONT_MAIN, 13), width=18,
                           bg="#1E1E1E", fg="#FBBF24", insertbackground="#FFFFFF", bd=1, relief="solid", highlightbackground="#282828")
            ent.grid(row=row, column=1, padx=8, pady=6)
            return ent

        if sel == "nCr":
            make_entry(0, "Enter n:", comb_n_var)
            make_entry(1, "Enter r:", comb_r_var)
            comb_example_var.set("Example: n=5, r=2 ⇒ 5C2=10")
        elif sel == "With repetition":
            make_entry(0, "Enter n:", comb_n_var)
            make_entry(1, "Enter r:", comb_r_var)
            comb_example_var.set("Example: pick 2 from A,B,C ⇒ (3+2-1)C2 = 6")
        elif sel == "Word selection":
            make_entry(0, "Enter word:", comb_word_var)
            make_entry(1, "Select r letters:", comb_r_var)
            comb_example_var.set("Example: word='APPLE', r=3 ⇒ 5C3=10")
        elif sel == "Committees":
            make_entry(0, "Total people (n):", comb_n_var)
            make_entry(1, "Select k people:", comb_r_var)
            comb_example_var.set("Example: n=10, k=3 ⇒ 10C3=120")
        elif sel == "Identical items":
            make_entry(0, "Enter word with repeats:", comb_word_var)
            comb_example_var.set("Example: word='AAB' ⇒ total!/repeats!=3!/2!=3")

    comb_problem_combo.bind("<<ComboboxSelected>>", update_comb_inputs)
    update_comb_inputs()

show_permutations()

# Start by showing permutations



if __name__ == "__main__":
    root.mainloop()
