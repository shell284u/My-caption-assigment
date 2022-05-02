#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv.file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact number","E-mail ID"])
            
        writer.writerrow(info_list)  
        
if __name__ == '__main__':       
     condition = True
     student_num = 1
while(condition):
    student_info = input("enter some student information #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num)
   
  student_info_list = student_info.split(' ') 
                         
    print("\nThe entered information is -\nNAME: {}\nAGE: {}\nCONTACT_NUMBER: {}\nE-mail ID {}"
            .format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))
    choice_check = input("Is the entered information correct? (yes/no):")
    condition_check = input("enter (yes/no) if you want to enter information for another student: ")
    if condition_check == "yes":
        condition = True
        student_num = student_num + 1                 
    elif condition_check == "no":
        condition = False
   elif choice_check == "no":
       print("\nPlease re-enter the values!")                  


# In[ ]:




