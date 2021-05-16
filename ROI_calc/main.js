function calculateROI() {
    var finalvalue, initialvalue, costofinvestment, returnofinvestment;
    finalvalue=Number(document.roicalc.inputfinalvalue.value);
    initialvalue=Number(document.roicalc.inputinitialvalue.value);
    costofinvestment=Number(document.roicalc.inputcostofinvestment.value);
    
    returnofinvestment = (finalvalue - initialvalue) / costofinvestment * 100;
    
    document.roicalc.resultreturnofinvestment.value=returnofinvestment;
    
};