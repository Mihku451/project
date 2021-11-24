"use strict";
let forms_container = document.querySelector('.forms');
let forms = document.querySelectorAll('.forms > div');
let selected = 0;

//# Открыть нужную по счету форму (от 0 до кол-ва форм)
function selectForm(index) {
    for (let i = 0; i < forms.length; i++) {
        if (i < index) {
            forms[i].classList.remove('toright');
            forms[i].classList.add('toleft');
        }
        else if (i > index) {
            forms[i].classList.add('toright');
            forms[i].classList.remove('toleft');
        } else{
            forms[i].classList.remove('toright');
            forms[i].classList.remove('toleft');
        }
    }
}

selectForm(selected);
let pg_switcher_1 = document.querySelectorAll('#pg-1');
pg_switcher_1.forEach((el) => {
    el.addEventListener('click', () => {
        selected = 0
        selectForm(selected);
    });
})


let pg_switcher_2 = document.querySelectorAll('#pg-2');
pg_switcher_2.forEach((el) => {
    el.addEventListener('click', () => {
        selected = 1
        selectForm(selected);
    });
})
//# у нас пока нет верификации, поэтому пусть весит без дела
let pg_switcher_3 = document.querySelectorAll('#pg-3');
pg_switcher_3.forEach((el) => {
    el.addEventListener('click', () => {
        selected = 2
        selectForm(selected);
    });
})
//# Шобы крутилось кароч для теста
// setInterval(() => {
 //    selectForm(selected);
   //  selected = (selected + 1) % 3
//}, 1000)

//#region AUTH 

let login_submit = document.getElementById('submit-login');

login_submit.addEventListener('click', async function() {
    let response = await $.ajax({
        url: 'https://127.0.0.1/response.json'
    }) 

    console.log(response);
});

//#endregion

