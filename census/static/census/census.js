//Function to make all of same type equal height
equalheight = function (container) {
    var currentTallest = 0,
        currentRowStart = 0,
        rowDivs = [],
        $el,
        topPosition = 0;
    $(container).each(function () {

        $el = $(this);
        $($el).height('auto');
        topPostion = $el.position().top;

        if (currentRowStart !== topPostion) {
            for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
                rowDivs[currentDiv].height(currentTallest);
            }
            rowDivs.length = 0; // empty the array
            currentRowStart = topPostion;
            currentTallest = $el.height();
            rowDivs.push($el);
        } else {
            rowDivs.push($el);
            currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
        }
        for (currentDiv = 0; currentDiv < rowDivs.length; currentDiv++) {
            rowDivs[currentDiv].height(currentTallest);
        }
    });
};

$(document).ready(function () {
    //Keeps all census view cards the same
    equalheight('.csview_card');

    //Add OC rate and VC Rate to headers
    $("#census_view tr:first").append("<th>Occupancy Rate</td><th>Vacancy Rate</td>");

    //Calculate Occupancy rate and Vacancy Rates
    $("#census_view tbody tr").each(function () {
        var h1_val = parseInt($(this).find(".H0030001").text());
        var h2_val = parseInt($(this).find(".H0030002").text());
        var h3_val = parseInt($(this).find(".H0030003").text());

        var oc_rate = Math.floor((h2_val / h1_val) * 100);
        var vc_rate = Math.floor((h3_val / h1_val) * 100);

        $(this).append("<td>" + oc_rate + "%</td><td>" + vc_rate + "%</td>");
    });

    $(window).load(function () {

        //create datatable
        var table = $('#census_view').DataTable({
            "fnInitComplete": function (oSettings, json) {
                $('#census_view').fadeIn(500);
            }
        });

        //make datatable responsive
        new $.fn.dataTable.Responsive(table, {
        });

    });

    $(window).resize(function () {
        equalheight('.csview_card');
    });

});
