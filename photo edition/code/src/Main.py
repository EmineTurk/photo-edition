inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_imagefile(f):
    qualities=f.readline().rstrip()
    newqu=qualities.split()
    sutun,satir=newqu[1],newqu[2]
    max=newqu[3]
    rest=f.read()
    pixels=rest.split()
    counter=0
    img_matrix=[]
    for c in range(int(satir)):
        rows=list()
        for b in range(int(sutun)):
            rows.append(pixels[counter])
            counter+=1
        img_matrix.append(rows)
    return img_matrix
def write_imagefile(f,img_matrix):
    f.write("P2"+' ')
    f.write(str(len(img_matrix[0]))+' ')
    f.write(str(len(img_matrix))+' ')
    f.write("255\n")
    for i in range(len(img_matrix)):
        for z in range(len(img_matrix[0])-1):
            f.write(str(img_matrix[i][z])+' ')
        f.write(str(img_matrix[i][-1]))
        f.write('\n')

def misalign(img_matrix):
    liste=[]
    for i in img_matrix:
        a=i.copy()
        liste.append(a)
    for a in range(len(img_matrix[0])):
        for b in range(len(img_matrix)):
            if a%2==1:
                liste[b][a]=img_matrix[(-1*b)-1][a]

    return liste
def sort_columns(img_matrix):
    listem=[]
    for i in range(len(img_matrix[0])):
        newlist=[]
        for b in range(len(img_matrix)):
            newlist.append(int(img_matrix[b][i]))
        newlist.sort()
        listem.append(newlist)
    for z in range(len(img_matrix[0])):
        for t in range(len(img_matrix)):
            img_matrix[t][z]=listem[z][t]
    return img_matrix




def sort_rows_border(img_matrix):
    listem=[]
    for i in img_matrix:
        liste=[]
        for c in i:
            liste.append(int(c))
        listem.append(liste)
    legendlist=[]
    for z in listem:
        newlist = []
        listetut = []
        if 0 not in z:
            z.sort()
            for elem in z:
                newlist.append(str(elem))
            legendlist.append(newlist)
        else:
            for i in range(len(img_matrix[0])):
                if z[i]!=0:
                    listetut.append(z[i])
                if z[i]==0 and z[i-1]!=0:
                    a=sorted(listetut)
                    for elem in a:
                        newlist.append(str(elem))
                    newlist.append(str(z[i]))
                    listetut=[]
                if z[i]==0 and z[i-1]==0:
                    newlist.append(str(z[i]))
                    listetut=[]
            listetut.sort()
            for elem in listetut:
                newlist.append(str(elem))
            legendlist.append(newlist)

    return legendlist


def convolution(img_matrix,kernel):
    listem=[]
    for i in img_matrix:
        a=i.copy()
        listem.append(a)
    listeasil=[]
    for b in listem:
        listecik=[]
        for c in b:
            listecik.append(int(c))
        listeasil.append(listecik)
    for d in listeasil:
        d.insert(0,0)
        d.insert(len(d),0)
    listeyeni=[[0]*(len(img_matrix[0])+2)]+listeasil+[[0]*(len(img_matrix[0])+2)]
    for a in  range(1,(len(listeyeni))-1):
        for b in range(1,(len(listeyeni[0])-1)):
            sum=0
            sum+=listeyeni[a][b]*kernel[1][1]+listeyeni[a-1][b-1]*kernel[0][0]+listeyeni[a-1][b]*kernel[0][1]+listeyeni[a-1][b+1]*kernel[0][2]+listeyeni[a][b-1]*kernel[1][0]
            sum+=listeyeni[a][b+1]*kernel[1][2]+listeyeni[a+1][b-1]*kernel[2][0]+listeyeni[a+1][b]*kernel[2][1]+listeyeni[a+1][b+1]*kernel[2][2]
            if sum<0:
                sum=0
            if sum>=255:
                sum=255
            img_matrix[a-1][b-1]=str(sum)
    return img_matrix


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
