// Profile dropdown
const profileDropdown = document.querySelector("#profile-dropdown");
const profileMenu = document.querySelector('#profile-menu');

profileDropdown.addEventListener('click', () => {
   profileMenu.classList.toggle('hidden');
});

// Mobile Menu
const mobileMenuBtn = document.querySelector("#mobile-menu-btn");
const mobileMenu = document.querySelector("#mobile-menu");

mobileMenuBtn.addEventListener("click", () => {
   mobileMenu.classList.toggle("hidden");
});


    //-- Google places autocompletion
    // autocomplete = new google.maps.Map(
    //   document.querySelector("#search"),
    //   {
    //     componentRestrictions: {'country': ['us']},
    //     fields: ['geometry', 'name'],
    //     types: ['establishment']
    //   });

    //   autocomplete.addListener("place_changed", () => {
    //     const place = autocomplete.getPlace();
    //     new google.maps.Marker({
    //       position: place.geometry.location,
    //       title: place.name,
    //       map: map
    //     })
    //   });
