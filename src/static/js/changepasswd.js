var regpassword = document.getElementById("regpassword");
var confirm_password = document.getElementById("confirm_password");
var oldpassword = document.getElementById("oldPassword");

var passwordError = document.getElementById("password_error");
var conPassError = document.getElementById("confirm_password_error");
var old_passwordError = document.getElementById("old_password_error")

var passStr = document.getElementById("password_strength");


function Validate() {

  if (oldpassword != null) {
    if (oldpassword.value == "") {
      oldpassword.style.border = "1px solid red";
      old_passwordError.textContent = "To pole jest wymagane";
      return false;
    }
  }

  if (regpassword.value == "") {
    regpassword.style.border = "1px solid red";
    passwordError.textContent = "To pole jest wymagane";
    return false;
  }

  if (confirm_password.value == "") {
    confirm_password.style.border = "1px solid red";
    conPassError.textContent = "To pole jest wymagane";
    return false;
  }

  if (regpassword.value != confirm_password.value) {
    confirm_password.style.border = "1px solid red";
    conPassError.textContent = "Hasła nie są identyczne"
    return false;
  }
}

function oldPasswordVerify() {
  if (oldpassword.value != "") {
    oldpassword.style.border = "1px solid #ccc";
    old_passwordError.innerHTML = "";
    return true;
  }
}

function passwordVerify() {
  if (regpassword.value != "") {
    regpassword.style.border = "1px solid #ccc";
    passwordError.innerHTML = "";
    return true;
  }
}

function conPasswordVerify() {
  if (confirm_password.value != "") {
    confirm_password.style.border = "1px solid #ccc";
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
      passStr.textContent = "Siła hasła: SŁABE";
      break
    case 2:
      passStr.style.color = "#f47741";
      passStr.textContent = "Siła hasła: ŚREDNIE";
      break
    case 3:
      passStr.style.color = "#f4a341";
      passStr.textContent = "Siła hasła: SILNE";
      break
    case 4:
      passStr.style.color = "#2d8e32";
      passStr.textContent = "Siła hasła: BARDZO SILNE";
      break
  }
}

if (oldpassword != null) {
  oldpassword.addEventListener("blur", oldPasswordVerify);
}

regpassword.addEventListener("blur", passwordVerify);
confirm_password.addEventListener("blur", conPasswordVerify);
regpassword.addEventListener("keyup", checkPasswordStrength);