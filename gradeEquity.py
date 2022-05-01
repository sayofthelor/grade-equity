from matplotlib import pyplot as plt
import csv 
import numpy as np
import sys

# testing some things up here
aMath, bMath, cMath, dMath, eMath = [], [], [], [], []
group_map = {'group A': aMath, 'group B': bMath, 'group C': cMath, 'group D': dMath, 'group E': eMath}
with open('exams.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      group_map[row['ethnicity']].append(int(row['math score'])) # right? 

# probability distribution function
def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out

# To generate an array of x-values 
# x = np.arange(-4, 2, 0.1) 
  
# To generate an array of 
# y-values using corresponding x-values
# y = pdf(x)

  
# To fill in values under the bell-curve
# x_fill = x 
# y_fill = pdf(x_fill)

# Plotting the bell-shaped curve
plt.style.use('dark_background')
plt.figure(figsize = (6, 6))
# plt.plot(x, y, color = 'black',
#          linestyle = 'solid')
colors = ['r', 'g', 'b', 'c', 'm'] # ? you'll see
labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
for i, dataset in enumerate(group_map.values()):
    print(f"{labels[i]}: " + str(dataset)) 
    x = np.sort(np.array(dataset)) 
    y = pdf(x) 
    x_fill = x 
    y_fill = pdf(x_fill) 
    plt.plot(x, y, color = colors[i], label = labels[i])
    plt.fill_between(x_fill, y_fill, 0, alpha= 0.2, color = colors[i])
    

# show each point on the graph 
# plt.scatter(x, y, marker = 'o', s = 25, color = 'red')
  
# plt.fill_between(x_fill, y_fill, 0, alpha = 0.2, color = 'blue')
titleFont = {'family':'DejaVu Sans', 'weight':'bold', 'size':20}
plt.title('Math Scores by Ethnicity', fontdict = titleFont)
plt.legend()
plt.show()

# references: ------ 
# - https://docs.python.org/3/library/csv.html 
# - https://www.geeksforgeeks.org/how-to-make-a-bell-curve-in-python/ 
# - http://roycekimmons.com/tools/generated_data/exams 
# - https://www.dunderdata.com/blog/view-all-available-matplotlib-styles 