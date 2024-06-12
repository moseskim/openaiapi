import openai

api_key = "YOUR_OPENAI_API_KEY_HERE"

suffix_prompt = "\n\n1. "

def read_prompt(fname):
  f = open(fname, encoding='utf-8')
  content = f.read()
  f.close()
  return content

def access_openai(prompt_value):
  openai.api_key = api_key
  prompt = read_prompt("prompt.txt")
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt + prompt_value + suffix_prompt,
    suffix="\n5. 완성입니다.",
    max_tokens=200)
  result = response.choices[0].text.strip()
  print("1. " + result + "\n\n5. 완성입니다.")


if __name__ == "__main__":
    input_text = input("텍스트를 입력하십시오: ")
    access_openai(input_text)

