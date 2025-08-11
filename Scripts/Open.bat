@echo off
echo Starting apps with high priority...

REM Launch Google Chrome
start "" /high "C:\Program Files\Google\Chrome\Application\chrome.exe"

REM Launch File Explorer
start "" /high explorer.exe

REM Launch Discord
start "" /high "%LocalAppData%\Discord\Update.exe" --processStart Discord.exe

REM Launch Spotify
start "" /high "%AppData%\Spotify\Spotify.exe"

exit
