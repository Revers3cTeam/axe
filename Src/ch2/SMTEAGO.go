package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"github.com/gorilla/securecookie"
	"net/http"
)

var cookieHandler = securecookie.New(
	securecookie.GenerateRandomKey(64),
	securecookie.GenerateRandomKey(32))

func getUserName(request *http.Request) (userName string) {
	if cookie, err := request.Cookie("session"); err == nil {
		cookieValue := make(map[string]string)
		if err = cookieHandler.Decode("session", cookie.Value, &cookieValue); err == nil {
			userName = cookieValue["name"]
		}
	}
	return userName
}

func setSession(userName string, response http.ResponseWriter) {
	value := map[string]string{
		"name": userName,
	}
	if encoded, err := cookieHandler.Encode("session", value); err == nil {
		cookie := &http.Cookie{
			Name:  "session",
			Value: encoded,
			Path:  "/",
		}
		http.SetCookie(response, cookie)
	}
}

func clearSession(response http.ResponseWriter) {
	cookie := &http.Cookie{
		Name:   "session",
		Value:  "",
		Path:   "/",
		MaxAge: -1,
	}
	http.SetCookie(response, cookie)
}

// login handler

func loginHandler(response http.ResponseWriter, request *http.Request) {
	name := request.FormValue("name")
	redirectTarget := "/"
	if name != "" {
		setSession(name, response)
		redirectTarget = "/check"
	}
	http.Redirect(response, request, redirectTarget, 302)
}

// logout handler

func logoutHandler(response http.ResponseWriter, request *http.Request) {
	clearSession(response)
	http.Redirect(response, request, "/", 302)
}

// index page

const indexPage = `
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>SM TEA GO!</title>
  <style>
      @import url(https://fonts.googleapis.com/css?family=Roboto:300);
      .login-page {
        width: 360px;
        padding-top: 35px;
        padding-right: 20px;
        padding-bottom: 20px;
        padding-left: 20px;
        max-width: 500px;
        margin: auto;
      }
      .form {
        position: relative;
        z-index: 1;
        background: #FFFFFF;
        max-width: 360px;
        margin: 0 auto 100px;
        padding: 45px;
        text-align: center;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
      }
      .form input {
        font-family: "Roboto", sans-serif;
        outline: 0;
        background: #f2f2f2;
        width: 100%;
        border: 0;
        margin: 0 0 15px;
        padding: 15px;
        box-sizing: border-box;
        font-size: 14px;
      }
      .form button {
        font-family: "Roboto", sans-serif;
        text-transform: uppercase;
        outline: 0;
        background: #4CAF50;
        width: 100%;
        border: 0;
        padding: 15px;
        color: #FFFFFF;
        font-size: 14px;
        -webkit-transition: all 0.3 ease;
        transition: all 0.3 ease;
        cursor: pointer;
      }
      .form button:hover,.form button:active,.form button:focus {
        background: #43A047;
      }
      .form .message {
        margin: 15px 0 0;
        color: #b3b3b3;
        font-size: 12px;
      }
      .form .message a {
        color: #4CAF50;
        text-decoration: none;
      }
      .form .register-form {
        display: none;
      }
      .container {
        position: relative;
        z-index: 1;
        max-width: 300px;
        margin: 0 auto;
      }
      .container:before, .container:after {
        content: "";
        display: block;
        clear: both;
      }
      .container .info {
        margin: 50px auto;
        text-align: center;
      }
      .container .info h1 {
        margin: 0 0 15px;
        padding: 0;
        font-size: 36px;
        font-weight: 300;
        color: #1a1a1a;
      }
      .container .info span {
        color: #4d4d4d;
        font-size: 12px;
      }
      .container .info span a {
        color: #000000;
        text-decoration: none;
      }
      .container .info span .fa {
        color: #EF3B3A;
      }
      body {
        background: #76b852; /* fallback for old browsers */
        background: -webkit-linear-gradient(right, #76b852, #8DC26F);
        background: -moz-linear-gradient(right, #76b852, #8DC26F);
        background: -o-linear-gradient(right, #76b852, #8DC26F);
        background: linear-gradient(to left, #76b852, #8DC26F);
        font-family: "Roboto", sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;      
      }
  </style>
</head>
<body>

<div class="login-page">
  <div class="form">
    <form method="post" action="/login" class="login-form">
      <input type="text" placeholder="Administrator" disabled/>
      <input type="password" id="name" name="name" placeholder="password"/>
      <button type="submit">Login</button>
    </form>
  </div>
</div>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  <script>
    $('.message a').click(function(){
      $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });
  </script>
</body>
</html>
`


func indexPageHandler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, indexPage)
}


func checkPageHandler(response http.ResponseWriter, request *http.Request) {
	// Administrator
	// [65 100 109 105 110 105 115 116 114 97 116 111 114]
	// G015C0Nfu51ng
	// [71 48 49 53 67 48 78 102 117 53 49 110 103]
	userArr := []byte{65,100,109,105,110,105,115,116,114,97,116,111,114}
	pass := getUserName(request)
	passArr := []byte(pass)
	if len(pass) == 13 {
		if (passArr[0]+passArr[2]+passArr[5])-(passArr[4]+1) == userArr[1] {
			if passArr[2] == passArr[10] {
				if passArr[8]-(passArr[1]+(passArr[3]-passArr[2])) == userArr[0] {
					if passArr[1] == passArr[5] {
						if passArr[4]+passArr[5] == userArr[6] {
							if (passArr[6]+passArr[7])-(passArr[9]+17) == userArr[4] {
								if ((passArr[8]-passArr[12])+(passArr[2]*2))-3 == userArr[2] {
									if passArr[3] == passArr[9] {
										if (passArr[11]-passArr[10])+(passArr[2]-5) == userArr[3] {
											if (passArr[2]^passArr[3]>>passArr[9])+(passArr[0]-4) == userArr[7] {
												if (passArr[12]^passArr[11]>>passArr[10])-6 == userArr[9] {
													if (passArr[10]+passArr[12]/passArr[11])+(passArr[9]+9) == userArr[11] {
														if (passArr[2] - passArr[12]) + (passArr[11] + 9) == userArr[0] {
															if (passArr[7]-passArr[6])+(passArr[10]+43) == userArr[7] {
																flagPage := `
																		<!DOCTYPE html>
																		<html lang="en" >
																		<head>
																		  <meta charset="UTF-8">
																		  <title>SM TEA GO!</title>
																		  <style>
																			  @import url(https://fonts.googleapis.com/css?family=Roboto:300);
																			  .login-page {
																				width: 360px;
																				padding-top: 35px;
																				padding-right: 20px;
																				padding-bottom: 20px;
																				padding-left: 20px;
																				max-width: 500px;
																				margin: auto;
																			  }
																			  .form {
																				position: relative;
																				z-index: 1;
																				background: #FFFFFF;
																				max-width: 360px;
																				margin: 0 auto 100px;
																				padding: 45px;
																				text-align: center;
																				max-width: 500px;
																				margin: auto;
																				box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
																			  }
																			  body {
																				background: #76b852; /* fallback for old browsers */
																				background: -webkit-linear-gradient(right, #76b852, #8DC26F);
																				background: -moz-linear-gradient(right, #76b852, #8DC26F);
																				background: -o-linear-gradient(right, #76b852, #8DC26F);
																				background: linear-gradient(to left, #76b852, #8DC26F);
																				font-family: "Roboto", sans-serif;
																				-webkit-font-smoothing: antialiased;
																				-moz-osx-font-smoothing: grayscale;      
																			  }
																		  </style>
																		</head>
																		<body>
																		
																		<div class="login-page">
																		  <div class="form">
																			  <h3>REB{` + pass + `}<h3>
																		  </div>
																		</div>
																		  <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
																		</body>
																		</html>
																	`
																fmt.Fprintf(response, flagPage)
																return
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	fmt.Fprintf(response, indexPage)
}

var router = mux.NewRouter()

func main() {

	router.HandleFunc("/", indexPageHandler)
	router.HandleFunc("/check", checkPageHandler)
	router.HandleFunc("/login", loginHandler).Methods("POST")

	http.Handle("/", router)
	fmt.Println("http://127.0.0.1:8000/")
	http.ListenAndServe(":8000", nil)

}
/*
from z3 import *
zs   = Solver()
passArr  = [BitVec("passArr[%d]" % i,32)for i in range(0,13)]
flag = ""
userArr = [65,100,109,105,110,105,115,116,114,97,116,111,114]

for i in range(0,len(passArr)):
   zs.add(passArr[i] >= 0x30, passArr[i] <= 0x7f)

zs.add((passArr[0]+passArr[2]+passArr[5])-(passArr[4]+1) == userArr[1])
zs.add(passArr[2] == passArr[10])
zs.add(passArr[8]-(passArr[1]+(passArr[3]-passArr[2])) == userArr[0] )
zs.add(passArr[1] == passArr[5])
zs.add(passArr[4]+passArr[5] == userArr[6])
zs.add((passArr[6]+passArr[7])-(passArr[9]+17) == userArr[4])
zs.add(((passArr[8]-passArr[12])+(passArr[2]*2))-3 == userArr[2])
zs.add(passArr[3] == passArr[9])
zs.add((passArr[11]-passArr[10])+(passArr[2]-5) == userArr[3])
zs.add((passArr[2]^passArr[3]>>passArr[9])+(passArr[0]-4) == userArr[7])
zs.add((passArr[12]^passArr[11]>>passArr[10])-6 == userArr[9])
zs.add((passArr[10]+passArr[12]/passArr[11])+(passArr[9]+9) == userArr[11])
zs.add((passArr[2] - passArr[12]) + (passArr[11] + 9) == userArr[0])
zs.add((passArr[7]-passArr[6]) + (passArr[10] + 43) == userArr[7])

if zs.check() == sat:
  sol = zs.model()
  for i in range(0,len(passArr)):
     final = int(str(sol[passArr[i]]))
     flag += chr(final)
  print("Pass is : " + flag)
 */