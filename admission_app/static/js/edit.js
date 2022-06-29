


// update btn if the user not approved yet
$(document).ready(function(){
  $('#btn').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $('#courses').attr("disabled", false);
      $('#cv').attr("disabled", false);
      $("#btn").hide();
      $('#update_btn').show();
      $('#viewer').hide();
      
  });
});

// update btn if the user approved 
$(document).ready(function(){
  $('#btn2').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $('#cv').attr("disabled", false);
      //$('#cv-label').removeClass("disabled");
      $("#btn2").hide();
      $('#update_btn').show();
  });
});










