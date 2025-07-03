// Detect if running locally (e.g., file:// or localhost)
const isLocal = window.location.hostname === 'localhost' || window.location.protocol === 'file:';
const baseUrl = isLocal ? 'http://127.0.0.1:5000' : 'https://grocery-backend-v3yy.onrender.com';
console.log('Base URL:', baseUrl); // Add this line
var productListApiUrl = `${baseUrl}/getProducts`;
// Define your APIs here
var uomListApiUrl = `${baseUrl}/getUOM`;
var productSaveApiUrl = `${baseUrl}/insertProduct`;
var productDeleteApiUrl = `${baseUrl}/deleteProduct`;
var orderListApiUrl = `${baseUrl}/getAllOrders`;
var orderSaveApiUrl = `${baseUrl}/insertOrder`;

// For product drop in order (external API, keep separate)
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    }).fail(function(xhr, status, error) {
        console.error('API Error:', error);
        alert('Failed to process request. Check console for details.');
    });
}

function calculateValue() {
    var total = 0;
    $(".product-item").each(function( index ) {
        var qty = parseFloat($(this).find('.product-qty').val());
        var price = parseFloat($(this).find('#product_price').val());
        price = price*qty;
        $(this).find('#item_total').val(price.toFixed(2));
        total += price;
    });
    $("#product_grand_total").val(total.toFixed(2));
}

function productParser(product) {
    return {
        id: product.product_id,
        name: product.name,
        unit: product.uom_name,
        price: product.price_per_unit
    };
}

function orderParser(order) {
    return {
        id: order.order_id,
        date: order.datatime || 'N/A',
        orderNo: order.order_id,
        customerName: order.customer_name || 'N/A',
        cost: parseFloat(order.total) || 0
    };
}
function productDropParser(product) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });