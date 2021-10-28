$('div.card').click(function() {
    var text = $(this).text();


    if (text.includes("Total Lead")){

        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="block";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Active Lead")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="block";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Lost Lead")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="block";

    }
    else if (text.includes("Pipe Line")){
        document.getElementById("table1").style.display="block";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Proposition")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="block";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Progress")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="block";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Won Opportunity")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="block";
        document.getElementById("table5").style.display="none";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }
    else if (text.includes("Lost Opportunity")){
        document.getElementById("table1").style.display="none";
        document.getElementById("table2").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
        document.getElementById("table5").style.display="block";
        document.getElementById("table6").style.display="none";
        document.getElementById("table7").style.display="none";
        document.getElementById("table8").style.display="none";
    }

});