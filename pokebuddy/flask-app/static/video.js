console.log("Video script loaded")

let video;
let poseNet; // This would be the machine learning model
let poses;
let imgs = [];

var cnv;

function setup() {
    cnv = createCanvas(640, 480);
    centerCanvas();

    video = createCapture(VIDEO);
    video.hide() // hides the html element

    options = {
        imageScaleFactor: 0.3,
        outputStride: 8,
        flipHorizontal: false,
        minConfidence: 0.25,
        scoreThreshold: 0.5,
        nmsRadius: 20,
        detectionType: 'single',
        multiplier: 0.75,
    }

    poseNet = ml5.poseNet(video, options, console.log("Model Loaded"));
    poseNet.detectionType = 'single';
    poseNet.on('pose', (results) => {
        poses = results; // store the trained data into poses 
    });
    // img = loadImage("0001.png");
}

function draw() {
    // image(img, x, y, w, h)
    translate(width, 0);
    scale(-1, 1);
    image(video, 0, 0); // Video gives an image every frame, display at given coords

    let sx, sy, ex, ey, rsx, rsy, rex, rey;
    if (poses != undefined) {

        for (let j = 0; j < poses[0].pose.keypoints.length; j++) { // Looping over the keypoints in each pose
            // console.log(poses[0].pose.keypoints[j].part);
            let p = poses[0].pose.keypoints[j];
            if (p.part == "leftShoulder") {
                sx = p.position.x;
                sy = p.position.y;
            }
            if (p.part == "leftEar") {
                ex = p.position.x; 
                ey = p.position.y; 
            }
            if (p.part == "rightShoulder") {
                rsx = p.position.x;
                rsy = p.position.y;
            }
            if (p.part == "rightEar") {
                rex = p.position.x; 
                rey = p.position.y; 
            }

            let lw = 2 * (ex - sx);
            let lh = 2 * (sy - ey);
            let ld = Math.min(abs(lw), abs(lh));
            // d = w;
            // if (abs(w)>=abs(h)) d = h;
            let lx = ex + ld;
            let ly = sy - ld;
            // console.log(x, y, w, h, ex, ey, sx, sy)
            // console.log(mouseX, mouseY);

            let rw = 2 * (rsx - rex);
            let rh = 2 * (rsy - rey);
            let rd = Math.min(abs(rw), abs(rh));
            let rx = rex - rd;
            let ry = rsy - rd;

            fill(255, 0, 0);
            // rect(x,y,-d,d);
            if (imgs.length != 0) {
                image(imgs[0], lx, ly, -ld, ld);
                image(imgs[1], rx, ry, rd, rd);
            }
        }
    }


}

// Canvas Centering
function centerCanvas() {
    var x = (windowWidth - width) / 2;
    var y = (windowHeight - height) / 2;
    cnv.position(x, y);
}

function windowResized() {
    centerCanvas();
}

// Loading image
function getImage(n1, n2, n3) {
    imgs = [loadImage("static/images/" + n1), loadImage("static/images/" + n2), loadImage("static/images/" + n3)];
    console.log(imgs);
}