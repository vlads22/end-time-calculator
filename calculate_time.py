
def calculate_time(start, duration, week_day=0):
    start_hour = 0
    start_minutes_am_pm = 0
    start_minutes = 0
    start_am_pm = 0
    hours_until_pm = 0
    minutes_until_pm = 0
    minutes_after_first_hour = 0
    minutes_until_end_day = 0
    minutes_of_one_day = int(60 * 24)
    minutes_of_one_week = minutes_of_one_day * 7
    
    duration_hour = 0
    duration_minutes = 0

    week_day_monday = 1
    week_day_tuesday = 2
    week_day_wednesday = 3
    week_day_thursday = 4
    week_day_friday = 5
    week_day_saturday = 6
    week_day_sunday = 7
    week_day_result = 0
    
    if week_day:
        week_day = week_day.lower()
        week_day = week_day.capitalize()
    
    week_day_number = 0
    if week_day == 'Monday':
        week_day_number = 1
    if week_day == 'Tuesday':
        week_day_number = 2
    if week_day == 'Wednesday':
        week_day_number = 3
    if week_day == 'Thursday':
        week_day_number = 4
    if week_day == 'Friday':
        week_day_number = 5
    if week_day == 'Saturday':
        week_day_number = 6
    if week_day == 'Sunday':
        week_day_number = 7



    minutes_until_endweek = 0
    minutes_after_firstweek = 0
   

    result_hour = 0
    result_minutes = 0
    result_am_pm = 0
    result_day = 0
    days_later = 0
    days_later_number = 0
    result = ''
        
    start_split = start.split(':')
    start_hour = int(start_split[0])
    start_minutes_am_pm = start_split[1]
    start_minutes_am_pm_split = start_minutes_am_pm.split()
    start_minutes = int(start_minutes_am_pm_split[0])
    start_am_pm = start_minutes_am_pm_split[1]

    if start_am_pm == 'PM':
        minutes_until_end_day = (60 - start_minutes) + ((11 - start_hour) * 60)
    elif start_am_pm == 'AM':
        minutes_until_end_day = (60 - start_minutes) + ((23 - start_hour) * 60)

    duration_split = duration.split(':')
    duration_hour = int(duration_split[0])
    duration_minutes = int(duration_split[1])
    duration_total_minutes = duration_hour * 60 + duration_minutes
    duration_left_after_end_day = duration_total_minutes - minutes_until_end_day
    duration_days = int(duration_left_after_end_day / minutes_of_one_day)
    minutes_last_day = int(duration_left_after_end_day % minutes_of_one_day)
    minutes_left_in_first_hour = int(60 - start_minutes)
    minutes_after_first_hour = int(duration_total_minutes - minutes_left_in_first_hour)
    hours_last_day = int(minutes_last_day / 60)
    
    
    #0 same hour
    if minutes_after_first_hour < 0:
        result_hour = start_hour
        result_am_pm = start_am_pm
        result_minutes = int(start_minutes + duration_minutes)
        if week_day:
                result = str(str(result_hour) + ':' + str(result_minutes).rjust(2, '0') + ' ' + str(result_am_pm) +
            ', ' + str(result_day) + ' ' + str(days_later))
        
        else:
            result = str(str(result_hour) + 
                    ':' + str(result_minutes).rjust(2, '0') + ' ' + str(result_am_pm))


    #1 same day after first hour
    elif minutes_after_first_hour > 0 and duration_total_minutes < minutes_until_end_day:
        if minutes_after_first_hour < 60:   #checked
            result_hour = start_hour + 1
            if start_hour < 11: 
                result_am_pm = start_am_pm
            elif start_hour == 11:
                result_am_pm = 'PM'

        elif minutes_after_first_hour > 60:
            result_hour = int(start_hour + 1 + minutes_after_first_hour / 60)
            if start_am_pm == 'PM':
                result_am_pm = 'PM'
            elif start_am_pm == 'AM':
                if result_hour < 12:
                    result_am_pm = 'AM'
                elif result_hour > 12:
                    result_am_pm = 'PM'
                    result_hour = int(result_hour - 12)                        
        
        result_minutes = int(minutes_after_first_hour) % 60

        if week_day:
            result = str(str(result_hour) + ':' + str(result_minutes).rjust(2, '0') + ' ' + str(result_am_pm) +
        ', ' + week_day)
    
        else:
            result = str(str(result_hour) + 
                ':' + str(result_minutes).rjust(2, '0') + ' ' + str(result_am_pm))
    
    
    #wednesday 3   4 x 
    minutes_until_endweek = (7-week_day_number) * minutes_of_one_day

    
    # weekday calculation for same week scenario
    if minutes_until_endweek > duration_left_after_end_day:
        if (duration_left_after_end_day / minutes_of_one_day) <= 1:
            week_day_result = int(week_day_number + 1)
        if (duration_left_after_end_day / minutes_of_one_day) < 2 and (duration_left_after_end_day / minutes_of_one_day) > 1:
            week_day_result = int(week_day_number + 1 + (duration_left_after_end_day / minutes_of_one_day))
        if (duration_left_after_end_day / minutes_of_one_day) >= 2:
            week_day_result = int(week_day_number + (duration_left_after_end_day / minutes_of_one_day))

    # you surpass the current week, you go into next weeks    
    elif minutes_until_endweek < duration_left_after_end_day:
        minutes_after_firstweek = int(duration_left_after_end_day - minutes_until_endweek)
        minutes_in_last_week = int(minutes_after_firstweek % minutes_of_one_week)
        week_day_result = int(minutes_in_last_week / minutes_of_one_day)
        if week_day_result < 1:
            week_day_result = 1
    
    if week_day_result == 0:
        if week_day == 'Monday':
            result_day = 'Tuesday'
        if week_day == 'Tuesday':
            result_day = 'Wednesday'
        if week_day == 'Wednesday':
            result_day = 'Thursday'
        if week_day == 'Thursday':
            result_day = 'Friday'
        if week_day == 'Friday':
            result_day = 'Saturday'
        if week_day == 'Saturday':
            result_day = 'Sunday'
        if week_day == 'Sunday':
            result_day = 'Monday'
    elif week_day_result == 1:
        result_day = 'Monday'
    elif week_day_result == 2:
        result_day = 'Tuesday'
    elif week_day_result == 3:
        result_day = 'Wednesday'
    elif week_day_result == 4:
        result_day = 'Thursday'
    elif week_day_result == 5:
        result_day = 'Friday'
    elif week_day_result == 6:
        result_day = 'Saturday'
    elif week_day_result == 7:
        result_day = 'Sunday'
    



    #2   after first day, same week  , we start from minutes_last_day and hours_last_day
    if duration_total_minutes > minutes_until_end_day:

        if duration_left_after_end_day < minutes_of_one_day:
            days_later = '(next day)'
        elif duration_left_after_end_day > minutes_of_one_day:
            days_later_number = int(duration_left_after_end_day / minutes_of_one_day + 1)
            days_later = ('(' + str(days_later_number) + ' days later' + ')')

        if hours_last_day > 12:
            result_am_pm = 'PM'
            result_hour = int(hours_last_day - 12)
        elif hours_last_day < 12:
            result_am_pm = 'AM'
            result_hour = hours_last_day
        result_minutes = int(minutes_last_day % 60)
        if result_hour == 0:
            result_hour = 12

        if week_day:
            result = str(str(result_hour) + ':' + str(result_minutes).rjust(2, '0') + ' ' + str(result_am_pm) +
         ', ' + str(result_day) + ' ' + str(days_later))
    
        else:
            result = str((str(result_hour) + ':' + str(result_minutes).rjust(2, '0') + ' ' + result_am_pm + ' ' 
        + str(days_later)))
    
    #print(duration_left_after_end_day )
    #print(minutes_of_one_day)
    #print(duration_left_after_end_day / minutes_of_one_day)
    #print(minutes_until_end_day)
    #print(week_day_number)
    #print(minutes_until_endweek)  # it wrong 10.080, that is minutes of a whole week
    #print(week_day_result)
    # print(minutes_after_firstweek)
    # print(minutes_of_one_week)
    # print(minutes_in_last_week)
    
    
    return result


print(calculate_time("2:59 AM", "24:00", "saturDay"))    

#print(60*24+5)
# Returns: 12:03 AM, Thursday (2 days later)

    #print(minutes_last_day)
    #print(hours_last_day)
    #print(result_hour)
    #print(result_am_pm)
    #print(result_minutes)
    #print(days_later)
    #print(week_day)
    #print(minutes_in_last_week)
    #print(week_day_result)
    #print(result_day)
    #print(result)
    #print(minutes_until_end_day)
   




