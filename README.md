
# FaceSwap :zap:
FaceSwap as the name suggests is a face swapper that uses an object detection algorithm (Haar Cascade Classifier ) to detect faces on the webcam and swap them with another face! 

# About the project
This project uses a haar cascade classifier in order to detect all faces in real-time video and swap all the faces with a face of Keanu Revees xD

# Haar Cascade Classifier
 This is an object detection algorithm proposed by Viola and Jones that is used to detect facial features. The haar cascade classifier has 4 main stages  :
## A. Calculating haar features
 A feature is essentially calculations that are performed on adjacent rectangular regions at a specific location. The calculation involves the summation of pixel intensities at each region and the difference between their sums. Example of haar features:
![Haar features description](https://static-01.hindawi.com/articles/tswj/volume-2014/753860/figures/753860.fig.001.jpg)
## B. Creating Integral Images
For large images, the features can be hard to determine, and hence to reduce computational complexity we use integral images. An integral image is calculated from the original image in such a way that each pixel is the sum of all pixels lying to the left and above it in the original image. This means that the last pixel would basically be the sum of all pixels in the image. Most of the features will be irrelevant, hence AdaBoost is used to determine the relevant features

## C. AdaBoost Training
 AdaBoost essentially chooses the best features and trains the classifiers to use them. It uses a combination of weak learners to build a strong classifier
 
 ## D. Implementing a  Cascade Classifier
 The idea behind this is, not all the features need to run on each and every window. If a feature fails on a particular window, then we can say that the facial features are not present there. The cascade classifier is made up of a series of stages, where each stage is a collection of weak learners. Weak learners are trained using boosting, which allows for a highly accurate classifier from the mean prediction of all weak learners.

# To-Do

 - [ ] Add a CLI interface
 - [ ] Swap faces using a better algorithm

# Contributing Help

If you are really interested in contributing to the please follow the below steps and rules.
1. Fork the project :fork_and_knife: (Star :star: the repo before that :stuck_out_tongue:)
2. Clone it.
3. Build the project.
4. Look for any issues in the To-Do section.
5. Always create a new branch and work on the feature or bug. Check this if you are not that familiar with branching, [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
6. If you are using any other module for implementing any new features, please install the modules in the virtual environment and update them in the `requirements.txt` by using the below command.
```
pip freeze > requirements.txt
```

If you have any doubts or issues, let the maintainers know about it. They would be ready to help.

  
