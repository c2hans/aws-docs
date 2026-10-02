---
source_url: https://docs.aws.amazon.com/frauddetector/index.html
---

---
title: 'Amazon Fraud Detector Documentation'
canonical_url: https://docs.aws.amazon.com/frauddetector/
source: aws-documentation
generated_on: 2026-10-02
---

# Amazon Fraud Detector Documentation

Amazon Fraud Detector is a fully managed service that makes it easy to identify potentially fraudulent online activities such as online payment fraud and creation of fake accounts. In a few steps, you can create machine learning models to identify a variety of fraudulent activities.

## Getting started

- [Overview](https://docs.aws.amazon.com/frauddetector/latest/ug/what-is-frauddetector.html): Understand what Amazon Fraud Detector is, how it works, and how to use it for your business use case.
- [Set up for Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/set-up.html): Before you get started with Amazon Fraud Detector, set up the interfaces you plan to use.
- [Start using Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector/latest/ug/get-started.html): Use the tutorial to get started with Amazon Fraud Detector using the AWS Management Console or the AWS SDK for Python.

## Build and train fraud detection model

- [Choose model type](https://docs.aws.amazon.com/frauddetector/latest/ug/choosing-model-type.html): Choose a model type for your business use case and gain insights into the dataset requirements for the model type.
- [Prepare dataset](https://docs.aws.amazon.com/frauddetector/latest/ug/create-event-dataset.html): Gather data from your business for your use case with the help of the insights provided for the model type you have chosen.
- [Define event type](https://docs.aws.amazon.com/frauddetector/latest/ug/event-type.html): Define the event that you want to use for evaluating fraud. An event is the business activity that you want to evaluate for fraud risk. An event type defines the structure of the individual event.
- [Store data](https://docs.aws.amazon.com/frauddetector/latest/ug/event-data-storage.html): Store the data that you gathered from your business for the event that you want to evaluate for fraud. You can store your dataset internally with Amazon Fraud Detector or externally with Amazon S3.
- [Build and train a fraud detection model](https://docs.aws.amazon.com/frauddetector/latest/ug/building-a-model.html): Amazon Fraud Detector builds a fraud detection model using the model type that you choose for the event type that you define. The model is trained using the dataset that you prepared.
- [Analyze your model performance](https://docs.aws.amazon.com/frauddetector/latest/ug/training-performance-metrics.html): As part of the model training, Amazon Fraud Detector generates a model performance score and other model performance metrics. Use the metrics to evaluate your model performance.

## Fraud detection, prediction, and downstream processing

- [Create and test detector](https://docs.aws.amazon.com/frauddetector/latest/ug/detector.html): Create a detector by adding your trained model and rules for detecting fraud. Detector is a container that contains a fraud detection model and rules, for one specific business event you want to evaluate for fraud.
- [Deploy detector](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-detector-version.html): Deploy detector in your production environment.
- [Fraud prediction](https://docs.aws.amazon.com/frauddetector/latest/ug/getting-fraud-predictions.html): Get fraud predictions for a single event in real time or get fraud predictions offline for a set of events and then use prediction explanations to gain insight into how each variable that you use in your dataset impacts your model's fraud prediction score.
- [Event orchestration](https://docs.aws.amazon.com/frauddetector/latest/ug/event-orchestration.html): Set up orchestration to send your events data to other AWS services for downstream processing of the events after fraud prediction.

## Model resources, security, and monitoring

- [Model resources](https://docs.aws.amazon.com/frauddetector/latest/ug/create-resources.html): Learn how to manage the resources that the models and detectors use to evaluate your business events for fraud. Resources can be variables, rules, outcomes, labels, lists, and entities.
- [Security](https://docs.aws.amazon.com/frauddetector/latest/ug/security.html): Understand how to configure Amazon Fraud Detector to control access to resources, to protect your data, and to meet your security and compliance objectives.
- [Monitoring](https://docs.aws.amazon.com/frauddetector/latest/ug/monitoring-overview.html): Use monitoring tools that AWS provides to monitor Amazon Fraud Detector, report when something is wrong, and take action when appropriate.

## References

- [API Reference](https://docs.aws.amazon.com/frauddetector/latest/api/Welcome.html): Describes all of the API operations for Amazon Fraud Detector, with sample requests, responses, and errors for the supported web service protocols.
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html): Describes all of the classes that are included in the Amazon Fraud Detector AWS SDK for Python (Boto3).
- [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/FraudDetector.html): Describes all API operations for the AWS SDK for JavaScript, with sample requests, responses, and errors for the supported web service protocols.
- [AWS Command Line Interface (AWS CLI) Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html): Documents the Amazon Fraud Detector commands that are available in the AWS CLI.
- [CloudFormation Resource Type Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.html): Documents the reference information for all Amazon Fraud Detector resources and property types that CloudFormation supports.

## Other resources

- [Amazon Fraud Detector product page](https://aws.amazon.com/fraud-detector/?nc2=h_ql_prod_ml_fd): Use the Amazon Fraud Detector product page to gain an overall understanding of the product and if it meets your business use case.
- [Amazon Fraud Detector FAQs](https://aws.amazon.com/fraud-detector/faqs/): Find answers to frequently asked questions
- [Blogs](https://aws.amazon.com/search/?searchQuery=Amazon+Fraud+Detector): Use the blogs to create fraud detection solutions for your business use case.
- [Amazon Fraud Detector re:Post forum](https://repost.aws/search/questions?globalSearch=Amazon+Fraud+Detector): Ask questions or browse through the questions and answers to find solutions for issues with your specific use case.

---

## Related Links

- [AWS Glossary](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html)
- [Getting Started with AWS](https://aws.amazon.com/documentation/gettingstarted/)
- [SDKs & Tools](https://aws.amazon.com/tools/)
- [AWS General Reference](http://docs.aws.amazon.com/general/latest/gr/Welcome.html)
- [AWS Training](https://aws.amazon.com/training/)
- [AWS Case Studies](https://aws.amazon.com/solutions/case-studies/)
- [AWS White papers](https://aws.amazon.com/whitepapers/)
