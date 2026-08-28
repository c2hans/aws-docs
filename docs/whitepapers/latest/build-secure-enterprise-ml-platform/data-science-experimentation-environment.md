---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/data-science-experimentation-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data science experimentation environment
<a name="data-science-experimentation-environment"></a>

Data scientists and ML engineers use the experimentation environment for individual or team-based experimentations for the different science projects. The environment needs to provide services and tools for data querying and analysis, code authoring, data processing, model training and tuning, container development, model hosting testing, source code control, and data science library package access.

## Data science services
<a name="data-science-services"></a>

The following services can be provisioned in the experimentation environment in the data science account:

**Amazon Athena** — Data scientists and ML engineers can use [Amazon Athena](https://aws.amazon.com/athena) to query data in the data lake directly using SQL language. Athena provides an easy way to quickly identify and analyze a large amount of data directly against data stored in S3.

**Amazon SageMaker AI Notebook Instance and SageMaker AI Studio** — Data scientists and ML engineers can use a [SageMaker Notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) or [SageMaker Studio](https://aws.amazon.com/sagemaker/studio/) to author code, prepare data, and run model training directly inside a [Jupyter](https://jupyter.org/) environment. SageMaker AI Notebook instances and [SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) come pre-installed with a list of library packages and kernels (such as [TensorFlow](https://www.tensorflow.org/), [Scikit-learn](https://scikit-learn.org/stable/), and [PyTorch](https://pytorch.org/)) for easy model development.

If you use a SageMaker AI Notebook instance for code authoring and experimentation, the SageMaker AI Notebook instance provides Lifecycle script support, which can be used for:
+ Setting up environment variables such as VPC, Security Group, and KMS keys
+ Configuring the Code Repo connection
+ Configuring a connection to the internal package management server (such as ArtiFactory or CodeArtifact)

This [sample CloudFormation script](https://github.com/aws-samples/secure-data-science-reference-architecture/blob/production/cloudformation/ds_env_sagemaker.yaml) creates a Lifecycle configuration that sets up environment variables, configures a GitHub connection, and configure a PyPi mirror server. If you use SageMaker AI Studio, you can use the SageMaker AI Studio custom image to set up connection to private package management server. A SageMaker AI Studio custom image allows you to create a Docker image with your own selections of kernels, language packages, and other files to run a Jupyter notebook in SageMaker AI Studio. For more information, see [Private package installation in Amazon SageMaker AI running in internet-free mode](https://aws.amazon.com/es/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/).

To use SageMaker AI Notebook instances or Studio in an enterprise environment, data scientists often need to provide infrastructure configuration information such as VPC configurations, KMS keys, and IAM roles for processing, training and hosing. To pass configurations to SageMaker AI training, processing jobs or model endpoints, consider using [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) to store these parameters in an encrypted fashion, and use a Python script to call these parameters via APIs. The Python script can be loaded onto the SageMaker AI notebook instance at startup using lifecycle configurations, or in a SageMaker AI Studio custom image.
+ **Amazon SageMaker AI Data Wrangler (Data Wrangler) **— [Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) is a feature of SageMaker AI Studio to import, transform, visualize, and analyze data. Data scientists can use Data Wrangler to perform data preparation tasks such as plotting histogram and scatter charts against datasets, running data transformations such as one-hot encoding, or handing data outliers.
+ **Amazon SageMaker AI Processing** — Data scientists and ML engineers can use [SageMaker AI processing](https://aws.amazon.com/blogs/aws/amazon-sagemaker-processing-fully-managed-data-processing-and-model-evaluation/) for large data processing jobs. SageMaker AI processing provides built-in open-source containers for Scikit-learn and Spark. Data scientists can also bring custom containers to run processing jobs.
+ **Amazon SageMaker AI Feature Store **— [SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) can help data scientists share common data features with other data scientists across teams for model training and inference. SageMaker AI Feature Store supports both offline feature store for training and online feature store for online inferencing.****
+ **Amazon SageMaker AI Training / Tuning service** — For [model training and tuning](https://aws.amazon.com/getting-started/hands-on/train-tune-deep-learning-model-amazon-sagemaker/), SageMaker AI provides fully managed model training and tuning services. It provides a list of built-in algorithms for different machine learning tasks such as classification, regression, clustering, computer vision, natural language processing, time series, and anomaly detection. It also provides a list of fully managed training open-source containers for [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), [Apache MXNet](https://mxnet.apache.org/versions/1.8.0/), and [Scikit-learn](https://scikit-learn.org/stable/). Custom training containers can also be used for model training and tuning.
+ **Amazon SageMaker Clarify (SageMaker Clarify)** — Data scientists and ML engineers can use [SageMaker Clarify](https://aws.amazon.com/sagemaker/clarify/) to compute pre-training and post-training bias metrics and feature attribution for explainability.
+ **Amazon SageMaker AI Hosting** — Data scientists and ML engineers can test model deployment and real-time inference using the [SageMaker AI hosting service](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html#how-it-works-hosting). Models trained using the SageMaker AI built-in algorithms and managed containers can be deployed quickly using a single API command. Custom model inference containers can also be brought in to host custom models.****
+ **Amazon SageMaker AI Pipelines **— [SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) is a fully managed CI/CD service for machine learning. It can be used to automate various steps of the ML workflow such as data processing/transformation, training and tuning, and model deployment.
+ **AWS Step Functions** — [AWS Step Functions](https://aws.amazon.com/step-functions) is a fully managed workflow orchestration tool. It comes with a data science SDK that provides easy integration of SageMaker AI services such as processing, training, tuning, and hosting. Data scientists and ML engineers can use AWS Step Functions to build workflow pipelines to automate the different steps (such as data processing and model training) in the experimentation environments.
+ **Code repository** — A code repository such as [Bitbucket](https://bitbucket.org/) or [CodeCommit](https://aws.amazon.com/codecommit/) should be provided to data scientists and ML engineers for code management and version control. The code repository can reside in the Shared Services account or on-premises, and it is accessible from the data science account.
+ **Amazon ECR (ECR)** — [ECR](https://aws.amazon.com/ecr/) is used to store training, processing, and inference containers. Data scientists and ML engineers can use ECR in the data science account to manage custom containers for experimentation.
+ **Artifacts repository** — Organizations with strict internet access control often do not allow its users to download and install library packages from public package repositories directly, such as the [Python Package Index](http://pypi.org/) (PyPi) or [Anaconda](https://www.anaconda.com/). Private package repositories such as [Artifactory](https://jfrog.com/artifactory), [AWS CodeArtifact](https://aws.amazon.com/codeartifact/), or mirroring PyPI servers can be created to support private packages management. These servers can be used to host private packages as well as a mirroring site for public package sites such as the PyPi for Pip or [Anaconda main package channel](http://repo.anaconda.com/pkgs/main) and [Conda-forge channel](https://conda.anaconda.org/conda-forge/) for Anaconda.

![A diagram showing core components in the experimentation environment.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-9.png)

*Core components in the experimentation environment*

## Enabling self-service
<a name="enabling-self-service"></a>

To improve onboarding efficiency for data scientists and ML engineers, consider developing a self-service capability using the [Service Catalog](https://aws.amazon.com/servicecatalog/?aws-service-catalog.sort-by=item.additionalFields.createdDate&aws-service-catalog.sort-order=desc). The Service Catalog enables you to create self-service portfolio and products using CloudFormation scripts, and data scientists can directly request access to SageMaker AI Notebook / SageMaker AI Studio and other related AWS services without going through manual provisioning. Follow the instructions in [Enable self-service, secured data science using Amazon SageMaker AI notebooks and Service Catalog](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/) to enable self-service for data science products.

![A diagram that shows enabling self-service for data science products with Service Catalog.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-10.png)

*Enabling self-service for data science products with Service Catalog*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
