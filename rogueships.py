# Hello World program in Python

def ships(n1,n2):
    firstn1 = n1.split()[0]
    firstn2 = n2.split()[0]
    alt1 = altego(n1)
    alt2 = altego(n2)
    print n1+" x "+n2
    if altego(n2) == "OTHER ":
        tag = firstn1+" x "+firstn2
    elif firstn1 < firstn2 and not altego(n2) == "OTHER ":
        tag = firstn1+" x "+firstn2 # alphabetical ie evan x leonard
    else:
        tag = firstn2+" x "+firstn1
    print n1+" "+alt1+n2+" "+alt2+firstn2+firstn1+" "+firstn1+firstn2+" shipname"
    


def altego(nam):
    if nam == "axel walker":
        return "trickster 1 i "
    elif nam == "albert desmond":
        return "dr. dr alchemy "
    elif nam == "alvin desmond":
        return "mr. mr element "
    elif nam == "amunet black":
        return "blacksmith "
    elif nam == "digger harkness":
        return "george captain boomerang 1 i "
    elif nam == "evan mcculloch":
        return "mirror master 2 ii  "
    elif nam == "frances kane" or nam == "frankie kane":
        return "magenta frankie "
    elif nam == "hartley rathaway":
        return "pied piper "
    elif nam == "james jesse":
        return "trickster 1 i "
    elif nam == "leonard snart":
        return "captain cold "
    elif nam == "lisa snart":
        return "golden glider "
    elif nam == "marco mardon" or nam == "mark mardon":
        return "weather wizard mark "
    elif nam == "anthony gambi" or nam == "tony gambi":
        return "replicant anthony  "
    elif nam == "mick rory":
        return "heatwave heat wave "
    elif nam == "owen mercer":
        return "captain boomerang ii 2 "
    elif nam == "rosa dillon":
        return "top rosalind "
    elif nam == "roscoe dillon":
        return "top "
    elif nam == "roy bivolo":
        return "prism rainbow raider "
    elif nam == "sam scudder":
        return "mirror master 1 i "
    elif nam == "shawna baez" or nam == "lashawn baez":
        return "peekaboo peek-a-boo peek a boo shawna "
    elif nam == "abra kadabra" or nam == "citizen abra":
        return "abra kadabra citizen Abhararakadhararbarakh "
    elif nam == "jake simmons":
        return "deathbolt "
    elif nam == "jared morillo":
        return "plunder "
    elif nam == "jeremy tell":
        return "double down "
    elif nam == "joey monteleone":
        return "tarpit tar pit "
    elif nam == "kyle nimbus":
        return "mist "
    elif nam == "michael amar":
        return "christian murmur "
    elif nam == "roscoe hynes":
        return "turbine "
    elif nam == "anthony woodward" or nam == "tony woodward":
        return "girder anthony "
    else:
        return "OTHER "
    
    
    
#ships("frances kane", "wally west")



# AUTO GENERATING THE HTML FOR THE SHIPS PAGE 

def shiptml(n1,n2):
    firstn1 = n1.split()[0] # first names ie lisa
    firstn2 = n2.split()[0]
    if n1.split()[1]==n2.split()[1]:
        family = True
    else: family = False
    alt1 = altego(n1) # alter egos ie golden glider
    alt2 = altego(n2)
    label = n1+" x "+n2 # lisa snart x caitlin snow
    if altego(n2) == "OTHER ": #not-rogues go second
        tag = firstn1+" x "+firstn2
    elif firstn1 < firstn2 and not altego(n2) == "OTHER ":
        tag = firstn1+" x "+firstn2 # alphabetical ie evan x leonard
    else:
        tag = firstn2+" x "+firstn1
    filters = n1+" "+alt1+" "+n2+" "+alt2+" "+n1.split()[1]*family+" "+family*"family "+firstn2+firstn1+" "+firstn1+firstn2+" shipname" # most of the ship names
    print "    <!-- START TAG -->"
    print "<li><a href=\"/tagged/{0}\">{1}</a>".format(tag,label)
    print "<span class=\"tagslist\">{0} </span>".format(filters)

#shiptml("frances kane", "wally west")


def titletml(n1): 
    alt1 = altego(n1)
    print "    <!-- START TITLE -->"
    print "<li><div class=\"title\">{0}:</div>".format(n1)
    print "<span class=\"tagslist\">{0} {1} </span>".format(n1,alt1)
   
   
   
# rogue =  "lashawn baez"
# titletml(rogue)
# shipstomake = ["axel walker","barry allen","bette sans souci","caitlin snow","cisco ramon","clay parker","kendra saunders","leonard snart","lisa snart","marco mardon","rosa dillon","sara lance"]
# for i in shipstomake:
#     shiptml(rogue,i)
# print "\n<!--------------------------------------------------------------------------->"


    




















