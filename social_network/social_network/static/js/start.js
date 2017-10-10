function fNSpan1(){
   
        if (document.forms.formR.username.innerHTML =='') 
            {
       document.forms.formR.username.style.borderBottomColor="#f00";
        getTag('span',[0]).style.display="inline-block";    

            }
        else{
       document.forms.formR.username.style.borderBottomColor="#fff";
       getTag('span',[0]).style.display="none";
            } 
}