---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/rekognition-custom-labels.html
---

# Amazon Rekognition Custom Labels
<a name="rekognition-custom-labels"></a>

If Amazon Rekognition doesn't support all of the labels that you need for your use case, you can train an [Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html) model . Amazon Rekognition Custom Labels extends the existing capabilities of Amazon Rekognition. Instead of fully training a model with thousands or tens of thousands of images, you can upload a small set of labeled training images (typically a few hundred or less per class) that are specific to your use case. If your images are already labeled, Amazon Rekognition Custom Labels can begin training a model in a short time. If not, you can label the images directly within the labeling interface, or you can use Amazon SageMaker Ground Truth to label them for you.

After Amazon Rekognition Custom Labels begins training from your image set, it can produce a custom image analysis model for you in just a few hours. Behind the scenes, Amazon Rekognition Custom Labels automatically loads and inspects the training data, selects the right machine learning algorithms, trains a model, and provides model performance metrics. You can then use your custom model through the Amazon Rekognition Custom Labels API and integrate it into your applications.

The following are the advantages of Amazon Rekognition Custom Labels:
+ Automated training and tuning requires minimal effort
+ Supports multi-label classification

The following are the disadvantages of Amazon Rekognition Custom Labels:
+ No control over objective function, network architecture, or initial model weights.
+ Automated training and tuning can be time-consuming and more expensive than a training pipeline with more customizable settings. (This is less important if the training is infrequent.)

For more information, see the following:
+ [Setting up Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/setting-up.html) in the *Amazon Rekognition Custom Labels Developer Guide*
+ [Getting started with Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/getting-started.html) in the *Amazon Rekognition Custom Labels Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
