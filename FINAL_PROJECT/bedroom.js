function createSingleBed(position){
    var options = THREE.DoubleSide;
      var bed = importObjMtl('assets/models/bed/room-bed.obj', 'assets/models/bed/room-bed.mtl', options, null);
      bed.scale.set(.22,.25,.27);
      //bed.scale.set(.1,.1,.1);
      bed.rotation.x = Math.PI/2;
      bed.position.set(position[0],position[1], position[2]);
      return bed;
  }

  function createArmadio(position){
    var options = THREE.DoubleSide;
      var bed = importObjMtl('assets/models/mobileAzzurro/mobileAzzurro.obj', 'assets/models/mobileAzzurro/mobileAzzurro.mtl', options, null);
      bed.scale.set(.1,.1,.1);
      bed.rotation.x = Math.PI/2;
      bed.position.set(position[0],position[1], position[2]);
      return bed;
  }
function createDoubleBed(position){
  var options = THREE.DoubleSide;
      var bed = importObjMtl('assets/models/bed/futon.obj', 'assets/models/bed/futon.mtl', options, null);
      bed.scale.set(.08,.08,.08);
      bed.position.set(position[0],position[1], position[2]);
      bed.rotation.x = Math.PI/2;
      return bed;

}
  function createDesk(position){
    var options = THREE.DoubleSide;
      var desk = importObjMtl('assets/models/scrivania/desk.obj', 'assets/models/scrivania/desk.mtl', options, null);
      desk.scale.set(10,10,10);
            desk.rotation.x = Math.PI/2;

      desk.position.set(position[0],position[1], position[2]);
      return position;

  }
  function createSamsung(position){
  var options = THREE.DoubleSide;
      var bed = importObjMtl('assets/models/samsung.obj', 'assets/models/samsung.mtl', options, null);
      bed.scale.set(.2,.4,.25);
      bed.position.set(position[0],position[1], position[2]);
      bed.rotation.x = Math.PI/2;
      return bed;

}