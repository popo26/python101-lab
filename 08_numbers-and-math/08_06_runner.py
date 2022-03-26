# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

km_for_10miles = 10 * 1.6
print(km_for_10miles)

seconds_for_30min_and_30sec = 30 * 60 + 30
print(seconds_for_30min_and_30sec)

ave_km_per_sec = km_for_10miles / seconds_for_30min_and_30sec
print(ave_km_per_sec)

ave_km_per_hour = ave_km_per_sec * 60 * 60
print(f" this runner can run {ave_km_per_hour} km per hour")



