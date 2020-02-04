function validate_form(){
    var basic_result = valiate_ifexist(['username','password','confirm_password',
                            'supplier_id','supplier_name','supplier_address',
                            'supplier_TINnum','supplier_CSTnum',
                            'supplier_email','supplier_contact',
                            'cash','quote_id','requisition_reason']);
                            
         
    if  (basic_result != true ){
        return basic_result;
    }
    
    var result_email = validate_email (['supplier_email',]);
    
    if  (result_email != true ){
        return result_email;
    } 
    var result_contact = validate_contact (['supplier_contact',]);
    
    if  (result_contact != true ){
        return result_contact;
    } 
    
    var result_digit = validate_digit(['cash', ]);
    if  (result_digit != true ){
        return result_digit;
    } 
    
    var purchases =document.getElementsByClassName('purchase_digit');       
    for ( var i = 0; i < purchases.length ; i++ ){          
        var basic_result = valiate_ifexist([purchases[i].id,]);
        if  (basic_result != true ){
            return basic_result;
        }
        
        var result_digit = validate_digit([purchases[i].id,]);
        if  (result_digit != true ){
            return result_digit;
        }     
    }

    purchases =document.getElementsByClassName('purchase');       
    for ( var i = 0; i < purchases.length ; i++ ){          
        var basic_result = valiate_ifexist([purchases[i].id,]);
        if  (basic_result != true ){
            return basic_result;
        }   
    }
    return true;
    //Below methods should be hosted in another common file.
    
    function validate_digit(field){
        for ( var i = 0; i < field.length ; i++ ){          
            if (document.getElementById(field[i])) {
                var field_val = document.getElementById(field[i]).value;
                var re_validate = /[^\d\.]+/ ;
                if (re_validate.exec(field_val)){
                    var field_name_error = field[i].replace("_"," ") + " : ";
                    document.getElementById('error_message').innerHTML =  field_name_error + ": Expected only digits";
                    return false;
                }                
            }
        }
        return true;
    };
    
    function validate_GST(field){

        for ( var i = 0; i < field.length ; i++ ){
            if (document.getElementById(field[i])) {
                var field_val = document.getElementById(field[i]).value;
                if (field_val.length != 15){
                    document.getElementById('error_message').innerHTML =  "GST number should be of 15 digits";
                    return false;
                }
            }
        }
        return true;
    };
    
    function validate_email(field){

        for ( var i = 0; i < field.length ; i++ ){
            if (document.getElementById(field[i])) {
                var field_val = document.getElementById(field[i]).value;
                if (! /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(field_val)){  
                    document.getElementById('error_message').innerHTML =  "Entered Email ID is invalid";
                    return false;
                }
            }
        }
        return true;
    };
    
    var result_contact = validate_contact (['supplier_contact',]);
    
    if  (result_contact != true ){
        return result_contact;
    } 
    
    var result_contact = validate_GST (['supplier_GSTnum',]);
    
    if  (result_contact != true ){
        return result_contact;
    }     
        
    function validate_contact(field){

        for ( var i = 0; i < field.length ; i++ ){
            if (document.getElementById(field[i])) {
                var field_val = document.getElementById(field[i]).value;
                if  ((! /[\+\d]+/.test(field_val)) ||  (field_val.length <9) || (field_val.length > 13)){  
                    document.getElementById('error_message').innerHTML =  "Entered Phone contact is invalid";
                    return false;
                }
            }
        }
        return true;
    };
    
    
    function valiate_ifexist(field){
        for ( var i = 0; i < field.length ; i++ ){
            if (document.getElementById(field[i])) {
                var result_basics =  validate_basics (field[i]);
                if (result_basics != true){
                    return result_basics;  
                }
            }
        }
        return true
    };
    
    function validate_basics(field){
            var field_val = document.getElementById(field).value;
            var field_name_error = field.replace("_"," ") + " : "

            var result = [validate_empty(field_val),validate_en(field_val),validate_length(field_val)]            
            for ( var i = 0; i < result.length ; i++ ){
                if (result[i] != true){                    
                    document.getElementById('error_message').innerHTML =  field_name_error + result[i];
                    return false;
                }
            }
            return true;
    };
  
    function validate_empty(field_val){
        if (field_val==""){
             return "No input provided";
        }else {
            return true;
        }
    };
    
    function validate_length(field_val){
        if (field_val.length > 250 ){
             return "Field text exceeded 250 letters";
        }else {
            return true;
        }
    };
    
    function validate_en(field_val){
        
        var re_validate_en = /([^\x00-\x7F])+/ ;
        if (re_validate_en.exec(field_val)){
             return "Use the keyboard characters.Please reach out to VEvolve if you need support for other letters";
        }else {
            return true;
        }
    };
    
    return true;
};
