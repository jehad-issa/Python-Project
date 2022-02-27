$(document).ready(function(){
    $("#select").on("change", function() {
        var value = $(this).val()
        $("#section form").filter(function() {
            $(this).toggle($(this).text().indexOf(value) > -1)
        });
    });
});