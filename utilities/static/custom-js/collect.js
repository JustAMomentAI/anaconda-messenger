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
function setMeeting(){
    var date = document.getElementById("meeting-date").value;
    var time =  document.getElementById("meeting-time").value;
    var content = document.getElementById("meeting-content").value;
    var note = document.getElementById("meeting-notes").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST","/utilities/meetingset", true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log("success");
        }
    };
    var data = JSON.stringify({
        date : date,
        time : time,
        content : content,
        note : note
    });
    xhr.send(data)
}