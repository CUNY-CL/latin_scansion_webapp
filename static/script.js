$(document).ready(function() {
    $('.tabs li').click(function(){
      if ($(this).hasClass('selected')===false) {
        $('.tabs li').removeClass('selected');
        $(this).addClass('selected');
      }
      var selectionId = $(this).attr('id');
      $('.content').fadeOut('fast', function(){
        $('div .page').css('display','none');
        $('.page#'+selectionId).css('display','block');
        $('.content').fadeIn('fast');
      });
    });
  });
/* 
  $(document).on('submit','#form',function(e) 
  {
        e.preventDefault();
        $.ajax({
          type: "POST",
          url: "/result.html",
          dataType: 'html',
          success: function (data) {
            console.log('success');
            $('#page.tab1').html(data);
          }
        });
      });
 */
