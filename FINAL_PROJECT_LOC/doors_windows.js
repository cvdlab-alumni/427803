 function createFloorTexture (height, weight){
            var planeGeometry = new THREE.PlaneGeometry(weight,height,weight, height);
            var planeMaterial = new THREE.MeshLambertMaterial({ ambient: 0xFFFFff,
            specular: 0xffffff, shininess: 10, shading: THREE.SmoothShading });
            //var plane = new THREE.Mesh(planeGeometry,planeMaterial);

            var plane = createMesh(planeGeometry, "floor-wood.jpg");

            return plane;

        }