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

const validarNombre = (nombre) => {
    return nombre && nombre.length >= 3 && nombre.length <= 80
}

const validarTexto = (texto) => {
    return texto && texto.length >= 5
}

let formComment = document.getElementById("formComentario")

formComment.addEventListener("submit", function(event) {
    event.preventDefault()
    console.log("submited")

    let divErrores = document.getElementById("erroresComentario")

    let nombre = document.getElementById("autor").value
    let texto =  document.getElementById("comment").value

    if (!validarNombre(nombre)) {
        divErrores.innerHTML = "El nombre no cumple con el formato"
        divErrores.className = "erroresComentario"
    } else if (!validarTexto(texto)) {
        divErrores.innerHTML = "El comentario no cumple con el formato"
        divErrores.className = "erroresComentario"
    } else {
        divErrores.innerHTML = ""
        divErrores.className = ""
        this.submit()
    }
})


imagen.addEventListener("click", agrandarImg)


