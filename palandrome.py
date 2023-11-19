def is_palandrome(text):
    if text == text[::-1]:
      print("palandrome")
    else:
      print("not palandrome")


text = "radar"

is_palandrome(text)
