

function editDetail(id){
    let element=document.getElementById(id)
    email=element.parentNode.parentNode.parentNode.children[1].innerText
    firstname=element.parentNode.parentNode.parentNode.children[2].innerText
    lastname=element.parentNode.parentNode.parentNode.children[3].innerText
    Address=element.parentNode.parentNode.parentNode.children[4].innerText
    console.log(element.parentNode.parentNode.parentNode)
   
    
}
