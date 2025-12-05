antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures) ### Insert code here
lowest_temp = min(antarctic_temperatures) ### Insert code here

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
average_temp = sum(antarctic_temperatures)/len(antarctic_temperatures)### Insert code here
average_temp_rounded = round(average_temp,1)
print("Average temperature:", average_temp_rounded, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp) ### Insert code here
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")