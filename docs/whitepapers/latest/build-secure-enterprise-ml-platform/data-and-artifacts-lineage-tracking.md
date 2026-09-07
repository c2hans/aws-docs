---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data and artifacts lineage tracking
<a name="data-and-artifacts-lineage-tracking"></a>

For regulated customers, tracking all the artifacts used for a production model is an essential requirement for reproducing the model to meet regulatory and control requirements. The following diagram shows the various artifacts that need to be tracked and versioned to recreate the data processing, model training, and model deployment process.

![A diagram showing artifacts needed for tracking.](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-20.png)

*Artifacts needed for tracking*
+ **Code versioning** — Code repositories such as GitLab, Bitbucket, and CodeCommit support versioning of the code artifacts. You can check-in / check-out code by commit ID. Commit ID uniquely identifies a version of source code in a repository.
+ **Dataset versioning** — Training data can be version controlled by using a proper S3 data partition scheme. Every time there is a new training dataset, a unique S3 bucket / prefix can be created to uniquely identify the training dataset.

  [DVC](https://dvc.org/), an open-source data versioning system for machine learning, can track different versions of a dataset. The DVC repository can be created with a code repository such as GitHub and CodeCommit, and S3 can be used as the back-end store for data.

  Metadata associated with the datasets can also be tracked along with the dataset using services such as [SageMaker AI Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).
+ **Container versioning** — Amazon ECR uniquely identifies each image with an Image URI (repository URI \+ image digest ID). Images can also be pulled with repository URI \+ tag (if a unique tag is properly enforced for each image push). Additional tags can be added to track other metadata for source code repo URI and commit ID for traceability.
+ **Training job versioning** — Each SageMaker AI training job is uniquely identified with an ARN, and other metadata such as hyperparameters, container URI, data set URI, and model output URI are automatically tracked with the training job.
+ **Model versioning** — A model package can be registered in SageMaker AI using the URL of the model files in S3 and URI to the container image in ECR. An ARN is assigned to the model package to identify the model package uniquely. Additional tags can be added to the SageMaker AI model package with the model name and version ID to track different versions of the model.
+ **Endpoint versioning** — Each SageMaker AI endpoint has a unique ARN, and other metadata, such as the model used, are tracked as part of the endpoint configuration.

## Infrastructure configuration change management
<a name="infrastructure-configuration-change-management"></a>

As part of the ML platform operation, Cloud Engineering / MLOps team needs to monitor and track resource configuration changes in core architecture components such as automation pipelines and model hosting environment.

[AWS Config](https://aws.amazon.com/config/) is a service that enables you to assess, audit, and evaluate the configuration of AWS resources. It tracks changes in CodePipeline pipeline definitions, CodeBuild projects, and CloudFormation stacks, and it can report configuration changes across timelines.

AWS CloudTrail can track and log SageMaker AI API events for the create, delete, and update operations for model registry, model hosting endpoint configuration, and model hosting endpoint to detect production environment changes.
