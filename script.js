// script.js
document.addEventListener("DOMContentLoaded", function() {
  var lang = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
  if (lang.startsWith('es')) {
    document.querySelectorAll('.lang-es').forEach(el => el.style.display = 'block');
  } else {
    document.querySelectorAll('.lang-en').forEach(el => el.style.display = 'block');
  }
});
