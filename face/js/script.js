let video;
let poseNet; // This would be the machine learning model
let poses;
let emojis = [];
let neutral;
// import FaceExpressionNet from 'lib/faceapi'
// let net = FaceExpressionNet();
// console.log(net);


function setup() {
    createCanvas(1280, 720);
    background(255);
    video = createCapture(VIDEO);
    video.hide() // hides the html element

    for(let i = 0; i<7; i++){
        emojis.push(loadImage('img/'+i.toString()+'.png'));
    }

    // poseNet = ml5.poseNet(video, console.log("Model Loaded"));
    // poseNet.on('pose', (results) => {
    //     poses = results; // store the trained data into poses 
    // });

    faceapi.load
    faceapi.loadSsdMobilenetv1Model('/models')
    faceapi.loadFaceExpressionModel('/models');
    console.log(faceapi.nets)

}

function draw() {
    // background(0);
    // image(img, x, y, w, h)
    // image(video, 0, 0); // Video gives an image every frame, display at given coords
    // console.log(video.elt)

    const detectionsWithExpressions = faceapi.detectSingleFace(video.elt).withFaceExpressions()
        .then((detectionsWithExpressions) => {

            console.log(detectionsWithExpressions);

            let bestExpr = "";
            let max = 0;


            if (detectionsWithExpressions == undefined) {
                console.log("No face detected");
                // bestExpr = "neutral";
                // max = 1;
                background(255);
                image(video, 0, 0);
            }
            else {
                let face = detectionsWithExpressions.detection;
                let exprs = detectionsWithExpressions.expressions;
                for (let i = 0; i < exprs.length; i++) {
                    if (exprs[i].probability > max) {
                        max = exprs[i].probability;
                        bestExpr = exprs[i].expression;
                        bestImg = emojis[i];
                    }
                }

                let small = Math.max(face.box.width, face.box.height);
                background(255);
                image(video, 0, 0);
                image(bestImg, face.box.x, face.box.y, small, small);
                // console.log(neutral, face.box.x, face.box.y, small, small);
                console.log(bestExpr);
            }
                

            });


    // if (poses != undefined) {

    //     for (let i = 0; i < poses.length; i++) { // Looping over all the poses
    //         for (let j = 0; j < poses[i].pose.keypoints.length; j++) { // Looping over the keypoints in each pose
    //             console.log(poses[i].pose.keypoints[j].part);
    //             let x = poses[i].pose.keypoints[j].position.x; // x coord of part
    //             let y = poses[i].pose.keypoints[j].position.y; // y coord of part

    //             fill(255, 255, 0);
    //             noStroke();
    //             ellipse(x, y, 5, 5); // draw an ellipse at that point
    //         }
    //     }

    // }
}

function modelLoaded() {
    console.log("Model Loaded");
}