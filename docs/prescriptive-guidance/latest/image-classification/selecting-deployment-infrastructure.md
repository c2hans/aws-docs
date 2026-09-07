---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/selecting-deployment-infrastructure.html
---

# Selecting deployment infrastructure
<a name="selecting-deployment-infrastructure"></a>

We recommend selecting the best deployment option for an image classification endpoint through consideration of three main aspects:
+ Required endpoint response time
+ Solution complexity and available human resources
+ Cost limitations

The endpoint response time and cost limitations are more easily quantified and are better to determine first. Solution complexity constraints depend on balancing staff time and resources. The least complex solutions involve using Amazon Rekognition or Amazon Rekognition Custom Labels. Large computer vision models, when placed behind an Amazon API Gateway instance and an AWS Lambda function, can take up to 1 second to respond. Amazon SageMaker AI Canvas can also deploy an endpoint that responds within 1 second or less, with a low level of development effort.

Image classification models can be placed in AWS Lambda functions by using a Docker image. When a Lambda function is called, there may be a cold start that delays the endpoint response due to the model loading time. You can also use the [provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) option to make a Lambda function respond in less than 1 second, for a specified level of concurrency or according to an auto-scaling policy.

Model response times vary based on the model processing time and the deployed endpoint response time. The following are the response times for each deployment option, organized by implementation effort:
+ **Lowest effort** – Amazon Rekognition, Amazon Rekognition Custom Labels, and SageMaker AI Canvas are the lowest effort deployment options. Response times for these solutions can range from less than one second to hours.
+ **Medium effort ­**– SageMaker AI is a medium-effort deployment option. SageMaker AI real-time endpoints can respond in less than one second, SageMaker AI serverless inference units can respond in multiple seconds, and SageMaker AI batch transforms typically respond in hours.
+ **Highest effort** – Amazon ECS or Amazon EKS custom endpoints and AWS Lambda functions are the highest effort deployment option. Response times for these custom training jobs can range from less than one second to hours. For less than one second response times, you can provision concurrency for Lambda functions.

The highest-effort solutions are more likely to have lower infrastructure costs. However, compare the savings to the additional cost of maintenance time for engineers.

A common deployment pattern is to have an API gateway and Lambda function in front of an endpoint call, as shown in the following image. This is preferable in situations where the inference response from Amazon Rekognition needs further processing before it is sent back to the calling client through the Amazon API Gateway.

![Common deployment pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/images/guide-img/3c71b76a-1e6e-4c69-b783-1676c6b7fb2d/images/66a02f94-aa73-4163-9189-beca76f439be.png)

However, situations where processing is quite heavy may necessitate a different workflow to reduce the network latency penalty resulting from the processing Lambda function. For very low latency, the Lambda function can be omitted at the cost of forcing the Amazon Rekognition API in the API Gateway call.

For image classification systems that can tolerate a few seconds of latency, use a SageMaker AI serverless inference endpoint. For both SageMaker AI serverless inference and AWS Lambda deployments, there is a 15-minute limit on execution time for each invocation. This is a large margin of safety for the most popular image classification models.

For offline image classification or for applications where quick response time is not important, you can use batch inference with Amazon Rekognition. For more information, see [Batch image processing with Amazon Rekognition Custom Labels](https://aws.amazon.com/blogs/machine-learning/batch-image-processing-with-amazon-rekognition-custom-labels/) in the AWS Machine Learning Blog. You can also use SageMaker AI batch transform for a SageMaker AI model that is trained in SageMaker AI Canvas or other means. For an example, see the [SageMaker AI Batch Transform for PyTorch Batch Inference](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_batch_transform/pytorch_mnist_batch_transform/pytorch-mnist-batch-transform.ipynb) notebook on GitHub.
