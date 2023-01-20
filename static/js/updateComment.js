editButtons = document.querySelectorAll('.edit-comment');
console.log(editButtons)

for (const button of editButtons) {
  console.log(button);
  button.addEventListener('click', () => {
    // Prompt for new comment
    const newComment = prompt('Add your new comment here.');
    const formInputs = {
      updated_comment: newComment,
      comment_id: button.id,
    };

    // send a fetch request to the update data
    fetch('/update_comment', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if (response.ok) {
        document.querySelector(`#comment-id-${button.id}`).innerHTML = newComment;
      } else {
        alert('Failed to update comment.');
      }
    });
  });
}
