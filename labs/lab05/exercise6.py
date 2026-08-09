print("Time in minutes:")
minute = int(input())
hours = minute // 60
remaining_minute = minute % 60
print("Original minutes:", minute)
print(f"Converted time: {hours} hour(s) and {remaining_minute} minute(s)")
print(type(remaining_minute))