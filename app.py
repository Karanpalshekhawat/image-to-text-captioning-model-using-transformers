"""
This module creates UI interface for the demo of the model
"""
import os
import gradio as gr

from model.run_main import run_app, running_caption_generating_model


class Slideshow:
    def __init__(self, images):
        self.images = images
        self.current_index = 0
        self.image_display = gr.Image()
        self.button = gr.Button("Next")
        self.interface = gr.Interface(
            self.display_next_image,
            inputs=self.button,
            outputs=self.image_display,
            title="Image Slideshow",
            description="Click 'Next' to view the next image.",
        )

    def display_next_image(self, next_button_clicked):
        if next_button_clicked:
            # Load the next image
            image_url = self.images[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.images)
            return image_url

    def run(self):
        self.interface.launch()


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
        output = gr.Image(label=query.value)
        output2 = gr.Textbox(label="Caption Generated using ML Model")
    button.click(fn=run_app, inputs=[query, slider])
    # images = running_caption_generating_model(query)
    # slideshow = Slideshow(images)
    # button2.click(fn=lambda: slideshow.run())
    button2.click(fn=running_caption_generating_model, inputs=None, outputs=[output, output2])

demo.launch()
