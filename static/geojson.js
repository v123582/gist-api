function initialize() {
  var mapProp = {
	center:new google.maps.LatLng(22.6379779771347, 120.302701321097), //intial location
	zoom:15,
  };
  var map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
  var input_geojson = {                               //input geojson
	"type": "FeatureCollection",
	"features": [{
		"type": "Feature",
		"geometry":
		{
			"type": "LineString",
	        "coordinates": [
        		[
	              120.306174420106,
	              22.7696673164653
	            ],
	            [
	              120.306238844439,
	              22.7695141378747
	            ],
	            [
	              120.306454399018,
	              22.7691168670165
	            ],
	            [
	              120.307093477532,
	              22.7681180481609
	            ],
	            [
	              120.307714328453,
	              22.766586950146
	            ]
	        ]
		},
		"properties": {
			"icon": "http://google-maps-icons.googlecode.com/files/beach-pet.png"
		}
	}]
};
 //map.data.loadGeoJson("https://dl.dropboxusercontent.com/u/12537630/geo.json");  //geojson input
  map.data.addGeoJson(input_geojson); //geojson function
}
google.maps.event.addDomListener(window, 'load', initialize);

function Go(){
   var start = $('#input1').val();
   var end = $('#input2').val();
   $.ajax({
         url:"gist-api.herokuapp.com/"+start+"/"+end,
         crossDomain: true,
         type:"GET",
         dataType:'json',
         success: function(html) {
         	api = html['api'];
            console.log(api["SOURCE_BUS"]);
            console.log(api['SOURCE_MRT']);
            console.log(api['TARGET_BUS']);
            console.log(api['TARGET_MRT']);
            console.log(api['Rule']['type1']);
            console.log(api['Rule']['type2']);
            console.log(api['Rule']['type3']);
            console.log(api['Rule']['type4']);
            console.log(api['Rule']['type5']);
          	source = html['input'][0];
          	console.log(source);
          	target = html['input'][1];
          	console.log(target);
        },
        error:function(html){
            alert('error');
        }
   });

}
