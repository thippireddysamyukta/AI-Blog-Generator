!pip -q install google-genai gradio
from google import genai
import gradio as gr
client = genai.Client(api_key="")
def generate_blog(topic, audience, tone, words):
  prompt = f"""
  write a {words}-word blog.
  Topic: {topic}
  Audience: {audience}
  Tone: {tone}
  Include:
  - Introduction
  - Fun Facts
  - Tips
  - Advantages
  - Conclusion
  """
  response=client.models.generate_conten(
      model="gemini-2.5-flash",
      contents=prompt
  )
  return response,text
demo=gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Audience"),
        gr.Dropdown(
            ["Proffesional","Casual","Funny","Sarcastic","Sad","Technical"],
            label="Tone"
        ),
        gr.Slider(200,1000,value=500,label="Word Count"),
        gr.Radio(
            ["Informative", "Storytelling", "SEO-Friendly"],
            label="Blog Style"
        ),
    ],
    outputs="markdown",
    title="AI Blog Generator (Gemini)"
)
demo.launch() blog
