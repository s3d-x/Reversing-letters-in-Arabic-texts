!c:: ; ALT+C تغيير الزر   
    ClipSaved := ClipboardAll ; 
    Send ^c
    ClipWait, 0.1
    if ErrorLevel {
        MsgBox, Failed to copy text.
        return
    }

    ; reshape_scriptهنا ضع مسار السكربت مع الصيغة الخاصة به
    RunWait, pythonw.exe "ضع مسار مع الصيغة reshape_script.py هنا", , Hide

    ; 
    ClipWait, 0.1
    if ErrorLevel {
        MsgBox, Failed to update clipboard.
        return
    }

    Send ^v ; 
    Clipboard := ClipSaved ; 
return
