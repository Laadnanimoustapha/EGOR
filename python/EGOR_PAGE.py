from fastapi.responses import HTMLResponse

# THE MAINE HTML CONVERTED TO VIA PYTHON

HTML_PAGE = HTMLResponse("""
<html>
    <head>
    <style>

     body{
      margin:0;
      height:100vh;
      display:flex;
      justify-content: center;
      align-items:center;
      background:black;
      color:rgb(243, 240, 80);
      font-family:monospace;
      }

      pre{
       font-size:18px;
       text-align:center;
       animation: glow 2s ease-in-out infinite alternate;
       }

       @keyframes glow{
        from{
            text-shadow: 0 0 5px #fff;
        }
        to{
            text-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700;
        }
       }

    </style>
    </head>
    <body>
    <pre>
     ███████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔════╝░██╔══██╗██╔══██╗
    █████╗░░██║░░██╗░██║░░██║██████╔╝
    ██╔══╝░░██║░░╚██╗██║░░██║██╔══██╗
    ███████╗╚██████╔╝╚█████╔╝██║░░██║
    ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
    </pre>
    </html>
""")
