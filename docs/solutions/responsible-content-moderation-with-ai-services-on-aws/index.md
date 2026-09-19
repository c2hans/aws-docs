---
source_url: https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/index.html
---

---
title: 'Guidance for Responsible Content Moderation with AI Services on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Responsible Content Moderation with AI Services on AWS

## Overview

This Guidance demonstrates how game developers can moderate user-generated content (UGC) to ensure appropriate and safe player interactions. With AWS managed services and custom machine learning models, developers can quickly set up a content moderation backend system in one place. This backend system supports detecting and filtering comprehensive toxic content, along with customizable content flagging. The well-designed APIs allow for fast integration with the game and community tools. Ultimately, this allows developers to face the operational risks of user-provided content in online gaming platforms head-on; manual content moderation is error-prone and costly, whereas content moderation, powered by artificial intelligence (AI), dramatically accelerates the process to keep gaming communities safe.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/responsible-content-moderation-with-ai-services-on-aws.pdf)

![Architecture diagram](/images/solutions/responsible-content-moderation-with-ai-services-on-aws/images/responsible-content-moderation-with-ai-services-on-aws-1.png)

1. **Step 1**: The developer prepares the images and label data in Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Amazon SageMaker notebooks and training jobs use training materials to train the custom model.
1. **Step 3**: On completion, training jobs output the custom model in the Amazon S3 bucket.
1. **Step 4**: The developer deploys the model to a SageMaker endpoint for a custom moderation handler.
1. **Step 5**: Amazon API Gateway receives images for image moderation requests.
1. **Step 6**: Amazon Elastic Container Registry (Amazon ECR) hosts a container image repository for AWS Lambda.
1. **Step 7**: The moderation handler in Lambda processes the request based on the parameters in the URL and merges the results from the handlers.
1. **Step 8**: The moderation handler distributes the request to Amazon Rekognition based on the image moderation labels.
1. **Step 9**: The moderation handler distributes the request to the SageMaker endpoint based on the image moderation labels.
1. **Step 10**: (Optional) A video file is uploaded to Amazon S3 to invoke the video handler in Lambda.
1. **Step 11**: (Optional) Amazon S3 stores the key frame images from videos and starts the invocation of the moderation handler to process the detection of the images.
1. **Step 12**: (Optional) The video handler processes the moderation result and returns it to the original Amazon S3 bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-powered-ugc-content-moderation-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda and API Gateway are used in this Guidance to support operational excellence by managing infrastructure and providing monitoring capabilities. Lambda handles all infrastructure needs to complete functions with minimal maintenance. Meanwhile, both Lambda and API Gateway integrate with Amazon CloudWatch metrics that can be used to monitor individual application components. Additionally, Lambda enables seamless deploying, debugging, and troubleshooting through infrastructure as code (IaC) tools like the AWS Serverless Application Model (AWS SAM) and the AWS Cloud Development Kit (AWS CDK). It handles all function maintenance, security patching, and monitoring by providing invocation as well as processing logs and metrics to identify errors and performance bottlenecks. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Lambda and API Gateway are native AWS security services that help developers to reduce risky external dependencies while securing access to sensitive functionalities. Specifically, Lambda uses AWS Identity and Access Management (IAM) roles configured with least privilege principles to communicate with other AWS services such as Amazon Rekognition and SageMaker. This restricts services to only the permissions they require. Additionally, API Gateway simplifies authentication and authorization by integrating with IAM and Lambda. Together, these facilitate a secure environment where credentials and access can be precisely managed according to best practices. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Regional AWS services utilized—including Lambda, API Gateway, and Amazon Rekognition—take advantage of Availability Zones (AZs) and multi-AZ redundancy to ensure high availability targets are met. By leveraging these fully managed services, developers can focus on core application logic rather than complex availability management. Lambda auto-scaling and automated retries shield developers from these concerns while ensuring reliability is maintained even under peak loads. Tapping into the innate high availability of AWS Regional services allows developers to easily achieve resilient network topology without architecting complex solutions themselves. The automation and self-healing capabilities make the backend infrastructure extremely durable in the face of most typical failures or surges. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The fully managed auto-scaling capabilities of Lambda and SageMaker make them ideal choices to support the near real-time and high concurrency demands of content moderation. As more moderation requests flow in, Lambda automatically handles the provisioning of additional environments to fulfill each one with low latency. Similarly, SageMaker endpoints dynamically adjust the number of machine learning (ML) inference instances based on fluctuating request workloads. Developers can rely on the innate scaling of these services to efficiently process bursting request volumes without over-provisioning resources. By leveraging the performance efficiency optimizations of Lambda and SageMaker, the backend infrastructure can cost-effectively manage unpredictable traffic—maintaining responsive moderation at any scale. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The serverless services used in this Guidance, like Lambda, API Gateway, and Amazon S3, are leveraged to minimize costs and avoid overprovisioning. Lambda bills in millisecond increments based on actual computation time used—developers only pay for the precise resources needed to process each moderation request. Similarly, API Gateway charges are incurred per API call, so costs scale directly with usage. And Amazon S3 provides a low total cost of ownership for stored content. Since moderation queries per second can fluctuate drastically and be hard to predict, the serverless pay-as-you-go model is ideal when compared to overprovisioning dedicated servers. By tapping into these auto-scaling cloud services that align cost with usage, developers can optimize expenses even with volatile request patterns. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless services used in this Guidance optimize sustainability by only consuming compute resources that scale directly with the velocity of the workloads. Since these are fully managed AWS offerings, no energy is wasted on idle, overprovisioned capacity. Lambda and API Gateway scale precisely to usage levels, so developers have no useless idle resources. And by leveraging SageMaker for ML inferencing rather than training models, inference compute needs are minimized. This serverless, event-driven architecture allows workloads to breathe with traffic patterns, optimizing energy demands accordingly. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
