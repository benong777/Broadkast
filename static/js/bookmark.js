const btnBookmarks = document.querySelectorAll(".bookmark");
// console.log('Bookmarks: ', btnBookmarks);

for (const btnBookmark of btnBookmarks) {
   console.log('Bookmark:', btnBookmark);
   console.log('Bookmark innerHTML:', btnBookmark.innerHTML);
   console.log('Bookmark child:', btnBookmark.firstChild);

   btnBookmark.addEventListener("click", () => {
      console.log(`${btnBookmark.id} clicked!`);
      const location = {
         locationId: btnBookmark.id
      }

      //-- Update database bookmark table
      fetch('/add_bookmark', {
         method: 'POST',
         body: JSON.stringify(location),
         headers: {
           'Content-Type': 'application/json',
         }
      })
      .then(res => res.json())
      .then(data => {
         //-- Fill color when bookmarked
         if (data['is_bookmarked']) {
                  btnBookmark.getElementsByClassName('bookmark-icon')[0].setAttribute('fill', 'blue');
         } else {
                  btnBookmark.getElementsByClassName('bookmark-icon')[0].setAttribute('fill', 'None');
         }
      });
   });
}