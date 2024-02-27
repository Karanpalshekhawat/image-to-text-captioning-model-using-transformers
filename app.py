"""
This module creates UI interface for the demo of the model
"""
import os
import gradio as gr

from model.run_main import run_app, running_caption_generating_model

with gr.Blocks() as demo:
    with gr.Tab("Download Images"):
        with gr.Row():
            query = gr.Textbox(label="Query", placeholder="Describe the images that you want to download in 3-4 words")
            slider = gr.Slider(1, 20, step=1, label="How many images you want to download?")
        with gr.Column():
            button = gr.Button("Download Images")
        with gr.Column():
            ot_pt = gr.Markdown()
    with gr.Tab("Caption Images"):
        with gr.Column():
            gr.Markdown("""# Now we will run ML model to caption downloaded images! 
                           Please click on any image for slideshow and better clarity of Caption""")
            button2 = gr.Button("Caption Downloaded Images")
        with gr.Column():
            gallery = gr.Gallery(show_label=True, elem_id="gallery", object_fit="contain")
    button.click(fn=run_app, inputs=[query, slider], outputs=ot_pt)
    button2.click(fn=running_caption_generating_model, inputs=None, outputs=gallery)

demo.launch()
