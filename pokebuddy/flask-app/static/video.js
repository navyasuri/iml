console.log("Video script loaded")

let video;
let poseNet; // This would be the machine learning model
let poses;
let img;

var cnv;

function setup() {
    cnv = createCanvas(640, 480);
    centerCanvas();

    video = createCapture(VIDEO);
    video.hide() // hides the html element

    poseNet = ml5.poseNet(video, console.log("Model Loaded"));
    poseNet.detectionType='single';
    poseNet.on('pose', (results) => {
        poses = results; // store the trained data into poses 
    });
    img = loadImage("0001.png");
}

function draw() {
    // image(img, x, y, w, h)
    translate(width, 0);
    scale(-1, 1);
    image(video, 0, 0); // Video gives an image every frame, display at given coords

    if (poses != undefined) {
        let sx, sy, ex, ey;
        for (let j = 0; j < poses[0].pose.keypoints.length; j++) { // Looping over the keypoints in each pose
            // console.log(poses[0].pose.keypoints[j].part);
            let p = poses[0].pose.keypoints[j]
            if (p.part == "leftShoulder") {
                sx=p.position.x; // x coord of part
                sy=p.position.y; // y coord of part 
                // fill(255, 255, 0);
                // noStroke();
                // ellipse(sx, sy, 5, 5); // draw an ellipse at that point
            }
            if (p.part=="leftEar"){
                ex=p.position.x; // x coord of part
                ey=p.position.y; // y coord of part
                // fill(255, 255, 0);
                // noStroke();
                // ellipse(ex, ey, 5, 5)
            }
            
            w = 2* (ex-sx);
            h = 2* (sy-ey);
            let d = Math.min(abs(w), abs(h));
            // d = w;
            // if (abs(w)>=abs(h)) d = h;
            x = ex + d;
            y = sy - d;
            console.log(x, y, w, h, ex, ey, sx, sy)
            // console.log(mouseX, mouseY);
            
            fill(255, 0, 0);
            // rect(x,y,-d,d);
            image(img, x, y, -d, d)
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
function getImage(num){
    img = loadImage("static/images/"+num);
}