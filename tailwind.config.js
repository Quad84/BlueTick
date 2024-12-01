/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html', ],
  darkMode : 'class',
  theme: {
    extend: {
      backgroundImage: {
        'hero-dark': "url('/img/pexels-zhuhehuai-544917.jpg')",
        'hero-light': "url('/img/pexels-nout-gons-80280-378570.jpg')",
      }
    }
  },
  plugins: [],
}