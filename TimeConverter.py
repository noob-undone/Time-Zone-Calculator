print("Calculate the time in different countries!")
print()
country = input("Enter a country you want to check the time: ")
hour = input("Enter the current hour(military time) in the Philippines: ")
minute = input("And enter the current minute: ")

# convert hours
try:
    hour = int(hour)
except:
    hour = 0
if hour > 24:
    hour = 24
# convert minutes
try:
    minute = int(minute)
except:
    minute = 0
if minute > 59:
    minute = 59

ogHour = hour
ogMin = minute

greenwichHour = hour - 8

def calEZ(timezone, minuteExtra):
    hour = greenwichHour + timezone
    minute + minuteExtra
    if minuteExtra != 0:
        print()
        print("#Minutes might not be accurate!")
        print()
    print()
    print("Time in "+str(country)+" is "+str(hour)+":"+str(minute))
    print("You are "+ str(ogHour - hour) + " hours apart from the Capital of", country)

if country == "Canada":
    calEZ(-4, 0)
elif country == "Mexico":
    calEZ(-5, 0)
elif country == "Uganda":
    calEZ(3, 0)
elif country == "India":
    calEZ(5, 30)
elif country == "Netherlands":
        calEZ(2, 0)
else:
    print()
    print("Sorry! We don't have that country listed at the moment...")
    print("Or there is a syntax error")
