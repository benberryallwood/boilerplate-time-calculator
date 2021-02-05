def add_time(start, duration, day=None):
    start_hh, start_mm = start.split()[0].split(':')
    time_of_day = start.split()[1]
    dur_hh, dur_mm = duration.split(':')

    dur_hh = int(dur_hh)
    new_mm = (int(start_mm) + int(dur_mm)) % 60
    if int(start_mm) + int(dur_mm) > 60:
        dur_hh += (int(start_mm) + int(dur_mm)) // 60
    new_hh = (int(start_hh) + dur_hh)

    switch = 0
    if (new_hh // 12) % 2 == 1:
        if time_of_day == 'AM':
            time_of_day = 'PM'
        else:
            time_of_day = 'AM'
            switch = 1

    next_day = False
    if (new_hh >= 24 and new_hh < 48) or switch == 1:
        next_day = True
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 
    'sunday']
    num_days_later = new_hh // 24 + switch
    if day != None:
        day_index = days.index(day.lower())
        day_index = (day_index + num_days_later) % 7
        day = days[day_index]

    new_hh = new_hh % 12
    if new_hh == 0:
        new_hh = 12

    new_hh = str(new_hh)
    if len(str(new_mm)) == 1:
        new_mm = '0' + str(new_mm)
    else:
        new_mm = str(new_mm)

    new_time = new_hh + ':' + new_mm + ' ' + time_of_day
    if day != None:
        new_time += ', ' + day.capitalize()

    if num_days_later == 1:
        new_time += ' (next day)'

    if num_days_later > 1:
        new_time += ' (' + str(num_days_later) + ' days later)'
    return new_time