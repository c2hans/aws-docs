---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/step6.html
---

# Step 6. Expand the pipeline
<a name="step6"></a>

This guide explains how you can get started building ML pipelines on AWS quickly, with concrete architecture. There are additional considerations for maturing the pipeline, such as metadata management, experiment tracking, and monitoring. These are important topics that are outside the scope of this guide. The following sections discuss another aspect of pipeline management, which is pipeline automation.

## Different levels of automation
<a name="automation"></a>

Although you can set up a training pipeline manually in the AWS SageMaker console, in practice, we recommend minimizing manual touchpoints in the deployment of ML training pipelines to ensure that ML models are deployed consistently and repeatedly. Depending on your requirements and the business problems you're addressing, you can determine and implement a deployment strategy on three levels: semi-automated, fully automated, and fully managed.
+ Semi-automated ─ By default, the steps discussed in the previous section follow a semi-automated approach, because they deploy the training and inference pipeline by using AWS Cloudformation templates. This helps ensure the reproducibility of the pipeline and helps you change and update it easily.
+ Fully automated ─ A more advanced option is to use continuous integration and continuous deployment (CI/CD) to the development, staging, and production environments. Incorporating CI/CD practices to the deployment of the training pipeline can ensure that automation includes traceability as well as quality gates.
+ Fully managed ─ Ultimately, you can develop a fully managed system so that you can deploy a ML training pipeline with a set of simple manifests, and the system can self-configure and coordinate required AWS services.

In this guide, we chose to present a concrete architecture. However, there are alternative technologies you can consider. The next two sections discuss some alternative choices for the platform and the orchestration engine.

## Different platforms for ML workloads
<a name="platforms"></a>

[AWS SageMaker](https://aws.amazon.com/sagemaker/) is the AWS managed service for training and serving ML models. Many users appreciate its wide array of built-in features and the many options it offers for running ML workloads. SageMaker is particularly useful if you are just getting started with implementing ML in the cloud. The key features of SageMaker include:
+ Built-in traceability (including labeling, training, model tracking, optimization, and inference).
+ Built-in one-click options** **for training and inference with minimal Python and ML experience.
+ Advanced hyperparameter tuning.
+ Support for all major artificial intelligence and machine learning (ML/AI) frameworks and custom Docker containers.
+ Built-in monitoring capabilities.
+ Built-in tracking of histories, including training jobs, processing jobs, batch transform jobs, models, endpoints, and searchability. Some histories, such as training, processing, and batch transform, are immutable and append-only.

One of the alternatives to using Amazon SageMaker is [AWS Batch](https://aws.amazon.com/batch/). AWS Batch provides a lower level of control over the compute and orchestration for your environment, but it isn't custom-built for machine learning. Some of its key features include:
+ Out-of-the-box automatic scaling of compute resources based on workload.
+ Out-of-the-box support for job priority, retries, and job dependencies.
+ Queue-based approach that supports building recurrent and on-demand jobs.
+ Support for CPU and GPU workloads. The ability to use GPU for building ML models is critical, because GPU can speed up the training process significantly, especially for deep learning models.
+ Ability to define a custom [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) for the compute environment.

## Different engines for pipeline orchestration
<a name="engines"></a>

The second main component is the pipeline orchestration layer. AWS provides [Step Functions](https://aws.amazon.com/step-functions/) for a fully managed orchestration experience. A popular alternative to Step Functions is Apache Airflow. When making a decision between the two, consider the following:
+ Required infrastructure – AWS Step Functions is a fully managed service and is serverless, whereas Airflow requires managing your own infrastructure and is based on open-source software. As a result, Step Functions provides high availability out of the box, whereas administering Apache Airflow requires additional steps.
+ Scheduling capabilities – Both Step Functions and Airflow provide comparable functionalities.
+ Visualization capabilities and UI – Both Step Functions and Airflow provide comparable functionalities.
+ Passing variables within the computational graph – Step Functions provides limited functionality for using AWS Lambda functions, whereas Airflow provides XCom interfaces.
+ Usage – Step Functions is very popular among AWS customers, and Airflow has been widely adopted by the data engineering community.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
