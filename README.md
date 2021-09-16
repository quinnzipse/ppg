# Python rPPG Implementation 
By: Quinn Zipse

## Vision
The goal of this project is to be able to make an application that can obtain an accurate heartrate of a subject using a webcam with ambient light.

## Progress Made
I have created a system that:
1. Identifies a face (shown with a circle)
2. Waits for the subject to stand still (Indicated by the color of the circle)
3. Identifies the region of interest (the subject's forehead) and obtains a histogram of the corresponding subimage.
4. Displays histogram of the region of interest.

## Challenges
Here are some things found in preliminary research that will pose a challenge:
1. Using optical flow to track ROI
2. Filtering out noise from retrieved signal
3. Detrending the signal
4. Frequency estimation to evaluate heartrate

## Resources
Original article referenced before beginning project:
https://pubmed.ncbi.nlm.nih.gov/17322588/ 

I found a YouTube video demonstrating an existing implementation for rPPG:
https://www.youtube.com/watch?v=D_KYv7pXAvQ 

Resources cited in the decription of the video led me to this article which I used as my "preliminary research":
https://link.springer.com/chapter/10.1007/978-3-319-41402-7_20 

## How to run program

To run the code, install required dependancies:

```pip3 install -r requirements.txt```

Then, use the `python3` command to run the file:

```python3 detect.py```