/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.{html, js}",
    "./**/**/*.{html, js}",
    "./**/**/**/*.{html, js}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'login-img': "url('./img/arroz.jpg')" ,
        'login-img2': "url('./img/embasado.jpg')",
        'login-img3': "url('./img/soplado.jpg')",
        'login-img4': "url('./img/arroz2.jpg')",
        
      }
    },
  },
  plugins: [],
}

