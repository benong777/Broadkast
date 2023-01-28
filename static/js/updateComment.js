editButtons = document.querySelectorAll('.edit-comment-btn');

for (const button of editButtons) {
  button.addEventListener('click', () => {
    // const currComment = document.querySelector(`#comment-id-${button.id}`);
    // currComment.classList.add("hidden");

    //-- Get ID: Split name by "-" and get last element, which is the ID
    const editBtnId = (button.id).split("-").at(-1);
    // console.log("Remove input:", editInput.id);
    // console.log("ID:", commentId);

    //-- Hide comment
    document.getElementById(`comment-id-${editBtnId}`).classList.toggle("hidden");
    //-- Show input field
    document.getElementById(`edit-input-id-${editBtnId}`).classList.toggle("hidden");

    if (button.innerHTML === 'Edit') {
      button.innerHTML = "Cancel";
    } else {
      button.innerHTML = "Edit";
    }

    // const formInputs = {
    //   updated_comment: newComment,
    //   comment_id: button.id,
    // };

    // // send a fetch request to the update data
    // fetch('/update_comment', {
    //   method: 'POST',
    //   body: JSON.stringify(formInputs),
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    // }).then((response) => {
    //   if (response.ok) {
    //     document.querySelector(`#comment-id-${button.id}`).innerHTML = newComment;
    //   } else {
    //     alert('Failed to update comment.');
    //   }
    // });
  });
}

const editInputs = document.querySelectorAll('.edit-input');

for (const editInput of editInputs) {
  editInput.addEventListener("keypress", (e) => {
    //-- When the enter key is pressed, grab value and send AJAX fetch
    if (e.key === "Enter") {
      //-- Get ID: Split name by "-" and get last element, which is the ID
      const commentId = (editInput.id).split("-").at(-1);
      // console.log("Remove input:", editInput.id);
      // console.log("ID:", commentId);

      const oldComment = document.getElementById(`comment-id-${commentId}`).innerHTML;

      //-- Get updated text that were typed in and show the comment
      const newComment = document.getElementById(`edit-input-id-${commentId}`).value;

      //-- Restore edit btn
      const currEditButton = document.getElementById(`edit-comment-btn-id-${commentId}`);
      currEditButton.innerHTML = "Edit";

      const formInputs = {
        updated_comment: newComment,
        comment_id: commentId,
      };
     
      //-- send a fetch request to the update data
      fetch('/update_comment', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        if (response.ok) {
          const commentElement = document.getElementById(`comment-id-${commentId}`)
          commentElement.innerHTML = newComment;
          commentElement.classList.toggle("hidden");

          //-- Hide input textarea
          document.getElementById(`edit-input-id-${commentId}`).classList.toggle("hidden");

        } else {
          document.querySelector(`#comment-id-${button.id}`).innerHTML = oldComment;
          alert('Failed to update comment.');
        }
      });
    }
  });
}

function clickPress(event) {
  // if (event.key == "Enter") {
  //   const myInput = event.target.value;
  //   console.log(myInput);

  //   document.getElementById("comment-id-1").classList.toggle("hidden");

  //   const formInputs = {
  //     updated_comment: myInput,
  //     comment_id: 8,
  //   };

  //   // send a fetch request to the update data
  //   fetch('/update_comment', {
  //     method: 'POST',
  //     body: JSON.stringify(formInputs),
  //     headers: {
  //       'Content-Type': 'application/json',
  //     },
  //   }).then((response) => {
  //     if (response.ok) {
  //       document.querySelector(`#comment-id-${8}`).innerHTML = myInput;
  //     } else {
  //       alert('Failed to update comment.');
  //     }
  //   });
  // }
}