function createSofa(position){
	  var options = THREE.DoubleSide;

 	  var sofa = importObjMtl('assets/models/burlap_sofa/burlap_sofa.obj', 'assets/models/burlap_sofa/burlap_sofa.mtl', options, null);
      sofa.scale.set(0.11,0.11,0.11);
      sofa.rotation.x = Math.PI/2;
      sofa.rotation.y = Math.PI;

      sofa.position.set(position[0],position[1], position[2]);
      return sofa;

  }
  function createKitchen(position){
  	  var options = THREE.DoubleSide;
      var kitchen = importObjMtl('assets/models/kitchen/kitchen.obj', 'assets/models/kitchen/kitchen.mtl', options, null);
      kitchen.rotation.x = Math.PI/2;
      kitchen.position.set(position[0],position[1], position[2]);
      kitchen.scale.set(.1,.1,.1);

      return kitchen;

  }
  function createKitchenTexture (height, weight){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight, height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 10, shading: THREE.SmoothShading });
            //var plane = new THREE.Mesh(planeGeometry,planeMaterial);

            var plane = createMesh(planeGeometry, "assets/textures/general/kitchen.jpg");

            return plane;

        }

  function createLamp(position){
  	var options = THREE.DoubleSide;
    var lamp = importObjMtl('assets/models/living_lamp/living_lamp.obj', 'assets/models/living_lamp/living_lamp.mtl', options, null);
    lamp.position.set(position[0],position[1], position[2]);
    lamp.scale.set(13,13,13);
    lamp.rotation.x = Math.PI/2;
    var light = createLightForLamp(1/13, position);
    light.position.y = 1.28;
    light.position.x = .185;


    lamp.add(light);
    return lamp;



  }

  function createWallLamp(position){
  	var options = THREE.DoubleSide;
    var lamp = importObjMtl('assets/models/living_lamp/wall-spotlight.obj', 'assets/models/living_lamp/wall-spotlight.mtl', options, null);
    lamp.position.set(position[0],position[1], position[2]);
    //lamp.scale.set(13,13,13);
    //lamp.rotation.x = Math.PI/2;
    var light = createLightForWallLamp(.37, position);
    light.position.z = 1.45;
    light.position.y = -.45;

    lamp.add(light);
    lamp.rotation.z = Math.PI/2;
    lamp.rotation.y = Math.PI/2;
    lamp.scale.set(1.2,1.2,1.2);
    lamp.rotation.x = Math.PI;


    return lamp;

  }

  function createLampadario(position){
  	var options = THREE.DoubleSide;
    var lamp = importObjMtl('assets/models/living_lamp/hanging-restaurant-light.obj', 'assets/models/living_lamp/hanging-restaurant-light.mtl', options, null);
    lamp.position.set(position[0],position[1], position[2]);
    //lamp.rotation.x = Math.PI/2;
    var light = createLightForLampadario(.6, position);
   
   light.position.y = 0.7;
   light.rotation.y = Math.PI;
    lamp.add(light);
    lamp.rotation.y = Math.PI/2;
    lamp.scale.set(1.2,1.2,1.2);
    lamp.rotation.x = Math.PI/2;


    return lamp;

  }


  function createLightForWallLamp(diameter, position){
  		  var sphereGeometry = new THREE.SphereGeometry(diameter/2,15,15);
          var sphereMaterial = new THREE.MeshPhongMaterial({color: 0xFFFF99, shininess: 100, side: THREE.DoubleSide });
          var bulb = new THREE.Mesh(sphereGeometry, sphereMaterial);


          //Point Light
          var spotLight1= new THREE.PointLight(0xFFFFEB);
          spotLight1.position = bulb.position;
          spotLight1.intensity = .8;
          spotLight1.distance = 60;

         
          //Point light
          var pointColor = "#fbfdfc";
          var pointLight = new THREE.PointLight(pointColor);
          pointLight.distance = 7.5;
          pointLight.intensity = .01;
          pointLight.position = bulb.position;


          var sphereGeometryT = new THREE.SphereGeometry(5,15,15);
          var sphereMaterialT = new THREE.MeshLambertMaterial({color: 0xFFFF00, castShadow: true});
        
          bulb.add(spotLight1);
          bulb.add(pointLight);
          bulb.position.set(0,0,0);

          return bulb;
  }

  function createLightForLampadario(diameter, position){
  		  var sphereGeometry = new THREE.SphereGeometry(diameter/2,15,15);
          var sphereMaterial = new THREE.MeshPhongMaterial({color: 0xFFFF99, shininess: 10, side: THREE.DoubleSide });
          var bulb = new THREE.Mesh(sphereGeometry, sphereMaterial);


          //Point Light
          var spotLight1= new THREE.PointLight(0xFFFFEB);
          spotLight1.position = bulb.position;
          spotLight1.intensity = .9;
          spotLight1.distance = 60;

          var spotLightHelper = new THREE.PointLightHelper( spotLight1, 2 );
          scene.add(spotLightHelper );

         
          //Point light
          var pointColor = "#fbfdfc";
          var pointLight = new THREE.PointLight(pointColor);
          pointLight.distance = 7.5;
          pointLight.intensity = 1;
          pointLight.position = bulb.position;


          var sphereGeometryT = new THREE.SphereGeometry(5,15,15);
          var sphereMaterialT = new THREE.MeshLambertMaterial({color: 0xFFFF00, castShadow: true});
        
          bulb.add(spotLight1);
          bulb.add(pointLight);
          bulb.position.set(0,0,0);

          return bulb;
  }

  function createLightForLamp(diameter, position){
          var sphereGeometry = new THREE.SphereGeometry(diameter/2,15,15);
          var sphereMaterial = new THREE.MeshPhongMaterial({color: 0xFFFF99, shininess: 10, opacity: 0.9, transparent: true, side: THREE.BackSide });
          var bulb = new THREE.Mesh(sphereGeometry, sphereMaterial);


          //Spot light DOWN
          var spotLight = new THREE.SpotLight( 0xFFFFC7 ,1);
          spotLight.position.set(0,0,0);
          spotLight.intensity = .5;
          var target = new THREE.Object3D();
          target.position.set(position[0]-2,0, position[2]-5);
          target.visible = false;

          spotLight.target = target;
          spotLight.angle = Math.PI/5;
          spotLight.rotation.x = Math.PI/2;

          var lightDiffuse = new THREE.PointLight (0xFFFFC7);
          lightDiffuse.distance = 30;
          lightDiffuse.intensity = .6;
          lightDiffuse.position.set(0,0,0);

          //Spot light UP
          var spotLightU = new THREE.SpotLight( 0xFFFFC7 ,1);
          spotLightU.position.set(0,0,0);
          spotLightU.intensity = .5;
          var targetU = new THREE.Object3D();
          targetU.position.set(position[0]-2,30, position[2]-5);
          targetU.visible = false;

          spotLightU.target = targetU;
          spotLightU.angle = Math.PI/5;
          spotLightU.rotation.x = -Math.PI/2;



          var sphereSize3 = 2;
          var spotLightHelper = new THREE.SpotLightHelper( spotLight, sphereSize3 );
          scene.add(spotLightHelper );
          var spotLightHelperU = new THREE.SpotLightHelper( spotLightU, sphereSize3 );
          scene.add(spotLightHelperU );
         


          //Point light
          var pointColor = "#fbfdfc";
          var pointLight = new THREE.PointLight(pointColor);
          pointLight.distance = 7.5;
          pointLight.intensity = .5;
          pointLight.position = bulb.position;


          var sphereGeometryT = new THREE.SphereGeometry(5,15,15);
          var sphereMaterialT = new THREE.MeshLambertMaterial({color: 0xFFFF00, castShadow: true});
          //var target = new THREE.Mesh(sphereGeometryT, sphereMaterialT);


          //target.position.x = 0;
          //target.position.y = 0;
          //target.position.z = 4;
          //spotLight.add(target);
          //target.visible = false;

          bulb.add(spotLightU);
          bulb.add(spotLight);
          bulb.add(lightDiffuse);
          bulb.add(pointLight);
          bulb.position.set(0,0,0);

          return bulb;


        }
        function createFridge(position){
          var options = THREE.DoubleSide;
      	  var fridge = importObjMtl('assets/models/refridgerator/refridgerator.obj', 'assets/models/refridgerator/refridgerator.mtl', options, null);
      	  fridge.rotation.x = Math.PI/2;
          fridge.scale.set(15,15,15);
          fridge.position.set(position[0],position[1], position[2]);
          return fridge;


  }

  	function createTable(position){
  		var options = THREE.DoubleSide;
      var table = importObjMtl('assets/models/tableD/table.obj', 'assets/models/tableD/table.mtl', options, null);
      table.scale.set(.145,.155,.145);
       table.rotation.x = Math.PI/2;

      table.position.set(position[0],position[1], position[2]);
      return table;
  	}


  	function createTvStand(position){
  		var options = THREE.DoubleSide;
      var table = importObjMtl('assets/models/tv-stand/tvtable.obj', 'assets/models/tv-stand/tvtable.mtl', options, null);
      table.scale.set(4,4.5,4);
      table.rotation.x = Math.PI/2;
      table.position.set(position[0],position[1], position[2]);
      return table;
  	}
