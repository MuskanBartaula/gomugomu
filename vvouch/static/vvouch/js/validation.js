$(document).ready(function(){

    var is_cod = $("#is_cod_input").val();
    if (is_cod === "Advance")
        $("#advancePayment").prop("checked", true);
    else if (is_cod === "Cash On Delivery")
        $("#cashondelivery").prop("checked", true);

    var payment_mode = $("#payment_mode_input").val();
    if (payment_mode === "Cash")
        $("#cashPayment").prop("checked", true);
    else if (payment_mode === "Card")
        $("#cardPayment").prop("checked", true);
    else if (payment_mode === "Both")
        $("#bothPayment").prop("checked", true);

    var is_secp = $("#business_type_input").val();
    if (is_secp)
        $('#is_secp').val("1");
    else
        $('#is_secp').val("0");


    $(".password-reset-btn").click(function(e) {
        e.preventDefault();
        var all_ok = true;
        var password = $("#password").val();
        var confirm_password = $("#confirm-password").val();
        if (!password) {
            $(".error").text("Please enter password.");
            $(".error").show();
            all_ok = false;
        }
        else if (!confirm_password) {
            $(".error").text("Please enter confirm password.");
            $(".error").show();
            all_ok = false;
        }
        else if (password !== confirm_password) {
            $(".error").text("Please enter the same password.");
            $(".error").show();
            all_ok = false;
        }
        if (all_ok) {
            $(".reset_form").submit();
        }
    });
});