window.addEvent('domready', function(){
    // execution
    var number="";
    var operation="";
    var previous_value="0";
     $('screen').focus();
    
    $('add-button').addEvent('click', function(){
        number = document.calc.wtcalc.value;
        operation="+";
		document.calc.wtcalc.value='';                        
         $('screen').focus();  
        
    });
    $('subtract-button').addEvent('click', function(){
        number = document.calc.wtcalc.value;
        operation="-";
        document.calc.wtcalc.value='';                       
         $('screen').focus();  
        
    });
    $('multiply-button').addEvent('click', function(){
        number = document.calc.wtcalc.value;
        operation="*";
        document.calc.wtcalc.value='';
        $('screen').focus();
    });
    $('division-button').addEvent('click', function(){
        number = document.calc.wtcalc.value;
        operation="/";
        document.calc.wtcalc.value='';
        $('screen').focus();
    });
    $('c').addEvent('click', function(){
        document.calc.wtcalc.value = previous_value;
        $('screen').focus();
       
    });
    $('calculate').addEvent('click', function(){
        var last = $('screen').value;
        document.calc.wtcalc.value= eval(number+operation+last);
      
        $('screen').focus();
    });
    
    
});
