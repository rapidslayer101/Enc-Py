#print("hello, please input code")
#lines = []
#while True:
#    text_changes = input()
#    if text_changes:
#        lines.append(text_changes)
#    else:
#        text_changes = input()
#        if text_changes:
#            lines.append(text_changes)
#        else:
#            break
#text = '_'.join(lines)
#text_changes = text

import time

#time.sleep(0.05)
#pass
#print("you have entered", text_changes)
#input()

def encrypt(text):
    ciphertextmangle = text
    import time

    start_time = time.time()
    x = 0

    for i in range(500000):
        x = x + 1
        import random

        for i in range(1):
            def get_random_unicode(length):

                try:
                    get_char = unichr
                except NameError:
                    get_char = chr

                # Update this to include code point ranges to be sampled
                include_ranges = [
                    (0x0021, 0x0021),
                    (0x0023, 0x0026),
                    (0x0028, 0x007E),
                    (0x00A1, 0x00AC),
                    (0x00AE, 0x00FF),
                    (0x0100, 0x017F),
                    (0x0180, 0x024F),
                    (0x2C60, 0x2C7F),
                    (0x16A0, 0x16F0),
                    (0x0370, 0x0377),
                    (0x037A, 0x037E),
                    (0x0384, 0x038A),
                    (0x038C, 0x038C),
                ]

                alphabet = [
                    get_char(code_point) for current_range in include_ranges
                    for code_point in range(current_range[0], current_range[1] + 1)
                ]
                return ''.join(random.choice(alphabet) for i in range(length))


            if __name__ == '__main__':
                inp = get_random_unicode(94)


        def remove2(string):
            value1 = inp[1:2]
            return string.replace("1", value1)


        def remove3(string):
            value2 = inp[2:3]
            return string.replace("2", value2)


        def remove4(string):
            value3 = inp[3:4]
            return string.replace("3", value3)


        def remove5(string):
            value4 = inp[4:5]
            return string.replace("4", value4)


        def remove6(string):
            value5 = inp[5:6]
            return string.replace("5", value5)


        def remove7(string):
            value6 = inp[6:7]
            return string.replace("6", value6)


        def remove8(string):
            value7 = inp[7:8]
            return string.replace("7", value7)


        def remove9(string):
            value8 = inp[8:9]
            return string.replace("8", value8)


        def remove10(string):
            value9 = inp[9:10]
            return string.replace("9", value9)


        def remove11(string):
            value0 = inp[0:1]
            return string.replace("0", value0)


        def remove12(string):
            value10 = inp[11:12]
            return string.replace("!", value10)


        def remove13(string):
            value11 = inp[12:13]
            return string.replace("£", value11)


        def remove14(string):
            value12 = inp[13:14]
            return string.replace("$", value12)


        def remove15(string):
            value13 = inp[13:14]
            return string.replace("%", value13)


        def remove16(string):
            value14 = inp[14:15]
            return string.replace("^", value14)


        def remove17(string):
            value15 = inp[15:16]
            return string.replace("&", value15)


        def remove18(string):
            value16 = inp[16:17]
            return string.replace("*", value16)


        def remove19(string):
            value17 = inp[17:18]
            return string.replace("(", value17)


        def remove20(string):
            value18 = inp[18:19]
            return string.replace(")", value18)


        def remove21(string):
            value19 = inp[19:20]
            return string.replace("-", value19)


        def remove22(string):
            value20 = inp[20:21]
            return string.replace("+", value20)


        def remove23(string):
            value21 = inp[21:22]
            return string.replace(" ", value21)


        def remove24(string):
            value22 = inp[22:23]
            return string.replace('=', value22)


        def remove25(string):
            value23 = inp[23:24]
            return string.replace("{", value23)


        def remove26(string):
            value24 = inp[24:25]
            return string.replace("}", value24)


        def remove27(string):
            value25 = inp[25:26]
            return string.replace(":", value25)


        def remove28(string):
            value26 = inp[26:27]
            return string.replace(";", value26)


        def remove29(string):
            value27 = inp[27:28]
            return string.replace("@", value27)


        def remove30(string):
            value28 = inp[28:29]
            return string.replace("~", value28)


        def remove31(string):
            value29 = inp[29:30]
            return string.replace("'", value29)


        def remove32(string):
            value30 = inp[30:31]
            return string.replace("#", value30)


        def remove33(string):
            value31 = inp[31:32]
            return string.replace("<", value31)


        def remove34(string):
            value32 = inp[32:33]
            return string.replace(">", value32)


        def remove35(string):
            value33 = inp[33:34]
            return string.replace(",", value33)


        def remove36(string):
            value34 = inp[34:35]
            return string.replace(".", value34)


        def remove37(string):
            value35 = inp[35:36]
            return string.replace("?", value35)


        def remove38(string):
            value36 = inp[36:37]
            return string.replace("/", value36)


        def remove39(string):
            value37 = inp[37:38]
            return string.replace("|", value37)


        def remove40(string):
            value38 = inp[38:39]
            return string.replace("\"", value38)


        def remove41(string):
            value39 = inp[39:40]
            return string.replace("\\", value39)


        def remove42(string):
            value40 = inp[40:41]
            return string.replace("a", value40)


        def remove43(string):
            value41 = inp[41:42]
            return string.replace("b", value41)


        def remove44(string):
            value42 = inp[42:43]
            return string.replace("c", value42)


        def remove45(string):
            value43 = inp[43:44]
            return string.replace("d", value43)


        def remove46(string):
            value44 = inp[44:45]
            return string.replace("e", value44)


        def remove47(string):
            value45 = inp[45:46]
            return string.replace("f", value45)


        def remove48(string):
            value46 = inp[46:47]
            return string.replace("g", value46)


        def remove49(string):
            value47 = inp[47:48]
            return string.replace("h", value47)


        def remove50(string):
            value48 = inp[48:49]
            return string.replace("i", value48)


        def remove51(string):
            value49 = inp[49:50]
            return string.replace("j", value49)


        def remove52(string):
            value50 = inp[50:51]
            return string.replace("k", value50)


        def remove53(string):
            value51 = inp[51:52]
            return string.replace("l", value51)


        def remove54(string):
            value52 = inp[52:53]
            return string.replace("m", value52)


        def remove55(string):
            value53 = inp[53:54]
            return string.replace("n", value53)


        def remove56(string):
            value54 = inp[54:55]
            return string.replace("o", value54)


        def remove57(string):
            value55 = inp[55:56]
            return string.replace("p", value55)


        def remove58(string):
            value56 = inp[56:57]
            return string.replace("q", value56)


        def remove59(string):
            value57 = inp[57:58]
            return string.replace("r", value57)


        def remove60(string):
            value58 = inp[58:59]
            return string.replace("s", value58)


        def remove61(string):
            value59 = inp[59:60]
            return string.replace("t", value59)


        def remove62(string):
            value60 = inp[60:61]
            return string.replace("u", value60)


        def remove63(string):
            value61 = inp[61:62]
            return string.replace("v", value61)


        def remove64(string):
            value62 = inp[62:63]
            return string.replace("w", value62)


        def remove65(string):
            value63 = inp[63:64]
            return string.replace("x", value63)


        def remove66(string):
            value64 = inp[64:65]
            return string.replace("y", value64)


        def remove67(string):
            value65 = inp[65:66]
            return string.replace("z", value65)


        def remove68(string):
            value66 = inp[66:67]
            return string.replace("A", value66)


        def remove69(string):
            value67 = inp[67:68]
            return string.replace("B", value67)


        def remove70(string):
            value68 = inp[68:69]
            return string.replace("B", value68)


        def remove71(string):
            value69 = inp[69:70]
            return string.replace("C", value69)


        def remove72(string):
            value70 = inp[70:71]
            return string.replace("D", value70)


        def remove73(string):
            value71 = inp[71:72]
            return string.replace("E", value71)


        def remove74(string):
            value72 = inp[72:73]
            return string.replace("F", value72)


        def remove75(string):
            value73 = inp[73:74]
            return string.replace("G", value73)


        def remove76(string):
            value74 = inp[74:75]
            return string.replace("H", value74)


        def remove77(string):
            value75 = inp[75:76]
            return string.replace("I", value75)


        def remove78(string):
            value76 = inp[76:77]
            return string.replace("J", value76)


        def remove79(string):
            value77 = inp[77:78]
            return string.replace("K", value77)


        def remove80(string):
            value78 = inp[78:79]
            return string.replace("L", value78)


        def remove81(string):
            value79 = inp[79:80]
            return string.replace("M", value79)


        def remove82(string):
            value80 = inp[80:81]
            return string.replace("N", value80)


        def remove83(string):
            value81 = inp[81:82]
            return string.replace("O", value81)


        def remove84(string):
            value82 = inp[82:83]
            return string.replace("P", value82)


        def remove85(string):
            value83 = inp[83:84]
            return string.replace("Q", value83)


        def remove86(string):
            value84 = inp[84:85]
            return string.replace("R", value84)


        def remove87(string):
            value85 = inp[85:86]
            return string.replace("S", value85)


        def remove88(string):
            value86 = inp[86:87]
            return string.replace("T", value86)


        def remove89(string):
            value87 = inp[87:88]
            return string.replace("U", value87)


        def remove90(string):
            value88 = inp[88:89]
            return string.replace("V", value88)


        def remove91(string):
            value89 = inp[89:90]
            return string.replace("W", value89)


        def remove92(string):
            value90 = inp[90:91]
            return string.replace("X", value90)


        def remove93(string):
            value91 = inp[91:92]
            return string.replace("Y", value91)


        def remove94(string):
            value92 = inp[92:93]
            return string.replace("Z", value92)


        ciphertext = ciphertextmangle
        ciphertextmangle2 = remove2(ciphertextmangle)
        ciphertextmangle3 = remove3(ciphertextmangle2)
        ciphertextmangle4 = remove4(ciphertextmangle3)
        ciphertextmangle5 = remove5(ciphertextmangle4)
        ciphertextmangle6 = remove6(ciphertextmangle5)
        ciphertextmangle7 = remove7(ciphertextmangle6)
        ciphertextmangle8 = remove8(ciphertextmangle7)
        ciphertextmangle9 = remove9(ciphertextmangle8)
        ciphertextmangle10 = remove10(ciphertextmangle9)
        ciphertextmangle11 = remove11(ciphertextmangle10)
        ciphertextmangle12 = remove12(ciphertextmangle11)
        ciphertextmangle13 = remove13(ciphertextmangle12)
        ciphertextmangle14 = remove14(ciphertextmangle13)
        ciphertextmangle15 = remove15(ciphertextmangle14)
        ciphertextmangle16 = remove16(ciphertextmangle15)
        ciphertextmangle17 = remove17(ciphertextmangle16)
        ciphertextmangle18 = remove18(ciphertextmangle17)
        ciphertextmangle19 = remove19(ciphertextmangle18)
        ciphertextmangle20 = remove20(ciphertextmangle19)
        ciphertextmangle21 = remove21(ciphertextmangle20)
        ciphertextmangle22 = remove22(ciphertextmangle21)
        ciphertextmangle23 = remove23(ciphertextmangle22)
        ciphertextmangle24 = remove24(ciphertextmangle23)
        ciphertextmangle25 = remove25(ciphertextmangle24)
        ciphertextmangle26 = remove26(ciphertextmangle25)
        ciphertextmangle27 = remove27(ciphertextmangle26)
        ciphertextmangle28 = remove28(ciphertextmangle27)
        ciphertextmangle29 = remove29(ciphertextmangle28)
        ciphertextmangle30 = remove30(ciphertextmangle29)
        ciphertextmangle31 = remove31(ciphertextmangle30)
        ciphertextmangle32 = remove32(ciphertextmangle31)
        ciphertextmangle33 = remove33(ciphertextmangle32)
        ciphertextmangle34 = remove34(ciphertextmangle33)
        ciphertextmangle35 = remove35(ciphertextmangle34)
        ciphertextmangle36 = remove36(ciphertextmangle35)
        ciphertextmangle37 = remove37(ciphertextmangle36)
        ciphertextmangle38 = remove38(ciphertextmangle37)
        ciphertextmangle39 = remove39(ciphertextmangle38)
        ciphertextmangle40 = remove40(ciphertextmangle39)
        ciphertextmangle41 = remove41(ciphertextmangle40)
        ciphertextmangle42 = remove42(ciphertextmangle41)
        ciphertextmangle43 = remove43(ciphertextmangle42)
        ciphertextmangle44 = remove44(ciphertextmangle43)
        ciphertextmangle45 = remove45(ciphertextmangle44)
        ciphertextmangle46 = remove46(ciphertextmangle45)
        ciphertextmangle47 = remove47(ciphertextmangle46)
        ciphertextmangle48 = remove48(ciphertextmangle47)
        ciphertextmangle49 = remove49(ciphertextmangle48)
        ciphertextmangle50 = remove50(ciphertextmangle49)
        ciphertextmangle51 = remove51(ciphertextmangle50)
        ciphertextmangle52 = remove52(ciphertextmangle51)
        ciphertextmangle53 = remove53(ciphertextmangle52)
        ciphertextmangle54 = remove54(ciphertextmangle53)
        ciphertextmangle55 = remove55(ciphertextmangle54)
        ciphertextmangle56 = remove56(ciphertextmangle55)
        ciphertextmangle57 = remove57(ciphertextmangle56)
        ciphertextmangle58 = remove58(ciphertextmangle57)
        ciphertextmangle59 = remove59(ciphertextmangle58)
        ciphertextmangle60 = remove60(ciphertextmangle59)
        ciphertextmangle61 = remove61(ciphertextmangle60)
        ciphertextmangle62 = remove62(ciphertextmangle61)
        ciphertextmangle63 = remove63(ciphertextmangle62)
        ciphertextmangle64 = remove64(ciphertextmangle63)
        ciphertextmangle65 = remove65(ciphertextmangle64)
        ciphertextmangle66 = remove66(ciphertextmangle65)
        ciphertextmangle67 = remove67(ciphertextmangle66)
        ciphertextmangle68 = remove68(ciphertextmangle67)
        ciphertextmangle69 = remove69(ciphertextmangle68)
        ciphertextmangle70 = remove70(ciphertextmangle69)
        ciphertextmangle71 = remove71(ciphertextmangle70)
        ciphertextmangle72 = remove72(ciphertextmangle71)
        ciphertextmangle73 = remove73(ciphertextmangle72)
        ciphertextmangle74 = remove74(ciphertextmangle73)
        ciphertextmangle75 = remove75(ciphertextmangle74)
        ciphertextmangle76 = remove76(ciphertextmangle75)
        ciphertextmangle77 = remove77(ciphertextmangle76)
        ciphertextmangle78 = remove78(ciphertextmangle77)
        ciphertextmangle79 = remove79(ciphertextmangle78)
        ciphertextmangle80 = remove80(ciphertextmangle79)
        ciphertextmangle81 = remove81(ciphertextmangle80)
        ciphertextmangle82 = remove82(ciphertextmangle81)
        ciphertextmangle83 = remove83(ciphertextmangle82)
        ciphertextmangle84 = remove84(ciphertextmangle83)
        ciphertextmangle85 = remove85(ciphertextmangle84)
        ciphertextmangle86 = remove86(ciphertextmangle85)
        ciphertextmangle87 = remove87(ciphertextmangle86)
        ciphertextmangle88 = remove88(ciphertextmangle87)
        ciphertextmangle89 = remove89(ciphertextmangle88)
        ciphertextmangle90 = remove90(ciphertextmangle89)
        ciphertextmangle91 = remove91(ciphertextmangle90)
        ciphertextmangle92 = remove92(ciphertextmangle91)
        ciphertextmangle93 = remove93(ciphertextmangle92)
        ciphertextmangle94 = remove94(ciphertextmangle93)
        possible = ciphertextmangle94

        ciphertextmangle0 = ciphertextmangle94
        inp = inp


        def remove2(string):
            value1 = inp[1:2]
            return string.replace(value1, "1")


        def remove3(string):
            value2 = inp[2:3]
            return string.replace(value2, "2")


        def remove4(string):
            value3 = inp[3:4]
            return string.replace(value3, "3")


        def remove5(string):
            value4 = inp[4:5]
            return string.replace(value4, "4")


        def remove6(string):
            value5 = inp[5:6]
            return string.replace(value5, "5")


        def remove7(string):
            value6 = inp[6:7]
            return string.replace(value6, "6")


        def remove8(string):
            value7 = inp[7:8]
            return string.replace(value7, "7")


        def remove9(string):
            value8 = inp[8:9]
            return string.replace(value8, "8")


        def remove10(string):
            value9 = inp[9:10]
            return string.replace(value9, "9")


        def remove11(string):
            value0 = inp[0:1]
            return string.replace(value0, "0")


        def remove12(string):
            value10 = inp[11:12]
            return string.replace(value10, "!")


        def remove13(string):
            value11 = inp[12:13]
            return string.replace(value11, "£")


        def remove14(string):
            value12 = inp[13:14]
            return string.replace(value12, "$")


        def remove15(string):
            value13 = inp[13:14]
            return string.replace(value13, "%")


        def remove16(string):
            value14 = inp[14:15]
            return string.replace(value14, "^")


        def remove17(string):
            value15 = inp[15:16]
            return string.replace(value15, "&")


        def remove18(string):
            value16 = inp[16:17]
            return string.replace(value16, "*")


        def remove19(string):
            value17 = inp[17:18]
            return string.replace(value17, "(")


        def remove20(string):
            value18 = inp[18:19]
            return string.replace(value18, ")")


        def remove21(string):
            value19 = inp[19:20]
            return string.replace(value19, "-")


        def remove22(string):
            value20 = inp[20:21]
            return string.replace(value20, "+")


        def remove23(string):
            value21 = inp[21:22]
            return string.replace(value21, " ")


        def remove24(string):
            value22 = inp[22:23]
            return string.replace(value22, '=')


        def remove25(string):
            value23 = inp[23:24]
            return string.replace(value23, "{")


        def remove26(string):
            value24 = inp[24:25]
            return string.replace(value24, "}")


        def remove27(string):
            value25 = inp[25:26]
            return string.replace(value25, ":")


        def remove28(string):
            value26 = inp[26:27]
            return string.replace(value26, ";")


        def remove29(string):
            value27 = inp[27:28]
            return string.replace(value27, "@")


        def remove30(string):
            value28 = inp[28:29]
            return string.replace(value28, "~")


        def remove31(string):
            value29 = inp[29:30]
            return string.replace(value29, "'")


        def remove32(string):
            value30 = inp[30:31]
            return string.replace(value30, "#")


        def remove33(string):
            value31 = inp[31:32]
            return string.replace(value31, "<")


        def remove34(string):
            value32 = inp[32:33]
            return string.replace(value32, ">")


        def remove35(string):
            value33 = inp[33:34]
            return string.replace(value33, ",")


        def remove36(string):
            value34 = inp[34:35]
            return string.replace(value34, ".")


        def remove37(string):
            value35 = inp[35:36]
            return string.replace(value35, "?")


        def remove38(string):
            value36 = inp[36:37]
            return string.replace(value36, "/")


        def remove39(string):
            value37 = inp[37:38]
            return string.replace(value37, "|")


        def remove40(string):
            value38 = inp[38:39]
            return string.replace(value38, "\"")


        def remove41(string):
            value39 = inp[39:40]
            return string.replace(value39, "\\")


        def remove42(string):
            value40 = inp[40:41]
            return string.replace(value40, "a")


        def remove43(string):
            value41 = inp[41:42]
            return string.replace(value41, "b")


        def remove44(string):
            value42 = inp[42:43]
            return string.replace(value42, "c")


        def remove45(string):
            value43 = inp[43:44]
            return string.replace(value43, "d")


        def remove46(string):
            value44 = inp[44:45]
            return string.replace(value44, "e")


        def remove47(string):
            value45 = inp[45:46]
            return string.replace(value45, "f")


        def remove48(string):
            value46 = inp[46:47]
            return string.replace(value46, "g")


        def remove49(string):
            value47 = inp[47:48]
            return string.replace(value47, "h")


        def remove50(string):
            value48 = inp[48:49]
            return string.replace(value48, "i")


        def remove51(string):
            value49 = inp[49:50]
            return string.replace(value49, "j")


        def remove52(string):
            value50 = inp[50:51]
            return string.replace(value50, "k")


        def remove53(string):
            value51 = inp[51:52]
            return string.replace(value51, "l")


        def remove54(string):
            value52 = inp[52:53]
            return string.replace(value52, "m")


        def remove55(string):
            value53 = inp[53:54]
            return string.replace(value53, "n")


        def remove56(string):
            value54 = inp[54:55]
            return string.replace(value54, "o")


        def remove57(string):
            value55 = inp[55:56]
            return string.replace(value55, "p")


        def remove58(string):
            value56 = inp[56:57]
            return string.replace(value56, "q")


        def remove59(string):
            value57 = inp[57:58]
            return string.replace(value57, "r")


        def remove60(string):
            value58 = inp[58:59]
            return string.replace(value58, "s")


        def remove61(string):
            value59 = inp[59:60]
            return string.replace(value59, "t")


        def remove62(string):
            value60 = inp[60:61]
            return string.replace(value60, "u")


        def remove63(string):
            value61 = inp[61:62]
            return string.replace(value61, "v")


        def remove64(string):
            value62 = inp[62:63]
            return string.replace(value62, "w")


        def remove65(string):
            value63 = inp[63:64]
            return string.replace(value63, "x")


        def remove66(string):
            value64 = inp[64:65]
            return string.replace(value64, "y")


        def remove67(string):
            value65 = inp[65:66]
            return string.replace(value65, "z")


        def remove68(string):
            value66 = inp[66:67]
            return string.replace(value66, "A")


        def remove69(string):
            value67 = inp[67:68]
            return string.replace(value67, "B")


        def remove70(string):
            value68 = inp[68:69]
            return string.replace(value68, "B")


        def remove71(string):
            value69 = inp[69:70]
            return string.replace(value69, "C")


        def remove72(string):
            value70 = inp[70:71]
            return string.replace(value70, "D")


        def remove73(string):
            value71 = inp[71:72]
            return string.replace(value71, "E")


        def remove74(string):
            value72 = inp[72:73]
            return string.replace(value72, "F")


        def remove75(string):
            value73 = inp[73:74]
            return string.replace(value73, "G")


        def remove76(string):
            value74 = inp[74:75]
            return string.replace(value74, "H")


        def remove77(string):
            value75 = inp[75:76]
            return string.replace(value75, "I")


        def remove78(string):
            value76 = inp[76:77]
            return string.replace(value76, "J")


        def remove79(string):
            value77 = inp[77:78]
            return string.replace(value77, "K")


        def remove80(string):
            value78 = inp[78:79]
            return string.replace(value78, "L")


        def remove81(string):
            value79 = inp[79:80]
            return string.replace(value79, "M")


        def remove82(string):
            value80 = inp[80:81]
            return string.replace(value80, "N")


        def remove83(string):
            value81 = inp[81:82]
            return string.replace(value81, "O")


        def remove84(string):
            value82 = inp[82:83]
            return string.replace(value82, "P")


        def remove85(string):
            value83 = inp[83:84]
            return string.replace(value83, "Q")


        def remove86(string):
            value84 = inp[84:85]
            return string.replace(value84, "R")


        def remove87(string):
            value85 = inp[85:86]
            return string.replace(value85, "S")


        def remove88(string):
            value86 = inp[86:87]
            return string.replace(value86, "T")


        def remove89(string):
            value87 = inp[87:88]
            return string.replace(value87, "U")


        def remove90(string):
            value88 = inp[88:89]
            return string.replace(value88, "V")


        def remove91(string):
            value89 = inp[89:90]
            return string.replace(value89, "W")


        def remove92(string):
            value90 = inp[90:91]
            return string.replace(value90, "X")


        def remove93(string):
            value91 = inp[91:92]
            return string.replace(value91, "Y")


        def remove94(string):
            value92 = inp[92:93]
            return string.replace(value92, "Z")


        ciphertext = ciphertextmangle0
        ciphertextmangle1 = ciphertextmangle0
        ciphertextmangle2 = remove2(ciphertextmangle0)
        ciphertextmangle3 = remove3(ciphertextmangle2)
        ciphertextmangle4 = remove4(ciphertextmangle3)
        ciphertextmangle5 = remove5(ciphertextmangle4)
        ciphertextmangle6 = remove6(ciphertextmangle5)
        ciphertextmangle7 = remove7(ciphertextmangle6)
        ciphertextmangle8 = remove8(ciphertextmangle7)
        ciphertextmangle9 = remove9(ciphertextmangle8)
        ciphertextmangle10 = remove10(ciphertextmangle9)
        ciphertextmangle11 = remove11(ciphertextmangle10)
        ciphertextmangle12 = remove12(ciphertextmangle11)
        ciphertextmangle13 = remove13(ciphertextmangle12)
        ciphertextmangle14 = remove14(ciphertextmangle13)
        ciphertextmangle15 = remove15(ciphertextmangle14)
        ciphertextmangle16 = remove16(ciphertextmangle15)
        ciphertextmangle17 = remove17(ciphertextmangle16)
        ciphertextmangle18 = remove18(ciphertextmangle17)
        ciphertextmangle19 = remove19(ciphertextmangle18)
        ciphertextmangle20 = remove20(ciphertextmangle19)
        ciphertextmangle21 = remove21(ciphertextmangle20)
        ciphertextmangle22 = remove22(ciphertextmangle21)
        ciphertextmangle23 = remove23(ciphertextmangle22)
        ciphertextmangle24 = remove24(ciphertextmangle23)
        ciphertextmangle25 = remove25(ciphertextmangle24)
        ciphertextmangle26 = remove26(ciphertextmangle25)
        ciphertextmangle27 = remove27(ciphertextmangle26)
        ciphertextmangle28 = remove28(ciphertextmangle27)
        ciphertextmangle29 = remove29(ciphertextmangle28)
        ciphertextmangle30 = remove30(ciphertextmangle29)
        ciphertextmangle31 = remove31(ciphertextmangle30)
        ciphertextmangle32 = remove32(ciphertextmangle31)
        ciphertextmangle33 = remove33(ciphertextmangle32)
        ciphertextmangle34 = remove34(ciphertextmangle33)
        ciphertextmangle35 = remove35(ciphertextmangle34)
        ciphertextmangle36 = remove36(ciphertextmangle35)
        ciphertextmangle37 = remove37(ciphertextmangle36)
        ciphertextmangle38 = remove38(ciphertextmangle37)
        ciphertextmangle39 = remove39(ciphertextmangle38)
        ciphertextmangle40 = remove40(ciphertextmangle39)
        ciphertextmangle41 = remove41(ciphertextmangle40)
        ciphertextmangle42 = remove42(ciphertextmangle41)
        ciphertextmangle43 = remove43(ciphertextmangle42)
        ciphertextmangle44 = remove44(ciphertextmangle43)
        ciphertextmangle45 = remove45(ciphertextmangle44)
        ciphertextmangle46 = remove46(ciphertextmangle45)
        ciphertextmangle47 = remove47(ciphertextmangle46)
        ciphertextmangle48 = remove48(ciphertextmangle47)
        ciphertextmangle49 = remove49(ciphertextmangle48)
        ciphertextmangle50 = remove50(ciphertextmangle49)
        ciphertextmangle51 = remove51(ciphertextmangle50)
        ciphertextmangle52 = remove52(ciphertextmangle51)
        ciphertextmangle53 = remove53(ciphertextmangle52)
        ciphertextmangle54 = remove54(ciphertextmangle53)
        ciphertextmangle55 = remove55(ciphertextmangle54)
        ciphertextmangle56 = remove56(ciphertextmangle55)
        ciphertextmangle57 = remove57(ciphertextmangle56)
        ciphertextmangle58 = remove58(ciphertextmangle57)
        ciphertextmangle59 = remove59(ciphertextmangle58)
        ciphertextmangle60 = remove60(ciphertextmangle59)
        ciphertextmangle61 = remove61(ciphertextmangle60)
        ciphertextmangle62 = remove62(ciphertextmangle61)
        ciphertextmangle63 = remove63(ciphertextmangle62)
        ciphertextmangle64 = remove64(ciphertextmangle63)
        ciphertextmangle65 = remove65(ciphertextmangle64)
        ciphertextmangle66 = remove66(ciphertextmangle65)
        ciphertextmangle67 = remove67(ciphertextmangle66)
        ciphertextmangle68 = remove68(ciphertextmangle67)
        ciphertextmangle69 = remove69(ciphertextmangle68)
        ciphertextmangle70 = remove70(ciphertextmangle69)
        ciphertextmangle71 = remove71(ciphertextmangle70)
        ciphertextmangle72 = remove72(ciphertextmangle71)
        ciphertextmangle73 = remove73(ciphertextmangle72)
        ciphertextmangle74 = remove74(ciphertextmangle73)
        ciphertextmangle75 = remove75(ciphertextmangle74)
        ciphertextmangle76 = remove76(ciphertextmangle75)
        ciphertextmangle77 = remove77(ciphertextmangle76)
        ciphertextmangle78 = remove78(ciphertextmangle77)
        ciphertextmangle79 = remove79(ciphertextmangle78)
        ciphertextmangle80 = remove80(ciphertextmangle79)
        ciphertextmangle81 = remove81(ciphertextmangle80)
        ciphertextmangle82 = remove82(ciphertextmangle81)
        ciphertextmangle83 = remove83(ciphertextmangle82)
        ciphertextmangle84 = remove84(ciphertextmangle83)
        ciphertextmangle85 = remove85(ciphertextmangle84)
        ciphertextmangle86 = remove86(ciphertextmangle85)
        ciphertextmangle87 = remove87(ciphertextmangle86)
        ciphertextmangle88 = remove88(ciphertextmangle87)
        ciphertextmangle89 = remove89(ciphertextmangle88)
        ciphertextmangle90 = remove90(ciphertextmangle89)
        ciphertextmangle91 = remove91(ciphertextmangle90)
        ciphertextmangle92 = remove92(ciphertextmangle91)
        ciphertextmangle93 = remove93(ciphertextmangle92)
        ciphertextmangle94 = remove94(ciphertextmangle93)
        print("TRIAL NUMBER", x, "--- %s seconds ---" % (time.time() - start_time))

        if ciphertextmangle94 == text:
            print("")
            print("")
            print("")
            print("lossless match found")
            print("it only took:" "--- %s seconds ---" % (time.time() - start_time))
            print(ciphertextmangle94)
            print("")
            print(possible)
            print("")
            print(inp)
            print("")
            print("press enter to search again")
            return possible
            input()

    print("oh well thats an oof")
    print("ran 500000 trials but none could provide a lossless result")
    print("you can use any of the trials but some data will be lost")
    return "ERROR"