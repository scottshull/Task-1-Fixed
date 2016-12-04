selection = 0
while selection >= 0:
    print "[======================]"
    print "   1. Returning Customer"
    print "   2. New Customer"
    print "   3. Guest"
    print "[======================]\n"

    selection = int(raw_input("Pick a selection:  "))
    try:
        if selection <1 or selection > 3:
            selection = int(raw_input("Pick a selection:   "))
        elif selection == 1:
            print "Welcome Back!"
            selection = -1
        elif selection == 2:
            print "Welcome!\n"
            selection = -1
        elif selection == 3:
            print "Hello Guest"
            selection = -1
        else:
            print "\n\nPick a selection:   "
    except ValueError:
        print "Pick a selection:   "
