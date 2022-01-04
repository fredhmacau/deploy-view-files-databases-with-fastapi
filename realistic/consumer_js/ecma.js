const img=document.querySelector("#img");
const btnSend=document.querySelector("#btnImg");



async function submitHandler(event) {
  event.preventDefault();
  const data=new FormData()
  data.append("img",img.files[0])
    const config = {
      method: "POST",
      body: data,
    };
    await fetch("http://127.0.0.1:8000/img",config)
    .then(resp=>console.log(resp.json()))
    .then(dat=>console.log(dat))
    .catch(error=>console.log(error));
}

const submitData=async (file)=>{
    
    
}

btnSend.addEventListener("click",submitHandler,true)