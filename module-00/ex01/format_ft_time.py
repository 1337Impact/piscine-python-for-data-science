import datetime

def ft_format_time(date_in_seconds: int) -> str:
    str_date = str(date_in_seconds)
    int_part = int(str_date.split(".")[0])
    frac = str_date.split(".")[1]
    return f'{int_part:,}' + "." + frac[:4]


first_date = datetime.datetime(1970, 1, 1)
current_date = datetime.datetime.now()
time_since = current_date - first_date

date_in_seconds = time_since.total_seconds()
scientific_notation="{:e}".format(date_in_seconds)

print("Seconds since January 1, 1970:", ft_format_time(date_in_seconds), "or", scientific_notation, "in scientific notation")
print(current_date.strftime("%b %d %Y"))
print(f'{date_in_seconds:,}')