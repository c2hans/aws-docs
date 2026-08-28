---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/building-image-classification-model.html
---

# Building an image classification model
<a name="building-image-classification-model"></a>

The following are the phases of developing an image classification model:

1. **Determine your requirements** – Determine your model and deployment requirements, such as your required response time, build level of effort, model requirements, maintenance requirements, and budget.

1. **Choose a model** – Create a list of model options with the associated benefits and costs for each model. Each model has a different deployment option. Select a model based on the cost-benefit analysis.

1. **Determine the deployment infrastructure** – For the model selected, refine the deployment infrastructure plan (if needed).

1. **Determine the model monitoring and maintenance workflow** – This includes updates to the model architecture, periodic retraining, and corrections triggered by monitoring alarms for bias and data quality. The structure of this workflow is application dependent. For example, a demand-forecasting model might require frequent retraining and monitoring to account for model drift due to market trends or other factors. A classification model that detects humans in security footage might need to be updated only when an improved model architecture is available.

The following image shows the phases and considerations that you must account for when choosing and deploying an image classification model.

![Phases of choosing and deploying an image classification model](http://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/images/guide-img/3c71b76a-1e6e-4c69-b783-1676c6b7fb2d/images/ed4ff4a0-e31a-453c-baf7-14db055ce327.png)

Although these phases are ordered to show dependence, the bulk of the decisions occur in the second phase, choosing a model. In this phase, you perform a cost-benefit analysis of the options that meet the requirements you defined in the first phase. This is because each modeling option is associated with different deployment and maintenance possibilities.

In this guide, you use these phases to gather your requirements and then evaluate the modeling options. It explains the modeling options that are available through AWS services and how to organize the subsequent infrastructure development after you choose a modeling approach.

The following steps outline a simplified version for determining a modeling approach, assuming your goal is to minimized the amount of code and complexity:

1. Check whether classes are already included in the Amazon Rekognition labels. If so, benchmark this service for your use case. For more information, see [Amazon Rekognition](rekognition.md) in this guide.

1. If the default pretrained service does not meet your needs, explore Amazon Rekognition Custom Labels. For more information, see [Amazon Rekognition Custom Labels](rekognition-custom-labels.md) in this guide.

1. If neither Amazon Rekognition or Amazon Rekognition Custom Labels  works for you use case, consider image classification through Amazon SageMaker AI Canvas. For more information, see [Amazon SageMaker AI Canvas](sagemaker-canvas.md) in this guide.

1. If your use case is not covered by SageMaker AI Canvas, consider a SageMaker AI endpoint (either server-based or serverless). For more information, see [Amazon SageMaker AI endpoints](sagemaker.md) in this guide.

1. If none of these services address your use case, use a containerized solution in Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS). For more information, see [Custom training jobs](custom-training-jobs.md) in this guide.

Given certain requirements for your solution, it is possible to skip over these steps very quickly in some cases. For example, if an involved augmentation routine is required beyond one that can easily be accomplished by creating additional images, you can skip steps 1 and 2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
