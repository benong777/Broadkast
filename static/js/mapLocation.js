//-- TODO:
//      Geolocation - get user's current location
//                  - https://www.youtube.com/watch?v=oVr6unKZbg4

function initMapLocation() {
    const currentName = document.getElementById("location-vars").getAttribute("data-name");
    const currentAddr = document.getElementById("location-vars").getAttribute("data-addr");
    const currentLat = document.getElementById("location-vars").getAttribute("data-lat");
    const currentLng = document.getElementById("location-vars").getAttribute("data-lng");

    const currentLocation = {
      // lat: locationLat,
      // lng: locationLng,
      lat: parseFloat(currentLat),
      lng: parseFloat(currentLng),
      // lat: 37.3304293,
      // lng: -121.8601749,
    };

    console.log('Current location:', currentLocation);

    const options = {
      center: currentLocation,
      zoom: 9
    }

   const sfBayCoords = {
      lat: 37.3984,
      lng: -121.9752,
    };
    
    const basicMap = new google.maps.Map(document.getElementById('map-location'), options);

    const sfMarker = new google.maps.Marker({
      // position: sfBayCoords,
      position: currentLocation,
      title: currentName,
      map: basicMap,
    });
  
    sfMarker.addListener('click', () => {
      alert('Hi!');
    });
  
    const sfInfo = new google.maps.InfoWindow({
      content: `<h1>${currentName}</h1>
                <h2>${currentAddr}</h2>`,
    });
  
    sfInfo.open(basicMap, sfMarker);
  
    const locations = [
      // {
      //   name: 'Hackbright Academy',
      //   coords: {
      //     lat: 37.7887459,
      //     lng: -122.4115852,
      //   },
      // },
      // {
      //   name: 'Powell Street Station',
      //   coords: {
      //     lat: 37.7844605,
      //     lng: -122.4079702,
      //   },
      // },
      // {
      //   name: 'Montgomery Station',
      //   coords: {
      //     lat: 37.7894094,
      //     lng: -122.4013037,
      //   },
      // },
    ];
  
    const markers = [];
    for (const location of locations) {
      markers.push(
        new google.maps.Marker({
          position: location.coords,
          title: location.name,
          map: basicMap,
         //  icon: {
         //    // custom icon
         //    url: '/static/img/marker.svg',
         //    scaledSize: {
         //      width: 30,
         //      height: 30,
         //    },
         //  },
        }),
      );
    }
  
    for (const marker of markers) {
      const markerInfo = `
        <h1>${marker.title}</h1>
        <p>
          Located at: <code>${marker.position.lat()}</code>,
          <code>${marker.position.lng()}</code>
        </p>
      `;
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200,
      });
  
      marker.addListener('click', () => {
        infoWindow.open(basicMap, marker);
      });
    }  

    //-------------------------------------
    // Google places autocompletion
    //-------------------------------------
    autocomplete = new google.maps.places.Autocomplete(
      document.getElementById("search"),
      {
        componentRestrictions: {'country': ['us']},
        // fields: ['geometry', 'name', 'formatted_address', 'photos'],
        fields: ['geometry', 'name', 'formatted_address'],
        types: ['establishment']
      });

      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();

        const name = place.name;
        const formatted_address = place.formatted_address;
        const geometry = place.geometry;
        const lat = geometry.location.lat();
        const lng = geometry.location.lng();
        const photos = place.photos;

        console.log("Photos: ", photos);
        console.log("name: ", name);
        console.log("Address: ", formatted_address);
        console.log("Geometry: ", geometry);
        console.log("Lat: ", lat);
        console.log("Long: ", lng);

        if (!place.geometry) {
          alert("No location found");
          //-- Clear
          document.getElementById("search").value = "";
        } else {
          //-- Place a marker
          new google.maps.Marker({
            position: place.geometry.location,
            title: place.name,
            map: basicMap
          });

          //-- Center map to searched location
          basicMap.setCenter(place.geometry.location);
          basicMap.setZoom(18);

          // Check if location exist in DB
          // const queryString = new URLSearchParams({ locationName: place.name, locationGeometry: place.geometry.location, locationAddr: place.formatted_address }).toString();
          const queryString = new URLSearchParams({ locationName: place.name, locationLat: lat, locationLng: lng, locationAddr: place.formatted_address }).toString();
          const url = `/get_location?${queryString}`;
          console.log(url);

          fetch(url)
            .then((res) => res.json())
            .then((data) => {
              console.log(`++++++++ ${data.location_id} ++++++++`);
              // target = document.querySelector('#history');

              // div_1 = document.createElement("div");
              // div_1.className = "pt-3";
              // a_1 = document.createElement("a");
              // a_1.innerHTML = place.name;
              // a_1.setAttribute("href", "/location/1");

              // div_2 = document.createElement("div");
              // div_2.innerHTML = place.formatted_address;
              // div_1.appendChild(a_1);
              // div_1.appendChild(div_2);
              // target.appendChild(div_1);

              //-- Update route
              // window.location.href = `http://localhost:5000/locations/${data.location_id}`;
              window.location.replace(`http://localhost:5000/locations/${data.location_id}`);
            })
        }
      });
 }