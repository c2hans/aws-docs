---
source_url: https://docs.aws.amazon.com/solutions/multimodal-video-analytics-of-smart-product-subscription-services-on-aws/index.html
---

---
title: 'Guidance for Multimodal Video Analytics of Smart Product Subscription Services on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multimodal-video-analytics-of-smart-product-subscription-services-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Multimodal Video Analytics of Smart Product Subscription Services on AWS

Video analytics that elevate your smart products

## Overview

This Guidance demonstrates how providers offering smart product subscriptions can use large language model (LLM) inferencing to create innovative video analytics services that drive customer value and revenue. By implementing AI-powered video analytics, providers can transform raw video data into meaningful, actionable intelligence that solves specific customer problems. For instance, home camera systems can use AI to detect and alert homeowners about package theft in real-time, generate comprehensive summaries of pet behaviors from camera footage, and provide actionable insights that enhance user engagement. By using AI to develop targeted subscription services, this Guidance can help providers increase product utility, improve their customer's experience, and create new revenue streams through intelligent, contextual video analysis that goes beyond traditional monitoring capabilities.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multimodal-video-analytics-of-smart-product-subscription-services-on-aws.pdf)

![Architecture diagram](/images/solutions/multimodal-video-analytics-of-smart-product-subscription-services-on-aws/images/multimodal-video-analytics-of-smart-product-subscription-services-on-aws-1.png)

1. **Step 1**: Ingest data, edit prompts, perform analytics, and set postprocessing actions on a website hosted on AWS Amplify.
1. **Step 2**: The website passes the request to and receives a response from Amazon API Gateway.
1. **Step 3**: API Gateway directs a request to the videostreaming-and-upload component, which integrates video data from a smart camera (using Amazon Kinesis Video Streams) or image data (from AWS IoT Core). Use AWS IoT Greengrass to manage and deploy machine learning models to edge devices.
1. **Step 4**: API Gateway forwards the analysis request, which includes video frames and prompts, to the visual analytics component. This component, equipped with an AWS Lambda function and a model library, processes the request and returns the result from the language model to API Gateway. The model library includes the foundation models on Amazon Bedrock and an open-source model hosted on Amazon SageMaker.
1. **Step 5**: If you specify a postprocessing action through natural language input, the LLM agent, delivered by an Amazon Bedrock agent or Lambda, will implement it through various capabilities hosted in Lambda functions. One example includes sending SMS messages to mobile clients or notifications to edge devices.
1. **Step 6**: You can store the videos in Amazon Simple Storage Service (Amazon S3). You can also store video metadata and fine-tune prompts on Amazon DynamoDB. The prompts can also be managed by Amazon Bedrock Prompt Management.
1. **Step 7**: You will have the option to save intermediate results of video analysis to Amazon OpenSearch Service through a Lambda function. Then, on the website, you can use an LLM through Amazon Bedrock to conduct question-and-answer sessions based on the video content.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multimodal-video-analytics-of-smart-product-subscription-services-on-aws?target=_blank)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda facilitates seamless deployment and debugging through infrastructure-as-code (IaC) tools like an AWS Cloud Development Kit (AWS CDK). Lambda also offloads the burden of infrastructure management, handling all maintenance, security patches, and monitoring for functions. For example, it works with API Gateway to supply Amazon CloudWatch metrics on workflow elements like video analytics inferencing and message postprocessing. Using these logs and metrics from Lambda functions, your developers can more easily troubleshoot errors and performance bottlenecks. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway acts as a proxy between the client and backend services, providing a protection layer when you invoke category services through an outbound API. This enables you to control access and implement security measures. Additionally, AWS IoT Core provides secure communication, authentication, authorization, and data protection mechanisms for edge devices. This helps it maintain the confidentiality, integrity, and availability of data exchanged between Internet of Things (IoT) devices and AWS, enabling secure and reliable edge computing operations. Finally, you can seamlessly integrate API Gateway and AWS IoT Core with AWS Identity and Access Management (IAM) so that you can control access to resources and data according to the principle of least privilege. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS Regional services like Lambda, Amazon Bedrock, Amazon S3, and DynamoDB, which use Availability Zones and static stability to achieve high availability. As managed services, Lambda and Amazon Bedrock provide retry and automatic scaling features. Additionally, Amazon S3 and DynamoDB are designed for high reliability, minimizing the risk of losing videos and prompts in the case of a failure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Kinesis Video Streams enables IP cameras to directly connect to the cloud, streamlining edge-to-cloud video processing in near real time. Additionally, Amazon Bedrock enables your developers to leverage LLMs for video analysis, using APIs to invoke and run inferences. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda bills per millisecond of resource use, so you can run video ingestion, analytics, and message postprocessing without paying for idle compute. Additionally, Amazon S3 and DynamoDB offer a low total cost of ownership for storing and retrieving prompts, video data, and images. Finally, Amazon Bedrock enables you to use LLMs without the need to host or manage your own LLM servers. It also provides a cost-effective API-based approach for invoking inferences, charging based on the number of input and output tokens used. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance invokes services like Lambda, API Gateway, and Amazon Bedrock only when there is a user query, minimizing resource overprovisioning. As serverless services, Lambda and API Gateway consume only the resources and energy required to support the workload. Additionally, as a managed service, Amazon Bedrock removes the need for you to host dedicated servers for LLMs. As a result, you can avoid the significant energy consumption associated with running such resource-intensive models. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
