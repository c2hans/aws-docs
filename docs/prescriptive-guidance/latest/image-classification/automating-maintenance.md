---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/automating-maintenance.html
---

# Automating maintenance of an image classification model
<a name="automating-maintenance"></a>

After your image classification model is deployed and available for use, it might require some maintenance. Consider the following example scenarios:
+ A model classifies corn cultivars to aid workers during harvest time. Over time, the corn cultivars' appearance is slowly changing, and at certain points, new cultivars might be introduced.
+ A model determines the type of vehicle parked in a spot in a parking garage. It performs fine-grained classification for a vehicle's model, make, and year. It must be updated every year for the new models that have been released.
+ A model is trained on social media posts to detect sentiment with regard to different entities and topics. The model needs to stay updated for new topics, entities, idioms, and emoji symbols.

In all of these scenarios, the models require periodic retraining. Retraining is required based on model drift (the properties of the input data have changed over time) or due to updates required for the model to handle a modified task. The creation of ML operations pipelines in AWS can be pursued at several levels of abstraction. The most flexible and abstract is to use AWS Step Functions to create the workflow for model maintenance.

For an example of an ML operations pipeline, see [MLOps End-to-End Example using Amazon SageMaker AI Pipeline, AWS CodePipeline, and AWS CDK](https://github.com/aws-samples/mlops-e2e) on GitHub.
