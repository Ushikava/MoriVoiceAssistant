function getRandomId(max) {
  return Math.floor(Math.random() * max);
}

async function send_text_msg(){
    
    var tag = document.createElement("p");
    var text = document.createTextNode(document.getElementById("id_msg").value);
    tag.style.padding = ('padding', '20px')
    tag.style.color = ('color', '#000000');
    tag.style.backgroundColor = ('background color', '#A3BEFF');
    tag.style.borderStyle = ('border style', 'solid');
    tag.style.borderColor = ('border color','0C213F');
    tag.style.borderRadius = ('border radius', '15px');
    tag.style.width = ('width', '110ch');
    tag.appendChild(text);
    var element = document.getElementById("messenger_id");
    element.appendChild(tag);

    var message = document.getElementById("id_msg").value;

    document.getElementById("id_msg").value = "";

    var tag = document.createElement("p");
    //var id = '' + getRandomId(10000);
    //tag.id = id;
    var text = document.createTextNode("Генерирую ответ...");
    tag.style.padding = ('padding', '20px');
    tag.style.color = ('color', '#FFFFFF');
    tag.style.backgroundColor = ('background color', '#0C213F');
    tag.style.borderStyle = ('border style', 'solid');
    tag.style.borderColor = ('border color','#A3BEFF');
    tag.style.borderRadius = ('border radius', '15px');
    tag.style.width = ('width', '110ch');
    tag.appendChild(text);
    var element = document.getElementById("messenger_id");
    element.appendChild(tag);

    let result = await eel.send_message(message)();

    var answer_tag = document.createElement("p");
    var answer_text = document.createTextNode(result);
    answer_tag.style.padding = ('padding', '20px');
    answer_tag.style.color = ('color', '#FFFFFF');
    answer_tag.style.backgroundColor = ('background color', '#0C213F');
    answer_tag.style.borderStyle = ('border style', 'solid');
    answer_tag.style.borderColor = ('border color','#A3BEFF');
    answer_tag.style.borderRadius = ('border radius', '15px');
    answer_tag.style.width = ('width', '110ch');
    answer_tag.appendChild(answer_text);

    element.replaceChild(answer_tag, tag);

    await eel.msg_reader(result)();
}

async function send_voice_msg(){
    let result = await eel.send_voice_message()();

    var tag = document.createElement("p");
    var text = document.createTextNode(result);
    tag.style.color = ('color', '#FFFFFF');
    tag.style.backgroundColor = ('background color', '#6993bf');
    tag.appendChild(text);
    var element = document.getElementById("messenger_id");
    element.appendChild(tag);
}

async function msg_length_change(){
    var new_value = document.getElementById("msg_length").value;
    await eel.max_length_change(new_value);
}

async function msg_repetition_change(){
    var new_value = document.getElementById("msg_repetition").value;
    await eel.repetition_penalty_change(new_value);
}

async function msg_top_k_change(){
    var new_value = document.getElementById("msg_top_k").value;
    await eel.top_k_change(new_value);
}

async function msg_top_p_change(){
    var new_value = document.getElementById("msg_top_p").value;
    await eel.top_p_change(new_value);
}

async function msg_temperature_change(){
    var new_value = document.getElementById("msg_temperature").value;
    await eel.temperature_change(new_value);
}