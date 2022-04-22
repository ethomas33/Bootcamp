// Creating map object
var myMap = L.map("map",{
    center: [42.3601, -71.0589],
    zoom: 10
})
// Add a tile layer
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
})
streets.addTo(myMap);
// Use this link to get the geojson data.
var link = "./static/data/Police_Districts.geojson";
// Get our GeoJSON data using d3.json
d3.json(link, function(data) {
    L.geoJSON(data).addTo(myMap);
});