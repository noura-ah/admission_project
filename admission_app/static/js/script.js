<<<<<<< HEAD
// switch between Login and Register form 
=======
// SWITCH BETWEEN LOGIN AND REGISTER FORM //
>>>>>>> 338796bb9cda5fb9c08e218f7a26211d4092b06f
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});




