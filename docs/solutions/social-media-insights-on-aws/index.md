---
source_url: https://docs.aws.amazon.com/solutions/social-media-insights-on-aws/index.html
---

# Guidance for Social Media Insights on AWS

## Overview

This Guidance shows how to obtain insights, like sentiment, entities, locations, and topics based on social media posts, customer reviews, or other short form content. With the accompanying sample code, you are given a code base to serve as an information extraction system. This system extracts information across various social media platforms, including X, Facebook, and Instagram using a large language model (LLM), providing you with actionable insights about your products and services.

## How it works

This Guidance helps you gain insight into what your customers are saying about your products and services on social media websites such as X, Facebook, and Instagram. Instead of filtering out posts manually, you can build a near real-time alert system that consumes data from social media and extracts insights, such as topics, entities, sentiment, and location using a large language model (LLM) in Amazon Bedrock.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/social-media-insights-on-aws.pdf)

![Architecture diagram](/images/solutions/social-media-insights-on-aws/images/social-media-insights-on-aws-1.png)

1. **Step 1**: An Amazon Elastic Container Service (Amazon ECS) task runs on serverless infrastructure managed by AWS Fargate and maintains an open connection to the social media.
1. **Step 2**: The social media access tokens are securely stored in AWS Systems Manager Parameter Store, and the container image is hosted on Amazon Elastic Container Registry (Amazon ECR).
1. **Step 3**: When a new social media post arrives, it's placed into an Amazon Simple Queue Service (Amazon SQS) queue.
1. **Step 4**: The logic of this Guidance resides in AWS Lambda function microservices, coordinated by AWS Step Functions.
1. **Step 5**: The post is processed in real-time by one of the large language models (LLMs) supported by Amazon Bedrock.
1. **Step 6**: Amazon Location Service transforms a location name into coordinates.
1. **Step 7**: The post and metadata (insights) are sent to Amazon Simple Storage Service (Amazon S3).
1. **Step 8**: Amazon Athena queries the processed tweets with standard SQL.
1. **Step 9**: Amazon Lookout for Metrics looks for anomalies in the volume of mentions per category. Amazon Simple Notification Service (Amazon SNS) sends an alert to users when an anomaly is detected.
1. **Step 10**: We recommend setting up a Amazon QuickSight dashboard so that users can easily visualize insights.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/ai-powered-text-insights)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch keeps logs of the operations performed in the text processing workflow, allowing for efficient monitoring of the applications status. Amazon CloudFormation allows for reproducibility of the deployment and can also be rolled back to a stable state in case deployment fails. Additionally, Amazon Bedrock is a managed service to use LLMs through a simple interface. This combination of monitoring, reproducible deployments, and AWS managed LLMs usage offers powerful natural language processing capabilities without having to manage the underlying infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The data stored in Amazon S3 is encrypted at rest using AWS Key Management Service (AWS KMS) keys, and AWS Identity and Access Management (IAM) is utilized to control access to the data. Specifically, AWS KMS assists in the creation and management of the encryption keys used to securely encrypt the data stored in Amazon S3. Whereas IAM provides the capability to configure granular permissions based on roles for least privilege access control to that data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The data is stored in Amazon S3, an object storage service that offers 99.999999999% (11 nines) durability. The LLMs are invoked using Amazon Bedrock through a simple and efficient API interface that can automatically scale up and down. Athena, QuickSight, and AWS Glue are used to query and visualize the data at scale without the need to provision infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Through the use of various serverless and managed AWS services, this Guidance is designed for your workloads to achieve high performance efficiency, automatically scaling resources to meet the demands of the workload, and providing a seamless experience for you to access insights from your social media platforms. For example, Lambda, a serverless compute service, automatically scales up and down based on demand, ensuring the compute capacity is optimized for the workload. With Amazon Bedrock, you can invoke LLMs from an extensive catalogue without the need to provision and manage the underlying servers. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda is used in this architecture to process events and initiate the batch transformation analysis, removing the need for a continuously running server. Moreover, AWS Glue jobs are used to perform extract, transform, load (ETL) on batches of user data, rather than individual records. By aggregating the data and processing in larger chunks, the overall compute and storage requirements are reduced, leading to lower costs compared to handling each record individually. Lastly, Amazon Bedrock allows for the use of the LLN that best fits your budget requirement so you do not incur unnecessary expenses associated with more powerful, but potentially over-provisioned, models. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, AWS Glue, Athena, and QuickSight are all serverless services that operate on-demand, adjusting their resource use to match the current workload. This helps ensure that the performance and use of resources are maximized, as the services scale up and down automatically to accommodate the required demand. By using these serverless offerings, this architecture can efficiently utilize the necessary resources, avoiding over-provisioning or under-utilization of compute, storage, and other infrastructure components. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build a news-based real-time alert system with Twitter, Amazon SageMaker, and Hugging Face**: This post demonstrates how to build a real-time alert system that consumes news from Twitter and classifies the tweets using a pre-trained model from the Hugging Face Hub.

[Build a news-based real-time alert system with Twitter, Amazon SageMaker, and Hugging Face](https://aws.amazon.com/blogs/machine-learning/build-a-news-based-real-time-alert-system-with-twitter-amazon-sagemaker-and-hugging-face/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
