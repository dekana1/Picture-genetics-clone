var parent_coll = document.getElementsByClassName('parent-collapsible');
var i;
for (i = 0; i < parent_coll; i++){
    parent_coll[i].addEventListener("click", function(){
        this.classList.toggle("active");
        var parent_content = this.nextElementSibling;
        if (parent_content.style.display === "block") {
            parent_content.style.display = 'none';
        } else{
            parent_content.style.display = "block";
        }
    });
}

var child_coll = document.getElementsByClassName('child-collapsible');
var j;
for (j = 0; j < child_coll; j++){
    child_coll[j].addEventListener("click", function(){
        this.classList.toggle("active");
        var child_content = this.nextElementSibling;
        if (child_content.style.display === "block") {
            child_content.style.display = 'none';
        } else{
            child_content.style.display = "block";
        }
    });
}

