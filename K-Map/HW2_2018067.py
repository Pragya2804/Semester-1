# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Pragya Sethi
# Roll Number: 2018067
# Section: A
# Group: 3
# Date: 13-10-18

def MakeBinary(l1,n):		#Function to convert elements of a string l1(Ones and Don't Cares) from decimal to binary. n is the number of variables
	binary=[]
	D={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','10':'1010','11':'1011','12':'1100','13':'1101','14':'1110','15':'1111'}
	for x in l1:
		if(n==2):
			binary.append('--'+D[x][2:])
		if(n==3):
			binary.append('-'+D[x][1:])
		if(n==4):
			binary.append(D[x])
	return binary

def isadjacent(a1,a2):		#Checks if two implicants are adjacent or not.
	difference=0
	for i in range(4):
		if(a1[i]!=a2[i]):
			difference+=1	
	if(difference==1):		#Adjacent if the values differ only by one digit as in grey code. eg 0110, 0010 or --10, --11
		return True
	else:
		return False

def minimize(m1,m2):	#Replaces non matching values with '-'. Eg 0110,0010 becomes 0-10
	minimized=''
	for i in range(4):
		if(m1[i]!=m2[i]):
			minimized+='-'
		else:
			minimized+=m1[i]
	return minimized


def simplify(l2,N):		#Simplifies till Quine-McCluskey table
#	print("Entered ", l2)
#	print("Entered ", N)
	net_term=[]				#Corresponds to lists of list of combined minterms
	netbinary_term=[]		#Binary combinations corresponding to combined minterms in terms of 0,1 and -
	included=[]
	for i in range(len(l2)):
		for j in range(i+1, len(l2)):
			join=[]
			if(isadjacent(l2[i],l2[j])==True):
				netbinary_term.append(minimize(l2[i],l2[j]))
				included.append(i)
				included.append(j)
				join=N[i]+N[j]
				net_term.append(join)
#	print(included)

	for k in range(len(l2)):						#Loop to include uncombined terms
		if((k in included) == False):
			netbinary_term.append(l2[k])
			net_term.append(N[k])

	for t in netbinary_term:						#Loop to remove repeated terms
		occurrence=netbinary_term.count(t)
		for i in range(occurrence-1):
			index=netbinary_term.index(t)
			netbinary_term.pop(index)
			net_term.pop(index)

#	print("Simplified ",netbinary_term)
#	print("Simplified ",net_term)
	return(net_term,netbinary_term)

def postulates(P):
	#XX=X
	NewP=[]
	#print("initial P ",P)
	for x in P:
		element=''
		#print("original x ",x)
		for y in x:
			c=x.count(y)
			if(c>1):			#If 113 is there, it gets converted to 13 since xx=x
				i=x.index(y)
				x=x[:i] + x[i+1:]

		element=x
		NewP.append(element)
		#print("After postulate ",x)

	#print("Final after first postulate ",NewP)
	#print("Next Distribution")
	
	#X+X=X
	
	SortList=[]
	for x in NewP:
		listelement=[]
		for i in x:
			listelement.append(i)
		listelement.sort()
		SortList.append(listelement)

	for x in SortList:
		c=SortList.count(x)
		if(c>1):					#If there is 123 and 213 combination, they get sorted to 123 and one existence is removed
			i=SortList.index(x)
			SortList.pop(i)
			NewP.pop(i)

	#print("Final P after second postulate ", NewP)


	return NewP





def distribute(P1,P2):
	STEP1=[]
	for x in P1:
		for y in P2:
			STEP1.append(x+y)	#Multiplies one POS with another to get SOP
	#print(STEP1)
	STEP2=postulates(STEP1)		#Simplified using the postulate function
	return STEP2



def getexp(ZerosOnes,n):		#Converts the expressions in 0,1,- to variables w,x,y,z. Here n is the number of variables
	expr=''
	if(n==4):					#for example 0110 gets converted to w'xyz'
		if(ZerosOnes[0]=='0'):
			expr+='w\''
		if(ZerosOnes[0]=='1'):
			expr+='w'
		if(ZerosOnes[1]=='0'):
			expr+='x\''
		if(ZerosOnes[1]=='1'):
			expr+='x'
		if(ZerosOnes[2]=='0'):
			expr+='y\''
		if(ZerosOnes[2]=='1'):
			expr+='y'
		if(ZerosOnes[3]=='0'):
			expr+='z\''
		if(ZerosOnes[3]=='1'):
			expr+='z'
		if(ZerosOnes[0]==ZerosOnes[1]==ZerosOnes[2]==ZerosOnes[3]=='-'):
			expr='1'
	elif(n==3):
		if(ZerosOnes[1]=='0'):
			expr+='w\''
		if(ZerosOnes[1]=='1'):
			expr+='w'
		if(ZerosOnes[2]=='0'):
			expr+='x\''
		if(ZerosOnes[2]=='1'):
			expr+='x'
		if(ZerosOnes[3]=='0'):
			expr+='y\''
		if(ZerosOnes[3]=='1'):
			expr+='y'
		if(ZerosOnes[0]==ZerosOnes[1]==ZerosOnes[2]==ZerosOnes[3]=='-'):
			expr='1'
	else:
		if(ZerosOnes[2]=='0'):
			expr+='w\''
		if(ZerosOnes[2]=='1'):
			expr+='w'
		if(ZerosOnes[3]=='0'):
			expr+='x\''
		if(ZerosOnes[3]=='1'):
			expr+='x'
		if(ZerosOnes[0]==ZerosOnes[1]==ZerosOnes[2]==ZerosOnes[3]=='-'):
			expr='1'


	return expr




def minFunc(numVar, stringIn):
	terms=stringIn.split('d')
	Ones=terms[0][1:-1].split(',')				#List of number of ones minterm eg ['4','8','5'] in (4,8,5)d(9,14)
	if('-' in terms[-1]):
		DontCare=[]
	else:
		DontCare=terms[1][1:-1].split(',')			#List of number of ones minterm e.g ['9','14']
	

	#print(Ones)
	#print(DontCare)
	Net=[]									#It will be the list of lists corresponding to minimized values [['4','8','5'],['4','5'],['8']]
	ZeroCube=[]								#First indivisual blocks including both ones and don't cares
	for x in Ones:
		ZeroCube.append([x])
	for x in DontCare:
		ZeroCube.append([x])
	Net.append(ZeroCube)
	NetBinary=[MakeBinary((Ones+DontCare),numVar)] #Binary form of numbers in Net list
	


	for x in range(numVar):
		(NetTerm, NetBinaryTerm)=simplify(NetBinary[x],Net[x])
		Net.append(NetTerm)
		NetBinary.append(NetBinaryTerm)

	#print(Net[-1])
	#print(NetBinary[-1])

	Petrick=[] #List of combinations corresponding to ones to get Essential Prime Implicants

	for x in Ones:
		POS=[]
		for i in range(len(Net[-1])):
			if((x in Net[-1][i]) == True):	
				POS.append(str(i))
		Petrick.append(POS)		#Combination in POS form eg (K+L)(K+M)(L+N)

	#print(Petrick)
		
	SOP=[]
	if(len(Petrick)>1):
		for i in range(len(Petrick)-1):		#Loop to distribute terms in POS form to get an SOP expression
			if(i==0):
				SOP=distribute(Petrick[0],Petrick[1])
			else:
				SOP=distribute(SOP,Petrick[i+1])
	else:
		SOP=Petrick

	#print(SOP)

	minimum=len(Net[-1])		#In Petrich's algorithm, term with minimum prime implicants combination forms the set of EPIs
	for x in SOP:
		if(len(x)<minimum):
			minimum=len(x)

	PossibleAns=[]				#List of all possible combinations of Essential Prime Implicants
	for k in SOP:
		if(len(k)==minimum):
			PossibleAns.append(k)

	#print(PossibleAns)

	Ans=[]						#List of all EPI combination in terms of variables w,x,y,z
	for x in PossibleAns:
		OneAns=[]
		for i in x:
			OneAns.append(getexp(NetBinary[-1][int(i)],numVar))
		OneAns.sort()
		#print(OneAns)
		Ans.append(OneAns)
	Ans.sort()					#Sorted lists to produce ans in lexographic order
	#print(Ans)

	AnsString=''
	for j in range(len(Ans)):
		if(j!=0):
			AnsString=AnsString+' OR '
		for i in range(len(Ans[j])):
			if(i==0):
				AnsString+=Ans[j][0]
			else:
				AnsString=AnsString+'+'+Ans[j][i]

	return AnsString

	



#print(minFunc(4,'(4,8,10,11,12,15)d(9,14)'))
#print(minFunc(4,'(4,8,10,11)d(9,14)'))
#print(minFunc(3,'(0,1,2,5,6,7)d-'))
#print(minFunc(3,'(0,1,2,5)d(3,4,6,7)'))
#print(minFunc(2,'(0)d(3)'))
#print(minFunc(3,'(1)d-'))