// Product backbone. Entirely related to the business rule
// That's why it is temporarily written in Brazilian Portuguese 

// Base
// const currentHour = now.getHours();
const currentHour = 8; // 8:00 (24h)
const currentMinute = 9;

// OnChange + OnListen
const tolerancia = 10;
const entrada = 8 * 60;
const intervaloSaida = 13 * 60;
const intervaloRetorno = 14 * 60;
const saida = 18 * 60;

// DB
const homeOffice = true;
const entradaFlexivel = false;
const almocoFlexivel = false;
const horaExtra = false;
const escalaEspecial = false;
const localExato = false;

var boolEntrada = false;
var boolIntervalo = false;
var boolIntervaloRetorno = false;
var boolSaida = false;

function verification() {
  // verifyOffline
  // verifyLocal();
  // verifyHours();
  verifyEvent();
}

function verifyLocal() {
  // Verify approximate / precise location, distance radius
}

function verifyOffline() {
  // Verify if the appointment was not settled because of internet / protocol issues   
}

function verifyHours() {
  // Compare server hour with device hour before everything else
}

function findEvent() {
  // Break in events
}

function verifyEvent() {
  const timeMin = currentHour * 60 + currentMinute;

  if (timeMin < entrada) {
    console.log('Not allowed');
  } else {
    if (entrada <= timeMin && timeMin <= entrada + tolerancia) {
      boolEntrada = true;
      sendDataToServer();
    } else {
      animation(true);
	  boolEntrada = true;
    }

    if (boolEntrada && boolIntervalo <= timeMin && timeMin <= intervaloSaida + tolerancia / 2) {
      boolIntervalo = true;
    } else {
      animation(true);
	  boolIntervalo = true;
    }

    if (boolEntrada && boolIntervalo && intervaloRetorno <= timeMin && timeMin <= intervaloRetorno + tolerancia / 2) {
      boolIntervaloRetorno = true;
      sendDataToServer();
	} else {
      animation(true);
	  boolIntervaloRetorno = true;
    }

    if (boolEntrada && boolIntervalo && saida <= timeMin && timeMin <= saida) {
      boolSaida = true;
	  sendDataToServer();
    } else {
      animation(true);
	  boolSaida = true;
    }
  }
}
