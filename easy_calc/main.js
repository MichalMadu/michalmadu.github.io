function sumValues() {
    var num1, num2, oper, res;
    num1=Number(document.formcalc.txtnum1.value);
    num2=Number(document.formcalc.txtnum2.value);
    res = num1 + num2;
    document.formcalc.txtres.value=res;
};