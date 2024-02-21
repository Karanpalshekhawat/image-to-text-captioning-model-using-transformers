"""
This module creates UI interface for the demo of the model
"""
import os
import gradio as gr

from model.run_main import run_app, running_caption_generating_model

with gr.Blocks() as demo:
    with gr.Row():
        query = gr.Textbox(label="Query", placeholder="Describe the images that you want to download in 3-4 words")
        slider = gr.Slider(1, 10, step=1, label="How many images you want to download?")
    with gr.Column():
        button = gr.Button("Download Images")
    with gr.Column():
        gr.Markdown("Now we will run ML model to caption downloaded images")
        button2 = gr.Button("Caption downloaded Images")
    with gr.Column():
        output = gr.Image()
    button.click(fn=run_app, inputs=[query, slider])
    button2.click(fn=running_caption_generating_model, inputs=query, outputs=output)

demo.launch()

