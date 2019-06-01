#Name: Pragya Sethi
#RollNo. : 2018067
#Section : A
#Group: 3


from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import matplotlib
from math import *


def MatrixMultiply(M1,M2):				#Function that multiplies the transformation matrix with coordinate matrix
	M=[]
	for row in M1:
		rowM=0
		for i in range(len(row)):
			rowM+=(row[i]*M2[i])
		M.append(rowM)


	return M

def scaling(Xi,Yi,Sx,Sy):
	"""
	Performs scaling operation on x,y coordinates and returns
	scaled coordinates.
	"""
	Matrix=[[Sx,0,0],[0,Sy,0],[0,0,1]]	#Transformation for scaling
	Xf=[]
	Yf=[]
	for i in range(len(Xi)):
		Matrix2=[Xi[i],Yi[i],1]
		Xf.append(MatrixMultiply(Matrix,Matrix2)[0])	#Xf and Yf are the coordinate list of polygon after transformation
		Yf.append(MatrixMultiply(Matrix,Matrix2)[1])




	return Xf,Yf

def translation(Xi,Yi,dx,dy):
	Matrix=[[1,0,dx],[0,1,dy],[0,0,1]]		#Matrix of translation transformation
	Xf=[]
	Yf=[]
	for i in range(len(Xi)):
		Matrix2=[Xi[i],Yi[i],1]
		Xf.append(MatrixMultiply(Matrix,Matrix2)[0])
		Yf.append(MatrixMultiply(Matrix,Matrix2)[1])


	return Xf,Yf


def rotation(Xi,Yi,deg):		
	rad=pi*deg/180			#converting angle entered in degrees into radians

	Matrix=[[cos(rad),(-1)*sin(rad),0],[sin(rad),cos(rad),0],[0,0,1]]	#Matrix for rotation transformation
	Xf=[]
	Yf=[]
	for i in range(len(Xi)):
		Matrix2=[Xi[i],Yi[i],1]
		Xf.append(MatrixMultiply(Matrix,Matrix2)[0])
		Yf.append(MatrixMultiply(Matrix,Matrix2)[1])

	return Xf,Yf

"""
def showdisc():			#Takes queries to be performed on disc and ellipse and implements them using functions
	abr=input()
	a,b,r=list(map(float,abr.split(' ')))
	Centre=[a,b]			# Centre, width, height and angle are the attributes related to an ellipse.
	width=2*r
	height=2*r
	angle=0
	plt.ion()
	e1=Ellipse(Centre,width,height,fill=False)
	fig, ax=plt.subplots(subplot_kw={'aspect': 'equal'})
	ax.add_patch(e1)
	plt.plot()
	plt.pause(1)
	query=input()
	while(query!='quit'):
		flag=1
		if(query[0]=='T'):
			X=[Centre[0]]
			Y=[Centre[1]]
			Trans_Op=query.split(' ')
			xT,yT=float(Trans_Op[1]),float(Trans_Op[-1])
			NewX,NewY=translation(X,Y,xT,yT)		#Centre is translated to a new position
			Centre=[NewX[0],NewY[0]]
		elif(query[0]=='S'):
			X=[a+width/2,a,a-width/2,a] + Centre[0]		#X is a list having x coordinates of end points of major and minor axis
			Y=[b,b+height/2,b,b-height/2] + Centre[1]		#Y is a list having y coordinates of end points of major and minor axis
			Scale_Op=query.split(' ')
			xS,yS=float(Scale_Op[1]),float(Scale_Op[-1])
			NewX,NewY=scaling(X,Y,xS,yS)		#X and Y coordinates are scaled as per values entered
			width=sqrt((NewX[0]-NewX[2])**2 + (NewY[0]-NewY[2])**2)	#Length of new major axis
			height=sqrt((NewX[1]-NewX[3])**2 + (NewY[1]-NewY[3])**2)	#Length of new minor axis
			Centre=[NewX[4],NewY[4]]

		elif(query[0]=='R'):				#Rotates the degree argument of Ellips patch
			Rot_op=query.split(' ')
			deg=float(Rot_op[-1])
			angle+=deg
			X=[a+width/2,a,a-width/2,a] + Centre[0]		#X is a list having x coordinates of end points of major and minor axis
			Y=[b,b+height/2,b,b-height/2] + Centre[1]		#Y is a list having y coordinates of end points of major and minor axis
			Rot_Op=query.split(' ')
			deg=float(Rot_Op[1])
			NewX,NewY=scaling(X,Y,xS,yS)		#X and Y coordinates are scaled as per values entered
			width=sqrt((NewX[0]-NewX[2])**2 + (NewY[0]-NewY[2])**2)	#Length of new major axis
			height=sqrt((NewX[1]-NewX[3])**2 + (NewY[1]-NewY[3])**2)	#Length of new minor axis
			Centre=[NewX[4],NewY[4]]

		else:
			flag=0			#Flag is 1 when the query is right
			print("Wrong query")
			
		if(flag!=0):
			e1=Ellipse(Centre,width,height,fill=False, angle=angle)
			ax.add_patch(e1)
			plt.plot()
			plt.pause(2)
			query=input()

	return None
"""




def showpolygonordisc(figure):
	if(figure=='polygon'):
		X=list(map(float,input().split(' ')))	#X is the list of x coordinates of vertices of the polygon
		Y=list(map(float,input().split(' ')))	#Y is the list of y coordinates of vertices of the polygon
		X.append(X[0])
		Y.append(Y[0])
		
	if(figure=='disc'):
		Arg=list(map(float,input().split(' ')))
		Centre=[Arg[0],Arg[1]]
		r=Arg[2]
		major=2*r
		minor=2*r
		X=[]
		Y=[]
		theta=2*pi/500
		for i in range(501):
			x=r*cos(theta*i)
			y=r*sin(theta*i)
			X.append(x)
			Y.append(y)

	plt.ion()
	fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
	plt.plot(X,Y)
	plt.pause(1)


	query=input()
	while(query!='quit'):
		flag=1			#flag remains 1 while the queries are right
		if(query[0]=='S'):
			Scale_Op=query.split(' ')
			xS,yS=float(Scale_Op[1]),float(Scale_Op[-1])
			NewX,NewY=scaling(X,Y,xS,yS)			#Scaling function scales the original values by Sx and Sy.
		elif(query[0]=='R'):
			Rot_op=query.split(' ')
			deg=float(Rot_op[-1])
			NewX,NewY=rotation(X,Y,deg)			#NewX and NewY are the lists of coordinates after the implementation of transformation
		elif(query[0]=='T'):
			Trans_Op=query.split(' ')
			xT,yT=float(Trans_Op[1]),float(Trans_Op[-1])
			NewX,NewY=translation(X,Y,xT,yT)

		else:
			print("Wrong query")
			flag=0


		if(flag!=0):
			plt.plot(NewX,NewY)
			if(figure=='polygon'):
				print(NewX[:-1])		#Prints the new coordinates
				print(NewY[:-1])
			if(figure=='disc'):
				print(Centre)
			print()
			plt.pause(1)
			X=list(NewX)
			Y=list(NewY)

		
		query=input()
		

	"""
	Rotate_Op=input().split(' ')
	degree=float(Rotate_Op[1])
	NewX,NewY=rotation
	"""
	return None





Figure=input()
if(Figure=='polygon'):
	showpolygonordisc('polygon')
elif(Figure=='disc'):
	showpolygonordisc('disc')
else:
	print("Wrong figure entered")
	


