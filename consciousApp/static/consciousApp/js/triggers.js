const triggers = ["9 11", "9-11", "9/11", "ableism", "abusive", "ageism", "alcoholism", "animal abuse", "animal death", "animal violence", "bestiality", "gore", "corpse", "bully", "cannibal", "car accident", "child abuse", "childbirth", "classism", "death", "decapitation", "abuse", "drug", "heroin", "cocaine", "eating disorder", "anorexia", "binge eating", "bulimia", "fatphobia", "forced captivity", "holocaust", "hitler", "homophobia", "hostage", "incest", "kidnap", "murder", "nazi", "overdose", "pedophilia", "prostitution", "PTSD", "racism", "racist", "rape", "raping", "scarification", "self-harm", "self harm", "cutting", "sexism", "slavery", "slurs", "suicide", "suicidal", "swearing", "terminal illness", "terrorism", "torture", "transphobia", "violence", "warfare"];
const text = document.getElementById('exampleFormControlTextarea1').innerHTML.toLowerCase();

let foundTriggers = [];

triggers.forEach(findTrig);

function findTrig(value){
    if (text.indexOf(value)>-1){
        foundTriggers.push(value);
    }
}

alert(foundTriggers.join("\n"));