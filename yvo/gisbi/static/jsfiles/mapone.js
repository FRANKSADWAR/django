//MAPVIEW FOR ROUTES, DEFAULT VIEW
console.log('confirm for map view');
var point_1 = [-1.313360,36.852621];
var point_2 = [-1.305190,36.828198];
var point_3 =[-1.220479,36.893479];
var point_4 =[-1.249460,36.858066];
var point_5 = [-1.298783,36.816247];
var point_6 = [-1.303686,36.814171];
var map = L.map('Routes').setView([-1.295365,36.895221],10);
maplink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
//tile layer
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
  attribution :'&copy;'+maplink,
}).addTo(map);
//markers
var marker_1 = L.marker([-1.295365,36.895221],{
  draggable:false,
  clickable:true
}).addTo(map);

marker_1.bindPopup("<h4>Starting point</h4><br><ul> <li>Lat:-1.295365</li><li>Long:36.895221</li></ul>");
