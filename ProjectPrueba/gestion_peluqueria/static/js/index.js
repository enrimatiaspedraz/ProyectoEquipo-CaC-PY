document.getElementById('enlace').addEventListener('click', function(event) {
    event.preventDefault(); 
    var contenido = document.querySelector('.contenido');
    contenido.classList.add('desaparecer');
    
    setTimeout(function() {
      window.location.href = "{% url 'home' %}";
    }, 1000); 
  });