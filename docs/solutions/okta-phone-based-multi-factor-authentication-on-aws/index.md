---
source_url: https://docs.aws.amazon.com/solutions/okta-phone-based-multi-factor-authentication-on-aws/index.html
---

# Guidance for Okta Phone-Based Multi-Factor Authentication on AWS

## Overview

This Guidance demonstrates how to implement a secure and scalable one-time passcode (OTP) delivery solution by using AWS with Okta’s identity platform. The Guidance supports multiple languages and communication methods and stores language-specific message templates in a dynamic, scalable database. This enables you to tailor OTP messages based on users’ preferred languages and delivery channels, such as SMS or voice calls. By using this Guidance, you can implement a reliable, flexible, and secure OTP delivery method that helps you accommodate a diverse user base.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/okta-phone-based-multi-factor-authentication-on-aws.pdf)

![Architecture diagram](/images/solutions/okta-phone-based-multi-factor-authentication-on-aws/images/okta-phone-based-multi-factor-authentication-on-aws-1.png)

1. **Step 1**: A user initiates sign-in on Okta and is prompted for phone-based authentication. The user chooses SMS or voice delivery to receive the OTP. Okta's telephony inline hook is activated, creating a JSON web token (JWT) request for OTP delivery through Amazon API Gateway.
1. **Step 2**: AWS WAF protects the API Gateway endpoint by applying rules managed by AWS to block malicious traffic. All traffic is filtered through AWS WAF web access control lists (ACL), and requests deemed safe are allowed to pass through to API Gateway.
1. **Step 3**: API Gateway first receives the JWT request from Okta. It then invokes a custom AWS Lambda function that acts as an authorizer to validate the JWT token before allowing the request to proceed.
1. **Step 4**: The Lambda authorizer is responsible for verifying the integrity and validity of the JWT token. It performs several checks to ensure the token is valid.
1. **Step 5**: The Lambda authorizer verifies the JWT token by decoding it, using Okta's public key to validate the signature and checking the expiration time.
1. **Step 6**: If the JWT token is valid, the Lambda authorizer creates an AWS Identity and Access Management (IAM) policy that grants permission to invoke API Gateway.
1. **Step 7**: The Lambda authorizer returns the IAM policy to API Gateway. If access is allowed, API Gateway is invoked and forwards the request to the backend Lambda function.
1. **Step 8**: If the Lambda function encounters an error or exception while processing the user's request, it may send the request to an Amazon Simple Queue Service (Amazon SQS) dead-letter queue for further investigation and troubleshooting.
1. **Step 9**: If no errors are found, the Lambda function contacts Amazon DynamoDB to retrieve message data based on the user's request details, such as their language preference and their choice of SMS or voice delivery. A DynamoDB table stores message templates tailored for various languages and communication methods. The Lambda function retrieves the appropriate message template that matches the user's request details.
1. **Step 10**: The Lambda function retrieves the message data and uses it to create a personalized message for the user. The message includes the OTP authentication code. Depending on the user's chosen method of communication, the function formats the message accordingly.
1. **Step 11**: AWS End User Messaging then sends the message to the user. For SMS, it sends a text message directly to the user's phone. For voice delivery, it converts the text into a voice message and delivers by phone call.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-okta-phone-based-multi-factor-authentication-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Lambda, API Gateway, and Amazon SQS to implement a serverless approach that provides scalability, flexibility, and ease of maintenance. For example, Lambda right-sizes its functions based on the minimum amount of memory and CPU required to complete their tasks. If one function encounters an error or exception, Lambda sends the failed event to an Amazon SQS dead-letter queue for further investigation and troubleshooting. Additionally, Amazon CloudWatch provides critical monitoring for proactive issue detection and resolution, supporting operational excellence. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance enhances security by implementing strong access control and data protection mechanisms. AWS WAF protects the API Gateway endpoint by applying managed rules to block malicious traffic. A custom Lambda function acts as an authorizer to validate JWTs before allowing requests to proceed. This authorizer decodes the JWT (which uses Okta’s public key to validate the signature) and checks the expiration time to confirm token validity. IAM manages access permissions, using the principle of least privilege to make sure that only authorized users and services can access resources. Additionally, AWS Key Management Service (AWS KMS) encrypts sensitive data, such as OTPs, and it encrypts CloudWatch logs to protect the confidentiality of recorded information. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance supports reliability through distributed workloads, error handling mechanisms, durable data storage, and a highly available messaging service. It distributes Lambda functions across multiple Availability Zones (AZs), helping you avoid the risk of a single point of failure caused by an AZ outage. The Amazon SQS dead-letter queue provides reliable message delivery by handling errors and retries, and it enables you to investigate any failed message processing. Additionally, DynamoDB offers a highly available and durable data store for user preferences and message templates. Finally, AWS End User Messaging enhances reliability by providing a highly available and scalable messaging service for SMS and voice communication. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless services so that you can quickly retrieve and process data without the need to manually manage infrastructure. Lambda scales automatically with your workloads and right-sizes its functions to achieve efficient resource use, and DynamoDB facilitates quick and efficient data retrieval. AWS End User Messaging converts text to speech on-demand for voice calls. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance minimizes costs by using on-demand, pay-as-you-go services. DynamoDB provides a flexible pricing model, and its on-demand capacity mode adjusts to workload volume, helping you reduce costs. For Lambda, you only pay for the compute time you consume, and its scalability helps you optimize costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses scalable, on-demand services to reduce the environmental impact of your cloud workloads and minimize waste. Lambda automatically scales on demand, helping you avoid the use of idle resources. Additionally, DynamoDB provides an on-demand mode that scales with the workload, delivering efficient resource use. Both services align with best practices for minimizing hardware usage and energy consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
