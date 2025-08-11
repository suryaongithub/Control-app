' popup_bold.vbs
Dim IE
Set IE = CreateObject("InternetExplorer.Application")

With IE
    .Visible = True
    .Width = 270
    .Height = 250
    .menubar = False
    .toolbar = False
    .statusbar = False
    .navigate "about:blank"
    
    Do While .Busy
        WScript.Sleep 100
    Loop
    
    ' Set HTML content with a custom window title
    .document.title = "Quick Launch - App List"
    .document.body.innerHTML = "<div style='font-family:Segoe UI; font-size:13px; padding:20px;'>" & _
                               "The following apps are launching:<br><br>" & _
                               "----------<br>" & _
                               "1. <i>Google Chrome</i><br>" & _
                               "2. <i>File Explorer</i><br>" & _
                               "3. <i>Discord</i><br>" & _
                               "4. <i>Spotify</i><br>" & _
                               "-----------" & _
                               "</div>"
End With
