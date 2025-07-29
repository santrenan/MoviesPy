Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

venvPath = scriptDir & "\venv\Scripts\activate.bat"
scriptPath = scriptDir & "\app.py"

' Executa ativação da venv e app.py (cmd fecha após rodar)
shell.Run "cmd.exe /C """ & venvPath & " && python """ & scriptPath & """", 0, False

' Aguarda o servidor Flask iniciar (3 segundos)
WScript.Sleep 50

' Abre o navegador padrão apontando para o servidor Flask
' shell.Run "cmd /C start http://127.0.0.1:5000", 0, False
