---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/custom-training-jobs.html
---

# Custom training jobs
<a name="custom-training-jobs"></a>

On AWS, Amazon Rekognition, Amazon Rekognition Custom Labels, SageMaker AI Canvas, and SageMaker AI are expected to handle most cases for training image classification endpoints. For training jobs that require more control over the container properties, you can deploy an ML model on [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).

The following are examples of situations that require more control over the container properties:
+ You have a model that loads multiple model artifacts that are versioned separately. For example, you might load a sentence-embedding model that is used to feed a separately versioned multi-layer perceptron classifier that is trained on the embeddings.
+ You have an endpoint that does not use or require a model artifact. One case would be a clustering endpoint, which takes a data payload and returns cluster labels. This could still be served through SageMaker AI, but you would need to provide a dummy Amazon Simple Storage Service (Amazon S3) artifact path because every SageMaker AI model must have an associated artifact.
+ You want to use an Amazon Elastic Compute Cloud (Amazon EC2) instance type that is not supported by SageMaker AI. If you would like to use an instance type that is not available for SageMaker AI endpoints, typically for either cost or performance reasons, you can use Amazon ECS or Amazon EKS to use any Amazon EC2 instance type.
