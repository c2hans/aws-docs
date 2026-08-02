---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html
---

# Build an MLOps workflow by using Amazon SageMaker AI and Azure DevOps
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops"></a>

*Deepika Kumar, Sara van de Moosdijk, and Philips Kokoh Prasetyo, Amazon Web Services*

## Summary
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-summary"></a>

Machine learning operations (MLOps) is a set of practices that automate and simplify machine learning (ML) workflows and deployments. MLOps focuses on automating the ML lifecycle. It helps ensure that models are not just developed but also deployed, monitored, and retrained systematically and repeatedly. It brings DevOps principles to ML. MLOps results in faster deployment of ML models, better accuracy over time, and stronger assurance that they provide real business value.

Organizations often have existing DevOps tools and data storage solutions before starting their MLOps journey. This pattern showcases how to harness the strengths of both Microsoft Azure and AWS. It helps you integrate Azure DevOps with Amazon SageMaker AI to create an MLOps workflow.

The solution simplifies working between Azure and AWS. You can use Azure for development and AWS for machine learning. It promotes an effective process for making machine learning models from start to finish, including data handling, training, and deployment on AWS. For efficiency, you manage these processes through Azure DevOps pipelines. The solution is applicable to foundation model operations (FMOps) and large language model operations (LLMOps) in generative AI, which includes fine-tuning, vector databases, and prompt management.

## Prerequisites and limitations
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-prereqs"></a>

**Prerequisites**
+ **Azure subscription** – Access to Azure services, such as Azure DevOps, for setting up the continuous integration and continuous deployment (CI/CD) pipelines.
+ **Active AWS account** – Permissions to use the AWS services used in this pattern.
+ **Data** – Access to historical data for training the machine learning model.
+ **Familiarity with ML concepts** – Understanding of Python, Jupyter Notebooks, and machine learning model development.
+ **Security configuration** – Proper configuration of roles, policies, and permissions across both Azure and AWS to ensure secure data transfer and access.
+ **(Optional) Vector database **– If you're using a Retrieval Augmented Generation (RAG) approach and a third-party service for the vector database, you need access to the external vector database.

**Limitations**
+ This guidance does not discuss secure cross-cloud data transfers. For more information about cross-cloud data transfers, see [AWS Solutions for Hybrid and Multicloud](https://aws.amazon.com/hybrid-multicloud/).
+ Multicloud solutions may increase latency for real-time data processing and model inference.
+ This guidance provides one example of a multi-account MLOps architecture. Adjustments are necessary based on your machine learning and AWS strategy.
+ This guidance does not describe the use of AI/ML services other than Amazon SageMaker AI.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-architecture"></a>

**Target architecture**

The target architecture integrates Azure DevOps with Amazon SageMaker AI, creating a cross-cloud ML workflow. It uses Azure for CI/CD processes and SageMaker AI for ML model training and deployment. It outlines the process of obtaining data (from sources such as Amazon S3, Snowflake, and Azure Data Lake) through model building and deployment. Key components include CI/CD pipelines for model building and deployment, data preparation, infrastructure management, and Amazon SageMaker AI for training and fine-tuning, evaluation, and deployment of ML models. This architecture is designed to provide efficient, automated, and scalable ML workflows across cloud platforms.

![Architecture diagram of an MLOps workflow that uses Azure Devops and SageMaker.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/95fdf414-e561-4a93-9628-b41db39a577e/images/84ddcc36-54ef-473e-875f-154fae18cb13.png)

The architecture consists of the following components:

1. Data scientists perform ML experiments in the development account to explore different approaches for ML use cases by using various data sources. Data scientists perform unit tests and trials, and to track their experiments, they can use [Amazon SageMaker AI with MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html). In generative AI model development, data scientists fine-tune foundation models from Amazon SageMaker AI JumpStart model hub. Following model evaluation, data scientists push and merge the code to the Model Build repository, which is hosted on Azure DevOps. This repository contains code for a multi-step model building pipeline.

1. On Azure DevOps, the Model Build pipeline, which provides continuous integration (CI), can be activated automatically or manually upon code merge to the main branch. In the Automation account, this activates the SageMaker AI pipeline for data preprocessing, model training and fine-tuning, model evaluation, and conditional model registration based on accuracy.

1. The Automation account is a central account across ML platforms that hosts ML environments (Amazon ECR), models (Amazon S3), model metadata (SageMaker AI Model Registry), features (SageMaker AI Feature Store), automated pipelines (SageMaker AI Pipelines), and ML log insights (CloudWatch). For a generative AI workload, you might require additional evaluations for prompts in the downstream applications. A prompt management application helps to streamline and automate the process. This account allows reusability of ML assets and enforces best practices accelerate delivery of ML use cases.

1. The latest model version is added to SageMaker AI Model Registry for review. It tracks model versions and respective artifacts (lineage and metadata). It also manages the status of the model (approve, reject, or pending), and it manages the version for downstream deployment.

1. After a trained model in Model Registry is approved through the studio interface or an API call, an event can be dispatched to Amazon EventBridge. EventBridge starts the Model Deploy pipeline on Azure DevOps.

1. The Model Deploy pipeline, which provides continuous deployment (CD), checks out the source from the Model Deploy repository. The source contains code, the configuration for the model deployment, and test scripts for quality benchmarks. The Model Deploy pipeline can be tailored to your inference type.

1. After quality control checks, the Model Deploy pipeline deploys the model to the Staging account. The Staging account is a copy of the Production account, and it is used for integration testing and evaluation. For a batch transformation, the Model Deploy pipeline can automatically update the batch inference process to use the latest approved model version. For a real-time, serverless, or asynchronous inference, it sets up or updates the respective model endpoint.

1. After successful testing in the Staging account, a model can be deployed to the Production account by manual approval through the Model Deploy pipeline. This pipeline provisions a production endpoint in the **Deploy to production** step, including model monitoring and a data feedback mechanism.

1. After the model is in production, use tools such as SageMaker AI Model Monitor and SageMaker AI Clarify to identify bias, detect drift, and continuously monitor the model's performance.

**Automation and scale**

Use infrastructure as code (IaC) to automatically deploy to multiple accounts and environments. By automating the process of setting up an MLOps workflow, it is possible to separate the environments used by ML teams working on different projects. [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you model, provision, and manage AWS resources by treating infrastructure as code.

## Tools
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-tools"></a>

**AWS services**
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a managed ML service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. In this pattern, Amazon S3 is used for data storage and integrated with SageMaker AI for model training and model objects.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use. In this pattern, Lambda is used for data pre-processing and post-processing tasks.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable. In this pattern, it stores Docker containers that SageMaker AI uses as training and deployment environments.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. In this pattern, EventBridge orchestrates event-driven or time-based workflows that initiate automatic model retraining or deployment.
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.  In this pattern, it is used to create an external-facing, single point of entry for SageMaker AI endpoints.
+ For RAG applications, you can use AWS services, such as [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) and [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html), to store the vector embeddings that provide the LLM with your internal data.

**Other tools**
+ [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops) helps you manage CI/CD pipelines and facilitate code builds, tests, and deployment.
+ [Azure Data Lake Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) or [Snowflake](https://docs.snowflake.com/en/) are possible third-party sources of training data for ML models.
+ [Pinecone](https://docs.pinecone.io/guides/get-started/overview), [Milvus](https://milvus.io/docs/overview.md), or [ChromaDB](https://docs.trychroma.com/) are possible third-party vector databases to store vector embeddings.

## Best practices
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-best-practices"></a>

Before implementing any component of this multicloud MLOps workflow, complete the following activities:
+ Define and understand the machine learning workflow and the tools required to support it. Different use cases require different workflows and components. For example, a feature store might be required for feature reuse and low latency inference in a personalization use case, but it may not be required for other use cases. Understanding the target workflow, use case requirements, and preferred collaboration methods of the data science team is needed to successfully customize the architecture.
+ Create a clear separation of responsibility for each component of the architecture. Spreading data storage across Azure Data Lake Storage, Snowflake, and Amazon S3 can increase complexity and cost. If possible, choose a consistent storage mechanism. Similarly, avoid using a combination of Azure and AWS DevOps services, or a combination of Azure and AWS ML services.
+ Choose one or more existing models and datasets to perform end-to-end testing of the MLOps workflow. The test artifacts should reflect real use cases that the data science teams develop when the platform enters production.

## Epics
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-epics"></a>

### Design your MLOps architecture
<a name="design-your-mlops-architecture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify data sources. | Based on current and future use cases, available data sources, and types of data (such as confidential data), document the data sources that need to be integrated with the MLOps platform. Data can be stored in Amazon S3, Azure Data Lake Storage, Snowflake, or other sources. For generative AI workloads, data might also include a knowledge base that grounds the generated response. This data is stored as vector embeddings in vector databases. Create a plan for integrating these sources with your platform and securing access to the correct resources. | Data engineer, Data scientist, Cloud architect |
| Choose applicable services. | Customize the architecture by adding or removing services based on the desired workflow of the data science team, applicable data sources, and existing cloud architecture. For example, data engineers and data scientists may perform data preprocessing and feature engineering in SageMaker AI, AWS Glue, or Amazon EMR. It is unlikely that all three services would be required. | AWS administrator, Data engineer, Data scientist, ML engineer |
| Analyze security requirements. | Gather and document security requirements. This includes determining:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops.html)<br />For more information about securing generative AI workloads, see [Securing generative AI: An introduction to the Generative AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/securing-generative-ai-an-introduction-to-the-generative-ai-security-scoping-matrix/) (AWS blog post). | AWS administrator, Cloud architect |

### Set up AWS Organizations
<a name="set-up-aolong"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS Organizations. | Set up AWS Organizations on the root AWS account. This helps you manage the subsequent accounts that you create as part of a multi-account MLOps strategy. For more information, see the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html). | AWS administrator |

### Set up the development environment and versioning
<a name="set-up-the-development-environment-and-versioning"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS development account. | Create an AWS account where data engineers and data scientists have permissions to experiment and create ML models. For instructions, see [Creating a member account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the AWS Organizations documentation. | AWS administrator |
| Create a Model Build repository. | Create a Git repository in Azure where data scientists can push their model build and deployment code after the experimentation phase is complete. For instructions, see [Set up a Git repository](https://learn.microsoft.com/en-us/devops/develop/git/set-up-a-git-repository) in the Azure DevOps documentation. | DevOps engineer, ML engineer |
| Create a Model Deploy repository. | Create a Git repository in Azure that stores standard deployment code and templates. It should include code for every deployment option that the organization uses, as identified in the design phase. For example, it should include real-time endpoints, asynchronous endpoints, serverless inference, or batch transforms. For instructions, see [Set up a Git repository](https://learn.microsoft.com/en-us/devops/develop/git/set-up-a-git-repository) in the Azure DevOps documentation. | DevOps engineer, ML engineer |
| Create an Amazon ECR repository. | Set up an Amazon ECR repository that stores the approved ML environments as Docker images. Allow data scientists and ML engineers to define new environments. For instructions, see [Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the Amazon ECR documentation. | ML engineer |
| Set up SageMaker AI Studio. | Set up SageMaker AI Studio on the development account according to the previously defined security requirements, preferred data science tools (such as MLflow), and preferred integrated development environment (IDE). Use lifecycle configurations to automate the installation of key functionality and create a uniform development environment for data scientists. For more information, see [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) and [MLflow tracking server](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) in the SageMaker AI documentation. | Data scientist, ML engineer, Prompt engineer |

### Integrate CI/CD pipelines
<a name="integrate-ci-cd-pipelines"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Automation account. | Create an AWS account where automated pipelines and jobs run. You can give data science teams read access to this account. For instructions, see [Creating a member account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the AWS Organizations documentation. | AWS administrator |
| Set up a model registry. | Set up SageMaker AI Model Registry in the Automation account. This registry stores the metadata for ML models and helps certain data scientists or team leads to approve or reject models. For more information, see [Register and deploy models with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) in the SageMaker AI documentation. | ML engineer |
| Create a Model Build pipeline. | Create a CI/CD pipeline in Azure that starts manually or automatically when code is pushed to the Model Build repository. The pipeline should check out the source code and create or update a SageMaker AI pipeline in the Automation account. The pipeline should add a new model to the model registry. For more information about creating a pipeline, see the [Azure Pipelines documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines). | DevOps engineer, ML engineer |

### Build the deployment stack
<a name="build-the-deployment-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create AWS staging and deployment accounts. | Create AWS accounts for staging and deployment of ML models. These accounts should be identical to allow for accurate testing of the models in staging before moving to production. You can give data science teams read access to the staging account. For instructions, see [Creating a member account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the AWS Organizations documentation. | AWS administrator |
| Set up S3 buckets for model monitoring. | Complete this step if you want to enable model monitoring for the deployed models that are created by the Model Deploy pipeline. Create Amazon S3 buckets for storing the input and output data. For more information about creating S3 buckets, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. Set up cross-account permissions so that the automated model monitoring jobs run in the Automation account. For more information, see [Monitor data and model quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) in the SageMaker AI documentation. | ML engineer |
| Create a Model Deploy pipeline. | Create a CI/CD pipeline in Azure that starts when a model is approved in the model registry. The pipeline should check out the source code and model artifact, build the infrastructure templates for deploying the model in the staging and production accounts, deploy the model in the staging account, run automated tests, wait for manual approval, and deploy the approved model into the production account. For more information about creating a pipeline, see the [Azure Pipelines documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines). | DevOps engineer, ML engineer |

### (Optional) Automate ML environment infrastructure
<a name="optional-automate-ml-environment-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Build AWS CDK or CloudFormation templates. | Define AWS Cloud Development Kit (AWS CDK) or AWS CloudFormation templates for all environments that need to be deployed automatically. This might include the development environment, automation environment, and staging and deployment environments. For more information, see the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) and [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) documentation. | AWS DevOps |
| Create an Infrastructure pipeline. | Create a CI/CD pipeline in Azure for infrastructure deployment. An administrator can initiate this pipeline to create new AWS accounts and set up the environments that the ML team requires. | DevOps engineer |

## Troubleshooting
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| **Insufficient monitoring and drift detection **– Inadequate monitoring can lead to missed detection of model performance issues or data drift. | Strengthen monitoring frameworks with tools such as Amazon CloudWatch, SageMaker AI Model Monitor, and SageMaker AI Clarify. Configure alerts for immediate action on identified issues. |
| **CI pipeline trigger errors **–** **The CI pipeline in Azure DevOps might not be triggered upon code merge due to misconfiguration. | Check the Azure DevOps project settings to ensure that the webhooks are properly set up and pointing to the correct SageMaker AI endpoints. |
| **Governance **–** **The central Automation account might not enforce best practices across ML platforms, leading to inconsistent workflows. | Audit the Automation account settings, ensuring that all ML environments and models conform to predefined best practices and policies. |
| **Model registry approval delays – **This happens when there's a delay in checking and approving the model, either because people take time to review it or because of technical issues. | Implement a notification system to alert stakeholders of models that are pending approval, and streamline the review process. |
| **Model deployment event failures **–** **Events dispatched to start model deployment pipelines might fail, causing deployment delays. | Confirm that Amazon EventBridge has the correct permissions and event patterns to invoke Azure DevOps pipelines successfully. |
| **Production deployment bottlenecks **–** **Manual approval processes can create bottlenecks, delaying the production deployment of models. | Optimize the approval workflow within the model deploy pipeline, promoting timely reviews and clear communication channels. |

## Related resources
<a name="build-an-mlops-workflow-by-using-amazon-sagemaker-and-azure-devops-resources"></a>

**AWS documentation**
+ [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/)
+ [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) (AWS Well Architected Framework)
+ [Planning for successful MLOps](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/welcome.html) (AWS Prescriptive Guidance)

**Other AWS resources**
+ [MLOps foundation roadmap for enterprises with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/) (AWS blog post)
+ [AWS Summit ANZ 2022 - End-to-end MLOps for architects](https://www.youtube.com/watch?v=UnAN35gu3Rw) (YouTube video)
+ [FMOps/LLMOps: Operationalize generative AI and differences with MLOps](https://aws.amazon.com/blogs/machine-learning/fmops-llmops-operationalize-generative-ai-and-differences-with-mlops/) (AWS blog post)
+ [Operationalize LLM Evaluation at Scale using Amazon SageMaker AI Clarify and MLOps services](https://aws.amazon.com/blogs/machine-learning/operationalize-llm-evaluation-at-scale-using-amazon-sagemaker-clarify-and-mlops-services/) (AWS blog post)
+ [The role of vector databases in generative AI applications](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/) (AWS blog post)

**Azure documentation**
+ [Azure DevOps documentation](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops)
+ [Azure Pipelines documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines)
