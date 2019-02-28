let video;
let poseNet; // This would be the machine learning model
let poses;


function setup() {
    createCanvas(640, 480);

    video = createCapture(VIDEO);
    // video.hide() // hides the html element

    poseNet = ml5.poseNet(video, console.log("Model Loaded"));
    poseNet.on('pose', (results) => {
        poses = results; // store the trained data into poses 
    });
}

function draw() {
    // image(img, x, y, w, h)
    image(video, 0, 0); // Video gives an image every frame, display at given coords

    if (poses != undefined) {

        for (let i = 0; i < poses.length; i++) { // Looping over all the poses
            for (let j = 0; j < poses[i].pose.keypoints.length; j++) { // Looping over the keypoints in each pose
                console.log(poses[i].pose.keypoints[j].part);
                let x = poses[i].pose.keypoints[j].position.x; // x coord of part
                let y = poses[i].pose.keypoints[j].position.y; // y coord of part

                fill(255, 255, 0);
                noStroke();
                ellipse(x, y, 5, 5); // draw an ellipse at that point
            }
        }

    }
}

function modelLoaded() {
    console.log("Model Loaded");
}