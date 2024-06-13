name = "venu"
experience = 8
location = "hydrabad"
print("my name is "+name+".I have around"+str(experience)+"year of experience and i lived in " +location+".")
print("my name is "+name+".I have around",experience,"year of experience and i lived in " +location+".")
print("my name is {}.I have around {},year of experience and i lived in {}.".format(name,experience,location))
print("my name is {2}.I have around {0},year of experience and i lived in {1}. ".format(experience,location,name))

#%s,%d,
print("my name is %s.I have around %d,year of experience and i lived in %s."%(name,experience,location))


