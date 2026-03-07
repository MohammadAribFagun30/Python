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

print( profile["CGPA"]) # CGPA-4 over write to 3.981


# dictionary inside a distionary (nested dictionary) :

# This is outside dictionary
profile2 = {
    "Department" : "CSE",
    # Inside dictionary
    "Subject" :{
        "Chem" : 90,
        "Math" : 85,
        "DLD" : 92
    }

}

print( profile2 )

# To print the element of nested dictionary :

print( profile2 ["Subject"] ["DLD"]  ) # print--> 92

