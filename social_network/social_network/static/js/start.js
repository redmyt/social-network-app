function getE(id){
    return document.getElementById(id);}

 function getTag(tag,number){
    return document.getElementsByTagName(tag)[number];
 }

//userName
getE('userName').onblur = function(){     
        if (document.forms.formR.username.innerHTML =='') 
            {
       document.forms.formR.userName.style.borderBottomColor="#f00";
        getTag('span',[0]).style.display="inline-block";    
            }
        else{
       document.forms.formR.userName.style.borderBottomColor="#fff";
       getTag('span',[0]).style.display="none";
            } 
}
//firstName
getE('firstName').onblur = function(){    
        if (document.forms.formR.firstName.innerHTML =='') 
            {
       document.forms.formR.firstName.style.borderBottomColor="#f00";
        getTag('span',[1]).style.display="inline-block";    
            }
        else{
       document.forms.formR.firstName.style.borderBottomColor="#fff";
       getTag('span',[1]).style.display="none";
            } 
}
//lastName
getE('lastName').onblur = function(){     
        if (document.forms.formR.lastName.innerHTML =='') 
            {
       document.forms.formR.lastName.style.borderBottomColor="#f00";
        getTag('span',[2]).style.display="inline-block";   
            }
        else{
       document.forms.formR.lastName.style.borderBottomColor="#fff";
       getTag('span',[2]).style.display="none";
            } 
}
//phone
getE('phone').onblur = function(){  
        if (document.forms.formR.phone.innerHTML =='') 
            {
       document.forms.formR.phone.style.borderBottomColor="#f00";
        getTag('span',[3]).style.display="inline-block";    
            }
        else{
       document.forms.formR.phone.style.borderBottomColor="#fff";
       getTag('span',[3]).style.display="none";
            } 
}
//password
getE('password').onblur = function(){     
        if (document.forms.formR.password.innerHTML =='') 
            {
       document.forms.formR.password.style.borderBottomColor="#f00";
        getTag('span',[4]).style.display="inline-block";  
            }
        else{
       document.forms.formR.password.style.borderBottomColor="#fff";
       getTag('span',[4]).style.display="none";
            } 
}
//password2
getE('password2').onblur = function(){  
 if (document.forms.formR.password2.innerHTML == document.forms.formR.password.innerHTML) 
            {
       document.forms.formR.password2.style.borderBottomColor="#f00";
        getTag('span',[5]).style.display="inline-block";    
            }
        else{
       document.forms.formR.password2.style.borderBottomColor="#fff";
       getTag('span',[5]).style.display="none";
            } 
}