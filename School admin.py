import csv
def write_info_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","E-mail Id"])
        writer.writerow(info_list)
        
if __name__=='__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter the student_info for student #{} in the following format (Name, Age, Mobile.no, E-mail id):".format(student_num))
        print("Entered information:"+student_info)
        student_info_list = student_info.split(" ")
        print("Entered split up information is:"+str(student_info_list))
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact Number: {}\nE-mail Id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is the entered information is correct? (yes/no):")
        if choice_check == "yes":
            write_info_csv(student_info_list)

            check_condition = input("Enter (yes/no) if u want to enter another student_info:")
            if check_condition == "yes":
                condition = True
                student_num = student_num + 1

            elif check_condition == "no":
                condition = False
        elif choice_check == "no":
            print("\n please re-enter the values!")
