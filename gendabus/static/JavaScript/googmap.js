let map;
const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let labelIndex = 0;
var datosj;
var markers = [];

/////////

//////////


const urlJ = "static/json/redT.json";



///
//obtenerlos del servidor
setInterval(() => {
const urlServ = 'http://127.0.0.1:8000/get';
const claveAcceso = '12345678901';

// Objeto de datos para la solicitud
const data = {
  clave_acceso: claveAcceso,
};

fetch(urlServ, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
  body: new URLSearchParams(data),
  mode: 'cors', 
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
    datosj = data;  
  })
  .catch(error => console.error('Error:', error));
}, 1000);
///

async function initMap() {
  const position = { lat: 26.893404006958008, lng: -101.40805053710938 };
  
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerView } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  

  setInterval(() => {
    deleteMarkers();
    
    for (i = 1; i <= 2; i++) {
      const inf = datosj["floresBorja"]["" + i]["IdaVuelta"];
      const np = datosj["floresBorja"]["" + i]["np"];
      const estadoFuncional = datosj["floresBorja"]["" + i]["estado"];
      const newPosition = {
        lat: datosj["floresBorja"][""+i]["u"][0],
        lng: datosj["floresBorja"][""+i]["u"][1]
      };
      addMarker(newPosition, map, inf, np, estadoFuncional);
    }
  }, 1000);
}

function addMarker(location, map, inf, np, estadoFuncional) {
  const marker = new google.maps.Marker({
    position: location,
    label: {
      text: inf[0] + " " + inf[1],  
      color: 'white',  
    },
    map: map,
    icon: 'static/img/icon/camion_ns.png',
  });

  ////
  const ruta = document.getElementById("ruta");
  const numeroDePasajeros = document.getElementById("numeroDePasajeros");
  const estadoFuncinalInf = document.getElementById("estadoFuncional");

  google.maps.event.addListener(marker, 'click', function() {
    //alert('Se hizo clic en el marcador: ' + inf[0] + " " + inf[1] + "\n numero de pasajeros: " + np);
    ruta.innerText = "ruta: " + inf[0] + " " + inf[1];
    numeroDePasajeros.innerText = "numero de pasajeros: " + np;
    estadoFuncinalInf.innerText = "estado funcional: " + estadoFuncional

  });
  ////

  markers.push(marker);
}

function deleteMarkers() {
  for (let i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers = [];
}


initMap();
