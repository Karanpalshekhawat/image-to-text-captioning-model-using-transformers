"""
This module creates UI interface for the demo of the model
"""

import gradio as gr

from model.run_main import run_app

demo = gr.Interface(
    fn=run_app,
    inputs=["text", "slider"],
    outputs="image",
    title="Image Reader",
    description="Display Image and its label using model"
)

demo.launch()
