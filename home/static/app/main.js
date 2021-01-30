const button = document.querySelector('.egg1');
button.addEventListener('click', function() {
  alert("Sabias que me demore mas de 1 Dia intentando poner una barra lateral xD.")
  //document.getElementById('slide_bar').classList.toggle('activate');
});

const barra = document.querySelector('.icon-desp');
barra.addEventListener('click', function(){
	document.getElementById('Barra').classList.toggle('nav-bar')	
})
