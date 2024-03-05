"""
This module creates UI interface for the demo of the model
"""
import logging
import gradio as gr

from pathlib import Path
from model.run_main import run_app, running_caption_generating_model
from model.Config.PropStoreConfig import GlobalProperties
from model.logging_format import set_log_file

if __name__ == "__main__":
    props = GlobalProperties.initialize("dev", "20240305")
    Path(props.main_folder).joinpath(props.cob).mkdir(exist_ok=True, parents=True)
    logger = logging.getLogger('[APP_IMG]')
    set_log_file(logger, props, f'app_run.log')
    logger.info("==== START UI LOADING ===")

    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """## An app to download images from internet and caption them using ML model""")
        with gr.Tab("Download Images"):
            with gr.Row():
                query = gr.Textbox(label="Query", placeholder="Describe images that you want to download in 3-4 words")
                slider = gr.Slider(1, 20, step=1, label="How many images you want to download?")
            with gr.Column():
                button = gr.Button("Download Images")
            with gr.Column():
                ot_pt = gr.Markdown()
        with gr.Tab("Caption Images"):
            with gr.Column():
                gr.Markdown("""# Now we will run the ML model to caption downloaded images! 
                               Please click on any image for slideshow and better clarity of generated Captions""")
                button2 = gr.Button("Caption Downloaded Images")
            with gr.Column():
                gallery = gr.Gallery(show_label=True, elem_id="gallery", object_fit="contain")
        button.click(fn=run_app, inputs=[query, slider], outputs=ot_pt)
        button2.click(fn=running_caption_generating_model, inputs=None, outputs=gallery)

    # demo.launch(share=True)
    demo.launch()
