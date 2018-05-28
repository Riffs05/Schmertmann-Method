#Group 7
#Rahul Kumar Chaudhary
#Gantavya Gupta
#Taking Input
import math
length=input("Enter the length of the footing : ")
breadth=input("Enter the breadth of the footing : ")
footingFactor=(length/breadth)-1
depth=input("Enter depth of the footing : ")
q=input("Enter the load to design : ")
watertable=input("Enter the depth of water table : ")
densityOfSoil=input("Enter the soil density : ")
time=input("Time of settlement : ")
#
#Calculation of surcharge 
#
if(watertable>=depth):
	surcharge=depth*densityOfSoil
if(watertable<depth):
	surcharge=(watertable*densityOfSoil)+(depth-watertable)*(densityOfSoil-9.81)
#Calculation of other facter
strainfactorMin=(footingFactor)*.0111 + .1
#Check for the max value of strainfactorMin 
#
if(strainfactorMin>.2):
	strainfactorMin=.2
#
#print(strainfactorMin)
maxStrainFactordepth=(footingFactor*.0555)+.5
if(maxStrainFactordepth>1):
	maxStrainFactordepth=1
#print(maxStrainFactordepth)

Z1=(maxStrainFactordepth*breadth)
heightAtMaxStrainFactor=(maxStrainFactordepth*breadth)+depth

#calculation of surcharge at maxHeigh of strain factor
if(watertable>heightAtMaxStrainFactor):
	stressZ=heightAtMaxStrainFactor*densityOfSoil
else:
	stressZ=(watertable*densityOfSoil)+((heightAtMaxStrainFactor-watertable)*(densityOfSoil-9.81))
maxStraiFactor=.5+(math.sqrt((q-surcharge)/stressZ))*.1
zeroStrainFactordepth=2+(footingFactor*0.222)
if(zeroStrainFactordepth>4):
	zeroStrainFactordepth=4
heightAtZeroStrain=zeroStrainFactordepth*breadth
influnceZone=heightAtZeroStrain
#Finding all the layer
layerimf=[]
checkdepth=depth
n=input("Enter the number of layer : ")
for i in range(n):
	d=input("Enter the thickness of the layer :")
	Qc=input("Enter the value of Qc : ")
	if(checkdepth<heightAtMaxStrainFactor and (checkdepth+d)>heightAtMaxStrainFactor):
		checkdepth=checkdepth+d
		newlayerdepth=d-(checkdepth-heightAtMaxStrainFactor)
		layerimf.append([newlayerdepth,Qc])
		newlayerdepth=checkdepth-heightAtMaxStrainFactor
		layerimf.append([newlayerdepth,Qc])
		
	else:
		layerimf.append([d,Qc])
		checkdepth=checkdepth+d
#Calculation of final array
fnialArray=[]
checkdepth=0
for j in range(len(layerimf)):
	#Calculation of Es
	d=layerimf[j][0]
	Qc=layerimf[j][1]
	z=checkdepth+d/2
	if(checkdepth<influnceZone):
		if(checkdepth<influnceZone and (checkdepth+d)>influnceZone):
			if((length/breadth)<10):
				if(length==breadth):
					Es=2.5*Qc
				else:
					Es=(1+(.4*math.log10(length/breadth)))*2.5*Qc
			else:
				Es=3.5*Qc
			Iz=((maxStraiFactor/(Z1-influnceZone))*(z-Z1)) + maxStraiFactor
			d=influnceZone- checkdepth
			checkdepth=checkdepth+d
		else:
			if((length/breadth)<10):
				if(length==breadth):
					Es=2.5*Qc
				else:
					Es=(1+(.4*math.log10(length/breadth)))*2.5*Qc
			else:
				Es=3.5*Qc
			if(z>Z1):
				Iz=((maxStraiFactor/(Z1-influnceZone))*(z-Z1)) + maxStraiFactor
				checkdepth=checkdepth+d
			else:
				Iz=(((maxStraiFactor- strainfactorMin)/Z1)*z + strainfactorMin)
				checkdepth=checkdepth+d
		Ez=(Iz*d)/Es
		fnialArray.append([Es,d,Iz,Ez])

sumIz=0
		
for k in range(len(fnialArray)):
	sumIz=sumIz+fnialArray[k][3]
constant1=1.0-.5*(surcharge/(q-surcharge))
constant2=1.0+.2*(math.log10(time/.1))
FinalSettlement=constant1*constant2*(q-surcharge)*sumIz


print(surcharge)
print(strainfactorMin)
print(maxStrainFactordepth)
print(stressZ)
print(maxStraiFactor)
print(heightAtZeroStrain)
print(heightAtMaxStrainFactor)
print(layerimf)
print("Printing the value of final array \n")
print(fnialArray)
print("Printing SUmZX")
print(sumIz)
print(constant1)
print(constant2)
print("Printing the final Settlement")
print(FinalSettlement)

#Now we will keep track of depth and nq value