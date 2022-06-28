

$(document).ready(function(){
  $('#btn').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $('#courses').attr("disabled", false);
      $("#btn").hide();
      $('#update_btn').show();
  });
});

$(document).ready(function(){
  $('#btn2').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $("#btn2").hide();
      $('#update_btn').show();
  });
});

