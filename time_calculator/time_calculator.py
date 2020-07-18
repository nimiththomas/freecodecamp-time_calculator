def add_time(start, duration,day="default"):
    #extracting hour,minute,am/pm from start time
    colon=start.find(":")
    thour=int(start[:colon])
    space=start.find(" ")
    tminute=int(start[colon+1:space])
    ampm=start[space+1:]
    #converting to 24 hour format
    if(ampm=="PM"):
        if(thour==12):
            thour=thour+0
        else:
            thour=thour+12
    else:
        if(thour==12):
            thour=0


    #extracting hour and minute from duration
    dcolon=duration.find(":")
    dhour=int(duration[:dcolon])
    dminute=int(duration[dcolon+1:])

    #if no day specified
    if(day=="default"):
        #calculating the minutes of result
        rhour=thour
        rminute=tminute+dminute
        #adding a one to hour if minutes greater than 60
        if(rminute>=60):
            rhour=rhour+1
            rminute=rminute-60

        #adding updated hours of start with duration hours
        rhour=rhour+dhour


        #if the rhour is less than 12 just printing the values
        if(rhour<12):
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end="")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm)
        #since 12 in 24hr format is 12pm
        elif(rhour==12):
            ampm="PM"
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end=" ")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm)

        elif(rhour<24):
            #when it is more than 12 it is pm in 24hr format so converting am to pm and conerting the 24hrformat to 12hr format
            if(ampm=="AM"):
                rhour=rhour-12
                ampm="PM"
                print(rhour,end="")
                print(":",end="")
                if(rminute==0):
                    print(rminute,end="")
                    print(rminute,end=" ")
                elif(rminute<10):
                    print("0",end="")
                    print(rminute,end=" ")

                else:
                    print(rminute,end=" ")
                print(ampm)
            else:
                rhour=rhour-12
                print(rhour,end="")
                print(":",end="")
                if(rminute==0):
                    print(rminute,end="")
                    print(rminute,end=" ")
                elif(rminute<10):
                    print("0",end="")
                    print(rminute,end=" ")

                else:
                    print(rminute,end=" ")
                print(ampm)
        #since 24 in 24hr format is 12 am and converting to 12 hrs format
        elif(rhour==24):
            ampm="AM"
            rhour=rhour-12
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end=" ")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm)
        #when rhour >24 the day changes
        else:
            #calculating no. of days
            n=int(rhour/24)
            #when n=1 print next day
            if(n==1):
                rhour=rhour%24
                if(rhour<12):
                    ampm="AM"
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")


                    else:
                        print(rminute,end=" ")

                    print(ampm,end=" ")
                    print("(next day)")
                else:
                    ampm="PM"
                    rhour=rhour-12
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")

                    else:
                        print(rminute,end=" ")

                    print(ampm,end=" ")
                    print("(next day)")
            #when n>1 printing the no. of days
            else:
                rhour=rhour%24
                if(rhour<12):
                    if(rhour==0):
                        rhour=12
                    ampm="AM"
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")


                    else:
                        print(rminute,end=" ")

                    print(ampm,end=" ")
                    print("(",end="")
                    print(n,end=" ")
                    print("days later",end="")
                    print(")")


                else:
                    ampm="PM"
                    rhour=rhour-12
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")

                    else:
                        print(rminute,end=" ")

                    print(ampm,end=" ")
                    print("(",end="")
                    print(n,end=" ")
                    print("days later",end="")
                    print(")")
    else:
        sday=day.lower()
        cday=sday.capitalize()



        #calculating the minutes of result
        rhour=thour
        rminute=tminute+dminute
        #adding a one to hour if minutes greater than 60
        if(rminute>=60):
            rhour=rhour+1
            rminute=rminute-60

        #adding updated hours of start with duration hours
        rhour=rhour+dhour


        #if the rhour is less than 12 just printing the values
        if(rhour<12):
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end="")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm,end="")
            print(",",end=" ")
            print(cday)

        #since 12 in 24hr format is 12pm
        elif(rhour==12):
            ampm="PM"
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end=" ")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm,end="")
            print(",",end=" ")
            print(cday)

        elif(rhour<24):
            #when it is more than 12 it is pm in 24hr format so converting am to pm and conerting the 24hrformat to 12hr format
            if(ampm=="AM"):
                rhour=rhour-12
                ampm="PM"
                print(rhour,end="")
                print(":",end="")
                if(rminute==0):
                    print(rminute,end="")
                    print(rminute,end=" ")
                elif(rminute<10):
                    print("0",end="")
                    print(rminute,end=" ")

                else:
                    print(rminute,end=" ")
                print(ampm,end="")
                print(",",end=" ")
                print(cday)
            else:
                rhour=rhour-12
                print(rhour,end="")
                print(":",end="")
                if(rminute==0):
                    print(rminute,end="")
                    print(rminute,end=" ")
                elif(rminute<10):
                    print("0",end="")
                    print(rminute,end=" ")

                else:
                    print(rminute,end=" ")
                print(ampm,end="")
                print(",",end=" ")
                print(cday)
        #since 24 in 24hr format is 12 am and converting to 12 hrs format
        elif(rhour==24):
            ampm="AM"
            rhour=rhour-12
            print(rhour,end="")
            print(":",end="")
            if(rminute==0):
                print(rminute,end="")
                print(rminute,end=" ")
            elif(rminute<10):
                print("0",end="")
                print(rminute,end=" ")

            else:
                print(rminute,end=" ")

            print(ampm,end="")
            print(",",end=" ")
            print(cday)
        #when rhour >24 the day changes
        else:
            #calculating no. of days
            n=int(rhour/24)
            #when n=1 print next day
            days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
            #finding the index of the day in list
            cdayindex=days.index(cday)


            if(n==1):
                rhour=rhour%24
                if(rhour<12):
                    ampm="AM"
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")


                    else:
                        print(rminute,end=" ")

                    print(ampm,end="")
                    print(",",end=" ")
                    l=cdayindex+1
                    if(l>6):
                        l=l-1
                    k=l%6
                    print(days[k],end="")

                    print("(next day)")
                else:
                    ampm="PM"
                    rhour=rhour-12
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")

                    else:
                        print(rminute,end=" ")

                    print(ampm,end="")
                    print(",",end=" ")
                    l=cdayindex+1
                    if(l>6):
                        l=l-1
                    k=l%6
                    print(days[k],end="")

                    print("(next day)")
            #when n>1 printing the no. of days
            else:
                rhour=rhour%24
                if(rhour<12):
                    if(rhour==0):
                        rhour=12
                    ampm="AM"
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")


                    else:
                        print(rminute,end=" ")

                    print(ampm,end="")
                    print(",",end=" ")
                    l=cdayindex+n
                    if(l>6):
                        l=l-1
                    k=l%6
                    print(days[k],end=" ")
                    print("(",end="")
                    print(n,end=" ")
                    print("days later",end="")
                    print(")")


                else:
                    ampm="PM"
                    rhour=rhour-12
                    print(rhour,end="")
                    print(":",end="")
                    if(rminute==0):
                        print(rminute,end="")
                        print(rminute,end=" ")
                    elif(rminute<10):
                        print("0",end="")
                        print(rminute,end=" ")

                    else:
                        print(rminute,end=" ")

                    print(ampm,end=" ")
                    print("(",end="")
                    print(n,end=" ")
                    print("days later",end="")
                    print(")")
