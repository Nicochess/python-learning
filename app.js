function formularioAnimado(){
    const arrow = document.querySelectorAll('.fa-arrow-circle-down')
    arrow.forEach(arrow =>{
        arrow.addEventListener('click', ()=>{
            const input = arrow.previousElementSibling
            const parent = arrow.parentElement
            const proxForm = parent.nextElementSibling
            console.log(input)

            //Validação formulário
            if(input.type === "text" && validarUser(input)){
                proximoSlide(parent, proxForm)
            } else if(input.type === "email" && validarEmail(input)){
                proximoSlide(parent, proxForm)
            } else if(input.type === "password" && validarUser(input)){
                proximoSlide(parent, proxForm)
            } else {
                parent.style.animation = "shake 0.5s ease"
            }

            parent.addEventListener("animationend", ()=>{
                parent.style.animation = ""
            })
        })
    })
}

function validarUser(user){
    if(user.value.length < 6){
        console.log('Sem caracteres suficientes')
        erro("rgb(255, 104, 104)")
    } else {
        erro("rgb(104, 255, 137)")
        return true
    }
}

function validarEmail(email){
    const validar = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if(validar.test(email.value)){
        erro("rgb(104, 255, 137)")
        return true
    } else {
        erro("rgb(255, 104, 104)")
    }
}

function proximoSlide(parent, proxForm){
    parent.classList.add('inativa')
    parent.classList.remove('ativo')
    proxForm.classList.add('ativo')
}

function erro(color){
    document.body.style.backgroundColor = color
}

formularioAnimado();