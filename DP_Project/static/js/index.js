$(document).ready(function(){
  $.ajax({
        url:"http://127.0.0.1:8000/getinfo/",
        type:"GET",
        success: function (resp){
            if(resp.result == "success"){
                alert(resp.volume)
            }
        }
    })
});
