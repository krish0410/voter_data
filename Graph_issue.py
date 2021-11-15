#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:25:43 2021

@author: krish
"""
import csv
import pandas as pd
import xlsxwriter 
from openpyxl import load_workbook
from csv import writer
import matplotlib.pyplot as plt
df=pd.read_csv('/home/krish/Downloads/voter_project.csv')

print("********************************************************************************")
print("********************************************************************************")
print("Voter Card Analysis by Arushi , Krish , Aditi , Ayushi , Kaushal ")
i=1
while i>0:
    task = input('Analysis of Country or State or -1 to exit ? ')
    if(task=="Country"):
        print("Please Select option from below :- ")
        print("1. Population of State above 18")
        print("2. Gender Ratio of Eligible ")
        print("3. Eligible having voter id & not having voter id for Male")
        print("4. Eligible having voter id & not having voter id for Female")
        print("5. Eligible having voter id & not having voter Overall")
        print("6. Not ALive & having voter id")
        print("7. Gender Analysis of different state")
        graph=int(input('Enter the your choice here : '))
        if(graph==1):
            x = []
            y = []
            with open('demo1.csv', 'r') as csvfile:
               plots = csv.reader(csvfile, delimiter = ',')
               for row in plots:
                   x.append(row[0])
                   y.append(int(row[1]))
            plt.bar(x, y, color = 'g', width = 0.72, label = "Population")
            plt.tick_params(axis='x', which='major', labelsize=6.5)
            plt.xlabel('State')
            plt.ylabel('Population above 18')
            plt.title('Anylisis')
            plt.legend()
            plt.show()
        elif(graph==2):
            dfeligible = df[df['Applicable for Vote']== 'Eligible']
            dfnew_1=dfeligible['Applicable for Vote'].groupby(df['Gender']).count()
            y1 = dfnew_1.to_dict()
            colors = ['green','red']
            explode = (0.03,0.03)
            total=0
            if y1.get('M') is None:
                total=0
            else:
                total+=y1.get('M')
            if y1.get('F') is None:
                total=total
            else:
                total+=y1.get('F')
            plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=90,explode = explode)   
            plt.tight_layout()
            plt.show()
        elif(graph==3):
            dfeligible = df[(df['Applicable for Vote']== 'Eligible') & (df['Gender']=='M')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(df['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['green','cyan']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle) 
            plt.tight_layout()
            plt.show()
        elif(graph==4):
            dfeligible = df[(df['Applicable for Vote']== 'Eligible') & (df['Gender']=='F')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(df['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['magenta','red']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=40,explode = explode)
            plt.tight_layout()
            plt.show()
        elif(graph==5):
            dfeligible = df[(df['Applicable for Vote']== 'Eligible')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(df['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['green','magenta']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode=explode)
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle) 
            plt.tight_layout()
            plt.show()
        elif(graph==6):
            dfeligible = df[(df['Is alive']== 'Not Alive')]
            dfnew_1=dfeligible['Is alive'].groupby(df['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['cyan','red']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=30,explode = explode)
            plt.tight_layout()
            plt.show()
        elif(graph==7):
            x = []
            y = []
            x1=[]
            y1=[] 
            with open('demo1.csv','r') as csvfile:
                 lines = csv.reader(csvfile, delimiter=',')
                 for row in lines:
                     x.append(row[0])
                     y.append(int(row[2]))
                     x1.append(row[0])
                     y1.append(int(row[3]))
            plt.plot(x, y, color = 'g', linestyle = 'dashed',marker = 'o',label = "Gender analysis---F")
            plt.plot(x1, y1, color = 'b', linestyle = 'dashed',marker = 'o',label = "Gender analysis---M")
            plt.xticks(rotation = 25)
            plt.xlabel('State')
            plt.ylabel('Gender anylisis')
            plt.grid()
            plt.legend()
            plt.show()
        else:
            print("Sorry , Please Select the above options only")
    elif (task=="State"):
        state = input('Analysis of which State ? ')
        print("Please Select option from below :- ")
        print("1. Data's of citizens of " , state)
        print("2. Gender Ratio of Eligible ",state)
        print("3. Eligible having voter id & not having voter id for Male ",state)
        print("4. Eligible having voter id & not having voter id for Female ",state)
        print("5. Eligible having voter id & not having voter Overall ",state)
        print("6. Not ALive & having voter id ",state)
        graph=int(input('Enter the your choice here : '))
        if(graph==1):
            print (df.to_string())
            print("statistical analysis of data")
            print(df.describe())
            print("\n")
            print("List of only eligible ones:--")
            new_df = df.dropna()
            print(new_df.to_string())
            print("data of particular state")
            print((df[(df == state).any(axis=1)]))
        elif(graph==2):
            dfnew=df[df['State']==state]
            dfeligible = dfnew[dfnew['Applicable for Vote']== 'Eligible']
            dfnew_1=dfeligible['Applicable for Vote'].groupby(dfnew['Gender']).count()
            colors = ['green','red']
            explode = (0.03,0.03)
            y1 = dfnew_1.to_dict()
            total=0
            if y1.get('M') is None:
                total=0
            else:
                total+=y1.get('M')
            if y1.get('F') is None:
                total=total
            else:
                total+=y1.get('F')
            if(len(y1)>1):
                plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            else:
                plt.pie(list(y1.values()),labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45)
            plt.tight_layout()
            plt.show()   
        elif(graph==3):
            dfnew=df[df['State']==state]
            dfeligible = dfnew[(dfnew['Applicable for Vote']== 'Eligible') & (dfnew['Gender']=='M')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(dfnew['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['green','cyan']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            if(len(y1)>1):
                plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            else:
                plt.pie(list(y1.values()),labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45)
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle) 
            plt.tight_layout()
            plt.show()
        elif(graph==4):
            dfnew=df[df['State']==state]
            dfeligible = dfnew[(dfnew['Applicable for Vote']== 'Eligible') & (dfnew['Gender']=='F')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(dfnew['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['magenta','red']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            if(len(y1)>1):
                plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            else:
                plt.pie(list(y1.values()),labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45)
            plt.tight_layout()
            plt.show()
        elif(graph==5):
            dfnew=df[df['State']==state]
            dfeligible = dfnew[(dfnew['Applicable for Vote']== 'Eligible')]
            dfnew_1=dfeligible['Applicable for Vote'].groupby(dfnew['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['green','magenta']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            if(len(y1)>1):
                plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            else:
                plt.pie(list(y1.values()),labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45)
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle) 
            plt.tight_layout()
            plt.show()
        elif(graph==6):
            dfnew=df[df['State']==state]
            dfeligible = dfnew[(dfnew['Is alive']== 'Not Alive')]
            dfnew_1=dfeligible['Is alive'].groupby(dfnew['Voter Card Issued']).count()
            y1 = dfnew_1.to_dict()
            colors = ['cyan','red']
            explode = (0.03,0.03)
            total=0
            if y1.get('Issued') is None:
                total=0
            else:
                total+=y1.get('Issued')
            if y1.get('Not Issued') is None:
                total=total
            else:
                total+=y1.get('Not Issued')
            if(len(y1)>1):
                plt.pie(list(y1.values()),colors = colors,labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45,explode = explode)
            else:
                plt.pie(list(y1.values()),labels=list(y1.keys()),autopct=lambda p: '{:.0f}'.format(p * total / 100),shadow=True, startangle=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Sorry , Please Select the above options only")
    elif task=='-1':
        break