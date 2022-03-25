def add_time(start_time, duration_time, starting_day=""):
    start_time_hours = int(start_time.split(":")[0]) if start_time.endswith("AM") else int(
        start_time.split(":")[0]) + 12
    start_time_minutes = int(start_time.split(":")[1].split()[0])

    duration_time_hours = int(duration_time.split(":")[0])
    duration_time_minutes = int(duration_time.split(":")[1])

    end_time_hours = start_time_hours + duration_time_hours + (start_time_minutes + duration_time_minutes) // 60
    end_time_minutes = (start_time_minutes + duration_time_minutes) % 60

    end_time_hours_string = end_time_hours % 12 if end_time_hours % 12 > 0 else 12
    end_time_minutes = f"{end_time_minutes:02d}"
    time_of_day = "AM" if end_time_hours % 24 < 12 else "PM"

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if starting_day.capitalize() in week_days:
        week_day = f", {week_days[(week_days.index(starting_day.capitalize()) + end_time_hours // 24) % 7]}"
    else:
        week_day = ""

    if end_time_hours >= 48:
        days_difference = f" ({end_time_hours // 24} days later)"
    elif end_time_hours >= 24:
        days_difference = " (next day)"
    else:
        days_difference = ""

    return f"{end_time_hours_string}:{end_time_minutes} {time_of_day}{week_day}{days_difference}"
