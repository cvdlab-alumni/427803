
	function createLavabo(position){
		var options = THREE.DoubleSide;
    	var lavabo = importObjMtl('assets/models/bathroom_vanity/bathroom_vanity.obj', 'assets/models/bathroom_vanity/bathroom_vanity.mtl', options, null);
    	lavabo.scale.set(12,12,12);
    	lavabo.rotation.x = Math.PI/2;
    	 lavabo.position.set(position[0],position[1], position[2]);

    	//lavabo.position.set(50,80,3);
    	return lavabo;
	}

	function createShower(position){
		var options = THREE.DoubleSide;
      var shower = importObjMtl('assets/models/shower.obj', 'assets/models/shower.mtl', options, null);
      shower.scale.set(0.09,0.09,0.09);
      shower.rotation.x = Math.PI/2;
       shower.position.set(position[0],position[1], position[2]);
       return shower;

	}

	function createWc(position){
		var options = THREE.DoubleSide;

		var wc = importObjMtl('assets/models/wc/wc.obj', 'assets/models/wc/wc.mtl', options, null);
      	wc.scale.set(.4,.4,.4);
      	wc.position.set(position[0],position[1], position[2]);
      	wc.rotation.x = Math.PI/2;
      	return wc;

	}
	