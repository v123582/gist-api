var map;
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
   //map.data.addGeoJson(input_geojson); //geojson function
}

google.maps.event.addDomListener(window, 'load', initialize);

function Go(){
   var start = $('#input1').val();
   var end = $('#input2').val();
   $.ajax({
         url:"/"+start+"/"+end,
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
			console.log(api['GeoJson6Point']);
			
			$('#start').html("起點: "+source[0]+" ("+source[1]+")");
			$('#end').html("終點: "+target[0]+" ("+target[1]+")");
			$('#SOURCE_BUS').html("離起點最近的公車站: "+api["SOURCE_BUS"]);
			$('#SOURCE_MRT').html("離起點最近的捷運站: "+api["SOURCE_MRT"]);
			$('#TARGET_BUS').html("離終點最近的公車站: "+api['TARGET_BUS']);
			$('#TARGET_MRT').html("離終點最近的公車站: "+api['TARGET_MRT']);
			var c = 1;
			if(api['Rule']['type1'].length != 0){
				$('#rule1').append(c + ": "+api['Rule']['type1']+"<br>");
				c += 1;
			}
			if(api['Rule']['type2'].length != 0){
				$('#rule2').append(c + ": "+api['Rule']['type2']+"<br>");
				c += 1;
			}
			$.each(api['Rule']['type3'],function(k,v){
				$('#rule3').append(c + ": "+v+"<br>");
				c += 1;
			});
			$.each(api['Rule']['type4'],function(k,v){
				$('#rule4').append(c + ": "+v+"<br>");
				c += 1;
			});
			$.each(api['Rule']['type5'],function(k,v){
				$('#rule5').append(c + ": "+v+"<br>");
				c += 1;
			});
			var mapProp = {
			center:new google.maps.LatLng(22.6379779771347, 120.302701321097), //intial location
			zoom:15,
			};
			var map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
			 map.data.setStyle(function(feature) {
				return { 'icon': feature.getProperty('icon') };
			  });
  
			map.data.addGeoJson(api['GeoJson6Point']);
			
        },
        error:function(html){
            alert('error');
        }
   });

}


