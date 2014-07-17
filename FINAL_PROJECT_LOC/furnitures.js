function createPicture (w,h, position){

      // create the picture
      var planeGeometry = new THREE.PlaneGeometry(w,h);
      var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
           specular: 0xffffff, shininess: 10, shading: THREE.SmoothShading });
      //var plane = new THREE.Mesh(planeGeometry,planeMaterial);

      var planeTexture = createMesh(new THREE.PlaneGeometry(w, h), "quadro.png", "cornice-bump.png", 0.9);

      planeTexture.position.set(position[0], position[1], position[2]);

      return planeTexture;
  }

  var texture;
var $video = $('#video');
var video = $video[0];
video.play();
texture = new THREE.Texture(video);
texture.minFilter = THREE.LinearFilter;
texture.magFilter = THREE.LinearFilter;
texture.format = THREE.RGBFormat;
texture.generateMipmaps = false;

var video_material = new THREE.MeshBasicMaterial({
  map: texture,
  shininess: 100
});

function createTvScreen () {
  var tvScreenGeometry = new THREE.PlaneGeometry(13, 8);
  var tvScreen = new THREE.Mesh(tvScreenGeometry, video_material);
  tvScreen.position.set(0, 3, 3);
  tvScreen.rotation.x =Math.PI / 2;
  tvScreen.visible = true;
  tvScreen.isOn = true;
  tvScreen.interact = function() {
    if (this.isOn) {
      video.pause();
      tvScreen.visible = false;
      //tvScreen.children[0].intensity = 0;
      this.isOn = false;
    } else {
      tvScreen.visible = true;
      video.play();
      //tvScreen.children[0].intensity = 4;
      this.isOn = true;
    }
  }
  //toIntersect.push(tvScreen);
  return tvScreen;
}

function createTV(position){
   var options = THREE.DoubleSide;

      var tv = importObjMtl('assets/models/tv.obj', 'assets/models/tv.mtl', options, null);
      //tv.rotation.x =Math.PI / 2;
      var screenTv = createTvScreen();
      tv.scale.set(2,1.8,1.8);
      tv.position.set(0, -7, -.81);
      screenTv.add(tv);
      screenTv.position.set(position[0], position[1], position[2])
      screenTv.scale.set(1,.9,.9);
      return screenTv;


}

function createMac(position){
  var options = THREE.DoubleSide;
      var mac = importObjMtl('assets/models/apple_pc/apple_pc.obj', 'assets/models/apple_pc/apple_pc.mtl', options, null);
      mac.scale.set(1.5,1.5,1.5);
      mac.rotation.x = Math.PI/2;
      mac.position.set(position[0], position[1], position[2]);
      return mac;


}

function createChair(position){
  var options = THREE.DoubleSide;
      var chair = importObjMtl('assets/models/chair.obj', 'assets/models/chair.mtl', options, null);
      chair.scale.set(12,12,12);
      chair.rotation.x = Math.PI/2;

      chair.position.set(position[0], position[1], position[2]);
      return chair;

}