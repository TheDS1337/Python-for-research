import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

birds_tracking_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/bird_tracking.csv"
birds_info = pd.read_csv(birds_tracking_file_name)

bird_names = birds_info.bird_name.unique()

plt.figure(figsize = (7, 7))

for bird_name in bird_names:
    bird_index = birds_info.bird_name == bird_name
    x, y = birds_info.longitude[bird_index], birds_info.latitude[bird_index]

    plt.plot(x, y, ".", label = bird_name)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc = "lower right")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/bird_trajectories.pdf")
plt.show()


speed = birds_info.speed_2d[birds_info.bird_name == "Eric"]
numbers_index = ~np.isnan(speed)

plt.figure(figsize = (8, 4))
plt.hist(speed[numbers_index], bins = np.linspace(0, 30, 20), density = True)
plt.xlabel("Speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/eric_speed.pdf")
plt.show()

birds_info.speed_2d.plot(kind = "hist", range = [0, 30])
plt.xlabel("Speed (m/s)")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/eric_speed_pandas.pdf")
plt.show()


timestamps = []

for k in range(len(birds_info)):
    timestamps.append(datetime.datetime.strptime(birds_info.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birds_info["timestamps"] = pd.Series(timestamps, index = birds_info.index)

eric_infos = birds_info[birds_info.bird_name == "Eric"]
eric_times = eric_infos.timestamps
elapsed_time = [(time - eric_times[0]) / datetime.timedelta(days = 1)  for time in eric_times]

plt.plot(np.array(elapsed_time))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (in days)")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/eric_elapsed_time.pdf")
plt.show()


next_day = 1
indexes = []
daily_mean_speed = []

for i, t in enumerate(elapsed_time):
    if t < next_day:
        indexes.append(i)
    else:
        daily_mean_speed.append(np.mean(eric_infos.speed_2d[indexes]))
        next_day += 1
        indexes = []

plt.figure(figsize = (8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Bird Migration/eric_mean_speed.pdf")
plt.show()