const btnBookmarks = document.querySelectorAll(".bookmark");

for (const btnBookmark of btnBookmarks) {
   btnBookmark.addEventListener("click", () => {
      console.log(`${btnBookmark.id} clicked!`);
      const location = {
         locationId: btnBookmark.id
      }

               // const fill = document.querySelector(".bookmark-icon").getAttribute('fill') 

               // if (fill == 'None') {
               //    document.querySelector(".bookmark-icon").setAttribute('fill', 'blue');
               // } else {
               //    document.querySelector(".bookmark-icon").setAttribute('fill', 'None');
               // }

      //-- Fetch: 
      fetch('/add_bookmark', {
         method: 'POST',
         body: JSON.stringify(location),
         headers: {
           'Content-Type': 'application/json',
         }
      })
      .then(res => res.json())
      .then(data => {
         console.log('*** === Data:', data);
         console.log(data['is_bookmarked']);
         if (data['is_bookmarked']) {
                  document.querySelector(".bookmark-icon").setAttribute('fill', 'blue');
         } else {
                  document.querySelector(".bookmark-icon").setAttribute('fill', 'None');
         }
      });
   });
}