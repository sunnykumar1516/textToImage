import gradio as gr
import time
import utility as s


with gr.Blocks() as demo:
    gr.Markdown("# I can generate image from text" )
    gr.Markdown("Enter a description in the text box below, and an image will be generated based on your input.")
   
    gr.Interface(
        fn=s.getImage,
        inputs="text",
        outputs="image"
    )
    gr.Markdown("<p style='color:red;'>Created By: <span style ='color:yellow'>Sunny Kumar</span>.</p>")
    gr.Markdown("<p style='color:red;'>Contact me at: <span style ='color:yellow'>SunnyKumar1516@gmail.com</span>.</p>")
    gr.Markdown("<p style='color:red;'>Linkdin: <span style ='color:yellow'>https://www.linkedin.com/in/sunny-kumar-b232417a/</span>.</p>")


demo.launch()
