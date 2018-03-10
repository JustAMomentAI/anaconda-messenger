function OnIdeaContentChanged(value){
    //counting num of words
    var count = 0;
    for(var i = 0; i<value.length ;i++){
        if(value[i] === " "){
            count++;
        }
    }
    count++;
    document.getElementById("idea-counting-words").innerHTML = (100 - count) + " words left";
    if(count === 100){
        document.getElementById("idea_content").disabled = true;
    }
}