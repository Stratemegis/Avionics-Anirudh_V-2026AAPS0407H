import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation #Imported Additionally

#Creating Our Required Lists for Raw data and Averaged data (Skip to line 40 for new shit)
with open('depth_data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)  
points,depth = [],[]
for row in data:
    try:
        points.append(int(row[0]))
    except: 
        points.append(0)  
    try:
        depth.append(float(row[1])) 
    except:
        depth.append(0)
#Refining the depth values
for i in range(1,len(depth)-1):   
    if abs(depth[i] - depth[i-1]) > 50:  
        depth[i] = (depth[i-1]+depth[i+1])/2 

#Our _points_ list and _depth_ list are ready.

av_depth = []
av_depth.append(depth[0])
for i in range(1,len(depth)-1):
    av_depth.append((depth[i-1]+depth[i]+depth[i+1])/3)  
av_depth.append(depth[-1]) 

av_av_depth = []
av_av_depth.append(av_depth[0]) 
for i in range(1,len(depth)-1):
    av_av_depth.append((av_depth[i-1]+av_depth[i]+av_depth[i+1])/3) 
av_av_depth.append(av_depth[-1])  
#av_av_depth CREATED 

def animate(i):
    x = points[:i+1]       #1 to 300 0n the x-axis
    y1 = depth[:i+1]       #Raw Depth Points
    y2 = av_av_depth[:i+1] #Averaged Depth Points
    y3 = [0]*(i+1)         #Surface Line

    plt.cla()
    plt.plot(x, y1,'o', markersize=2,alpha=0.7,label="Raw Data points") 
    plt.plot(x, y2,'r',linewidth=3,label="Depth line graph")
    plt.plot(x, y3,'k--',linewidth=1,label="Surface")       #Plotting everything

    #Markings and Labels
    plt.xlabel('Points -->',fontsize=14)
    plt.ylabel('<-- Depth',fontsize=14)
    plt.title('Depth Plot')

    #Beautification
    plt.grid(True,alpha=0.5)
    plt.style.use("fivethirtyeight")
    plt.legend(loc='upper right',bbox_to_anchor=(1, 0.95),fontsize=10,framealpha=0.7)

ani = FuncAnimation(plt.gcf(), animate, interval=1000,frames=len(points),repeat=False) #1000ms delay between frames

plt.show()