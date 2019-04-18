let style, video;
let output;
let transfer = false;
// let style_names = ['zaha','wave','udnie'];
// let styles = [];
// let style_index = 0;

function setup() {
  // put setup code here
  let cnv = createCanvas(640,480);
  cnv.parent('sketch-holder');
  video = createCapture(VIDEO);
  video.size(640,480);
  video.hide();

  // for(let i = 0; i < style_names.length; i++){
  //   let path = "../models/" + style_names[i];
  //   styles[i] = ml5.styleTransfer(path, video, function(){
  //     console.log(style_names[i] + "model is loaded");
  //   });
  // }
  style = ml5.styleTransfer("model", video, function(){
    console.log("model is loaded");
  });

  output = createImg('');
  output.hide();
}

function draw() {
  // put drawing code here

  if(style.ready && transfer){
    style.transfer(function(err, results){
      if(err){
        console.log("style transfer failed...");
      }else{
        output.attribute('src', results.src);
        console.log("transferred!");
      }
    });
  }

  if(transfer){
    image(output,0,0,640,480);
  }else{
    image(video,0,0);
  }

  //the error popup in class when the model is not ready
  //and the style transfer has started
}
function keyPressed(){
  if(key === ' '){
    transfer = !transfer;
    if(transfer){
      makeBoom();
    }
    else{
      removeBoom();
    }
  }
}

function makeBoom(){
  document.getElementById('sketch-holder').classList.remove('shaker');
  document.getElementById('sketch-holder').classList.add('shaker');

}

function removeBoom(){
  document.getElementById('sketch-holder').classList.remove('shaker');
}
