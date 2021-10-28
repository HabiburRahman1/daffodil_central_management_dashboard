$('div.card').click(function() {
    var text = $(this).text();


    if (text.includes("Total Present")){
        console.log("Total Present")
        document.getElementById("table2").style.display="block";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="none";
    }
    else if (text.includes("Total Absent")){
        console.log("Total Absent")
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="block";
    }
    else if (text.includes("Total Leave")){
        console.log("Total Leave")
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="none";
        document.getElementById("table3").style.display="none";

    }
    else {
        console.log("Total")
        document.getElementById("table2").style.display="none";
        document.getElementById("table1").style.display="block";
        document.getElementById("table3").style.display="none";
    }

});