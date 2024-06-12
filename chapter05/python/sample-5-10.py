import openai

api_key = "YOUR_OPENAI_API_KEY_HERE"

fname = "sample.m4a"

def access_openai():
  openai.api_key = api_key
  file= open(fname, "rb")
  transcript = openai.Audio.translate( #☆
    model="whisper-1",
    file=file)
  print(transcript.text)


if __name__ == "__main__":
  access_openai()
