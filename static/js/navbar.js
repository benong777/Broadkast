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
