---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/rekognition.html
---

# Amazon Rekognition
<a name="rekognition"></a>

For image classification in the visible spectrum, models are frequently created with transfer learning and fine-tuning from a pretrained neural network. You can automate the task of network selection and training by using the [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) service.

Amazon Rekognition provides a standard set of classification labels. A *label* is an object or concept (including scenes and actions) found in an image or video based on its contents. For example, an image of people on a tropical beach may contain labels such as `Palm Tree` (object), `Beach` (scene), `Running` (action), and `Outdoors` (concept). For more information about the labels supported by Amazon Rekognition, see [Detecting objects and concepts](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html) in the service documentation.

For tasks that require the standard labels in Amazon Rekognition, testing this service is worthwhile. If Amazon Rekognition can meet your requirements, the model selection, training, and maintenance are abstracted. It provides a pretrained service for inference, and AWS handles maintenance of the service. Obtaining predictions from Amazon Rekognition is straight-forward.

The following are the advantages of Amazon Rekognition:
+ Immediately available and scalable
+ No training or configuration required
+ Supports multi-label classification

The following are the disadvantages of Amazon Rekognition:
+ Fixed set of predicted classes
+ Inference units offer chunks of capacity, and the smallest unit might be costly for small throughput

For more information, see the following:
+ [Getting started with Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html) in the *Amazon Rekognition Developer Guide*
+ [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) in the *Amazon Rekognition API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
