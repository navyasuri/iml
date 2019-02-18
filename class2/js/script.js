let video;


function setup() {
    createCanvas(640, 480);

    video = createCapture(VIDEO);
    video.hide() // hides the html element
}

function draw() {
    // image(img, x, y, w, h)
    image(video, 0, 0); // Video gives an image every frame, display at given coords
}