import calendar

# Get the list of month names
months = list(calendar.month_name)

# Remove the first empty string (index 0) as there's no month 0
months = months[1:]

# Display the months
for month in months:
    print(month)