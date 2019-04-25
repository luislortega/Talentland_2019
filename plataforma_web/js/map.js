let map;
let infowindow;

function initMap() {
    cargarMapa();
    /* envia los JSON de la informacion */    
}

function cargarMarcadores(datos) {
    datos.forEach(elemento => {
        let location = new google.maps.LatLng(elemento.lat, elemento.long)
        let marker = new google.maps.Marker({
            position: location,
            map: map,
            titulo: elemento.title
        });
        
        google.maps.event.addListener(marker, 'click', (e) => {
            if(!isEmpty(infowindow)){
                infowindow.close()
            }
            infowindow = new google.maps.InfoWindow({
                content:marker.titulo
            });            
            infowindow.open(map,marker);
        });
    });
}

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

function cargarMapa() {
    let posicion = new google.maps.LatLng(19.390519,-99.4238064);
    map = new google.maps.Map(document.getElementById('map'), {
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
        disableDefaultUI: true,
        center: posicion,
        zoom: 5,
        styles: [
            { elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
            {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'poi',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{ color: '#263c3f' }]
            },
            {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#6b9a76' }]
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{ color: '#38414e' }]
            },
            {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#212a37' }]
            },
            {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#9ca5b3' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{ color: '#746855' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#1f2835' }]
            },
            {
                featureType: 'road.highway',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#f3d19c' }]
            },
            {
                featureType: 'transit',
                elementType: 'geometry',
                stylers: [{ color: '#2f3948' }]
            },
            {
                featureType: 'transit.station',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }]
            },
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{ color: '#17263c' }]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#515c6d' }]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.stroke',
                stylers: [{ color: '#17263c' }]
            }
        ]
    });
}