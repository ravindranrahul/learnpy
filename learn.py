import pygal 
import numpy as np
from pygal.style import TurquoiseStyle
#Assumed time 10hrs 6 day
time_span = 60
#total pages ignoring acknowledgement prefatce 
total_pages = 519
#ideal spead to finish in 6 days (pages / hr)
ideal_increment = 519/60
#pages read per hour
pages_read_per_hour = [
    10,
    20
]
#helper function to calculate remaining pages
def getRemainingPages(n):
  return total_pages-n
         
burn_down_chart = pygal.Line()
burn_down_chart.title = 'Burndown Chart - python crash course by eric matthes'.title()
burn_down_chart.x_labels = map(str,range(1,61,1))
#ideal reading array
ideal_reading_array = []
#generate ideal reading array
for i in range(1,time_span+1):
    current_increment = i*ideal_increment
    ideal_reading_array.append(current_increment) 
#reverse to predict ideal burndown
ideal_reading_array.reverse()
burn_down_chart.add("Ideal Reading Speed",ideal_reading_array)
burn_down_chart.add("Actual Reading Speed",map(getRemainingPages,pages_read_per_hour))
burn_down_chart.render_to_png('burndown.png')