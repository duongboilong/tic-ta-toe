from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def Constant(imageName):
    image = np.array(Image.open(imageName))
    row = image.shape[0]
    col = image.shape[1]
    newRow =  int(row +200)
    newCol =  int(col +200)
    newImg = np.resize(image, (newRow,newCol,3))
    
    distanceRow = int((newRow-row)/2 +1)
    distanceCol = int((newCol-col)/2 +1)
    
    for i in range(newRow):
        for j in range (newCol):
            if (((i>=0) and (i< (newRow- row)/2)) or ((i>(row + (newRow- row)/2)) and (i< newRow))):
                for k in range (len(newImg[i][j])):
                    newImg[i][j][k] = 0
            else:
                if (((j>=0) and (j< (newCol- col)/2)) or ((j>(col + (newCol- col)/2)) and (j< newCol))):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = 0
                else:
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][j-distanceCol][k]
    print(newImg.shape)
    return newImg

def Wrap(imageName):
    image = np.array(Image.open(imageName))
    row = image.shape[0]
    col = image.shape[1]
    newRow =  int(row +200)
    newCol =  int(col +200)
    newImg = np.resize(image, (newRow,newCol,3))
    
    distanceRow = int((newRow-row)/2 +1)
    distanceCol = int((newCol-col)/2 +1)
    
    for i in range(newRow):
        for j in range (newCol):
            
            #truong hop hang tren cung
            if ((i>=0) and (i< (newRow- row +1)/2)):
                
                #goc 1 
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row-(distanceRow-i)][col-(distanceCol-j)][k]
                #goc 3
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row-(distanceRow-i)][j-col-distanceCol][k]
                #goc 2
                else :
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row-(distanceRow-i)][j-distanceCol][k]
                        
            #truong hop hang duoi cung
            elif ((i>(row + (newRow- row)/2)) and (i< newRow)):
                
                #goc 7
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-row-distanceRow][col-(distanceCol-j)][k]
                #goc 9
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-row-distanceRow][j-col-distanceCol][k]
                #goc 8
                else :
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-row-distanceRow][j-distanceCol][k]
            
            #truong hop giua 
            else:
                #goc 4
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][col-(distanceCol-j)][k]
                #goc 5
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][j-col-distanceCol][k]
                #goc 6
                else :
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][j-distanceCol][k]
    print(newImg.shape)
    return newImg
    
def Reflect(imageName):
    image = np.array(Image.open(imageName))
    row = image.shape[0]
    col = image.shape[1]
    newRow =  int(row +200)
    newCol =  int(col +200)
    newImg = np.resize(image, (newRow,newCol,3))
    
    distanceRow = int((newRow-row)/2 +1)
    distanceCol = int((newCol-col)/2 +1)
    
    for i in range(newRow):
        for j in range (newCol):
            #truong hop hang tren cung
            if ((i>=0) and (i< (newRow- row +1)/2)):
                #goc 1 
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[distanceRow - i][distanceCol-j][k]
                #goc 3
                elif ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[distanceRow - i][col - (j-distanceCol)][k]
                #goc 2
                else:
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[distanceRow - i][j-distanceCol][k]
            #truong hop hang duoi cung
            elif ((i>(row + (newRow- row +1)/2)) and (i< newRow)):
                
                #goc 7
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row - (i-distanceRow)][distanceCol-j][k]
                #goc 9
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row - (i-distanceRow)][col - (j-distanceCol)][k]
                #goc 8
                else :
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row - (i-distanceRow)][j-distanceCol][k]
            #truong hop giua 
            else:
                #goc 4
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][distanceCol-j][k]
                #goc 5
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][col - (j-distanceCol)][k]
                #goc 6
                else:
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][j-distanceCol][k]
    print(newImg.shape)
    return newImg

    
def Replicate(imageName):
    image = np.array(Image.open(imageName))
    row = image.shape[0]
    col = image.shape[1]
    newRow =  int(row +200)
    newCol =  int(col +200)
    newImg = np.resize(image, (newRow,newCol,3))
    
    distanceRow = int((newRow-row)/2 +1)
    distanceCol = int((newCol-col)/2 +1)
    
    for i in range(newRow):
        for j in range (newCol):
            #truong hop hang tren cung
            if ((i>=0) and (i< (newRow- row +1)/2)):
                #goc 1 
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[0][distanceCol-j][k]
                #goc 3
                elif ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[0][col - (j-distanceCol)][k]
                #goc 2
                else:
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[0][j-distanceCol][k]
            #truong hop hang duoi cung
            elif ((i>(row + (newRow- row )/2)) and (i< newRow)):
                
                #goc 7
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row -1][distanceCol-j][k]
                #goc 9
                elif  ((j>(col + (newCol- col)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row - 1][col - (j-distanceCol)][k]
                #goc 8
                else :
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[row - 1][j-distanceCol][k]
            #truong hop giua 
            else:
                #goc 4
                if ((j>=0) and (j< (newCol- col +1)/2)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][0][k]
                #goc 5
                elif  ((j>(col + (newCol- col +1)/2)) and (j< newCol)):
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][col - 1][k]
                #goc 6
                else:
                    for k in range (len(newImg[i][j])):
                        newImg[i][j][k] = image[i-distanceRow][j-distanceCol][k]
    print(newImg.shape)
    return newImg

reflectIMG = Reflect("kmean.png")
WrapIMG = Wrap("kmean.png")
replicateIMG = Replicate("kmean.png")
constantIMG = Constant("kmean.png")
originIMG =  np.array(Image.open("kmean.png"))

# create figure
fig = plt.figure(figsize=(10, 7))
  
# setting values to rows and column variables
rows = 2
columns = 3

fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(originIMG)
plt.title("Origin")
  

# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(replicateIMG)
plt.title("replicate")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 3)
  
# showing image
plt.imshow(reflectIMG)
plt.title("Reflect")
  
# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 4)
  
# showing image
plt.imshow(WrapIMG)
plt.title("Wrap")
  
# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 5)
  
# showing image
plt.imshow(constantIMG)
plt.title("Constant")
    
