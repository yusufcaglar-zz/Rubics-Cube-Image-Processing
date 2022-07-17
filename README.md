# Rubics-Cube-Image-Processing

## PROBLEM
Taking photo of a rubic cube from 5 different views while 3 sides should be clearly visible at different light conditions. These 5 images should uploaded to GUI and then 2 pixels per color should be selected with a total of 12 pixels per image (6 colors).
Then with RGB masking same colors should be identified on the photo and must be depicted.
Later RGB to HIS conversion of the image is performed and again with masking, same colorsshould be identified on the photo and must be depicted.

## SOLUTION
I designed the GUI as asked and applied RGB masking to the images. At the end I found that this method is not very reliable because there were losses on color as depicted in below example.
![image](https://user-images.githubusercontent.com/37805650/179430049-cd8e1012-4c2e-4e86-a74c-d2d75d1a0223.png)
My GUI was disagned with grid, having 4 rows and 5 columns. First and third rows have only canvas while second and fourth row only having a label. I couldn’t get to RGB to HSI conversion of the image, so that part of the homework is unfortunately missing in my code.
