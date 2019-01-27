var reglogin = document.getElementById("reglogin");
var regpassword = document.getElementById("regpassword");
var confirm_password = document.getElementById("confirm_password");
var email = document.getElementById("email");
var loginError = document.getElementById("login_error");
var emailError = document.getElementById("email_error");
var passwordError = document.getElementById("password_error");
var conPassError = document.getElementById("confirm_password_error");
var regsubmit = document.getElementById("regsubmit");
var passStr = document.getElementById("password_strength");
var regquestion = document.getElementById("regquestion");
var reganswer = document.getElementById("reganswer");
var question_error = document.getElementById("question_error");
var answer_error = document.getElementById("answer_error");

function Validate() {
  if (reglogin.value == "") {
    reglogin.style.border = "2px solid red";
    loginError.textContent = "Pole wymagane";
    return false;
  }

  if (email.value == "") {
    email.style.border = "2px solid red";
    emailError.textContent = "Pole wymagane";
    return false;
  }

  var emailRegex = /(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@[*[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+]*/
  if (!emailRegex.test(email.value)) {
    email.style.border = "2px solid red";
    emailError.textContent = "Pole niepoprawne";
    return false;
  }

  if (regpassword.value == "") {
    regpassword.style.border = "2px solid red";
    passwordError.textContent = "Pole wymagane";
    return false;
  }

  if (confirm_password.value == "") {
    confirm_password.style.border = "2px solid red";
    conPassError.textContent = "Pole wymagane";
    return false;
  }

  if (regpassword.value != confirm_password.value) {
    confirm_password.style.border = "2px solid red";
    conPassError.textContent = "Pole identyczne"
    return false;
  }

  if (regquestion.value == "") {
    regquestion.style.border = "2px solid red";
    question_error.textContent = "Pole wymagane";
    return false;
  }

  if (reganswer.value == "") {
    reganswer.style.border = "2px solid red";
    answer_error.textContent = "Pole wymagane";
    return false;
  }

}

function questionVerify() {
  if (regquestion.value != "") {
    regquestion.style.border = "2px solid #ccc";
    question_error.innerHTML = "";
    return true;
  }
}

function answerVerify() {
  if (reganswer.value != "") {
    reganswer.style.border = "2px solid #ccc";
    answer_error.innerHTML = "";
    return true;
  }
}

function loginVerify() {
  if (reglogin.value != "") {
    reglogin.style.border = "2px solid #ccc";
    loginError.innerHTML = "";
    return true;
  }
}

function emailVerify() {
  if (email.value != "") {
    email.style.border = "2px solid #ccc";
    emailError.innerHTML = "";
    return true;
  }
}

function passwordVerify() {
  if (regpassword.value != "") {
    regpassword.style.border = "2px solid #ccc";
    passwordError.innerHTML = "";
    return true;
  }
}

function conPasswordVerify() {
  if (confirm_password.value != "") {
    confirm_password.style.border = "2px solid #ccc";
    conPassError.innerHTML = "";
    return true;
  }
}

function checkPasswordStrength() {
  var strength = 0;
  if (regpassword.value.match(/[a-zA-Z0-9][a-zA-Z0-9]+/)) {
    strength += 1
  }
  if (regpassword.value.match(/[~<>?]+/)) {
    strength += 1
  }
  if (regpassword.value.match(/[!@$%^&*()]+/)) {
    strength += 1
  }
  if (regpassword.value.length > 5) {
    strength += 1
  }
  switch (strength) {
    case 0:
      passStr.textContent = ""
      break
    case 1:
      passStr.style.color = "#f44b42";
      passStr.textContent = "SŁABE";
      break
    case 2:
      passStr.style.color = "#f47741";
      passStr.textContent = "ŚREDNIE";
      break
    case 3:
      passStr.style.color = "#f4a341";
      passStr.textContent = "SILNE";
      break
    case 4:
      passStr.style.color = "#2d8e32";
      passStr.textContent = "BARDZO SILNE";
      break
  }
}

reglogin.addEventListener("blur", loginVerify);
email.addEventListener("blur", emailVerify);
regpassword.addEventListener("blur", passwordVerify);
confirm_password.addEventListener("blur", conPasswordVerify);
regpassword.addEventListener("keyup", checkPasswordStrength);
regquestion.addEventListener("keyup", questionVerify);
reganswer.addEventListener("keyup",answerVerify);