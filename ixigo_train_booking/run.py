from booking.main import ixigo
print()
print("Fill out some details")
start = str(input("Strating journey from : "))
_end = str(input("Destination : "))
when = str(input("Date[dd mm yy] : "))
print("*"*25,"Available Trains are","*"*25)
with ixigo() as bot:
    bot.first_page()
    bot.start_from(start)
    bot.destination(_end)
    bot.d_date(when)
    try:
        bot.search()
        bot.avl_trains()
        print()
        print("Exiting....")
    except:
        exit()
    
    