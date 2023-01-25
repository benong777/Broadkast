function removeBookmark(locationId) {
   console.log('REMOVE:', locationId);
   console.log('Type:', typeof(locationId));

   const location = {
      locationId: locationId
   };

   //-- Get bookmark state from DB and set icon color
   fetch('/remove_bookmark', {
      method: 'POST',
      body: JSON.stringify(location),
      headers: {
        'Content-Type': 'application/json',
      }
   })
   .then(res => res.json())
   .then(data => {
      console.log("DATA: ", data);
      //-- If fetch is successful, update page
      if (data['result'] === 'Success') {
         console.log("SUCCESS!");
         // window.location.replace('/bookmarks');
         window.location.href = '/bookmarks';
      } 
   });
};

// function test(locationId) {
//    // window.location.href = `/locations/${locationId}`;
//          window.location.replace(`/locations/${locationId}`);
//    console.log('Success!');
// }