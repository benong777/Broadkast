const btnBookmarks = document.querySelectorAll(".bookmark");

for (const btnBookmark of btnBookmarks) {
   btnBookmark.addEventListener("click", () => {
      const location = {
         locationId: btnBookmark.id
      }

      //-- Fill color when bookmark icon clicked
      // bookmarkItems = document.querySelectorAll(".bookmark-item");
      // console.log('Bookmark items:', bookmarkItems);
      // btnBookmark.remove();

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
         //-- Fill color when bookmark icon clicked
         // if (data === 'Success') {
            window.location.replace('/bookmarks')
            // window.location.reload()
            // window.location.href('/bookmarks.html')
         // } 
      });
   });
}