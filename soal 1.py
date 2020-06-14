# Soal 1

def Hashtag(string):
    if len(string) > 0:
        kalimat = []
        for word in string.split():
            kalimat.append(word.capitalize())
        if len(''.join(kalimat)) > 140:
            return "False"
        else:
            return "#" + ''.join(kalimat)
    else:
        return "False"

print(Hashtag("hello there how are you doing"))
print(Hashtag("   hello   world   "))
print(Hashtag(""))