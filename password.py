def is_Valid(email):
  if '@' in email and '@' != email[0] and '@' != email[-1] and len(email)<256:
    index_of_at = email.find('@')
    if '.' != email[index_of_at + 1] and '.' != email[-1]:
      print("valid")
    else: 
      print("not_valid")
  else:
    print("not valid")

email = "saif@777.com"

is_Valid(email)

