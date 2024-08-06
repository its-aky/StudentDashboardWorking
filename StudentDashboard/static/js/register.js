// console.log("Register working")


const UsernameField=document.querySelector('#usernameField');
const EmailField=document.querySelector('#emailField');
const UsernameFeedback=document.querySelector('.UsernameFeedback');
const EmailFeedback=document.querySelector('.EmailFeedback');
const UsernameChecking=document.querySelector('.UsernameChecking');
const EmailChecking=document.querySelector('.EmailChecking');
const showPasswordToggle=document.querySelector('.showPasswordToggle');
const passwordField=document.querySelector('#passwordField');
const submitbtn=document.querySelector('.submit-btn');

// Sync the disabled submit btn
username_error=false;
email_error=false;


UsernameField.addEventListener("keyup",(e)=>{
    const UsernameVal=e.target.value;
    
    UsernameField.classList.remove("is-invalid");
    UsernameFeedback.style.display="none";

    if(UsernameVal.length>0){

        UsernameChecking.style.display="block";
        UsernameChecking.textContent=`Checking ${UsernameVal}`;
        fetch("/authentication/validate-username",{
            body:JSON.stringify({username:UsernameVal}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("User:",data);
            UsernameChecking.style.display="none";
            if(data.Username_Error){
                username_error=true;
                submitbtn.setAttribute('disabled','disabled');
                UsernameField.classList.add("is-invalid");
                UsernameFeedback.style.display="block";
                UsernameFeedback.innerHTML=`<p>${data.Username_Error}</p>`;
            }
            else{
                username_error=false;
                if(!email_error){
                    submitbtn.removeAttribute('disabled');
                }
                
            }
        });
    }
});

EmailField.addEventListener("keyup",(e)=>{
    const EmailVal=e.target.value;
    
    EmailField.classList.remove("is-invalid");
    EmailFeedback.style.display="none";

    if(EmailVal.length>0){
        EmailChecking.style.display="block";
        EmailChecking.textContent=`Checking ${EmailVal}`;
        
        fetch("/authentication/validate-email",{
            body:JSON.stringify({email:EmailVal}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("Email:",data);
            EmailChecking.style.display="none";

            if(data.Email_Error){
                email_error=true;
                submitbtn.setAttribute('disabled','disabled');
                EmailField.classList.add("is-invalid");
                EmailFeedback.style.display="block";
                EmailFeedback.innerHTML=`<p>${data.Email_Error}</p>`;
            }

            else{
                email_error=false;
                if(!username_error){
                    submitbtn.removeAttribute('disabled');
                }
                
            }
        });
    }
});

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
