let small = true
let imagen = document.getElementById("img")

const agrandarImg = () => {
    if (small) {
        imagen.width = 1280
        imagen.height = 1024
        small = false
    } else {
        imagen.width = 640
        imagen. height = 480
        small = true
    }
}

imagen.addEventListener("click", agrandarImg)


