let color = '#3aa757';

chrome.runtime.oninstalled.addListener[() => {

chrome.storage.sync.set[{color}];

console.log['Default background color set to %cgreen', `color:
${color}`]


}];

$('body').on('click', 'a[target="_blank"]', function(e){

    e.preventDefault();
    chrome.tabs.create({url: $(this).prop('href'), active: false});
    return false;

});