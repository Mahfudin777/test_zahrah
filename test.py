from ultralytics import solutions

solutions.Inference(
    model="best.pt",  # You can use any model that Ultralytics support, i.e. YOLO11, or custom trained model
)



### Make sure to run the file using command `streamlit run <file-name.py>
