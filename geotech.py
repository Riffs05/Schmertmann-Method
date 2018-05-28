#Group 7
#Rahul Kumar Chaudhary
#Gantavya Gupta

import math
import os
os.system('clear')
def Surcharge(WTlabel,depthF,densityOfSoil):
	if(WTlabel>=depthF):
		surcharge=depthF*densityOfSoil
	if(WTlabel<depthF):
		surcharge=(WTlabel*densityOfSoil)+(depthF - WTlabel)*(densityOfSoil-9.81)
	return surcharge
def MinStrainFactorValue(length,breadth):
	dimentionFactor=length/breadth
	Iz0=(dimentionFactor-1)*.0111 +.1
	if(Iz0>.2):
		Iz0=.2
	return Iz0
def DepthAtWhichIzMax(length,breadth):
	dimentionFactor=length/breadth
	z1=(dimentionFactor-1)*.0555+ .5
	if(z1>1):
		z1=1
	return z1*breadth
def MaxStrainFactor(surcharge,q,sigmaZ):
	Izmax=.5+(math.sqrt((q-surcharge)/sigmaZ))*.1
	return Izmax
def InfluenceZone(length,breadth):
	dimentionFactor=length/breadth
	Z2=2+(dimentionFactor-1)*0.222
	if(Z2>4):
		Z2=4
	return Z2*breadth
def main():
	# **********************************************Obtaining The Input**************************************************************
	length=input("Enter the length of the footing in Meter: ")
	breadth=input("Enter the breadth of the footing Meter : ")
	depth=input("Enter depth of the footing in Meter : ")
	watertable=input("Enter the depth of water table in Meter : ")
	densityOfSoil=input("Enter the soil density in kilo Newton Per cubic Meter:")
	q=input("Enter the load to design in kilo Pascal : ")
	time=input("Time of settlement in year : ")
	#********************************************** End of The Input Session**********************************************************
	#********************************************Backend will start from here*********************************************************
	surcharge=Surcharge(watertable,depth,densityOfSoil)                                     
	print "Value of surcharge : ",surcharge
	IzMin=MinStrainFactorValue(length,breadth)
	print "Value of minimum Influnce Factor Value :",IzMin                                              
	z1=DepthAtWhichIzMax(length,breadth)													
	print "Depth at Which Influnce Factor is maximum :",z1
	z1FromGroundLevel=z1+depth 										         				
	#print(z1FromGroundLevel)
	stressZ1=Surcharge(watertable,z1FromGroundLevel,densityOfSoil) 			         		 
	IzMax=MaxStrainFactor(surcharge,q,stressZ1)     
	print "Maximum Value of Influence Factor : ",IzMax 		                              
	z2=InfluenceZone(length,breadth)
	influnceZone=z2
	layerimf=[]
	checkdepth=depth
	#**************************************** Input Layer Imformation *****************************************************************
	n=input("Enter the number of layer : ")
	for i in range(n):
		d=input("Enter the thickness of the layer in Meter:")
		Qc=input("Enter the value of Qc In Megapascal per meter Square : ")
		if(checkdepth<z1FromGroundLevel and (checkdepth+d)>z1FromGroundLevel):
			checkdepth=checkdepth+d
			newlayerdepth=d-(checkdepth- z1FromGroundLevel)
			layerimf.append([newlayerdepth,Qc])
			newlayerdepth=checkdepth- z1FromGroundLevel
			layerimf.append([newlayerdepth,Qc])
		
		else:
			layerimf.append([d,Qc])
			checkdepth=checkdepth+d
	#print(layerimf)
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
				Iz=((IzMax/(z1-influnceZone))*(z-z1)) + IzMax
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
				if(z>z1):
					Iz=((IzMax/(z1-influnceZone))*(z-z1)) + IzMax
					checkdepth=checkdepth+d
				else:
					Iz=(((IzMax- IzMin)/z1)*z + IzMin)
					checkdepth=checkdepth+d
			Ez=(Iz*d)/Es
			fnialArray.append([Es,d,Iz,Ez])
	#print(fnialArray)
	sumIz=0
		
	for k in range(len(fnialArray)):
		sumIz=sumIz+fnialArray[k][3]
	constant1=1.0-.5*(surcharge/(q-surcharge))
	constant2=1.0+.2*(math.log10(time/.1))
	FinalSettlement=constant1*constant2*(q-surcharge)*sumIz
	print("Printing the Datasheet")
	print("Wait ......")
	print("Layer \t |\t \t Ez \t \t | \t Z \t     \t| \t Iz \t \t \t| \t Iz*Z/Es")
	for l in range(len(fnialArray)):
		print l," \t | \t ",fnialArray[l][0]," \t | \t ",fnialArray[l][1]," \t | \t ",fnialArray[l][2]," \t | \t ",fnialArray[l][3]
	print("Here is the final Result. Settlement Value in in mm ")
	print(FinalSettlement)

	
main()

#Now we will keep track of depth and nq value
