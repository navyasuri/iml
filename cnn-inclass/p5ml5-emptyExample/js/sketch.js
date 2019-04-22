let featureExtractor, classifier, video;
let labels=[];

function setup() {
  video = createCapture(VIDEO);
  createCanvas(640, 480);
  background(0);

  featureExtractor =ml5.featureExtractor("MobileNet", console.log("mobile net loaded"));
  featureExtractor.numClasses = 4;
  classifier = featureExtractor.classification(video, console.log(""));
  

  labels = ['Tree', 'NYU', 'Orange', 'kHeart'];

}


function draw() {
  
  if (ready2predict){
    classifier.classify(function(err, result){
      if(err){
        console.log(err);
      }
      else {
        label = result;
        console.log(result);
      }
    })
  }

}

function keyPressed(){
  if (key==='p' || key==='P'){
    ready2predict= !ready2predict;
  }

  if (key==='r'||key==='R'){
    classifier.addImage(labels[3], function(){
      console.log("label 3 added");
    });
  }

  if (key==='e'||key==='E'){
    classifier.addImage(labels[2], function(){
      console.log("label 2 added");
    });
  }

  if (key==='w'||key==='W'){
    classifier.addImage(labels[1], function(){
      console.log("label 1 added");
    });
  }

  if (key==='q'||key==='Q'){
    classifier.addImage(labels[0], function(){
      console.log("label 0 added");
    });
  }

  if (key==='t'||key==='T'){
    classifier.train(function(loss){
      console.log("loss is "+loss);
    });
    console.log("model is train(ing/ed)");
  }

}
