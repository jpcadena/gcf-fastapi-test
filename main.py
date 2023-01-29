"""
Main script
"""
from fastapi import FastAPI

DESCRIPTION: str = """**FastAPI**, and **Firestore** helps you do
 awesome stuff. 🚀\n\n ![Firestore](
https://miro.medium.com/max/1200/1*a2Da_CQHUsSKTCTRI2tYhQ.png)"""
contact: dict[str, str] = {
    "name": "Juan Pablo Cadena Aguilar",
    "url": "https://www.github.com/jpcadena", "email": "jpcadena@espol.edu.ec"}
LICENSE_INFO: dict[str, str] = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"}

app: FastAPI = FastAPI(
    title='Google Cloud Function for Push notifications',
    description=DESCRIPTION, contact=contact, license_info=LICENSE_INFO)


@app.get("/")
async def root() -> dict[str, str]:
    """
    Function to retrieve homepage.
    - :return: Welcome message
    - :rtype: dict[str, str]
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    Salutation
    :param name: Name of person to say hello
    :type name: str
    :return: Message with salutation
    :rtype: dict[str, str]
    """
    return {"message": f"Hello {name}"}
