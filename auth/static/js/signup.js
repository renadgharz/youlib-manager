document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        var errors = form.querySelectorAll('.form-error');
        for (var i = 0; i < errors.length; i++) {
            errors[i].style.display = 'block';
        }
        if (errors.length > 0) {
            event.preventDefault();
        }
    });
});