const API = "http://127.0.0.1:81"
let manaZina = document.querySelector('.info')
let chataZinas = document.querySelector('.chataZinas')
let vards = document.querySelector('.name')

function sutitZinu(){
    console.log("sutitzinu() darbojas")
    chataZinas.innerHTML += '<br/>' + manaZina.value
    fetch(API+'/sutit/'+vards.value+'/'+manaZina.value)
}

async function ieladetChataZinas(){
    let datiNoServera = await fetch(API + '/lasit')
    let dati = await datiNoServera.text()
    console.log(dati)

    chataZinas.innerHTML = dati

  
}

// setInterval(ieladetChataZinas, 1000)

async function ieladetChataZinasJson(){
    let datiNoServera = await fetch(API + '/lasit')
    let dati = await datiNoServera.json()

chataZinas.innerHTML = ''

    i=0;
    while(i < await dati.length){

        chataZinas.innerHTML = chataZinas.innerHTML + dati(i)['laiks'] + dati(i)['vards'] + ': ' + dati(i)['zina'] 
        i += 1
    }
}