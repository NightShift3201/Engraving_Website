var updateBtns = document.getElementsByClassName('update-cart')
 
for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, action)

        console.log(user)
        if(user ==='AnonymousUser'){
            console.log("Not logged in")
        }else{
            updateUserOrder(productId, action)
        }

    })
}

function updateUserOrder(productId, action){
    var url ='/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })
    
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}

const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

closeModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal2')
        closeModal(modal)
    })
})

function openModal(modal) {
    if (modal==null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal) {
    if (modal==null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}