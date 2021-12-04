const element = document.getElementById("create_qa");
        element.addEventListener("click", create_q_form);
        function create_q_form(){
            let element = document.getElementById("place_for_form");
            element.innerHTML += '<form action="create_q" method="post"> <input type="text" name="name_of_question" placeholder="вопрос?"> <input type="file" name="file"> </form> <button id="create_ans_form"> кнопка</button>';
        }
        const element = document.getElementById("create_ans_form");
        element.addEventListener("click", create_ans_form);
        function create_ans_form(){
            let element = document.getElementById("place_for_ans_form");
            element.innerHTML += '<form action="create_a" method="post"> <input type="text" name="name_of_ans" placeholder="вопрос?"> <input type="file" name="file"> </form> <button id="create_ans_form"> добавть ответ</button>';
        }