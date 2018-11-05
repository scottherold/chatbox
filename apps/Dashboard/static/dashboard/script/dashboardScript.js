


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
    
    
});