// $(function () {
//     //Json data by api call for order table
//     $.get(orderListApiUrl, function (response) {
//         if(response) {
//             var table = '';
//             var totalCost = 0;
//             $.each(response, function(index, order) {
//                 totalCost += parseFloat(order.total);
//                 table += '<tr>' +
//                     '<td>'+ order.datatime +'</td>'+
//                     '<td>'+ order.order_id +'</td>'+
//                     '<td>'+ order.customer_name +'</td>'+
//                     '<td>'+ order.total.toFixed(2) +' Rs</td></tr>';
//             });
//             table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Rs</b></td></tr>';
//             $("table").find('tbody').empty().html(table);
//         }
//     });
// });

$(function () {
  const baseUrl = isLocal ? 'http://127.0.0.1:5000' : 'https://grocery-backend-v3yy.onrender.com';
  var orderListApiUrl = `${baseUrl}/getAllOrders`; // Defined URL
  $.get(orderListApiUrl, function (response) {
    console.log("Response:", response); // Debug the response
    if (response && response.length > 0) {
      var table = "";
      var totalCost = 0;
      $.each(response, function (index, order) {
        totalCost += parseFloat(order.total);
        table +=
          "<tr>" +
          "<td>" +
          (order.datatime || "N/A") +
          "</td>" +
          "<td>" +
          order.order_id +
          "</td>" +
          "<td>" +
          order.customer_name +
          "</td>" +
          "<td>" +
          order.total.toFixed(2) +
          " Rs</td></tr>";
      });
      table +=
        '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' +
        totalCost.toFixed(2) +
        " Rs</b></td></tr>";
      $("table").find("tbody").empty().html(table);
    } else {
      $("table")
        .find("tbody")
        .html(
          '<tr><td colspan="4" class="text-center">No orders found</td></tr>'
        );
    }
  }).fail(function (error) {
    console.log("AJAX Error:", error);
    $("table")
      .find("tbody")
      .html(
        '<tr><td colspan="4" class="text-center">Error loading orders</td></tr>'
      );
  });
});
