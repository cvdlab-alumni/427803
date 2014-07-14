     function createMesh(geom, imageFile, bump, scale) {
            var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
            geom.computeVertexNormals();
            var mat = new THREE.MeshPhongMaterial();
            mat.map = texture;

            if (bump&&scale) {
              var bump = THREE.ImageUtils.loadTexture("assets/textures/general/" + bump)
              mat.bumpMap = bump;
              mat.bumpScale = scale;
            }

            var mesh = new THREE.Mesh(geom, mat);

            return mesh;
      }

 	function createFloorTextureExt (height, weight, position){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 30, shading: THREE.SmoothShading, side: THREE.DoubleSide});

            //var plane = new THREE.Mesh(planeGeometry,planeMaterial);

            var plane = createMesh(planeGeometry, "parquet.jpg");

            plane.position.set(position[0]+weight/2+3, position[1]+height/2, position[2]);

            return plane;

        }

 function createBathWall (height, weight, position){
 			var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 15, shading: THREE.SmoothShading, side: THREE.DoubleSide});
        	var plane = createMesh(planeGeometry, "bath-big.png", "bath-big-bump.png", 0.09);
			
			plane.position.set(position[0], position[1], position[2]);

			return plane;


		}

 function createBathFloor (height, weight, position){
 			var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 15, shading: THREE.SmoothShading, side: THREE.DoubleSide});
        	var plane = createMesh(planeGeometry, "floor-bath.jpg", "floor-bath-bump.jpg", 0.1);
			
			plane.position.set(position[0]+weight/2+3, position[1]+height/2, position[2]);

			return plane;

 }	

 function createEntryDoor (weight, position){
            var doorGeometry = new THREE.BoxGeometry(weight,22,1.4);
            var doorGeometryB = new THREE.BoxGeometry(weight, 22, 0.1);
            var isClosed = true;
            var door = createMesh(doorGeometry, "entry-door.jpg", "entry-door-bump.jpg", 0.1);
            var doorB = createMesh(doorGeometryB, "entry-door-back2.jpg", "entry-door-back-bump.jpg", 0.1);

            door.rotation.x = Math.PI/2;
            doorB.rotation.x = Math.PI;
            doorB.rotation.z = Math.PI;
            doorB.position.set(0,0,-.7);

            door.add(doorB);
            door.position.x = 8.5;

            var joint = new THREE.Object3D;

            joint.add(door);
            joint.position.set(position[0],position[1],position[2]);

            door.interact = function(){
               if(!isClosed){
                       if (reverse===1){
                               new TWEEN.Tween(joint.rotation)
                               .to({z: -Math.PI/2},1000)
                               .start();
                       } else {
                               new TWEEN.Tween(joint.rotation)
                               .to({z: Math.PI/2},1000)
                               .start();
                       }
                       
                       isClosed=true;
               } else {
                       new TWEEN.Tween(joint.rotation)
                       .to({z: 0},1000)
                       .start();
                       isClosed=false;
               }



 }
             return joint;

}


 function createStandardDoor (weight, position){
            var doorGeometry = new THREE.BoxGeometry(weight,22,0.9);
            var doorGeometryB = new THREE.BoxGeometry(weight, 22, 0.1);
           
            var door = createMesh(doorGeometry, "modern-door.jpg", "modern-door-bump.jpg", 0.1);
            var doorB = createMesh(doorGeometryB, "intern-door-back.jpg");

            

            door.rotation.x = Math.PI/2;
            doorB.rotation.x = Math.PI;
            doorB.rotation.z = Math.PI;
            doorB.position.set(0,0,-0.45);

            door.add(doorB);
            door.position.x = 5;

            var joint = new THREE.Object3D;

            joint.add(door);
            joint.position.set(position[0],position[1],position[2]);


            return joint;

 }

 function createGeneralWall (height, weight, position){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 15, shading: THREE.SmoothShading, side: THREE.DoubleSide});
            var plane = createMesh(planeGeometry, "white-wall.jpg", "white-wall-bump.jpg", 0.09);
            
            plane.position.set(position[0], position[1], position[2]);

            return plane;


        }

function createDoorWall(position){
            var shape = new THREE.Shape();
            var options = {amount: 0,bevelThickness: 2,bevelSize: 1,bevelSegments: 3,bevelEnabled: false,curveSegments: 12,steps: 1};
            // startpoint
            var shape = new THREE.Shape();
            // startpoint
            shape.moveTo(-.5, 0)      
            // straight line upwards
            shape.lineTo(-.5, 27);

            shape.lineTo(70, 27);
            shape.lineTo(70,0);
            shape.lineTo(60,0);
            shape.lineTo(59.9,22);
            shape.lineTo(50,22);
            shape.lineTo(50,0);

            shape.lineTo(37,0);
            shape.lineTo(37,22);
            shape.lineTo(28,22);
            shape.lineTo(28,0);

            shape.lineTo(15.4,0);
            shape.lineTo(15.4,22);
            shape.lineTo(5.5,22);
            shape.lineTo(5.5,0);

            var wallGeometry = new THREE.ExtrudeGeometry(shape,options);


            var mat = new THREE.MeshPhongMaterial();
            var wallMesh = new THREE.Mesh (wallGeometry, mat);
            wallMesh.rotation.y = Math.PI/2;
            wallMesh.rotation.x = Math.PI/2;
            wallMesh.position.set(position[0], position[1], position[2]);

            var wall = createMesh(wallGeometry, "white-grunge.jpg", null, 0.09);

            wall.material.map.wrapT = THREE.RepeatWrapping;
            wall.material.map.wrapS = THREE.RepeatWrapping;  
            wall.material.map.repeat.set(10,10);

            wall.rotation.y = Math.PI/2;
            wall.rotation.x = Math.PI/2;
            wall.position.set(position[0], position[1], position[2]);

            return wall;
        }

         function createKitchenWall (height, weight, position){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 15, shading: THREE.SmoothShading, side: THREE.DoubleSide});
            var plane = createMesh(planeGeometry, "kitchen.jpg", null, null);
            
            plane.position.set(position[0], position[1], position[2]);

            return plane;


        }
        function createWindowsWall(position){
            var shape = new THREE.Shape();
            var options = {amount: 0,bevelThickness: 2,bevelSize: 1,bevelSegments: 3,bevelEnabled: false,curveSegments: 12,steps: 1};
            // startpoint
            var shape = new THREE.Shape();
            // startpoint
            shape.moveTo(0, 0)      
            // straight line upwards
            shape.lineTo(23.5, 0);

            shape.lineTo(23.5,25);
            shape.lineTo(37.5,25);
            shape.lineTo(37.5,0);
            shape.lineTo(47,0);
            shape.lineTo(47, 30);
            shape.lineTo(0,30);

            var wallGeometry = new THREE.ExtrudeGeometry(shape,options);


            var mat = new THREE.MeshPhongMaterial();
            var wallMesh = new THREE.Mesh (wallGeometry, mat);
            wallMesh.rotation.y = Math.PI/2;
            wallMesh.rotation.x = Math.PI/2;
            wallMesh.position.set(position[0], position[1], position[2]);

            var wall = createMesh(wallGeometry, "white-grunge.jpg", "white-wall-bump.jpg", 0.09);

            wall.material.map.wrapT = THREE.RepeatWrapping;
            wall.material.map.wrapS = THREE.RepeatWrapping;  
            wall.material.map.repeat.set(10,10);

            wall.rotation.y = Math.PI/2;
            wall.rotation.x = Math.PI/2;
            wall.position.set(position[0], position[1], position[2]);

            return wall;
        }
 function createWindow (weight, position){
            var windowGeometry
            var options = THREE.DoubleSide;
            var finestra = importObjMtl('assets/models/windowobj/window.obj', 'assets/models/windowobj/window.mtl', options, null);
            finestra.rotation.x = Math.PI/2;
            finestra.rotation.y = -Math.PI/2;

            //finestra.scale.x = weight;
            //finestra.scale.y = 0.25;
            //finestra.scale.z = 0.1;
           finestra.position.set(position[0], position[1], position[2]);

           return finestra;
           
}

function createLivingWall (height, weight, position){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight,height,weight,height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 15, shading: THREE.SmoothShading, side: THREE.DoubleSide});
            var plane = createMesh(planeGeometry, "white-wall.jpg", "white-wall-bump.jpg", 0.09);
            
            plane.position.set(position[0], position[1], position[2]);

            return plane;


        }