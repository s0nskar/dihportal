function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
}

function onSignIn(googleUser) {
  var id_token = googleUser.getAuthResponse().id_token;

  $.ajax({
    type: "POST",
    url: "/tokensignin",
    data: {
      'id_token': id_token,
      'csrfmiddlewaretoken': getCookie('csrftoken')
    },
    success: function(data) {
      if (data.success){
        console.log('Logging you in....')
      } else {
        console.log(data.error);
      }
    },
  });
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
}
