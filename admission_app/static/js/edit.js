

$(document).ready(function(){
  $('#btn').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $('#courses').attr("disabled", false);
      $("#btn").hide();
      $('#update_btn').show();
  });
});
