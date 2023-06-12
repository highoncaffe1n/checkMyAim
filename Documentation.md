# Documentation
### Step 1: DATA CREATION
#### Setup:
1. Download ffmpeg to your local machine: https://ffmpeg.org/download.html
2. Copy the path of the bin folder form your local ffmpeg installation.
3. Insert the path on data_creation.py in ffmpegpath as a string like: ffmpegpath = 'C:\ffmpeg-2023-06-08-git-024c30aa3b-full_build\bin'
#### Usage:
1. Put a .mp4 file named input.mp4 into the data_creation directory.
2. Run data_creation.py, either in the IDE or with the command "$ Python data_creation.py" from within the directory.
3. You will get a video called output.mp4 which is input.mp4 scaled down to 18 fps and all the videos frames as images stored in the folder frames.
4. Copy the frames in to a different location to store them permanently and then delete the frames and output.mp4.
5. Now you can repeat this steps with a new input video.
### Step 2: BUILDING THE ENEMY DETECTION CASCADE CLASSIFIER
#### 1) Data sorting:
##### <u>negative images</u>
Negative images are images that do show, no enemy player model at all or a player model of a dead enemy.
##### <u>positive images</u>
Positive images show a variety of different situations, in which you can see an enemy player model like:
1. in the open
2. partly cover by an obstacle
3. crouching
4. falling
5. a Jett mid air
6. ...
##### Sorting the frames in negatives and positives
1. Download FastStone Image Viewer 7.7: https://www.faststone.org/FSIVDownload.htm
2. Create a folder and import all previous created images in there and create 2 empty folder called negative and positive.
3. Launch up FastStone and select the folder with the images. 
4. Go threw the images by using the arrow keys and if you want to move an image to the negative or positive folder press m and select the desired folder.