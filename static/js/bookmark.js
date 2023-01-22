const btnBookmarks = document.querySelectorAll(".bookmark");

for (const btnBookmark of btnBookmarks) {
   btnBookmark.addEventListener("click", () => {
      const location = {
         locationId: btnBookmark.id
      }

      //-- Get bookmark state from DB and set icon color
      fetch('/add_bookmark', {
         method: 'POST',
         body: JSON.stringify(location),
         headers: {
           'Content-Type': 'application/json',
         }
      })
      .then(res => res.json())
      .then(data => {
         //-- Fill color when bookmark icon clicked
         if (data['is_bookmarked']) {
                  btnBookmark.getElementsByClassName('bookmark-icon')[0].setAttribute('fill', 'blue');
         } else {
                  btnBookmark.getElementsByClassName('bookmark-icon')[0].setAttribute('fill', 'None');
         }
      });
   });
}