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
            if (!isEmpty(infowindow)) {
                infowindow.close()
            }
            infowindow = new google.maps.InfoWindow({
                content: marker.titulo
            });
            infowindow.open(map, marker);
        });
    });
}

function isEmpty(obj) {
    for (var key in obj) {
        if (obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

function cargarMapa() {
    let posicion = new google.maps.LatLng(19.390519, -99.4238064);
    map = new google.maps.Map(document.getElementById('map'), {
        streetViewControl: true,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
        disableDefaultUI: true,
        center: posicion,
        zoom: 5,
        styles: [{ "featureType": "administrative.land_parcel", "elementType": "labels", "stylers": [{ "visibility": "off" }] }, { "featureType": "poi", "elementType": "labels.text", "stylers": [{ "visibility": "off" }] }, { "featureType": "poi.business", "stylers": [{ "visibility": "off" }] }, { "featureType": "road", "elementType": "labels.icon", "stylers": [{ "visibility": "off" }] }, { "featureType": "road.arterial", "elementType": "labels", "stylers": [{ "visibility": "off" }] }, { "featureType": "road.highway", "elementType": "labels", "stylers": [{ "visibility": "off" }] }, { "featureType": "road.local", "stylers": [{ "visibility": "off" }] }, { "featureType": "road.local", "elementType": "labels", "stylers": [{ "visibility": "off" }] }, { "featureType": "transit", "stylers": [{ "visibility": "off" }] }]
    });
}