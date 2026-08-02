---
source_url: https://docs.aws.amazon.com/solutions/generative-ai-deployments-using-amazon-sagemaker-jumpstart/index.html
---

# Guidance for Generative AI Deployments using Amazon SageMaker JumpStart

## Overview

This Guidance demonstrates how to deploy a generative artificial intelligence (AI) model provided by Amazon SageMaker JumpStart to create an asynchronous SageMaker endpoint with the ease of the AWS Cloud Development Kit (AWS CDK). AWS CDK pipelines will create an asynchronous Amazon SageMaker endpoint and leverage the respective model to help accelerate and simplify the development process with preconfigured components that you can use to develop your applications. This Guidance uses the Stable Diffusion foundation model (FM) as an example, however, you can replace this model with any other model available on Amazon SageMaker JumpStart.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/generative-ai-deployments-using-amazon-sagemaker-jumpstart.pdf)

![Architecture diagram](/images/solutions/generative-ai-deployments-using-amazon-sagemaker-jumpstart/images/generative-ai-deployments-using-amazon-sagemaker-jumpstart-1.png)

1. **Step 1**: The AWS Admin deploys the AWS Cloud Development Kit (AWS CDK) repository and pipeline stacks, and pushes the project code to AWS CodeCommit.
1. **Step 2**: Once the code is pushed to CodeCommit, AWS CodePipeline invokes automatically.
1. **Step 3**: AWS CodeBuild downloads the foundational model inference code and the foundational model data from Amazon SageMaker.
1. **Step 4**: CodeBuild re-packages the retrieved model inference code and foundational model data into an image generation model to be used with a SageMaker endpoint later.
1. **Step 5**: The CodePipeline then deploys the application stack.
1. **Step 6**: The client or user can upload their model input (example - an image generation prompt) with parameters as a JSON file to an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 7**: The user invokes the asynchronous SageMaker endpoint.
1. **Step 8**: The SageMaker endpoint scales up inside its Application Auto Scaling group by starting at least one inference compute instance. It reads the input file from the Amazon S3 bucket.
1. **Step 9**: The endpoint generates the result according to the input, and stores the raw output in a JSON file in the same Amazon S3 bucket.
1. **Step 10**: The SageMaker endpoint sends the completed result of the operation to either a Success or Error Amazon Simple Notification Service (Amazon SNS) topic.
1. **Step 11**: The result from either topic is stored in the Amazon S3 bucket through an AWS Lambda function subscribed to the topics for easy state tracking by the user.
1. **Step 12**: In case the completion was successful, another Lambda function subscribed to the Success topic performs post-processing on the result from the Amazon S3 bucket.
1. **Step 13**: Lambda generates the post-processed result (example - converting JSON RGB values into a PNG image file) and stores it in the Amazon S3 bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-generative-ai-deployments-using-amazon-sagemaker-jumpstart)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses SageMaker endpoints, Lambda, CodePipeline, CodeCommit, and AWS CDK to enhance operational excellence. SageMaker provides standard logging and metrics for monitoring and analyzing the performance of deployed machine learning models, helping users gain insights into operational health and make data-driven decisions for continuous improvement. Lambda offers built-in logging and metrics capabilities, and we utilize Lambda Powertools to ensure consistent logging with the Lambda functions. CodePipeline and CodeCommit allow you to deploy changes as code for repeatability, consistency, and traceability with rollbacks and controlled change management to minimize disruptions and errors. Finally, the infrastructure-as-code approach with AWS CDK accelerates cloud development using common programming languages to model applications. These services help users with better visibility, troubleshooting, and understanding the behavior of their functions. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The services selected for this Guidance, coupled with the security measures integrated within this Guidance, support the goals of maintaining a secure environment, protecting sensitive data, and adhering to security best practices. AWS Identity and Access Management (IAM) helps enhance security by enabling you to manage user identities, roles, and permissions, ensuring that users only have the necessary access to AWS resources. The Amazon S3 bucket used in the codebase is encrypted by default, helping maintain the confidentiality and integrity of the stored data. The Amazon SNS topics only accept encrypted communication, ensuring secure transmission of messages. The permissions for accessing resources on other resources, such as Amazon S3 buckets, are set up according to AWS CDK standards. The code follows the principle of least-privilege, granting only the minimum level of access required for specific operations, helping reduce the attack surface area and mitigate the potential impact of any compromised credentials. These measures help protect sensitive information and mitigate risks associated with unauthorized access or data breaches. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance enhances reliability through scalable resources, efficient troubleshooting, automated deployments, and leveraging standard AWS functionality, promoting a stable and high-performing infrastructure that handles varying workloads and reduces downtime. The services used to enhance reliability in this Guidance include SageMaker, Lambda, Amazon SNS, Amazon S3, and AWS CDK pipelines. SageMaker provides scalability for the asynchronous endpoint, allowing users to configure the maximum count of instances to meet their specific needs. Lambda functions utilize Lambda Powertools to ensure proper logging format, enhancing troubleshooting capabilities, and reducing mean time to resolution. Using Amazon SNS and Amazon S3 for logging and storage, you can capture and store data reliably, supporting compliance requirements and reliable operations. The AWS CDK pipelines, CodeCommit, and CodePipeline enable automated and controlled deployments, ensure consistency, reducing the risk of errors, and offer rollbacks for a reliable architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SageMaker, Lambda, Amazon SNS, and Amazon S3 are used to support optimal model hosting, serverless orchestration, efficient storage, flexibility, and adaptability. This leads to cost-effective scaling, reduced latency, and improved overall performance. SageMaker provides the best option for hosting a machine learning model, with the asynchronous endpoints autoscaling functionality offering efficient inference and scalability, dynamically adjusting resources based on demand. Lambda and Amazon SNS are used to orchestrate the logic in a serverless, scalable, and cost-effective manner, helping you avoid manual infrastructure management for improved performance efficiency. Amazon S3 is utilized as a storage solution due to its purpose, performance, and features like built-in object lifecycle management that optimizes data access for image generation and reduced latency. The TOML configuration file used in the AWS CDK project allows for easy adjustment of deployment parameters, enabling rapid redeployment and resource calibration for specific performance requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker, with the auto-scaling endpoint, Amazon SNS, Lambda, and Amazon S3 help you optimize costs by minimizing idle resources, manage storage, and leverage pay-per-use services, so you can accurately estimate expenses and maximize the value obtained from AWS. The asynchronous SageMaker endpoint is set up with a scalable target, which ensures that no compute resources are permanently running when not in use. Lambda functions handle the conversion process and are pay-per-use. Amazon SNS is also a pay-per-use service, charging only for completion and message deliveries. Amazon S3 offers scalable, pay-as-you-go pricing where you can configure the Amazon S3 Lifecycle policy to remove older objects that are no longer of interest and reduce ongoing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, Amazon SNS, and Amazon S3 are serverless services and support on-demand resource consumption, with a scalable and flexible architecture and high resource utilization. Serverless services activate resources only when needed, reducing energy consumption and carbon footprint. Dynamic resource allocation optimizes utilization and sustainability. The SageMaker asynchronous endpoint is set up as a scalable target with a minimum instance count of 0, allowing for flexible scaling. By utilizing these services, you can minimize the overall resource consumption and maximize resource utilization, leading to improved sustainability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
