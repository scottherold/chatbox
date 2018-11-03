


$(document).ready(function () {

    $(".commentBox").hide();

    $(".viewAll").click(function () {
        console.log("view all commment is click")
        // $(this).next('.replies').slideToggle("slow");
        $(this).parent().siblings('div.commentBox').slideToggle();

    })
   
    $(".postingButton").hide();

    $(".comment").click(function () {
        console.log(" commment is click")
        // $(this).next('.replies').slideToggle("slow");
        $(this).parent().siblings("div.postingButton").slideToggle();

    })

    $(".ReplyButton").hide();

    $(".reply").click(function () {
        console.log(" reply is click")
        // $(this).next('.replies').slideToggle("slow");
        $(this).parent().parent().next().slideToggle();

    })

    $(".replyBox").hide();

    $(".Allreply").click(function () {
        console.log(" view all reply is click")
        // $(this).next('.replies').slideToggle("slow");
        $(this).parent().parent().parent().siblings("div.replyBox").slideToggle();

    })


    // Profile effects for edit modal
    $(".editPasswordSection").hide();

    $("#passswordButton").click(function(){
        $(".editInfoSection").hide();
        $(".editPasswordSection").show("slide",{ direction: "right" });
    })
    $("#editButton").click(function(){

        $(".editInfoSection").show("slide");
        $(".editPasswordSection").hide();

    })
})