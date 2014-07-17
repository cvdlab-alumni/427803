function importObjMtl(obj, mtl, doubleSide, transformObject) {
	var container = new THREE.Object3D();
	var loader = new THREE.OBJMTLLoader();
	loader.addEventListener('load', function(event) {
		var object = event.content;
		if (doubleSide) {
			object.traverse(function(child) {
				if (child instanceof THREE.Mesh) {
					child.material.side = THREE.DoubleSide;
				}
			});
		}
		if (transformObject) {
			transformObject(object);
		}
		container.add(object);
	});
	loader.load(obj,mtl);
	return container;
}

function importObj (obj) {
	var container = new THREE.Object3D(); 
  	loader = new THREE.OBJLoader();
    loader.load(obj, function (obj) {
    	global_o = obj;
        var multiMaterial = [
          new THREE.MeshLambertMaterial({color: 0x990000, metal: true })
        ];
        mesh = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);
        container.add(mesh);
    });
    return container;
}