
time = raw_input("Enter time : ")
length = len(time)
time_in = time[length-2:length]
if time_in.upper() == 'AM':
    hr_str = time.split(":")[0]
    hr = int(hr_str)
    if hr < 12:
        print time[0:length-2]
    if hr == 12:
        print time.replace(hr_str, "00",1)[0:length-2]
    if hr > 12 :
        print "invalid time"
else:
    if time_in.upper() == 'PM':
        hr_str = time.split(":")[0]
        hr = int(hr_str)
        if hr < 12:
            hr += 12
            print time.replace(hr_str, str(hr),1)[0:length-2]
        else :
            if hr == 12:
                print time[0:length-2]
            if hr > 12:
                print "Invalid time"
