import gradio as gr

# Define functions for button clicks
def button1_click():
    return "Button 1 clicked!"

def button2_click():
    return "Button 2 clicked!"

# Create button objects
button1 = gr.Interface.Button(text="Button 1")
button2 = gr.Interface.Button(text="Button 2")

# Create Gradio interface with buttons as inputs
iface = gr.Interface(
    fn=None,  # No main function as we're using buttons
    inputs=[button1, button2],
    outputs="text",
    title="Multiple Buttons Interface",
    description="Click a button to see its message.",
    allow_flagging=False  # Disable flagging for simplicity
)

# Assign functions to button clicks
button1.clicked(button1_click)
button2.clicked(button2_click)

# Launch the interface
iface.launch()