def timeConversion(s,t):
    time = s[-2:]
    hour, minnute, second = s[:-2].split(":")
    h,m,se = int(hour), int(minnute), int(second)
    if time == "PM" and h != 12:
        h += 12
    if time == "AM" and h == 12:
        h = 0
    se += t
    m += se // 60
    se %= 60
    h += m // 60
    m %= 60
    h %= 24
    return "{:02}:{:02}:{:02}".format(h,m,se)

    
