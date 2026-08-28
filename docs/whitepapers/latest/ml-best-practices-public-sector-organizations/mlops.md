---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/mlops.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MLOps
<a name="mlops"></a>

 MLOps is the discipline of integrating ML workloads into release management, Continuous Integration / Continuous Delivery (CI/CD), and operations.

 One of the major hurdles facing government organizations is the ability to create a repeatable process for deployment that is consistent with their organizational best practices. Using ML models in software development makes it difficult to achieve versioning, quality control, reliability, reproducibility, explainability, and audibility in that process. This is due to the number of changing artifacts to be managed in addition to the software code, such as the datasets, the ML models, the parameters and hyperparameters used by such models, and the size and portability of such artifacts can be orders of magnitude higher than the software code. In addition, different teams might own different parts of the process; data engineers might be building pipelines to make data accessible, while data scientists can be researching and exploring better models. ML engineers or developers have to work on integrating the models and releasing them to production. When these groups work independently, there is a high risk of creating friction in the process and delivering suboptimal results.

 AWS Cloud provides a number of different options that solve these challenges, either by building an MLOps pipeline from scratch or by using managed services.

## Amazon SageMaker AI Projects
<a name="amazon-sagemaker-projects"></a>

 A [SageMaker project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html) is an [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) provisioned product that enables creation of an end-to-end ML solution. By using a SageMaker project, teams of data scientists and developers can work together on ML business problems. SageMaker projects use MLOps templates that automate the model building and deployment pipelines using CI/CD. SageMaker-provided templates can be used to provision the initial setup required for a complete end-to-end MLOps system including model building, training, and deployment. Custom templates can also be used to customize the provisioning of resources.

## Amazon SageMaker AI Pipelines
<a name="amazon-sagemaker-pipelines"></a>

 [SageMaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/) is a purpose-built, CI/CD service for ML. SageMaker Pipelines brings CI/CD practices to ML, such as maintaining parity between development and production environments, version control, on-demand testing, and end-to-end automation, helping scale ML throughout the organization. Pipelines is integrated with SageMaker Python SDK as well as SageMaker Studio for visualization and management of workflows. With the SageMaker Pipelines model registry, model versions can be stored in a central repository for easy browsing, discovery, and selection of the right model for deployment based on business requirements. Pipelines provide the ability to log each step within the ML workflow for a complete audit trail of model components such as training data, platform configurations, model parameters, and learning gradients. Audit trails can be used to recreate models and help support compliance requirements.

## AWS CodePipeline and AWS Lambda
<a name="aws-codepipeline-and-aws-lambda"></a>

 For AWS programmers and teams that are already working with CodePipeline for deployment of other workloads, the option exists to utilize the same workflows for ML. Figure 3 below represents a reference pipeline for deployment on AWS.

![Reference Architecture CI/CD Pipeline for ML on AWS](http://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/images/reference-architecture-cicd.png)

 See [Build a CI/CD pipeline for deploying custom machine learning models using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services) for details on the reference architecture and implementation.

## AWS Step Functions Data Science Software Development Kit (SDK)
<a name="aws-stepfunctions-data-science-software-development-kit-sdk"></a>

 The [AWS Step Functions Data Science SDK](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-python-sdk.html) is an open-source Python library that allows data scientists to create workflows that process and publish ML models using SageMaker and Step Functions. This can be used by teams that are already comfortable using Python and AWS Step Functions. The SDK provides the ability to copy workflows, experiment with new options, and then put the refined workflow in production. The SDK can also be used to create and visualize end-to-end data science workflows that perform tasks such as data pre-processing on AWS Glue and model training, hyperparameter tuning, and endpoint creation on Amazon SageMaker AI. Workflows can be reused in production by exporting [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (infrastructure as code) templates.

## AWS MLOps Framework
<a name="aws-mlops-framework"></a>

 Figure 4 below illustrates an AWS solution that provides an extendable framework with a standard interface for managing ML pipelines.

![Diagram showing AWS MLOps Framework](http://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/images/aws-mlops-framework.png)

 The solution provides a ready-made template to upload trained models (also referred to as a *bring your own model*), configure the orchestration of the pipeline, and monitor the pipeline's operations.

## Deploy Custom Deep Learning Models
<a name="deploy-custom-deep-learning-models"></a>

 In addition to Amazon SageMaker AI, AWS also provides the option to deploy custom code on virtual machines using [Amazon EC2](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc), and containers using self-managed Kubernetes on Amazon EC2, [Amazon Elastic Container Service](https://aws.amazon.com/ecs/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&ecs-blogs.sort-by=item.additionalFields.createdDate&ecs-blogs.sort-order=desc) (Amazon ECS) and [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&eks-blogs.sort-by=item.additionalFields.createdDate&eks-blogs.sort-order=desc) (Amazon EKS). [AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/) can be used to accelerate deep learning by quickly launching Amazon EC2 instances that are pre-installed with popular deep learning frameworks. [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/) are Docker images pre-installed with deep learning frameworks to deploy optimized ML environments. For an example of how to deploy custom deep learning models, see [Deploy Deep Learning Models on Amazon ECS](https://aws.amazon.com/blogs/machine-learning/deploy-deep-learning-models-on-amazon-ecs/).

## Deploy ML at the edge
<a name="deploy-ml-at-the-edge"></a>

 Training your ML models requires powerful compute infrastructure available in the cloud. However, making inferences against these models typically requires far less computational power. In some cases, such as with edge devices, inferencing needs to occur even when there is limited or no connectivity to the cloud. Mining fields are an example of this type of use case. To make sure that an edge device can respond quickly to local events, it is critical that you can get inference results with low latency.

 [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) enables ML inference locally using models that are created, trained, and optimized in the cloud using Amazon SageMaker AI, AWS Deep Learning AMIs, or AWS Deep Learning Containers, and deployed on the edge devices.

 Performing inference locally on connected devices running AWS IoT Greengrass reduces latency and cost. Instead of sending all device data to the cloud to perform ML inference and make a prediction, you can run inference directly on the device. As predictions are made on these edge devices, you can capture the results and analyze them to detect outliers. Analyzed data can then be sent back to the cloud, where it can be reclassified and tagged to improve the ML model. For example, you can build a predictive model in Amazon SageMaker AI for scene detection analysis, optimize it to run on any camera, and then deploy it to send an alert when suspicious activity occurs. Data gathered from the inference running on AWS IoT Greengrass can be sent back to Amazon SageMaker AI, where it can be tagged and used to continuously improve the quality of the ML models. See [Machine Learning at the Edge: Using and Retraining Image Classification Models with AWS IoT Greengrass (Part 1)](https://aws.amazon.com/blogs/iot/machine-learning-at-the-edge-using-and-retraining-image-classification-models-with-aws-iot-greengrass-part-1/) for more details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
