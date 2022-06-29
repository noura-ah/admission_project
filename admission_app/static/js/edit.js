

$(document).ready(function(){
  $('#btn').click(function(){
      $("input[name='first_name']").attr('readonly', false); 
      $("input[name='last_name']").attr('readonly', false); 
      $('#courses').attr("disabled", false);
      $('#cv').attr("disabled", false);
      //$('#cv').closest('label').removeClass('disabled btn btn-info text-light mt-3 mb-3');
      //$('#cv-label').removeClass("disabled");
      $("#btn").hide();
      $('#update_btn').show();
  });
});

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



