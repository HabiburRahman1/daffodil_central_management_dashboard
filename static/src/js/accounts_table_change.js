$('div.card').click(function() {
    var text = $(this).text();

    if (text.includes("Total Income")){
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="block";
        document.getElementById("table3").style.display="none";
    }
    else if (text.includes("Cost of Good Sold")){
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="block";
    }
    else if (text.includes("Total Expense")){
        document.getElementById("table2").style.display="block";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="none";

    }

});