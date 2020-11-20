# import modules
import subprocess
from sklearn.preprocessing import LabelEncoder
import tkinter


from tkinter import *
import os
import csv
from tkinter import messagebox, ttk
#import pandas as pd
#import seaborn as sns
import numpy as np
#import matplotlib.pyplot as plt
import os


import mentalhealthsurvey
from hashTable import HashTable

from alg import Alg

calculations = Alg()

survey_answers1 = []
survey_answers = []
part_answered_often = []
part_answered_some = []
part_answered_often_fem = []
part_answered_some_fem = []
part_answered_often_other = []
part_answered_some_other = []
part_answered_often_male = []
part_answered_some_male = []
ages_ans_often = []
ages_ans_some = []
ages_ans_often_fem = []
ages_ans_some_fem = []
ages_ans_often_other= []
ages_ans_some_other = []
ages_ans_often_male = []
ages_ans_some_male = []
survey_answers_ages = []
survey_answers_ages_fem = []
survey_answers_ages_male = []
survey_answers_ages_other = []

with open('TechMentalHealthSurvey.csv', 'r') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')  # reads the CSV package file
    list_of_answers = list(csv_file)
    # print(list_of_packages[0][0])
    mhsurvey = HashTable()  # 15 - creates a hashtable object by calling the HashTable class

    Row_IDs = []
    Age = []
    Gender = []
    Country = []
    State = []
    Self_employed = []
    Family_history = []
    Treatment = []
    Work_interference = []
    No_employees = []
    Remote_work = []
    Tech_company = []
    Benefits = []
    Care_options = []
    Wellness_program = []
    Seek_help = []
    Anonymity = []
    Leave = []
    Mental_health_consequence = []
    Phys_health_consequence = []
    Coworkers = []
    Supervisor = []
    Mental_health_interview = []
    Phys_health_interview = []
    Mental_vs_physical = []
    Obs_consequence = []
    Comments = []

    # reads the package csv and creates attributes for each package
    for row in list_of_answers:  # space time complexity is O(N)
        row_id = int(row[0])
        age = int(row[1])
        gender = row[2]
        country = row[3]
        state = row[4]
        self_employed = row[5]
        family_history = row[6]
        treatment = row[7]
        work_interference = row[8]
        no_employees = row[9]
        remote_work = row[10]
        tech_company = row[11]
        benefits = row[12]
        care_options = row[13]
        wellness_program = row[14]
        seek_help = row[15]
        anonymity = row[16]
        leave = row[17]
        mental_health_consequence = row[18]
        phys_health_consequence = row[19]
        coworkers = row[20]
        supervisor = row[21]
        mental_health_interview = row[22]
        phys_health_interview = row[23]
        mental_vs_physical = row[24]
        obs_consequence = row[25]
        comments = row[26]

        # appends each value to respective lists
        Row_IDs.append(row_id)
        Age.append(age)
        Gender.append(gender)
        Country.append(country)
        State.append(state)
        Self_employed.append(self_employed)
        Family_history.append(family_history)
        Treatment.append(treatment)
        Work_interference.append(work_interference)
        No_employees.append(no_employees)
        Remote_work.append(remote_work)
        Tech_company.append(tech_company)
        Benefits.append(benefits)
        Care_options.append(care_options)
        Wellness_program.append(wellness_program)
        Seek_help.append(seek_help)
        Anonymity.append(anonymity)
        Leave.append(leave)
        Mental_health_consequence.append(mental_health_consequence)
        Phys_health_consequence.append(phys_health_consequence)
        Coworkers.append(coworkers)
        Supervisor.append(supervisor)
        Mental_health_interview.append(mental_health_interview)
        Phys_health_interview.append(phys_health_interview)
        Mental_vs_physical.append(mental_vs_physical)
        Obs_consequence.append(obs_consequence)
        Comments.append(comments)

        m = mentalhealthsurvey.MentalHealthSurvey(row_id, age, gender, country, state, self_employed,
                                                  family_history, treatment, work_interference, no_employees,
                                                  remote_work,
                                                  tech_company, benefits, care_options, wellness_program, seek_help,
                                                  anonymity, leave, mental_health_consequence,
                                                  phys_health_consequence,
                                                  coworkers, supervisor, mental_health_interview,
                                                  phys_health_interview,
                                                  mental_vs_physical, obs_consequence, comments)

        mhsurvey.get(row_id)  # look up the package by the id
        mhsurvey.insert(row_id, m)  # inserts the packages into the hashtable

        if 0 < m.row_id <= 1259:
            survey_answers.append(m)

fem_often = calculations.calculate_median_age_fem_often(survey_answers, survey_answers_ages_fem,
                                                        part_answered_often_fem, ages_ans_often_fem)

male_often = calculations.calculate_median_age_male_often(survey_answers, survey_answers_ages_male,
                                                        part_answered_often_male, ages_ans_often_male)

other_often = calculations.calculate_median_age_other_often(survey_answers, survey_answers_ages_other,
                                                        part_answered_often_other, ages_ans_often_other)

all_often = calculations.calculate_median_age_often(survey_answers, survey_answers_ages,
                                                        part_answered_often, ages_ans_often)

male_sometimes = calculations.calculate_median_age_male_sometimes(survey_answers, survey_answers_ages,
                                                               part_answered_some_male, ages_ans_some_male)

fem_sometimes = calculations.calculate_median_age_fem_sometimes(survey_answers, survey_answers_ages,
                                                                part_answered_some_fem, ages_ans_some_fem)

other_sometimes = calculations.calculate_median_age_other_sometimes(survey_answers, survey_answers_ages,
                                                                part_answered_some_other, ages_ans_some_other)

all_sometimes = calculations.calculate_median_age_sometimes(survey_answers, survey_answers_ages, part_answered_some,
                                                            ages_ans_some)

eighteen_twentyfive = []
for item in survey_answers:
    if 18 <= item.age <= 25:
        eighteen_twentyfive.append(item)
a18to25 = (len(eighteen_twentyfive))

twentysix_35 = []
for item in survey_answers:
    if 26 <= item.age <= 35:
        twentysix_35.append(item)
a26to35 = (len(twentysix_35))

thirtysix_45 = []
for item in survey_answers:
    if 36 <= item.age <= 45:
        thirtysix_45.append(item)
a36to45 = (len(thirtysix_45))

fortysix_55 = []
for item in survey_answers:
    if 46 <= item.age <= 55:
        fortysix_55.append(item)
a46to55 = (len(fortysix_55))

fiftysix_65 = []
for item in survey_answers:
    if 56 <= item.age <= 65:
        fiftysix_65.append(item)
a56to65 = (len(fiftysix_65))

part_woman = []
for item in survey_answers:
    if item.gender == 'f' or item.gender == 'F' or item.gender == 'Female' or item.gender == 'female' or item.gender == 'Cis Female':
        part_woman.append(item)
number_woman = (len(part_woman))

part_man = []
for item in survey_answers:
    if item.gender == 'm' or item.gender == 'M' or item.gender == 'male' or item.gender == 'Male' or item.gender == 'Cis Male':
        part_man.append(item)
number_man = len(part_man)
# print(len(part_man))

part_other = []
for item in survey_answers:
    if item.gender != 'm' and item.gender != 'M' and item.gender != 'male' and item.gender != 'Male' and item.gender != 'f' and \
            item.gender != 'F' and item.gender != 'Female' and item.gender != 'female' and item.gender != 'Cis Female' \
            and item.gender != 'Cis male':
        part_other.append(item)
number_other = len(part_other)

work_often = []
for item in survey_answers:
    if item.work_interference == 'Often':
        work_often.append(item)
ans_often1 = (len(work_often))
# print(ans_often1)

work_sometimes = []
for item in survey_answers:
    if item.work_interference == 'Sometimes':
        work_sometimes.append(item)
ans_sometimes1 = (len(work_sometimes))
# print(ans_sometimes1)

work_rarely = []
for item in survey_answers:
    if item.work_interference == 'Rarely':
        work_rarely.append(item)
ans_rarely1 = (len(work_rarely))
# print(ans_rarely1)

work_never = []
for item in survey_answers:
    if item.work_interference == 'Never':
        work_never.append(item)
ans_never1 = (len(work_never))
# print(ans_never1)

work_NA = []
for item in survey_answers:
    if item.work_interference == 'NA':
        work_NA.append(item)
ans_NA1 = (len(work_NA))
# print(ans_NA1)

# print(ans_often1 + ans_NA1 + ans_never1 + ans_rarely1 + ans_sometimes1)
cons_yes = []
for item in survey_answers:
    if item.mental_health_consequences == 'Yes':
        cons_yes.append(item)
ans_cons_yes1 = (len(cons_yes))
# print(ans_cons_yes1)

cons_no = []
for item in survey_answers:
    if item.mental_health_consequences == 'No':
        cons_no.append(item)
ans_cons_no1 = (len(cons_no))
# print(ans_cons_no1)

cons_maybe = []
for item in survey_answers:
    if item.mental_health_consequences == 'Maybe':
        cons_maybe.append(item)
ans_cons_maybe1 = (len(cons_maybe))
print(ans_cons_maybe1)


# Designing window for login
#

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg='aliceblue')
    Label(login_screen, text="Please enter details below to login", bg='aliceblue', font=("Baghdad", 13)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username", bg='aliceblue', font=("Baghdad", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password", bg='aliceblue', font=("Baghdad", 13)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1 =="admin":
        if password1 == "admin":
            login_sucess()

        else:
            password_nr()

    else:
        user_nf()



def login_sucess():
    global top
    global gender_input
    global freq_input
    gender_input = StringVar()
    freq_input = StringVar()
    top = Toplevel(login_screen)
    top.title("Home")
    top.geometry("770x600")
    top.configure(bg='aliceblue')
    Label(top, text="Home", bg='aliceblue', font=("Baghdad", 17, "bold")).pack()
    slabel1 = Label(top, text="Participants who seek treatment vs if they work remotely", height=0, width=0, font=("Baghdad", 13))
    slabel1.configure(bg='aliceblue')
    slabel1.place(x=20, y=90)

    slabel2 = Label(top, text="Participants who believe there will be consequences \n from disclosing physical vs mental illness to employers", height=0, width=0,
                    font=("Baghdad", 13))
    slabel2.configure(bg='aliceblue')
    slabel2.place(x=20, y=130)

    slabel3 = Label(top, text="Level that participant's mental health affect work", height=0, width=0,
                    font=("Baghdad", 13))
    slabel3.configure(bg='aliceblue')
    slabel3.place(x=20, y=220)

    slabel4 = Label(top, text="Correlations between different factors", height=0, width=0,
                    font=("Baghdad", 13))
    slabel4.configure(bg='aliceblue')
    slabel4.place(x=20, y=260)

    # slabel2 = Label(top, text="Gender: Type 'Often or Sometimes'", height=0, width=0)
    # slabel2.place(x=20, y=90)

    # entry1 = Entry(top, textvariable=gender_input)
    # entry1.place(x=250, y=40)
    # entry1.pack()
    #
    # # entry1 = Entry(top)
    # # entry1.pack()
    #
    #
    # entry2 = Entry(top, textvariable=freq_input)
    # # entry2.place(x=250, y=90)
    # entry2.pack()
    #
    # gen_freq_button = Button(top, text="Gen/Rep", width=10, height=1, command=gen_rep_verify)
    # gen_freq_button.pack(padx=5, pady=20)
    # gen_freq_button.place(x=400, y=40)
    # gen_freq_button.configure(bg="#ffdddd", background='red')

    remote_button = Button(top, text="Remote Work", width=11, height=1, command=remote)
    remote_button.pack(padx=5, pady=20)
    remote_button.place(x=400, y=90)
    remote_button.configure(bg="#ffdddd", background='red')

    mc_cons_button = Button(top, text="Consequence", width=10, height=1, command=mc_cons_verify)
    mc_cons_button.pack(padx=5, pady=20)
    mc_cons_button.place(x=400, y=130)
    mc_cons_button.configure(bg="#ffdddd", background='red')

    inter_button = Button(top, text="Work Interference", width=12, height=1, command=inter_break)
    inter_button.pack(padx=5, pady=20)
    inter_button.place(x=400, y=220)
    inter_button.configure(bg="#ffdddd", background='red')

    correl_button = Button(top, text="Correlations", width=10, height=1, command=correl_verify)
    correl_button.pack(padx=5, pady=20)
    correl_button.place(x=400, y=260)
    correl_button.configure(bg="#ffdddd", background='red')

    # gen_treat_button = Button(top, text="Gender/Treatment", width=12, height=1, command=gen_treat_verify)
    # gen_treat_button.pack(padx=5, pady=20)
    # gen_treat_button.place(x=400, y=250)
    # gen_treat_button.configure(bg="#ffdddd", background='red')

    db_change = Button(top, text="Data Breakdown", command=data_breakdown)
    db_change.pack(padx=5, pady=100)
    db_change.place(x=400, y=305)

    ab_change = Button(top, text="Age/Interference Breakdown", command=age_data_breakdown)
    ab_change.pack(padx=5, pady=100)
    ab_change.place(x=400, y=345)

    exit_button = Button(top, text="Exit", command=end_ls)
    exit_button.pack(padx=5, pady=100)
    exit_button.place(x=500, y=385)

def remote():
    survey = pd.read_csv('survey1.csv')
    survey.head()

    plt.figure(figsize=(12, 6))
    sns.countplot(y="remote_work", hue="treatment", data=survey, palette="cubehelix")
    plt.title("Treatment depends on if participant works remotely?", fontsize=18, fontweight="bold")
    plt.ylabel("")
    plt.show()



def inter_break():
    items_often = []
    items_rarely = []
    items_sometimes = []
    items_NA = []
    items_never = []
    for item in Work_interference:
        if item == 'Often':
            items_often.append(item)
    part_often = (len(items_often))
    # print(part_often)
    for item in Work_interference:
        if item == 'Rarely':
            items_rarely.append(item)
    part_rarely = (len(items_rarely))
    # print(part_rarely)
    for item in Work_interference:
        if item == 'Sometimes':
            items_sometimes.append(item)
    part_sometimes = (len(items_sometimes))
    # print(part_sometimes)
    for item in Work_interference:
        if item == 'NA':
            items_NA.append(item)
    part_NA = (len(items_NA))
    # print(part_NA)
    for item in Work_interference:
        if item == 'Never':
            items_never.append(item)
    part_never = (len(items_never))
    # print(part_never)


    my_labels = 'Often', 'Rarely', 'Sometimes', 'Never', 'NA'
    values= [part_often, part_rarely, part_sometimes, part_never, part_NA]
    plt.pie(values, labels=my_labels, autopct='%1.1f%%')
    plt.title('For participants with a mental health condition, how often does it interfere with their work?')
    plt.axis('equal')
    plt.show()

def data_breakdown():
    global top1
    global clicked
    # global gender_input
    # global freq_input
    # gender_input = StringVar()
    # freq_input = StringVar()
    top1 = Toplevel(top)
    top1.title("Data Breakdown")
    top1.geometry("500x500")
    top1.configure(bg='aliceblue')
    # Label(top1, text=" Screen").pack()
    slabel1 = Label(top1, text="Data Breakdown", height=0, width=0, font=("Baghdad", 13))
    slabel1.configure(bg='aliceblue')
    slabel1.place(x=40, y=65)


    options = [
        "Gender Breakdown",
        "Age Breakdown",
        "Work Interference Breakdown",
        "Consequences Breakdown",
    ]
    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(top1, clicked, *options)
    # drop.place(x=20, y=400)
    drop.pack(pady=65)

    myButton = Button(top1, text='Enter', command=selected)
    myButton.pack()
    myButton.place(x=350, y=65)

    myCombo = ttk.Combobox(top1, value=options)
    myCombo.current(0)
    myCombo.bind("ComboboxSelected", )


    myButton1 = Button(top1, text='Back', command=login_sucess)
    myButton1.pack()
    myButton1.place(x=350, y=150)


def selected():

        # myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Age Breakdown':
        myLabel = Label(top1, text="Age Breakdown \n 18-25: " + str(a18to25) + "\n26-35: " + str(a26to35) +
                                    "\n36-45: " + str(a36to45) + "\n46-55: " + str(a46to55) +
                                    "\n56-65: " + str(a56to65)).pack()

    if clicked.get() == 'Gender Breakdown':
        myLabel = Label(top1,
                        text="Gender Breakdown \n Female: " + str(number_woman) + "\n Male: " + str(number_man)
                            + "\n Other: " + str(number_other)).pack()

    if clicked.get() == 'Work Interference Breakdown':
        myLabel = Label(top1, text="Work Interference Breakdown \n Often: " + str(ans_often1) + "\n Rarely: " + str(
                ans_rarely1) + "\n Sometimes: " + str(ans_sometimes1) + "\n Never: " + str(ans_never1) +
                                "\n NA: " + str(ans_NA1)).pack()

    if clicked.get() == 'Consequences Breakdown':
        myLabel = Label(top1,
                    text="Participants who believe disclosing mental illness will result in consequences\n Yes: "
                        + str(ans_cons_yes1) + "\n No: " + str(ans_cons_no1) +
                            "\n Maybe: " + str(ans_cons_maybe1)).pack()


def age_data_breakdown():
    global root1
    global clicked1
    # global gender_input
    # global freq_input
    # gender_input = StringVar()
    # freq_input = StringVar()
    root1 = Toplevel(top)
    root1.title("Age/Gender/Work Interference Breakdown")
    root1.geometry("550x500")
    root1.configure(bg='aliceblue')
    # Label(top1, text=" Screen").pack()
    slabel1 = Label(root1, text="Median age of Gender and \n Work Interference Levels", height=0, width=0, font=("Baghdad", 13))
    slabel1.configure(bg='aliceblue')
    slabel1.place(x=35, y=65)

    options = [
        "Female and Often",
        "Female and Sometimes",
        "Male and Often",
        "Male and Sometimes",
        "Other and Often",
        "Other and Sometimes",
        "All and Often",
        "All and Sometimes",
    ]
    clicked1 = StringVar()
    clicked1.set(options[0])

    drop = OptionMenu(root1, clicked1, *options)
    drop.pack(pady=65)

    myButton = Button(root1, text='enter', command=selected2)
    myButton.pack()
    myButton.place(x=350, y=65)

    myCombo = ttk.Combobox(root1, value=options)
    myCombo.current(0)
    myCombo.bind("ComboboxSelected", )

    myButton2 = Button(root1, text='Back', command=login_sucess)
    myButton2.pack()
    myButton2.place(x=350, y=420)


def selected2():
    #myLabel = Label(root, text=clicked.get()).pack()
    if clicked1.get() == 'Female and Often':
        myLabel = Label(root1, text="Median age of females who's mental health OFTEN affects their work: " + str(fem_often)).pack()
    if clicked1.get() == 'Female and Sometimes':
        myLabel = Label(root1, text="Median age of females who's mental health SOMETIMES affects their work: " + str(fem_sometimes)).pack()
    if clicked1.get() == 'Male and Often':
        myLabel = Label(root1, text="Median age of males who's mental health OFTEN affects their work: " + str(male_often)).pack()
    if clicked1.get() == 'Male and Sometimes':
        myLabel = Label(root1, text="Median age of males who's mental health SOMETIMES affects their work: " + str(male_sometimes)).pack()
    if clicked1.get() == 'Other and Often':
        myLabel = Label(root1, text="Median age of non-female and non-males who's mental health \n OFTEN affects their work: " + str(other_often)).pack()
    if clicked1.get() == 'Other and Sometimes':
        myLabel = Label(root1, text="Median age of non-female and non-males who's mental health \n SOMETIMES affects their work: " + str(other_sometimes)).pack()
    if clicked1.get() == 'All and Often':
        myLabel = Label(root1, text="Median age of all participants who's mental health OFTEN affects their work: " + str(all_often)).pack()
    if clicked1.get() == 'All and Sometimes':
        myLabel = Label(root1, text="Median age of all participants who's mental health SOMETIMES affects their work: " + str(all_sometimes)).pack()





# Designing popup for login invalid password
def correl_verify():
    # mhsurvey = pd.read_csv('survey1.csv')
    # mhsurvey.head()
    #
    # plt.figure(figsize=(6, 5))
    # sns.countplot(mhsurvey['employees seeking mental health treatment'], palette="BrBG")
    # # sns.countplot(mhsurvey['treatment'], palette="PuBuGn_d")
    # plt.title("Treatment Distribution", fontsize=18, fontweight="bold")
    # plt.show()
    s = pd.read_csv('survey1.csv')
    s.head()

    n = LabelEncoder()
    for i in s.columns:
        s[i] = n.fit_transform(s[i].astype('str'))

    corr = s.corr()['treatment']
    corr[np.argsort(corr, axis=0)[::-1]]

    fc = s.corr()
    plt.figure(figsize=(8, 8))
    sns.heatmap(fc, vmax=1, square=True, annot=False, cmap="BuGn_r")
    plt.show()


def mc_cons_verify():

    items_mc_yes = []
    items_mc_no = []
    items_mc_maybe = []
    for item in Mental_health_consequence:
        if item == 'Yes':
            items_mc_yes.append(item)
    part_mc_yes = (len(items_mc_yes))
    # print(part_mc_yes)
    for item in Mental_health_consequence:
        if item == 'No':
            items_mc_no.append(item)
    part_mc_no = (len(items_mc_no))
    # print(part_mc_no)
    for item in Mental_health_consequence:
        if item == 'Maybe':
            items_mc_maybe.append(item)
    part_mc_maybe = (len(items_mc_maybe))
    # print(part_mc_maybe)


    my_labels1 = 'Yes', 'No', 'Maybe'
    values1= [part_mc_yes, part_mc_no, part_mc_maybe]
    plt.pie(values1, labels=my_labels1, autopct='%1.1f%%')
    plt.title('Participants who answered yes, no, and maybe to believing that discussing \n'
              'a mental health issue with your employer would have negative consequences')
    plt.axis('equal')
    plt.show()

    items_pc_yes = []
    items_pc_no = []
    items_pc_maybe = []
    for item in Phys_health_consequence:
        if item == 'Yes':
            items_pc_yes.append(item)
    part_pc_yes = (len(items_pc_yes))
    # print(part_pc_yes)
    for item in Phys_health_consequence:
        if item == 'No':
            items_pc_no.append(item)
    part_pc_no = (len(items_pc_no))
    # print(part_pc_no)
    for item in Phys_health_consequence:
        if item == 'Maybe':
            items_pc_maybe.append(item)
    part_pc_maybe = (len(items_pc_maybe))
    # print(part_pc_maybe)


    my_labels2 = 'Yes', 'No', 'Maybe'
    values2=[part_pc_yes, part_pc_no, part_pc_maybe]
    plt.pie(values2, labels=my_labels2, autopct='%1.1f%%')
    plt.title('Particpants who answered yes, no, and maybe to believing that discussing \n'
              'a physical health issue with your employer would have negative consequences')
    plt.axis('equal')
    plt.show()



    # subprocess.Popen([canvas], shell=True)
    # os.startfile('sample02.pdf')

def incorrect_gen_freq_input():
    messagebox.showinfo("Incorrect Input", "Please input the options provided")

def pdf_generated():
    messagebox.showinfo("Report generated", "The Report you are looking for has been generated.")

def password_nr():
    global incorrect_password
    incorrect_password = Toplevel(login_screen)
    incorrect_password.title("Success")
    incorrect_password.geometry("150x100")
    Label(incorrect_password, text="Invalid Password ").pack()
    Button(incorrect_password, text="OK", command=destroy_pnr).pack()


# Designing popup for user not found

def user_nf():
    global incorrect_user
    incorrect_user = Toplevel(login_screen)
    incorrect_user.title("Success")
    incorrect_user.geometry("150x100")
    Label(incorrect_user, text="User Not Found").pack()
    Button(incorrect_user, text="OK", command=destroy_ius).pack()


# Deleting popups

def end_ls():
    top.destroy()


def destroy_pnr():
    incorrect_password.destroy()


def destroy_ius():
    incorrect_user.destroy()


# Designing Main(first) window

def main_screen1():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Would you like to Login?")
    main_screen.configure(bg='aliceblue')
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Baghdad", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()


    main_screen.mainloop()


main_screen1()

