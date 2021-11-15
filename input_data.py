import pandas as pd
import xlsxwriter 
from openpyxl import load_workbook
from csv import writer
import uuid

class elections:
    def __init__(self, state,pincode,name,gender,age,is_alive,is_in_india,eligibility,Voter_card_issued,Voter_id):
        self.state=state
        self.pincode=pincode
        self.name=name
        self.gender = gender
        self.age=age
        self.is_alive=is_alive
        self.is_in_india=is_in_india
        self.eligibility=eligibility
        self.Unique_id=str(uuid.uuid4())
        self.Voter_card_issued=Voter_card_issued
        self.Voter_id=Voter_id

    def print_details(self):
        print(self.Unique_id)
        print(self.state)
        print(self.pincode)
        print(self.name)
        print(self.gender)
        print(self.age)
        print(self.is_alive)
        print(self.is_in_india)
        print(self.eligibility)
        print(self.Voter_card_issued)
        print(self.Voter_id)

    @classmethod
    def get_user_input(cls):
        state = input('Enter the state: ')
        pincode = int(input('Enter the pincode: '))
        name=input('Enter the name:')
        gender = input('Enter your Gender(M/F/Other): ')
        age=int(input('Enter the age: '))
        is_alive=input('is person alive yes/no: ')
        is_in_india=input('is person in india yes/no: ')
        if age>=18 and (is_alive=='yes' or is_alive=='Yes' or is_alive=='YES'):
            eligibility="Eligible"
        else:
            eligibility="Not eligible"
        if age>=18:
            voter_card_Present=input('Is Voter Card Present  yes/no:')
        else:
            voter_card_Present="No"
        if(voter_card_Present=="yes" or voter_card_Present=="Yes" or voter_card_Present=="YES"):
            Voter_id=input("Enter Voter Id:")
            Voter_card_issued="Issued"
        else:
            Voter_id="NA"
            Voter_card_issued="Not Issued"
        return cls(state,pincode,name,gender,age,is_alive,is_in_india,eligibility,Voter_card_issued,Voter_id)

  
s1=elections.get_user_input()
s1.print_details()


df = pd.DataFrame({'Person Id': [s1.Unique_id],'Name': [s1.name],
                    'Age': [s1.age], 'Gender' : [s1.gender], 'State' : [s1.state], 'Pincode' : [s1.pincode], 'Is alive?' : [s1.is_alive], 'Is Present in India?' : [s1.is_in_india], 'Eligibility' : [s1.eligibility],'Voter Card Issued' : [s1.Voter_card_issued],'Voter Id': [s1.Voter_id]})

with open('voter_project.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(df.iloc[0])
    f_object.close()