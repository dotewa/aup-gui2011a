				
window.addEvent('domready', function(){
	            var average=0;
	            var total=0;
				var two=0;
				var three=0;
				var four=0;
                var one = 0;
        $('count-button').addEvent('click', function(){
				
                var count = 0;
                
                
                $('students').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                              one= 60;                       
                              total=one+two+three+four;
                              average=total/count;
                       }else
                       {one=0;}
                       
                       
                       
                });
                $('count-textbox').set('text',average);
        });
         $('count-button1').addEvent('click', function(){
               
               var count = 0	;
            
                $('students').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                                two= 60;
                                total=one+two+three+four;
                                average=total/count;
                       }else
                       {two=0;}
                });
                $('count-textbox').set('text',average);
        });
         $('count-button2').addEvent('click', function(){
                
                var count = 0	;
            
                $('students').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
								three= 60;
								total=one+two+three+four;
                                average=total/count;
                       }else
                       {three=0;}
                       
                });
                $('count-textbox').set('text',average);
        });
         $('count-button3').addEvent('click', function(){
				
                var count = 0;
            
                $('students').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
							    four= 60;
							    total=one+two+three+four;
                                average=total/count;
                      }else if(e.type == 'checkbox' && e.unchecked)
                      {four=0;
                      total=0;}
                });
                $('count-textbox').set('text',average);
        });
        
});


