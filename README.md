# Image Classification using Resnet50 pre-trained weight and web frontend
By Hide Inada

If you are a photographer, you may have seen AI-enabled auto-classification for tagging a photo when you upload a photo to a stock photo agency.
If you want to build a basic version of classification, you can do it with very little code.
I implemented an image classification that classifies a photo into 1000 classes. I used ResNet50 as the ML backend with pre-trained weights and used Flask as the web frontend.
ResNet50 model with pre-trained weights has 74.9% accuracy according to [a Keras's web page](https://keras.io/applications/) for predicting the top 1 object in a photo.

## Samples of images
I used the photos from my portfolio to test how the classifier classifies my photos.

### Success cases
<IMG src="assets/images/lion.png" height="400px">	
<IMG src="assets/images/bear.png" height="400px">
<IMG src="assets/images/tiger.png" height="400px">
<IMG src="assets/images/espressodrink.png" height="400px">
<IMG src="assets/images/lamp.png" height="400px">	
<IMG src="assets/images/clock.png" height="400px">	
<IMG src="assets/images/toilet.png" height="400px">  

### Borderline case
<IMG src="assets/images/speedlimitsign.png" height="400px">

### Incorrect cases
This is a picture of Sacramento River, but the system classified as the lake.
<IMG src="assets/images/river.png" height="400px">
<IMG src="assets/images/flowervase.png" height="400px">

