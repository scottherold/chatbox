


$(document).ready(function () {
   

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

    // unfriend effects
    
    $(".friendBTN").hover(
        function(){
            $(".fa-user-friends+span").text("Unfriend");
            $(this).removeClass( "btn-primary" );
            $(this).toggleClass( "btn-warning" );
        }, 
        function(){
            $(".fa-user-friends+span").text("Friend");
            $(this).removeClass( "btn-warning" );
            $(this).toggleClass( "btn-primary" );

        } 
        
    );

     //ajaxx for like button for post

     $("#postContent").on('click','.like',function(e){
        e.preventDefault()
        var totalLikes=0;
        $.ajax({
            method:"GET",
            url:$(this).attr("href"),
            success:function(response){
                totalLikes=response.total_likes
            },
            async:false
            
        });
        
        $(this).closest("div.row").prevAll("div.postInfo").first().find("span.PostlikeCount").html(totalLikes);
    });


    //ajaxx for like button for comment

    $("#postContent").on('click','.comment_like',function(e){
        e.preventDefault()
        var totalLikes=0;
        $.ajax({
            method:"GET",
            url:$(this).attr("href"),
            success:function(response){
                totalLikes=response.total_likes
            },
            async:false
            
        });
        
        $(this).parent("span").nextAll(".commentLike").children(".commentLikeCount") .html(totalLikes);
    });
    
    
});