CREATE TABLE IF NOT EXISTS experiments (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(255) NOT NULL,
    task VARCHAR(255) NOT NULL,
    dataset VARCHAR(255) NOT NULL,
    metric_name VARCHAR(255) NOT NULL,
    metric_value FLOAT NOT NULL
);

-- Insert the fake experiments
INSERT INTO experiments (model_name, task, dataset, metric_name, metric_value)
VALUES
    ('ResNet', 'Image Classification', 'ImageNet', 'Accuracy', 0.75),
    ('YOLOv8', 'Object Detection', 'MS COCO', 'mAP', 0.65),
    ('ViT', 'Image Classification', 'ImageNet', 'Accuracy', 0.88),
    ('YOLOv7', 'Object Detection', 'MS COCO', 'mAP', 0.55),
    ('VGG16', 'Image Classification', 'ImageNet', 'Accuracy', 0.6),
    ('SWIN', 'Image Classification', 'ImageNet', 'Accuracy', 0.82);