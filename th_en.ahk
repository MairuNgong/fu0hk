FileCreateShortcut, %A_ScriptFullpath%, %A_Startup%\EngToThai.lnk

^q::
Clipboard := ""
Send, ^c
ClipWait, 1
if ErrorLevel
    return

EnChars := "1!@23#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{]}\|aAsSdDfFgGhHjJkKlL;:'""zZxXcCvVbBmM,<.>/? "
ThChars := "ๅ+๑/-๒ภ๓ถ๔ุูึ฿ค๕ต๖จ๗ข๘ช๙ๆ๐ไ""ำฎพฑะธัํี๊รณนฯยญบฐล|ฃฅฟฤหฆกฏดโเฌ้็่๋าษสศวซง.ผ(ป)แฉอฮิฺท?มฒใฬฝฦ "

Translated := ""

Loop, Parse, Clipboard
{
    char := A_LoopField

    ; EN -> TH
    pos := InStr(EnChars, char, true)
    if (pos > 0)
    {
        Translated .= SubStr(ThChars, pos, 1)
        continue
    }

    ; TH -> EN
    pos := InStr(ThChars, char, true)
    if (pos > 0)
    {
        Translated .= SubStr(EnChars, pos, 1)
        continue
    }

    ; keep same
    Translated .= char
}

Clipboard := Translated
Send, ^v
return