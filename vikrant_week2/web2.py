coll1={
	0:'',
	2:'twenty',
	3:'thirty',
	4:'fourty',
	5:'fifty',
	6:'sixty',
	7:'seventy',
	8:'eighty',
	9:'ninety'
}
coll2={
	0:'',
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine'
}
stri=''
for i in range(10):
	for j in range(10):
		if i==1:
			stri+='teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen'
		else:
			stri+=coll1[i]+coll2[j]
stri+='hundred'

print len(stri)
