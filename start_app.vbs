Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

' Caminho da pasta onde o VBS está
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Caminho do app.py (relativo)
scriptPath = scriptDir & "\app.py"

' Executa o Python com o app.py
shell.Run "python """ & scriptPath & """", 0, False

' Aguarda e abre o navegador
WScript.Sleep 50
shell.Run "http://127.0.0.1:5000", 0, False
