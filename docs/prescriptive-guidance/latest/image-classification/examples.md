---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/examples.html
---

# Examples of image classification models on AWS
<a name="examples"></a>

This section provides several examples about how you might choose an image classification solution for training, deployment, and maintenance.

## Pet adoption website
<a name="pet-adoption-website"></a>

A Pet adoption website wants to automatically label cat and dog pictures with a breed when they are uploaded. They expect approximately 5,000 invocations per day, at a relatively constant rate. The full set of cat and dog breeds is not available in Amazon Rekognition, so it is not a candidate for this use case.

Using the four-phase process described in [Building an image classification model](building-image-classification-model.md), the organization chooses an image classification solution as follows:

1. The team determines their service requirements. The endpoint should respond immediately, in less than 1 second. There are no machine learning personnel on the website staff, so the minimal maintenance effort is a priority.

1. The team performs the following cost-benefit analysis.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/examples.html)

1. The team determines their deployment infrastructure. Amazon Rekognition Custom Labels is selected for training and deployment because it meets the service requirements defined in phase 1. The deployment is fully managed in AWS.

1. The team determines their model maintenance workflow. They choose an AWS Step Functions state machine to manage the retraining workflow. They will initiate the state machine as needed to retrain and redeploy the model. This is expected to be an infrequent event because the breed types change slowly and new data acquisition is also slow.

## Speed monitoring system
<a name="speed-monitoring-system"></a>

A high-speed camera for a highway monitoring system captures images of vehicles and sends them to an image classification service to predict the vehicle type. Amazon Rekognition already contains the labels needed for the required classes. The organization expects around 400,000 images per day, with a peak rate of 10,000 images per hour. Immediate processing is not required. The organization has data scientists on staff who recommend that open source pretrained models can satisfy their needs. However, these come with more upfront costs and maintenance.

1. The team determines their service requirements. An immediate response is not necessary, but images should be processed within 24 hours.

1. The team performs the following cost-benefit analysis.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/examples.html)

1. The team determines their deployment infrastructure. Because the organization already has a data science team that can manage the model selection and maintenance, they choose to use a SageMaker AI model and deploy a SageMaker AI serverless endpoint.

1. The team determines their model maintenance workflow. They create a monitoring pipeline that provides statistics about model prediction confidences and sends alerts if the statistics are outside of configured tolerances.
