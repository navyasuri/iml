# Emojify
## What is this?
Have you ever felt tired of your face on camera? Do you  feel the need to express yourself but without showing your face?
Great! This is the perfect solution to your problems. 
Meet Emojify! It uses machine learning to read your facial expression and understand what you are feeling. And using the magic of drawing, it covers your face with an emoji instead. Voila!

## Examples

## How it works
This project uses [face-api.js](https://github.com/justadudewhohacks/face-api.js?files=1) and [p5.js](http://p5js.org/). 
P5JS provides the video input the html canvas on which the video is displayed.
Face-api.js has various pre-trained models that can be used for different purposes. This project uses a mobilenet model trained with faces from the internet (the SsdMobileNetv1 model). Along with face expression classification, the api also provides a bounding box for the face, using the coordinates of which an emoji is drawn on top of the face. The model has seven choices of emotions - 
  - Neutral
  - Happy
  - Sad
  - Angry
  - Surprise
  - Fear
  - Disgust

Given an input video image, it recognises the face(s), reads the expression(s) and returns an Array of probabilities of each emotion. My code loops over this array, finds the maximum probability emotion. Then, using the x and y coordinates of the bounding box, my code as able to draw an image that is almost exactly over the face of the person. 

## Why I did this
This project was an assignment for the class Interactive Machine Learning at NYU Shanghai. The task was to use machine learning in some creative way with a pre-trained model. 
