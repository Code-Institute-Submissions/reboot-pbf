$(document).ready(function () {

    // Re-Boot trading years appear in the footer
     
    $('#trading-year').text('2019 - ' + new Date().getFullYear());
    
    // Shopping cart popover
    
    $('#cart-popover').popover({
        html : true,
        container: 'body',
        content: function() {
            return $('#popover_content_wrapper').html();
        }
    });
});