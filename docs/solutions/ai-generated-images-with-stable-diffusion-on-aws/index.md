---
source_url: https://docs.aws.amazon.com/solutions/ai-generated-images-with-stable-diffusion-on-aws/index.html
---

---
title: 'Guidance for AI-Generated Images with Stable Diffusion on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ai-generated-images-with-stable-diffusion-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for AI-Generated Images with Stable Diffusion on AWS

Build and scale generative AI applications with high efficiency image generation capabilities

## Overview

This Guidance demonstrates how you can integrate Stable Diffusion from Stability AI with Amazon SageMaker to build and scale generative artificial intelligence (AI) applications. It makes it possible for you to decouple interdependent, monolithic generative AI applications that are often restrictive and time-consuming to modify, and implement automatic scaling and expansion for tasks like image inferences and model training. With enhanced platform management functions, such as resource access control, and API support for backend integration, you can use this Guidance to adapt generative AI to the specific needs of your organization.

## How it works

This architecture diagram shows how to use Stable Diffusion APIs to decouple applications into training and inference components that are hosted on Amazon SageMaker.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/ai-generated-images-with-stable-diffusion-on-aws.pdf)

![Architecture diagram](/images/solutions/ai-generated-images-with-stable-diffusion-on-aws/images/ai-generated-images-with-stable-diffusion-on-aws-1.png)

1. **Step 1**: The user submits the training or inference API query to Amazon API Gateway. The resource authorizers in API Gateway help limit the resource accessed by IPs.
1. **Step 2**: API Gateway passes the training or inference query to separate components. Both components contain AWS Lambda and Amazon SageMaker. Lambda gets the parameters in the query, then uses the parameters to initiate SageMaker training or the inference job. These parameters are used to train the Stable Diffusion model or used for the Stable Diffusion model to do image generation.
1. **Step 3**: SageMaker uses your customized Stable Diffusion docker image stored in Amazon Elastic Container Registry (Amazon ECR). Or, it can download the pre-trained Stable Diffusion models from Amazon Simple Storage Service (Amazon S3) to train the Stable Diffusion model, or generate images. SageMaker automatically scales based on request volume.
1. **Step 4**: The outputs of the training job are models or images. The outputs of the inference job are images. You can customize the outputs of the training jobs and inference jobs, and save the outputs into an Amazon S3 bucket. Then, API Gateway returns the generated image link to the user.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation is a service that helps you automate, test, and deploy infrastructure as code templates with continuous integration and continuous delivery (CI/CD) automations. Amazon CloudWatch, where you can use CloudWatch Logs, allows you to monitor, store, and access log files from Lambda and SageMaker,helping you record requests and visualize the state of your underlying services. Monitoring and storing log files by CloudWatch Logs helps you analyze and troubleshoot requests quickly. You can use versioning in Lambda to save your function's code and configuration as you develop it. Together with aliases, you can use versioning to perform blue/green and rolling deployments. Additionally, by using CloudFormation, you have production environments with templates, sandbox development capabilities, and test environments for increasing levels of operations control. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway uses a resource policy to control whether a specified principal, typically an AWS Identity and Access Management (IAM) role or group, can invoke the API. All IAM policies are scoped down to the minimum permissions required for Lambda and SageMaker to function properly. By scoping API Gateway resources and IAM policies to the minimum permissions required, you limit unauthorized access to applications and resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda runs functions in multiple Availability Zones to ensure that it is available to process events in case of a service interruption in a single zone. Also, Lambda automatically retries an error with delays between retries. Amazon S3 provides 99.999999999% (11 nines) durability and 99.99% availability of objects over a given year, which can help you store model and data resources with high reliability. API Gateway sets a limit on a steady-state rate and a burst of request submissions against all APIs in your account. You can configure custom throttling for your APIs. By limiting the number of requests per second or per minute, you can prevent your backend systems from being overwhelmed and maintain the reliability of your API. Lastly, SageMaker combined with Amazon S3 helps support your data resiliency and backup needs. SageMaker takes care of the underlying infrastructure required for training and deploying machine learning (ML) models, while AWS manages the compute instances, storage, and networking components, ensuring high availability and resilience. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is engineered to provide managed scaling automatically. When your function receives a request while it's processing a previous request, Lambda launches another instance of your function to handle the increased load. As traffic increases, Lambda increases the number of concurrent executions of your functions. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda uses a pay-per-use billing model, where you are billed only for the time your functions are running. SageMaker manages your ML infrastructure by automatically provisioning and scaling compute resources according to workload requirements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda is a serverless computing service, which means you don't have to provision or manage servers. It automatically scales your code in response to incoming events, and you only pay for the compute time used. This serverless architecture eliminates the need for idle servers, resulting in reduced energy consumption compared to traditional server-based architectures. With Lambda, you can optimize the utilization of computing resources, allowing you to break down your application into individual functions that can be independently scaled. This fine-grained scaling enables efficient resource allocation, as you only allocate resources to specific functions when they are actively processing requests. It eliminates the need to over-provision resources, leading to better resource utilization and reduced waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
