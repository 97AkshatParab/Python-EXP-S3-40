vcet='VIDYAVARDHINIS COLLEGE OF ENGINEERING & TECHNOLOGY'
print(vcet)
my_department="Computer, Science, & Engineering,- Data Science" #String Example
all_branches=["CSE_DS","COMPS","AI_DS","MECH","EXTC","CIVIL","IT","VLSI"] #List Example
all_HOD={"CSE-DS":"VIKAS GUPTA","COMPS":"MEGHA maam","AI_DS":"TATVADARSHI SIR","MECH":"UDAY ASWALEKAR","EXTC":"AMRITA RUPEREE"} #Dictionary Example
all_intakes=(180,180,60,60,60,60,60,60) #Tuple Example
print("A Brief Discription of VCET:")
print('''My Branch is:'''+my_department)
print("There are total eight branches in VCET:")
print(all_branches)
print("\n")
print("All HODS of Branches are:")
print(all_HOD)
print("No of Intakes of each branches are:-")
print(all_intakes[0:5]*2)
all_branches.insert(2,"Aerospace")
all_branches
all_HOD.keys()
print("\n")
all_HOD.pop("CSE-DS")
all_HOD
