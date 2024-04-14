#imports packages needed for code to run
import csv
import matplotlib.pyplot as plt
import statistics
import numpy as np

#23465321-patientIDtobeusedtoopenfile

#list of comorbilities that effect sepsis mortality rates
comorbilitieslist=["1. Mental & Behavioural Disorders due to Alcohol","2. Chronic Obstructive Pulmonary Disease", "3. Cancer", "4. Chronic Kidney Disease", "5. Chronic Liver Disease", "6. Diabetes"] 

mortalityrate=17.9 #standardised mortality rate for people diagnosed with sepsis in Ireland
patientidno=str(input("Please Enter Patient's ID Number")) #takes in patients ID number so their file can be called into the code
patientid=patientidno+".csv" #allows patient ID to be called as a file
file1=open(patientid,"r") #calls personalised file with patient's data
information=list(csv.reader(file1)) #creates list from csv file data (accesing data)
file1.close() #closes file
label=information[0]
labels1=label[1:len(label)] #extracts string data from csv file to be used as labels for graph
info=information[1] #takes data needed from csv file
info=[int(item) for item in info] #converts string data from csv file into integers using a for loop (pre-processing)
age=info[0] #saves patients age 

#checks that age data collected from microbit has been inputted correctly and falls within the accepted range
if age>8 or age<1:#if age data is invalid this piece of code gives the user the opportunity to rectify this to ensure data is as accurate as possible (pre-processing)
    print("1: Under 1")
    print("2: Between 1 and 2 years")
    print("3: Between 3 and 4 years")
    print("4: 5 years")
    print("5: Between 6 and 7 years")
    print("6: Between 8 and 11 years")
    print("7: Over 12")
    print("8: Over 15")
    age=int(input("Age inputted into Microbit appears to be incorrect. Please input correct data based on above table."))

if age==1:
    age=12.2 #converts the patients age into a figure that will later affect their recovery rate
elif age<=7:
    age=12.1#converts the patients age into a figure that will later affect their recovery rate
else:
    age=0

data=info[1:len(info)] #list indexing to extract data regarding patients symptoms

for item in data: #replaces any outliers in this data with a standardised figure (mean of two possible values)
    if item<0 or item>2:
        item=1

#uses matplotlib import to creat a bar graph that displays the patients symtoms in terms of the level of risk they indicate (visualisation of data)
#0=no risk, 1=some risk, 2=high risk
plt.bar(labels1, data) 
plt.title("Patient Risk Factors for Sepsis")
plt.xlabel("Risk Factors")
plt.ylabel("Risk Level")
plt.show()

patientrisk=0 #sets patient risk
analysis=False #uses boolean data to store whether the user should be offered an analysis of patients recovery rates as not necessary if the patient is not at risk
for i in data: #calls each item from list
    patientrisk=patientrisk+i #adds the level of risk each symtom indicates to the patients overall risk

#displays string to user indicating if the patient is at risk using an if statement
if patientrisk==0:
    print("Patient is not at risk for sepsis")
    quit()
elif patientrisk==1:
    print("Patient is at low to medium risk for sepsis")
    analysis=True
elif patientrisk>1:
    print("Patient is at high risk for sepis")
    analysis=True

if analysis==True: 
    response=input("Would you like a full analysis of predicted outcomes for patient (Y/N)") #offers users the option to input more data about patient in order to gain more accurate figures
    if response=="Y": #if user indicates they would like to avail of this service the algorithm calculates recovry rates adjusted for an increasing number of factors
        mortalityrate=mortalityrate-age #creates age adjusted mortality rate
        print("Does patient suffer from any of the following co-morbidities") #uses print and if statements to allow for user to input any patient comorbilities
        for i in comorbilitieslist:#prints all comorbilities that may affect mortality rates
            print(i)
        comorbidities=int(input("If patient suffers from any of these conditions please input it's corresponding number here. Else input 0.")) #allows user to input response
        while comorbidities!=0: #allows for user to import multiple comorbilities if the patient suffers from more than one
            if comorbidities==1:
                mortalityrate=mortalityrate+10.4 #adjusts mortality rate of patient based off data relating to affects of selected comorbilities
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
            elif comorbidities==2:
                mortalityrate=mortalityrate+12.5
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
            elif comorbidities==3:
                mortalityrate=mortalityrate+3.3
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
            elif comorbidities==4:
                mortalityrate=mortalityrate+8.6
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
            elif comorbidities==5:
                mortalityrate=mortalityrate+22.2
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
            elif comorbidities==6:
                mortalityrate=mortalityrate+2.3
                comorbidities=int(input("If patient suffers from any other of these conditions please input it's corresponding number here. Else input 0."))
        criticalcare=bool(input("Has patient been admitted to critical care (True/False)")) #takes in boolean data from user in relation to if the patient has stayed in the ICU
        if criticalcare==True:
            mortalityrate=mortalityrate+12.9 #adjusts mortality rate accordingly
        elif criticalcare==False:
            mortalityrate=mortalityrate-1.6
recovery=100-mortalityrate #calculates recpvery rate through subtraction of chance of mortality in percentage form (i.e. probability of non recovery)
print("The predicted chance of recovery for patient",patientidno,"is",recovery) #displays the predicted chance of recovery for patient before intervention or other diagnosis are considered

#visualises this data by means of a pie chart
names=["Chance of Fatality", "Chance of Recovery"]
figures=[mortalityrate, recovery]
plt.pie(figures, labels=names)
plt.title("Predicted Patient Outcomes")
plt.show()

#what if question 1
#considers the possibility that treatment (antibiotics and intravenous fluids) is administered within the recommended time frame
print("If treatment is administered within 1 hour of presentation of symptoms:")
onehour=mortalityrate-4.3 #adjusts mortality rate based off researched data
recovery1=100-onehour #calculates recovery
print("The patients chance of recovery is", recovery1) #displays this to user
#presents this data by means of a bar chart
figures=[onehour, recovery1]
plt.pie(figures, labels=names)
plt.title("Predicted Patient Outcomes if Treatment Administered Within 1 Hour")
plt.show()

print("If treatment is administered within 2 hours of presentation of symptoms:")
twohour=mortalityrate-12
recovery2=100-twohour
print("The patients chance of recovery is", recovery2)
figures=[twohour, recovery2]
plt.pie(figures, labels=names)
plt.title("Predicted Patient Outcomes if Treatment Administered Within 2 Hours")
plt.show()

print("If treatment is administered within 3 hours of presentation of symptoms:")
threehour=mortalityrate-7.4
recovery3=100-threehour
print("The patients chance of recovery is", recovery3)
figures=[threehour, recovery3]
plt.pie(figures, labels=names)
plt.title("Predicted Patient Outcomes if Treatment Administered Within 3 Hours")
plt.show()

#what if question 2
#analyses recovery rates if the infection is not sepsis but instead a different condition, or if it has developed into septic shock
def other_recovery_rates(sepsismortalityrate): #function to calculate recovery rates for such other illnesses to be unit tested
    infection1=sepsismortalityrate*0.2
    infection=100-infection1
    septicshock1=sepsismortalityrate*2.28
    septicshock=100-septicshock1
    otherdiagnosis1=sepsismortalityrate*0.056
    otherdiagnosis=100-otherdiagnosis1
    recovery=100-sepsismortalityrate
    recoveryrates=[otherdiagnosis, infection, recovery, septicshock] #saves calculated figures as a list to be graphed
    return recoveryrates #returns these figures to the main program
   
print("If the infection turns out to not be sepsis or have developed into severe sepsis or septic shock here is a graph of modelled recovery rates.")
#creates bar chart to represent this data to users
labels=["Other diagnosis","Infection", "Sepsis", "Septic Shock"]
recoveryrates=other_recovery_rates(mortalityrate)
plt.bar(labels, recoveryrates)
plt.title("Recovery Rates based off Diagnosed Condition")
plt.xlabel("Diagnosis")
plt.ylabel("Chance of Recovery (%)")
plt.show()


#provides user with an overview of hospital statistics in relation to sepsis symtoms
#allows user to visualise the amount of other patients who are likely to also have sepsis and to plan resources for patient in accordance with this (antibiotics, ICU beds)
hospitalreport=input("Would you like to see the hospital statistics (Y/N)")
if hospitalreport=="Y":
    file=open("Hospital.csv","r") #opens csv file with hospital data
    records=list(csv.reader(file)) #extracts data from this csv file
    file.close() #closes csv 
    risk_levels=[]
    temperature=[]
    heart_rate=[]
    respiratory_rate=[]
    change_in_behaviour=[]
    sepsis=[]
    risk_factors=["Temperature","Heart Rate","Respiratory Rate","Changes in Behaviours","Sepsis Risk Level"]
    for record in records [1:]: #creates lists from data extracted from csv file using list indexing
        risk_levels.append(record[0])
    for record in records [1:]:
        temperature.append(record[1])
    for record in records [1:]:
        heart_rate.append(record[2])
    for record in records [1:]:
        respiratory_rate.append(record[3])
    for record in records [1:]:
        change_in_behaviour.append(record[4])
    for record in records [1:]:
        sepsis.append(record[5])
    
    high_risk=[]
    low_risk=[]
    no_risk=[]
    def graph_lists(list1): #function to create lists consisting of the amount of patients exhibiting different levels of risk according to their symptoms
       high_risk.append(int(list1[0]))
       low_risk.append(int(list1[1]))
       no_risk.append(int(list1[2]))   
    graph_lists(temperature)#calls function for each symptom
    graph_lists(heart_rate)
    graph_lists(respiratory_rate)
    graph_lists(change_in_behaviour)
    graph_lists(sepsis)

    risk_levels2 = { #sets risk levels as keys and corresponding number of patients exhibiting that level of risk as values
        "high risk": (high_risk),
        "low risk": (low_risk),
        "no risk": (no_risk),
    }    
    x= np.arange(len(risk_factors)) #generates array of indices representing x-axis positions of bars in graph
    width=0.25
    multiplier=0

    fig, ax=plt.subplots(layout="constrained") #creates axis and figures for bar charts
    for attribute, measurement in risk_levels2.items(): #iterates through each risk level and corresponding measurements
        offset=width*multiplier #calculates offset of bars for different risk levels
        rects=ax.bar(x+offset, measurement, width, label=attribute) #creates bars
        ax.bar_label(rects, padding=3) #adds labels and padding of 3
        multiplier += 1 #increases mutliplier
    #creates grouped bar chart with labels
    ax.set_ylabel("No. of Patients")
    ax.set_title("Hospital Patients Risk for Sepsis")
    ax.set_xticks(x+width, risk_factors)
    ax.legend(loc="upper left", ncols=3)
    ax.set_ylim(0, 1000)

    plt.show()
   
   
   



       
