# Image Classification using ResNet50 pre-trained weight and web frontend
By Hide Inada

If you are a photographer, you may have seen AI-enabled auto-classification for tagging a photo when you upload a photo to a stock photo agency.
If you want to build a basic version of classification, you can do it with very little code.
I implemented an image classification that classifies a photo into 1000 classes. I used ResNet50 as the ML backend with pre-trained weights and used Flask as the web frontend.
ResNet50 model with pre-trained weights has 74.9% accuracy according to [a Keras's web page](https://keras.io/applications/) for predicting the top 1 object in a photo.
I ran the photos that I took by the system to see how it classifies. Please see the result at the end of this article.

## Deployed Instance
I deployed an instance on AWS and it is available for you to check out:

[http://ec2-3-83-93-180.compute-1.amazonaws.com:5000/](http://ec2-3-83-93-180.compute-1.amazonaws.com:5000/)

# How to use the deployed instance
When you access the above URL, you should see the below screen:
<IMG src="assets/images/initialscreen.png" height="400px">	

Drag & drop a photo from your file viewer (e.g. Finder) into the rectangular area.  Once the photo is dropped, it automatically uploads the image to my AWS instance for classification.  The result is returned on the same page so there is no need for you to do anything else.  If you want to try classifying more images, just hit the "Clear" button.

# Code
Entire code is checked in [https://github.com/hideyukiinada/ic/tree/master/web_app](https://github.com/hideyukiinada/ic/tree/master/web_app)
The key part of the code is where it loads the ResNet50 model and predicts classes:
[https://github.com/hideyukiinada/ic/blob/master/web_app/__init__.py](https://github.com/hideyukiinada/ic/blob/master/web_app/__init__.py)

## Samples of images
I used the photos from my portfolio to test how the classifier classifies my photos.

### Success cases
Classification for exotic animals and some household items worked well:

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
This is a picture of Sacramento River, but the system classified as the lake.  I think in this case, human would have guessed 
correctly because you can see the other side of the river, which would not be the case for a lake.

<IMG src="assets/images/river.png" height="400px">

The below picture has a flower, but the flower does not appear in the top 3. The vase does not have a narrow neck like a goblet, so the goblet is not right. Beaker would be wider than this. It still lists a vase on #3, so there is some hope.

<IMG src="assets/images/flowervase.png" height="400px">

