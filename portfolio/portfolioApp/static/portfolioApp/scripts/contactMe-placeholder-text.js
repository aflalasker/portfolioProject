console.log('placeholder JavaScript field')

function setPlaceholderText() {
    document.getElementById('id_name').placeholder = 'NAME';
    document.getElementById('id_email').placeholder = 'EMAIL';
    document.getElementById('id_subject').placeholder = 'SUBJECT';
    document.getElementById('id_message').placeholder = 'MESSAGE';
}

setPlaceholderText();

function isHidden(element) {
    return (element.offsetParent == null)
}


function clearInputFields() {
   var success = document.querySelector('li');

   if (isHidden(success) != true) {
       document.getElementById('id_name').value = '';
       document.getElementById('id_email').value = '';
       document.getElementById('id_subject').value = '';
       document.getElementById('id_message').value = '';
   }

   console.log(isHidden(success))
}

clearInputFields();