// Create our initial map object
// Set the longitude, latitude, and the starting zoom level
var myMap = L.map("map",{
    center: [45.52, -122.67],
    zoom: 13
});

// Add a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
L.titleLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v10/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}].addTo(myMap);