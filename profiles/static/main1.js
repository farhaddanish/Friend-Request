const form = document.querySelectorAll('.formUser')
console.log(form)

form.forEach(element => {
    element.addEventListener('submit', (event) => {
        event.preventDefault()
        const id = element.getAttribute("data-id")
        const csr = element.firstElementChild.value;
        console.log(csr)
        console.log(id)

        const Url = "http://127.0.0.1:8000/ajaxMakefriends"
     

        $.ajax({
            type: "POST",
            url: Url,
            data: {
                csrfmiddlewaretoken : csr,
                id: id
            },

            success: function (response) {
                if (response.message){
                    const btn = element.querySelector("#userBtn")
                    btn.textContent = "cancle Request"
                }else{
                    const btn = element.querySelector("#userBtn")
                    btn.textContent = "Add Friend"
                }
            }
        });


    })
});





//  accept or demied ajax


const form_accept = document.querySelectorAll('.form_accept')
form_accept.forEach((element)=>{
    element.addEventListener('submit',(event)=>{
        event.preventDefault()
        const id = element.getAttribute('data-id')
        const data_user_id = element.getAttribute('data-user-id')
        const csr = element.firstElementChild.value
        const url = "http://127.0.0.1:8000/acceptFriendRequest/"

        console.log(data_user_id)

        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken : csr,
                id : id,
                data_user :data_user_id
            },
            
            success: function (response) {
                const generaldiv = document.querySelector(`.general${id}`)
                if(response.accepted){
                    generaldiv.lastElementChild.remove()
                    generaldiv.lastElementChild.remove()
                    generaldiv.innerHTML += '<h3> You are now Friends </h3>'
                }else{
                    alert('something wrong')
                }
            }
        });
    })
})




const form_denied = document.querySelectorAll('.form_denied')
form_denied.forEach((element)=>{
    element.addEventListener('submit',(event)=>{
        event.preventDefault()
        const id = element.getAttribute('data-id')
        const data_user_id = element.getAttribute('data-user-id')
        const csr = element.firstElementChild.value
        const url = "http://127.0.0.1:8000/deniedFriendRequest/"

        console.log(data_user_id)

        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken : csr,
                id : id,
                data_user :data_user_id
            },
            
            success: function (response) {
                const generaldiv = document.querySelector(`.general${id}`)
                if(response.denied){
                    generaldiv.lastElementChild.remove()
                    generaldiv.lastElementChild.remove()
                    generaldiv.innerHTML += '<h3> You Remove that  </h3>'
                }else{
                    alert('something wrong')
                }
            }
        });
    })
})