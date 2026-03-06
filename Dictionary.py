profile = {

    "Name" : "Mohammad Arib Fagun",
    "CGPA" : 4,
    "Semester" : "2nd",
    "Subject" : ["DLD","Chemistry", "Statistics","GEED"], #tuple
    "Topper" : ("Labib", "Fahmid","Towhid","Albab") # list
}

print( profile )

# spcific element : 

print( profile["Name"]  ) # print--> Mohammad Arib Fagun

# Assign value :

profile["CGPA"] = 3.981

print( profile["CGPA"])


# dictionary inside a distionary (nested dictionary) :

profile2 = {
    "Department" : "CSE",
    # dictionary
    "Subject" :{
        "Chem" : 90,
        "Math" : 85,
        "DLD" : 92
    }

}

print( profile2 )

# To print the element of nested dictionary :

print( profile2 ["Subject"] ["DLD"]  ) # print--> 92

