class songs:
  def __init__(self,lyrics):
    self.lyr = lyrics


bithday_song = songs(["Happy Birthday to you,",
'Happy Birthday to you,',
'Happy Birthday dear [Name],',
'Happy Birthday to you.'])

embrace = songs(["I took a walk in the sunshine,Feeling the warmth on my face,The world around me comes alive,In nature is embrace"])

print(bithday_song.lyr)
print(embrace.lyr)
