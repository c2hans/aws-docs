---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/sagemaker-canvas.html
---

# Amazon SageMaker AI Canvas
<a name="sagemaker-canvas"></a>

[Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) is a feature of Amazon SageMaker AI that provides a no-code solution for image classification. Without writing a line of code, you can start classifying images by label, or you can create a labeled image set, train a classifier, and deploy an endpoint.

In SageMaker AI Canvas, you can use ready-to-use foundation models (FMs), or you can build your own custom ML model. The ready-to-use models can extract insights from your data for a variety of use cases. Ready-to-use models are powered by Amazon AI services, including Amazon Rekognition, Amazon Textract, and Amazon Comprehend. You only have to import your data and start using a solution to generate predictions. If you want a model that is customized to your use case and trained with your data, you can build a model.

Unlike Amazon Rekognition Custom Labels, you can control the deployment compute instance. This helps you control costs more precisely. If you are processing a few thousand images a month or more, SageMaker AI can be more cost effective than Amazon Rekognition.

The following are the advantages of SageMaker AI Canvas:
+ Data labeling and processing pipeline in one place
+ Automated training
+ Ability to select the instance type for your endpoint deployments

The following are the disadvantages of SageMaker AI Canvas:
+ Currently supports only single-label classification
+ No control over objective function, network architecture, or initial model weights

For more information, see the following:
+ [Getting started with using Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html) in the *Amazon SageMaker AI Developer Guide*.
+ [Use ready-to-use models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-ready-to-use-models.html) in the *Amazon SageMaker AI Developer Guide*.
+ [Use custom models](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-custom-models.html) in the *Amazon SageMaker AI Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
