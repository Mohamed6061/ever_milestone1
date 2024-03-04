import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read CSV data into a DataFrame
df = pd.read_csv('/home/moemen/Documents/ever_pkg/milestone_1/CSV Files/pedal and full time/pedal_1.csv')

# Convert 'Time' to milliseconds
df['Time'] = df['Time'] / 1e6

# Extract columns for time, Pedal Value, and Total Time
time = df['Time']
pedal_percent = df['Pedal Value'] * 100  # Convert Pedal Value to percentage

# Create visualizations
fig, ax3 = plt.subplots(1, 1, figsize=(10, 12))
ax3.grid(True)
# Plot Pedal Value as percentage over Time
ax3.plot(time, pedal_percent, label='Pedal Value (%)', color='blue')
ax3.set_title('Pedal over Time')
ax3.set_xlabel('Time (ms)')
ax3.set_ylabel('Pedal Value (%)')
# ax3.xaxis.set_major_locator(mdates.AutoDateLocator())
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax3.legend()

# Adjust layout
fig.suptitle('Pedal Analysis over Time')
plt.show()