for i in range(0,1000):
    if i in range(0,9):
        v = "00{}".format(i)
    if i in range(10,99):
        v = "0{}".format(i)
    else:
        v = str(i)
    print("IGNORE_SEARCHTERM={}".format(v))
	
