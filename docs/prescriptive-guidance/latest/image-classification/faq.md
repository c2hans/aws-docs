---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/faq.html
---

# FAQ
<a name="faq"></a>

## I already have image classification models containerized and deployed in AWS Fargate. What is the advantage of moving to an Amazon SageMaker AI serverless deployment?
<a name="faq-1"></a>

SageMaker AI offers tools for model training, monitoring, and deployment, which work within a standardized API. If you do not plan to make use of these features, there might not be a reason to change your deployment strategy.

## How can I incorporate a managed annotation solution into a retraining workflow?
<a name="faq-2"></a>

Amazon SageMaker Ground Truth provides an annotation solution for image classification that integrates with the rest of the SageMaker AI services. For more information, see [Image Classification (Single Label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-image-classification.html) and [Image Classification (Multi-label)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-image-classification-multilabel.html) in the *SageMaker AI Developer Guide*.

## How can I make sure my image classification model is fair and accurate?
<a name="faq-3"></a>

You can use services, such as [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/), to detect potential bias. You can also implement model monitoring and continuous evaluation with [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html). We recommend that you follow [AWS guidance for responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/) and use [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/groundtruth/) to create high-quality training data. We also recommend that you regularly retrain and update your model with new and diverse data.

## Can I use my own pretrained image classification model with Amazon Rekognition or Amazon Rekognition Custom Labels?
<a name="faq-4"></a>

No, Amazon Rekognition and Amazon Rekognition Custom Labels do not allow you to use your own pretrained models. You can deploy your existing pretrained model by using Amazon SageMaker AI or a custom container solution on Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS).
