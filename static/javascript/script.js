let testInput = document.querySelector("#testInputAppend");
let testButton = document.querySelector("#testButton");
// messageTypes is for the list options, while messageType is for the specific selection
let messageTypes = document.querySelector("#message-types");
let messageType = document.querySelector("#message-type");
// messageChoices is for the list options, while messageChoice is for the specific selection
let messageChoices = document.querySelector("#message-choices");
// let messageChoice = document.querySelector("#message-choice");

greetings = [
    {
        "topic" : "Back to School",
        "generic_message" : 
        {
            "bland" : "Happy 1st Day!",
            "reassuring" : "You got this!",
            "optimistic" : "Today is a good day to change the world!",
            "questionable" : "180 more schools days until summer..."   
        }

    },
    {
        "topic" : "Anniversary",
        "generic_message" : 
        {
            "bland" : "Happy Anniversary!",
            "reassuring" : "Another Beautiful Year!",
            "optimistic" : "Just Us Forever!",
            "questionable" : "Still Stuck With Me I See..."   
        }
    },

    {
        "topic" : "Birthday",
        "generic_message" : 
        {
            "bland" : "Happy Birthday!",
            "upbeat" : "Go Shawty, It's Your Birthday!",
            "dad jokey" : "A long time ago, in a galaxy far, far away...you were born.",
            "questionable" : "Another year from the beginning; another year closer to the end..."   
        }
    },    

    {
        "topic" : "Graduation",
        "generic_message" : 
        {
            "bland" :  "You made it!",
            "optimistic" : "Oh! The Places You'll Go!",
            "dad jokey" : "You did virtually the best job ever, GRAD.",
            "questionable" : "Uh, so you can move out now, right?"   
        }
    },

    {
        "topic" : "Appreciation",
        "generic_message" : 
        {
            "bland" : "I appreciate you.",
            "optimistic" : "If only everyone were a little more like you.",
            "mawkish" : "You shine the brightest when the night is darkest.",
            "questionable" : "I choose you Pikachu!"   
        }
    },

    {
        "topic" : "Sympathy",
        "generic_message" : 
        {
            "bland" : "My condolences.",
            "reassuring" : "Our thoughts are with you.",
            "assuming" : "Anyone who has loved a lot knows how your heart is breaking.",
            "questionable" : "I'm sorry for your loss, but not sorry enough to pick up a phone and call you."   
        }
    }

]

function loadMessageChoices() {
    for(let i = 0; i < greetings.length; i++){
        messageTypes.innerHTML += "<option value = '" + greetings[i]["topic"] + "'>";
        console.log("<option value = '" + greetings[i]["topic"] + "'>");
    }
}

messageType.addEventListener("change", (e) =>{
    const messageTypeSelection = e.target.value;
    console.log(messageTypeSelection);

    const messageIndexCriteria = (e) => e["topic"] == messageTypeSelection;
    const messageIndex = greetings.findIndex(messageIndexCriteria);
    
    for(var key in greetings[messageIndex]["generic_message"]){
        messageChoices.innerHTML += `<option value = "${greetings[messageIndex]["generic_message"][key]}">`
    }
})



