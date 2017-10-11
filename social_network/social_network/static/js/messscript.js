function getId(id){
    return document.getElementById(id);
}

function getTag(tag, number){
    return document.getElementsByTagName(tag)[number];
}

function getCl(ok, a){
    return document.querySelectorAll(ok)[a];
}

var arraymess = [];
getId('send').onclick = function(){
    var messBody = '<p align="right" class="text-success bg-success"> Я: ' + getId('message').value + '</p>';
    arraymess.push(messBody);
    var messagetext = arraymess.join('');
    getId('chatPlace').innerHTML = messagetext;
         
}



/*****************SEARCHFRIENDS*********************/
function myFunction() {
    
    var input, filter, ul, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}