function OnIdeaContentChanged(value){
    //counting num of words
    var count = 0;
    for(var i = 0; i<value.length ;i++){
        if(value[i] === " "){
            count++;
        }
    }
    count++;
    document.getElementById("idea-counting-words").innerHTML = count + "words left";
}