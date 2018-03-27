import pygal 
import numpy as np
from pygal.style import TurquoiseStyle
#Assumed time 10hrs/day, 6days in total (28 Dec - 2rd Jan)
time_span = 2*5
#total pages ignoring acknowledgement prefatce 
total_pages = 236
#ideal spead to finish in 6 days (pages / hr)
ideal_increment = total_pages/time_span
#pages read per hour
reading_progress = [
    #before
    0,5,
    #27 Mar
    5,
    #28 March
    
    #29 March
    #30 March
    #31 March
    ]

#percentage 
reading_percentage = reading_progress[-1]/total_pages*100
reading_percentage = str(reading_percentage)
reading_percentage =  reading_percentage[:4]
#helper function to calculate remaining pages
def getRemainingPages(n):
    return total_pages-n
  
burn_down_chart = pygal.Line(
    legend_at_bottom=True,
    style=TurquoiseStyle,
    x_title='No. Of Hours Targeted',
    y_title='Total No of pages in the book')
burn_down_chart.title = 'Burndown Chart: GRE | '+reading_percentage+'% Complete'
burn_down_chart.x_labels = map(str,range(1,time_span+1))

#ideal reading array
ideal_reading_array = []

#generate ideal reading array
for i in range(1,time_span+1):
    current_increment = i*ideal_increment
    ideal_reading_array.append(current_increment) 

#reverse to predict ideal burndown
ideal_reading_array.reverse()
burn_down_chart.add("Ideal Reading Speed",ideal_reading_array)
burn_down_chart.add("Actual Reading Speed",map(getRemainingPages,reading_progress))
burn_down_chart.render_to_png('burndown.png')

#calculate pages speed
pages_per_hour = []
for i in range(0,len(reading_progress)-2):
    pages_per_hour.append(reading_progress[i+1]-reading_progress[i]) 

#average speed
average_speed = str(np.mean(pages_per_hour))
#trim
average_speed = average_speed[:3]

#average reading time graph
reading_speed = pygal.Line(
    legend_at_bottom=True,
    style=TurquoiseStyle,
    x_title='No. Of Hours Targeted',
    y_title='Reading Speed (Pages)')

reading_speed.title = 'Reading Speed: GRE | Avg: '+average_speed+' pages/hr'
reading_speed.x_labels = map(str,range(1,time_span+1))
reading_speed.add("Pages Per Hour",pages_per_hour)
reading_speed.render_to_png('reading_speed.png')