async function getFormValue(e) {
    e.preventDefault();
    let formValue = $('.input-guess').val()
    let sendVal = await axios.post("/guess", {guess: formValue})
    // remember that 2nd argument in axios wants an object
    // server also wants an object to parse into a string
}

$('#input-form').on('submit', getFormValue)