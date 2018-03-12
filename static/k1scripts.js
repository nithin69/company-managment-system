

$(document).ready(function(){


var $select = $(".remhrs");




for (i=0;i<=24;i++){
$select.append($('<option></option>').val(i).html(i))

}

$select.append("<option value='A'>A</option>")
$select.append("<option value='L'>L</option>")


});



$(document).ready(function(){

var k1ndate,k1date, k1id, k1val;
var k1days = document.getElementsByClassName("daterm");
for(var i = 0; i < k1days.length; i++)
{

k1date = k1days[i].textContent;


k1ndate = new Date(k1date); 
k1id = "." + k1days[i].classList[1];
if((k1ndate.getDay() == 0)) {
console.log("sunday " + k1ndate);
console.log(k1id);
$(k1id).css("background-color", "#FFA5A5");

}

}




});


 $(".remhrs").change(function(){   
     var tid =  $(this).attr('id').substr(4,7);
     var sbtn = "#save" + tid;    
     
   });  


$(".attsave").click(function(){          
    var tid =  $(this).attr('id').substr(4,9);      
     console.log(tid);


var chattn = [];
var chadat = [];

var chahrs = [];

    var obj0id = "#r0em" + tid;  

    var hr0 = $(obj0id).val();
    console.log("hr0 is", hr0);
if (hr0 != 0){
    console.log("changed" + obj0id);
    var date0id = ".d0ate" + tid;

	chattn.push(obj0id);
        var date0 = $(date0id).text()
	chadat.push(date0);
        console.log(" chaadat is", date0);

	chahrs.push(hr0);
}





var obj1id = "#r1em" + tid;  
    

    console.log(obj1id);
    var hr1 = $(obj1id).val();
    console.log("hr1 is", hr1);
if (hr1 != 0){
    console.log("changed" + obj1id);
    var date1id = ".d1ate" + tid;

	chattn.push(obj1id);
        var date1 = $(date1id).text()

	chadat.push(date1);
	chahrs.push(hr1);


}




var obj2id = "#r2em" + tid;  
    

    console.log(obj2id);
    var hr2 = $(obj2id).val();
if (hr2 != 0){
    console.log("changed" + obj2id);
    var date2id = ".d2ate" + tid;

	chattn.push(obj2id);
        var date2 = $(date2id).text()

	chadat.push(date2);
	chahrs.push(hr2);


}




var obj3id = "#r3em" + tid;  
    

    console.log(obj3id);
    var hr3 = $(obj3id).val();
if (hr3 != 0){
    console.log("changed" + obj3id);
    var date3id = ".d3ate" + tid;

	chattn.push(obj3id);
        var date3 = $(date3id).text()

	chadat.push(date3);
	chahrs.push(hr3);


}



var obj4id = "#r4em" + tid;  
    

    console.log(obj4id);
    var hr4 = $(obj4id).val();
if (hr4 != 0){
    console.log("changed" + obj4id);
    var date4id = ".d4ate" + tid;

	chattn.push(obj4id);
        var date4 = $(date4id).text()

	chadat.push(date4);
	chahrs.push(hr4);


}


var obj5id = "#r5em" + tid;  
    

    console.log(obj5id);
    var hr5 = $(obj5id).val();

if (hr5 != 0){
    console.log("changed" + hr5);
    var date5id = ".d5ate" + tid;

	chattn.push(obj5id);
        var date5 = $(date5id).text()
	chadat.push(date5);
	chahrs.push(hr5);


}
 console.log("chattn is", chadat);
    


 var empid = tid;
var workorder = $("#loca").val();
var locacid = $("#locacid").val();
var desig = $("#desig").text();
var csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
var savesuccess = "#savesuccess" + tid;
var succmsg = "Saved Successfully";
var start_date =  $("#start_date").val();
var tops_date =  $("#tops_date").val();
var locationsid =  $("#locationsid").val();
 
 console.log(desig);
 var updateurl = "/saveatt/"
$.post({url : updateurl, 
		data: { 
                'chattn[]' : chattn,
                'chadat[]' : chadat,
                'chahrs[]' : chahrs,
		'empid' : empid,
                desig: desig,
                workorder : workorder, 
                locacid : locacid,
                locationsid : locationsid, 
                start_date : start_date,
                tops_date : tops_date, 
                csrfmiddlewaretoken: csrfmiddlewaretoken  
 }, 
   success : function(data){
 		 $(savesuccess).delay(100).fadeIn('normal', function() {
    $(savesuccess).text(succmsg);
$(savesuccess).css("background-color", "yellow");
      $(savesuccess).delay(500).fadeOut();

var hrs0 =  data['hrs0'] + " Hrs";
var hrs1 =  data['hrs1'] + " Hrs";
var hrs2 =  data['hrs2'] + " Hrs";
var hrs3 =  data['hrs3'] + " Hrs";
var hrs4 =  data['hrs4'] + " Hrs";
var hrs5 =  data['hrs5'] + " Hrs";


var lcn0name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn0name'] + "     " +  data['hrs0'] + " Hrs   <br/>";
var lcn1name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn1name'] + "     " +  data['hrs1'] + " Hrs   <br/>";
var lcn2name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn2name'] + "     " +  data['hrs2'] + " Hrs   <br/>";
var lcn3name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn3name'] + "     " +  data['hrs3'] + " Hrs   <br/>";
var lcn4name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn4name'] + "     " +  data['hrs4'] + " Hrs   <br/>";
var lcn5name =  " &nbsp;&nbsp;   &nbsp;&nbsp;  " + data['lcn5name'] + "     " +  data['hrs5'] + " Hrs   <br/>";




var balancex =  data['balancex'];
var rotax =  data['rotax'];
var ttlhrs = data['ttlhrs'];


console.log("rotax", rotax);

console.log("blnc", balancex);


$('#rd0').text(rotax[0]);
$('#rd1').text(rotax[1]);
$('#rd2').text(rotax[2]);

$('#rd3').text(rotax[3]);
$('#rd4').text(rotax[4]);
$('#rd5').text(rotax[5]);



$('#bd0').text(balancex[0]);
$('#bd1').text(balancex[1]);
$('#bd2').text(balancex[2]);

$('#bd3').text(balancex[3]);
$('#bd4').text(balancex[4]);
$('#bd5').text(balancex[5]);

var glcn;

var k, i;
for (var k = 0; k < chattn.length; k++) {
    i = chattn[k][2];

    if (i == 0){
    $('#pr0' + tid).prepend(lcn0name);
    }

    if (i == 1){
    $('#pr1' + tid).prepend(lcn1name);
    }

    if (i == 2){
    $('#pr2' + tid).prepend(lcn2name);
    }

    if (i == 3){
    $('#pr3' + tid).prepend(lcn3name);
    }

    if (i == 4){
    $('#pr4' + tid).prepend(lcn4name);
    }

    if (i == 5){
    $('#pr5' + tid).prepend(lcn5name);
    }

}




$('#ttlhrs' + tid).text(ttlhrs);


console.log(lcn0name, lcn1name, lcn2name, lcn3name, lcn4name, lcn5name);


console.log(hrs0, hrs1, hrs2, hrs3, hrs4, hrs5);


var $select = $(".remhrs");



$select.val('0')
  


		    });

},

           error : function(status){
			alert("synceopod...");
		    }, 	

  });

});

