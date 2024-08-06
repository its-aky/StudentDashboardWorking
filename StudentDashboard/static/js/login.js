// console.log("Login working")

const showPasswordToggle=document.querySelector('.showPasswordToggle');

showPasswordToggle.addEventListener('click',(evnt)=>{
    if(showPasswordToggle.textContent==="SHOW"){
        showPasswordToggle.textContent="HIDE";

        passwordField.setAttribute("type","text");
    }
    else{
        showPasswordToggle.textContent="SHOW";
        passwordField.setAttribute("type","password");
    }
});
