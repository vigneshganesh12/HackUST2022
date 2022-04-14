import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import mysql.connector
import pandas
import csv

global ROW_OF_DATA
ROW_OF_DATA=list()

#import yfinance







def PlotA():
    cars = ['BAJFINANCE', 'BRITANNIA', 'DIVISLAB', 'POWERGRID', 'INDUSINDBK', 'HDFCLIFE']

    data = [28.27, 17, 35, 29, 12, 41]


    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)

    colors = ( "orange", "cyan", "brown",
    "grey", "indigo", "beige")

    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)

    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                            autopct = lambda pct: func(pct, data),
                            explode = explode,
                            labels = cars,
                            shadow = True,
                            colors = colors,
                            startangle = 90,
                            wedgeprops = wp,
                            textprops = dict(color ="magenta"))

    ax.legend(wedges, cars,
    title ="Companies",
    loc ="upper left",
    bbox_to_anchor =(1, 0, 0.5, 1))

    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("ESG Performance of Different Companies")

    plt.show()

def PlotB():
    cars = ['Environment Score', 'Social Score', 'Governance Score']

    data = [2.13, 13.77, 12.78]


    explode = (0.1, 0.0, 0.2)

    colors = ( "orange", "blue", "brown")

    wp = { 'linewidth' : 1, 'edgecolor' : "black" }

    def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)

    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                            autopct = lambda pct: func(pct, data),
                            explode = explode,
                            labels = cars,
                            shadow = True,
                            colors = colors,
                            startangle = 90,
                            wedgeprops = wp,
                            textprops = dict(color ="black"))

    ax.legend(wedges, cars,
    title ="Component of ESG",
    loc ="upper left",
    bbox_to_anchor =(1, 0, 0.5, 1))

    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Composite ESG score for Axis Bank")
    plt.show()

def PlotC():
    barWidth = 0.20
    fig = plt.subplots(figsize =(11, 7))

    Environment_Score = [3.54, 13.46, 2.13, 3.38, 2.6]
    Social_Score = [3.68, 9.03, 13.77, 5.58, 8.92]
    Governance_Score = [6.5, 8.78, 12.78, 7.35, 14.69]
    Total_ESG_Score = [13.71, 31.27, 28.68, 16.31, 26.21]

    br1 = np.arange(len(Environment_Score))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    plt.bar(br1, Environment_Score, color ='orange', width = barWidth,
            edgecolor ='grey', label ='Environment_Score')
    plt.bar(br2, Social_Score, color ='maroon', width = barWidth,
            edgecolor ='grey', label ='Social_Score')
    plt.bar(br3, Governance_Score, color ='b', width = barWidth,
            edgecolor ='grey', label ='Governance_Score')
    plt.bar(br4, Total_ESG_Score, color ='purple', width = barWidth,
            edgecolor ='grey', label ='Total_ESG_Score')



    plt.xlabel('Company', fontweight ='bold', fontsize = 10)
    plt.ylabel('Weighted Score', fontweight ='bold', fontsize = 10)
    plt.xticks([r + barWidth for r in range(len(Environment_Score))],
            ['ADANIPORTS', 'ASIANPAINTS', 'AXISBANK', 'BAJAJAUTO', 'BAJAJFINS'])

    plt.legend()
    plt.show()


#Note to users and reviewers:
# The UI developed and generated through this source code is the most basic version of the UI that facilitates text inputs from users.
# There is scope of development for our UI with the aid of paid and distrutable licensed API's and sensors(ex. Smappee API and sensors) provided by startups.
# The sample data used to visualise ESG reports has been extracted from the yfinance library of Python.

# Future versions/Scope of our UI would include:

# 1. Extracting data from sensors and using a DBMS system to store the same.
# 2. Data visualisation through Smappee's API.
# 3. Improving the advising system to make it more automated and accurate through a predictive and self-learning AI model.

def Text():
    
    
    COMPANY=e1.get()
    EQ1=e2.get()
    EQ2=e3.get()
    EQ3=e4.get()
    EQ4=e5.get()
    ROW_OF_DATA = ROW_OF_DATA +[COMPANY,EQ1,EQ2,EQ3,EQ4,]
    
    

def Text2():
    
    WQ1=e2.get()
    WQ2=e3.get()
    WQ3=e5.get()
    ROW_OF_DATA = ROW_OF_DATA + [WQ1,WQ2,WQ3,]

    

def Text3():
    GIQ1=e1.get()
    GIQ2=e2.get()
    GIQ3=e3.get()
    GIQ4=e4.get()
    GIQ5=e5.get()
    ROW_OF_DATA = ROW_OF_DATA + [GIQ1,GIQ2,GIQ3,GIQ4,GIQ5,]
    header = ['Company Name','EQ1','EQ2','EQ3','EQ4','WQ1','WQ2','WQ3','GIQ1','GIQ2','GIQ3','GIQ4','GIQ5']

    #Note 
    # A new csv file is created and the data is stored in the same csv file when the following section of code is run along with the rest of the code
    # with open('./filepath.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)

    #write the header
    #     writer.writerow(header)

    #write the data
    #     writer.writerow(ROW_OF_DATA)

       




root=tk.Tk()



root.geometry('800x2400')
root.title('ESG UNIFIED ESG Questionnaire')
root.configure(bg='light blue')
t1=tk.Label(root,text="ESG UNIFIED",fg='black',bg='light blue',font=['Arial','24','bold italic'])


t2=tk.Label(root,text="This is a questionnare that would enable us to grasp a better understanding of your short and long term ESG goals",fg='black',bg='light blue',font=['Times New Roman','20','bold italic'])


t3=tk.Label(root,text="Company Name:",fg='black',bg='light blue',font=['Times New Roman','20','bold italic'])


e1=tk.Entry(root,width=20,font=18)


t4=tk.Label(root,text="Section I : Electricity consumption",fg='black',bg='light blue',font=['Times New Roman','20','bold italic'])


t5=tk.Label(root,text="Is there a system set up in order to track monthly KwH consumption of your properties(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e2=tk.Entry(root,width=10,font=18)


t6=tk.Label(root,text="Is it possible to identify the appliances that consume the most energy on a monthly basis(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e3=tk.Entry(root,width=10,font=18)


t7=tk.Label(root,text="Can wasted electricity(Devices on standby or running over-time) be measured(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])

e4=tk.Entry(root,width=10,font=18)

t8=tk.Label(root,text="What are the noticable trends in electricity consumption since the beginning of the COVID-19 Pandemic?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e5=tk.Entry(root,width=30,font=18)


B=tk.Button(root,text='Save',width=10,fg='white',bg='black',font=['Bahnschrift','12','bold'],command=Text)


B1=tk.Button(root,text='Next',width=10,fg='white',bg='black',font=['Bahnschrift','12','bold'],command=root.destroy)

t1.pack(padx=5,pady=10,side=tk.TOP)
t2.pack(padx=5,pady=10)
t3.pack(padx=5,pady=10)

e1.pack(padx=5,pady=10)

t4.pack(padx=5,pady=10)
t5.pack(padx=5,pady=3)

e2.pack(padx=5,pady=10)

t6.pack(padx=5,pady=3)

e3.pack(padx=5,pady=10)

t7.pack(padx=5,pady=3)

e4.pack(padx=5,pady=10)

t8.pack(padx=5,pady=3)

e5.pack(padx=5,pady=10)

B.pack(anchor='s')
B1.pack(anchor='se')

root.mainloop()




#Water consumption


root2=tk.Tk()
root2.geometry('800x2400')
root2.title('ESG UNIFIED ESG Questionnaire')
root2.configure(bg='light blue')
t1=tk.Label(root2,text="ESG UNIFIED",fg='black',bg='light blue',font=['Times New Roman','24','bold italic'])


t4=tk.Label(root2,text="Section II : Water consumption",fg='black',bg='light blue',font=['Times New Roman','18','bold italic'])


t5=tk.Label(root2,text="Is there a system set up in order to track monthly water consumption of your properties(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e2=tk.Entry(root2,width=10,font=18)


t6=tk.Label(root2,text="Is it possible to identify how much water is being wasted and used ineffectively(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e3=tk.Entry(root2,width=10,font=18)



t8=tk.Label(root2,text="What are the noticable trends in water consumption since the beginning of the COVID-19 Pandemic?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e5=tk.Entry(root2,width=30,font=18)


B=tk.Button(root2,text='Save',width=10,command=Text2,fg='white',bg='black',font=['Bahnschrift','12','bold'])


B1=tk.Button(root2,text='Next',width=10,command=root2.destroy,fg='white',bg='black',font=['Bahnschrift','12','bold'])

t1.pack(padx=5,pady=10,side=tk.TOP)


t4.pack(padx=5,pady=10)
t5.pack(padx=5,pady=3)

e2.pack(padx=5,pady=10)

t6.pack(padx=5,pady=3)

e3.pack(padx=5,pady=10)


t8.pack(padx=5,pady=3)

e5.pack(padx=5,pady=10)

B.pack(anchor='s')
B1.pack(anchor='se')

root2.mainloop()


#Section : Green Impact

root3=tk.Tk()



root3.geometry('800x2400')
root3.title('ESG UNIFIED ESG Questionnaire')
root3.configure(bg='light blue')
t1=tk.Label(root3,text="ESG UNIFIED",fg='black',bg='light blue',font=['Times New Roman','24','bold italic'])


t2=tk.Label(root3,text="Section III : Green Impact",fg='black',bg='light blue',font=['Times New Roman','20','bold italic'])


t3=tk.Label(root3,text="Are there any planes to replace inefficient appliances(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e1=tk.Entry(root3,width=10,font=18)


t4=tk.Label(root3,text="Do you currently use any renewable source of energy(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])

e2=tk.Entry(root3,width=10,font=18)




t5=tk.Label(root3,text="Have there been any steps that have been taken towards Greener Energy(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])

e3=tk.Entry(root3,width=10,font=18)

t6=tk.Label(root3,text="Are you willing to pay a premium for renewable energy(YES/NO)?",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])


e4=tk.Entry(root3,width=20,font=18)


t7=tk.Label(root3,text="If yes, How much more are you willing to pay compared to traditional energy sources?(Type NA if previous answer is NO)",fg='black',bg='light blue',font=['Bahnschrift','16','bold'])

e5=tk.Entry(root3,width=30,font=18)


B=tk.Button(root3,text='Save',width=10,command=Text3,fg='white',bg='black',font=['Bahnschrift','12','bold'])


B1=tk.Button(root3,text='Exit',width=10,command=root3.destroy,fg='white',bg='black',font=['Bahnschrift','12','bold'])

t1.pack(padx=5,pady=10,side=tk.TOP)
t2.pack(padx=5,pady=10)
t3.pack(padx=5,pady=10)

e1.pack(padx=5,pady=10)

t4.pack(padx=5,pady=10)

e2.pack(padx=5,pady=10)

t5.pack(padx=5,pady=3)

e3.pack(padx=5,pady=10)

t6.pack(padx=5,pady=3)

e4.pack(padx=5,pady=10)

t7.pack(padx=5,pady=3)

e5.pack(padx=5,pady=10)


B.pack(anchor='s')
B1.pack(anchor='se')

root3.mainloop()


root4=tk.Tk()



root4.geometry('800x2400')
root4.title('ESG UNIFIED - Sample ESG Report')
root4.configure(bg='light blue')
T1=tk.Label(root4,text="ESG UNIFIED",fg='black',bg='light blue',font=['Times New Roman','24','bold italic'])


T2=tk.Label(root4,text="ESG UNIFIED Sample ESG Report Generator",fg='black',bg='light blue',font=['Times New Roman','20','bold italic'])

L1=tk.Button(root4,text='ESG Performance of different companies',width=40,fg='white',bg='black',font=['Bahnschrift','16','bold'],command=PlotA)
L2=tk.Button(root4,text='Composite ESG score for Axis Bank',width=40,fg='white',bg='black',font=['Bahnschrift','16','bold'],command=PlotB)
L3=tk.Button(root4,text='Weighted ESG scores of different companies',width=40,fg='white',bg='black',font=['Bahnschrift','16','bold'],command=PlotC)


L4=tk.Button(root4,text='Exit',width=10,fg='white',bg='black',font=['Bahnschrift','16','bold'],command=root4.destroy)

T1.pack(padx=5,pady=10,side=tk.TOP)
T2.pack(padx=5,pady=10)

L1.pack(padx=5,pady=10,side=tk.TOP)
L2.pack(padx=5,pady=10,side=tk.TOP)
L3.pack(padx=5,pady=10,side=tk.TOP)
L4.pack(padx=5,pady=10,side=tk.TOP)

root4.mainloop()