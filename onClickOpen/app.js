let signupBtn = document.querySelector('#signup');
let signupForm = document.querySelector('.signupForm');
let signupCloseBtn = document.querySelector('#close');

signupBtn.addEventListener('click', (e) => {
	signupForm.classList.add('show');
});

signupCloseBtn.addEventListener('click', (e) => {
	console.log('Closing signup form');
	e.preventDefault();
	e.stopPropagation();
	signupForm.classList.remove('show');
});
