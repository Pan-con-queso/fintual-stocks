## Instrucciones de ejecución

1. Tener instalado Python, pip y pyenv
2. Crear un ambiente virtual, llamado por ejemplo `fintual-stocks`. Yo lo cree con `pyenv virtualenv 3.10.13 fintual-stocks`
3. Si tu ambiente se llama fintual-stocks, activarlo en la terminar usando `pyenv activate fintual stocks`
4. `sudo pip install -r requirements.txt` para instalar los requerimientos, en este caso pytest para correr los tests unitarios
5. Ejecutar los test con el comando `pytest` en la carpeta base