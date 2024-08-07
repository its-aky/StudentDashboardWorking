const searchField = document.querySelector("#searchField");
const table_output=document.querySelector('.table_output');
const app_table=document.querySelector('.app_table');
const table_body=document.querySelector('.table_body');
const no_results=document.querySelector('.no_results');

const pagination_container=document.querySelector('.pagination_container');

table_output.style.display='none';

searchField.addEventListener("keyup", (e)=>{

    const searchVal=e.target.value;

    if(searchVal.trim().length > 0){
        table_body.innerHTML="";
                    
        pagination_container.style.display="none";
        fetch("/dashboard/search",{
            body:JSON.stringify({searchText:searchVal}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data);

            
            app_table.style.display='none';
            table_output.style.display='block';

            if(data.length===0){
                table_output.style.display='none';
                no_results.style.display='block';
            }
            else{
                no_results.style.display='none';
                data.forEach((item)=> {
                    table_body.innerHTML+= `
                    
                    <tr>
                        <td>${item.name_of_company}</td>
                        <td>${item.year_of_passing}</td>
                        <td>${item.preferred_branch}</td>
                        <td>${item.type}</td>
                        <td>${item.mode}</td>
                        <td>${item.category}</td>
                    </tr> `;
                });

                
            }
        });
    }
    else{
        table_output.style.display='none';
        app_table.style.display='block';
        pagination_container.style.display="block";
    }



});