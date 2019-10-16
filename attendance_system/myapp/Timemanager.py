from .ConstantsConfig import THRESHOLD_TIME


def timeCompare(time_in):
    time_in = str(time_in)
    from datetime import timedelta
    import datetime
    date_format = '%H:%M:%S'
    cutoff_time = datetime.datetime.strptime(THRESHOLD_TIME, date_format)
    time_in = datetime.datetime.strptime(time_in, date_format)
    if time_in > cutoff_time:
        timediff = time_in - cutoff_time
        if timediff > timedelta(minutes=30):
            emp_color = 'red'
        else:
            emp_color = 'yellow'
    else:
        emp_color = 'green'
    return emp_color