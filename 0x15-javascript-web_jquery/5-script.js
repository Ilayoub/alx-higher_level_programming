// JavaScript script that adds a <li> element to a list when
// the user clicks on the tag DIV#add_item

$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });
