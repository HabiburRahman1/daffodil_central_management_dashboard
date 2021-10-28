$('div.card').click(function() {
    var text = $(this).text();


    if (text.includes("New")){

        document.getElementById("table2").style.display="block";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
    }
    else if (text.includes("Work In Progress")){

        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="block";
        document.getElementById("table4").style.display="none";
    }
    else if (text.includes("Closed")){

        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="block";

    }
    else {
        console.log("Total")
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="block";
        document.getElementById("table3").style.display="none";
        document.getElementById("table4").style.display="none";
    }

});