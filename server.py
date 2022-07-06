from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./CCS/estilos.css">
    <title>MyWeb5</title>
    <style>
    body 
{
  background-color: aliceblue;  
  color: blueviolet;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
}
    </style>
</head>
<body>
    <h1>Esta es nuestra Web</h1>
    <div>
        <img src="https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/MyWeb5/blob/main/imagen/imagemyweb5.jpeg?raw=true" width="500" height="400">
    </div>
</body>
</html>

       '''

if __name__ == '__main__':
    app.run()