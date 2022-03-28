$(function () {
    $.ajax({
        url:"http://127.0.0.1:8000/getinfo/",
        type:"GET",
        data:{
            platform:"web",
        },
        success: function (resp){
            alert(resp.volume)
        }
    })
})