import os
import gradio as gr
from gradio.flagging import SimpleCSVLogger
from PIL import Image
import onnx
import onnxruntime as ort
import numpy as np
import time
import socket

host_name = socket.gethostname()

class_labels = [
    "Beagle",
    "Boxer",
    "Bulldog",
    "Dachshund",
    "German_Shepherd",
    "Golden_Retriever",
    "Labrador_Retriever",
    "Poodle",
    "Rottweiler",
    "Yorkshire_Terrier",
]

INPUT_SIZE = (224, 224)
MEAN = np.array([0.485, 0.456, 0.406])
STD = np.array([0.229, 0.224, 0.225])

def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB")                            # Convert to RGB if not already
    image = image.resize(INPUT_SIZE)                        # Resize
    img_array = np.array(image).astype(np.float32) / 255.0  # Convert to numpy array and normalize
    img_array = (img_array - MEAN) / STD                    # Apply mean and std normalization
    img_array = img_array.transpose(2, 0, 1)                # Transpose to channel-first format (NCHW)
    img_array = np.expand_dims(img_array, 0)                # Add batch dimension
    return img_array


def predict_fn(image:Image.Image):
    session = ort.InferenceSession('mambaout.onnx')
    session_input_name = session.get_inputs()[0].name

    start_time = time.time()  # start-time

    img = preprocess_image(image=image)
    outputs = session.run(None,{session_input_name:img.astype(np.float32)})
    logits  = outputs[0][0]
    probabilities = np.exp(logits) / np.sum(np.exp(logits))
    # predictions = {class_labels[i]: float(prob) for i, prob in enumerate(probabilities)}
    predicted_label = class_labels[np.argmax(probabilities)]
    confidence = np.max(probabilities)

    end_time = time.time()  # end-time

    return ({f'Title:: {str(predicted_label)} ': float(confidence)},end_time-start_time)





gr.Interface(
    fn=predict_fn,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Label(num_top_classes=1, label="Predictions"),  # what are the outputs?
        gr.Number(label="Prediction time (ns)"),
    ],
    examples=[
        ["examples/" + i]
        for i in os.listdir(os.path.join(os.path.dirname(__file__), "examples"))
    ],
    title=f"Dog Breeds Classifier 🐈  - {host_name}",
    description="CNN-based Architecture for Fast and Accurate DogsBreed Classifier",
    article="Created by muthukamalan.m ❤️",
    cache_examples=True,
    flagging_options=[],
    flagging_callback=SimpleCSVLogger()
).launch(share=False, debug=False,server_name="0.0.0.0",server_port=7860)

