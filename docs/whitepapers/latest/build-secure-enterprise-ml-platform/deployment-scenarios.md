---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/deployment-scenarios.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deployment scenarios
<a name="deployment-scenarios"></a>

Depending on the deployment requirements, different pipelines need to be developed. Following are some examples of scenarios for deployment considerations:
+ **End-to-end pipeline** — This pipeline includes stages such as the Docker image build, data processing, model training, approval, and model deployment. This pipeline builds everything from a source code repository and input data and deploys a model to a production endpoint.
+ **Docker build pipeline** — This pipeline builds Docker images using source code (a Docker file) from the source code repository and pushes the images to a container registry such as Amazon ECR, along with additional metadata.
+ **Model training pipeline** — This pipeline trains/retrains a model with an existing Docker container image and dataset, and optionally registers the model in the model registry after it is trained.
+ **Model registration pipeline** — This pipeline registers an existing model saved in S3 and its associated inference container in ECR in the SageMaker AI model registry.
+ **Model deployment pipeline** — This pipeline deploys an existing model from the SageMaker AI model registry to an endpoint.

There are several ways to trigger a pipeline run, including:
+ A source code change
+ A scheduled event
+ On-demand via CLI / API

If source code change is used to trigger a pipeline run, you can either trigger the pipeline on any change in the source code repository, or only when a specific condition is met. If you use CodeCommit as the source, the following architecture pattern can be used to implement custom logic on whether to kick off a pipeline execution.

![A diagram showing the architecture pattern for kicking off pipeline based on custom logic.](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-15.png)

*Architecture pattern for kicking off pipeline based on custom logic*
