from schemas.experiment import Experiment

FAKE_EXPERIMENTS_DB = [
    Experiment(
        model_name="ResNet",
        task="Image Classification",
        dataset="ImageNet",
        metric_name="Accuracy",
        metric_value=0.75,
    ),
    Experiment(
        model_name="YOLOv8",
        task="Object Detection",
        dataset="MS COCO",
        metric_name="mAP",
        metric_value=0.6,
    ),
    Experiment(
        model_name="SWIN",
        task="Semantic Segmentation",
        dataset="Very Cool Images",
        metric_name="IoU",
        metric_value=0.01,
    ),
    Experiment(
        model_name="Linear Regression",
        task="Visual Question Answering",
        dataset="VQA9000",
        metric_name="Accuracy",
        metric_value=0.999,
    ),
]
