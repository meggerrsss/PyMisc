def macro(input1, input2, servers, instances, linkshells, capital):
  for server in servers:
    for instance in instances:
      print("{0},{1}".format(server, instance))
      for linkshell in linkshells:
        if capital == "nocaps":
          print("/{4} {2}{3} {0}{1}{3}".format(input2, server, "", instance, linkshell))
        else: 
          print("/{4} {2}{3} {0}{1}{3}".format(input2, server, server.upper(), instance, linkshell))
      print(" ")

def omnimacro(input, linkshells):  
  for linkshell in linkshells: 
    print("/{1} {0}".format(input, linkshell))



# definitions
shells = ["fc", "/ /l1", "l2", "l3", "/ /l4", "l5", "l6", "l7", "l8", "cwl1", "/ /cwl2", "/ /cwl3", "cwl4", "cwl5", "cwl6", "/ /cwl7", "/ /cwl8"]
nofcshells = ["/ /fc", "/ /l1", "l2", "l3", "/ /l4", "l5", "l6", "l7", "l8", "/ /cwl1", "/ /cwl2", "/ /cwl3", "cwl4", "cwl5", "cwl6", "/ /cwl7", "/ /cwl8"]
localonly = ["/fc", "/ /l1", "l2", "/ /l3", "/ /l4", "l5", "l6", "l7", "l8", "/cwl1", "/ /cwl2", "/ /cwl3", "cwl4", "/ /cwl5", "/ /cwl6", "/ /cwl7", "/ /cwl8"]
aeth = ""
clock = ""
arrow = ""
cross = ""
element = ""
dice = ""
crystal = ["Balmung", "Brynhildr", "Coeurl", "Diabolos", "Goblin", "Malboro", "Mateus", "Zalera"]
zones = ["", "", "", "", "", "", ""]
threezones = ["", "", "", ""]
boatzones = [""]


# need to make FATE relays (with instances), S rank relays (with instances), hunt boat relays (without instances)

print("----------------------------------------------------------------------------")
# boats
#print(macro("", "Hunt Boat " + arrow + " <flag> "+aeth, crystal, boatzones, shells, "nocaps"))
print(macro("", "Hunt Train " + arrow + " <flag> "+aeth, crystal, boatzones, nofcshells, "nocaps"))

print("----------------------------------------------------------------------------")
# instance only relays
#for i in zones:
#  print(i)
#  print(omnimacro(aeth+" Instance "+arrow+" " +i, shells))
#for i in zones:
#  print(i)
#  print(omnimacro(aeth+" Instance "+arrow+" " +i, nofcshells))

print("----------------------------------------------------------------------------")
# S ranks   
#print(macro("", element+"  S Rank  " +arrow+ " <flag> "+aeth, crystal, threezones, shells, "nocaps"))
#print(macro("", element+ " S Rank  " +arrow+ " <flag> "+aeth, crystal, threezones, nofcshells, "nocaps"))

print("----------------------------------------------------------------------------")
# FATEs
#print(macro("", dice+ "  Special FATE " + arrow + " <flag> "+aeth, crystal, boatzones, shells, "nocaps"))
#print(macro("", dice+ "  Special FATE " + arrow + " <flag> "+aeth, crystal, boatzones, nofcshells, "nocaps"))

print("----------------------------------------------------------------------------")
# SS minions
#print(omnimacro ("SS Minions in progress at previous relay", shells))
#print(omnimacro ("SS Minions in progress at previous relay", nofcshells))

print("----------------------------------------------------------------------------")
# Error
#print(omnimacro (cross+" Ignore previous relay", shells))
#print(omnimacro (cross+" Ignore previous relay", nofcshells))





#archive run macros
#print(macro("Hunt Boat  <flag> ", "Hunt Boat  <flag> "))
#print(macro("Hunt boat "))
#print(macro("S Rank Laideronnette  Central Shroud ", "Special FATE  <flag> ", "Balmung"))    
#print(macro(""))



#print(omnimacro("The Zalera Hunt boat will be departing from <flag> shortly"))
#print(omnimacro("Ignore previous relay!"))