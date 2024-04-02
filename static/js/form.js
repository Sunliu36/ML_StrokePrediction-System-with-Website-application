// 多個表格
// // Example starter JavaScript for disabling form submissions if there are invalid fields
// (function () {
//   'use strict'
//   console.log('success loading form js')
//   // Fetch all the forms we want to apply custom Bootstrap validation styles to
//   var forms = document.querySelectorAll('#contactForm')

//   // Loop over them and prevent submission
//   Array.prototype.slice.call(forms)
//     .forEach(function (form) {
//       form.addEventListener('submit', function (event) {
//         if (!form.checkValidity()) {
//           event.preventDefault()
//           event.stopPropagation()
//         }

//         form.classList.add('was-validated')
//       }, false)
//     })
// })()

// 單
(function () {
  'use strict';

  var form = document.querySelector('#contactForm');

  if (form) {
    form.addEventListener('/submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add('was-validated');
    }, false);
  }
})();