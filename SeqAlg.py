seq_1 = "CTTAG"
seq_2 = "GCTGAG"
baris = len(seq_1)+1
kolom = len(seq_2)+1
match = 6
mismatch = -2
gap = -6
align1=""
align2=""
matrix = [[[[None] for i in range(2)] for i in range(kolom)] for i in range(baris)]

#Initialize matrix
for i in range(kolom):
  matrix[0][i][0]=gap*i
  if(i>0):
    matrix[0][i][1]="hor"

for i in range(baris):
  matrix[i][0][0]=gap*i
  if(i>0):
    matrix[i][0][1]="ver"

for i in range(baris):
  print(str(matrix[i]))

#Fill the matrix
for i in range(1,baris):
  for j in range(1,kolom):
    hor=matrix[i][j-1][0]+gap
    ver=matrix[i-1][j][0]+gap
    if (seq_1[i-1]==seq_2[j-1]):
      diag=matrix[i-1][j-1][0]+match
    else:
      diag=matrix[i-1][j-1][0]+mismatch
    var = {hor:"hor",ver:"ver",diag:"diag"}
    hvd=[hor,ver,diag]
    matrix[i][j][0]=max(hvd)
    matrix[i][j][1]=var.get(max(var))
    #print(str(matrix))

for i in range(baris):
  print(str(matrix[i]))
    
k=baris
l=kolom
while(True):
  if(l==1 and k==1):
    break
  else:
    if(matrix[k-1][l-1][1]=="ver"):
      align1+=seq_1[k-2]
      align2+="-"
      k-=1
    elif(matrix[k-1][l-1][1]=="hor"):
      align1+="-"
      align2+=seq_2[l-2]
      l-=1
    elif (matrix[k-1][l-1][1]=="diag"):
      align1+=seq_1[k-2]
      align2+=seq_2[l-2]
      k-=1
      l-=1
      
align1=align1[::-1]
align2=align2[::-1]
print(align1)
print(align2)