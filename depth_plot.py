import matplotlib.pyplot as plt
import csv

#Grabbing za data
with open('depth_data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)  # Removing the header row
points,depth = [],[]
for row in data:
    try:
        points.append(int(row[0]))
    except: 
        points.append(0)   #Setting point to 0 if it is not an integer (no going to happen though)
    try:
        depth.append(float(row[1]))  #Setting depth to 0 if it is not a float
    except:
        depth.append(0)

#Refining the depth values
for i in range(1,len(depth)-1):   #First and last points are not checked
    if abs(depth[i] - depth[i-1]) > 50:  #Finding anamalous points
        depth[i] = (depth[i-1]+depth[i+1])/2    #Fixing depth as the average of the preceeding and succeding points


plt.plot(points, depth,'o', markersize=2,alpha=0.7,label="Raw Data points") 
plt.xlabel('Points -->',fontsize=14)
plt.ylabel('<-- Depth',fontsize=14)
plt.title('Depth Plot')
#We have now obtained an elementary depth plot. (I removed the blue line after obtaining the Red line)

#Next i am trying to reduce noise in the data

av_depth = []
av_depth.append(depth[0])  #First point is taken for granted
for i in range(1,len(depth)-1):
    av_depth.append((depth[i-1]+depth[i]+depth[i+1])/3)  #Averaging the depth values of the preceeding, current and succeding points
av_depth.append(depth[-1])  #Last point is also taken for granted

#plt.plot(points, av_depth)  <-- This not gud (smooth) enuf heheheha
#Copy pasting and changing variable names
av_av_depth = []
av_av_depth.append(av_depth[0]) 
for i in range(1,len(depth)-1):
    av_av_depth.append((av_depth[i-1]+av_depth[i]+av_depth[i+1])/3) 
av_av_depth.append(av_depth[-1])  
#TOTALLY NOT CONFUSING AM I RIGHT
plt.plot(points, av_av_depth,'r',linewidth=3,label="Depth line graph") #ok fine

plt.plot(points,[0]*len(points),'k--',linewidth=1,label="Surface")  #Adding a black line at depth = 0

#Beautification
plt.grid(True,alpha=0.5)
plt.style.use("fivethirtyeight")

plt.legend(loc='upper right',bbox_to_anchor=(1, 0.95),fontsize=10,framealpha=0.7)
plt.show()