def encript(text, shift):
  encription = ""
  for char in text:
      if char.isalpha():  # Check if the character is a letter
            # Determine whether to shift the character up or down the alphabet
          offset = 65 if char.isupper() else 97
          encription += chr((ord(char) - offset + shift) % 26 + offset)
      else:
          # If the character is not a letter, leave it unchanged
          encription += char
  return encription

def decript(encription,shift):
  plaintext = ""
  for char in encription:
      if char.isalpha():
          offset = 65 if char.isupper() else 97
          plaintext += chr((ord(char) - offset - shift) % 26 + offset)
      else:
          plaintext += char
  return plaintext

org_txt = "Vasanth"
print("Original ------>",org_txt)
en = encript(org_txt,21)
print("Encripted ----->",en)
txt = decript(en,21)
print("Decripted ----->",txt)
