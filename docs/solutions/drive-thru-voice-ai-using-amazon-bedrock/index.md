---
source_url: https://docs.aws.amazon.com//solutions/drive-thru-voice-ai-using-amazon-bedrock//index.html
---

---
title: 'Guidance for Drive Thru Voice AI using Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/drive-thru-voice-ai-using-amazon-bedrock/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Drive Thru Voice AI using Amazon Bedrock

## Overview

This Guidance demonstrates how to address the challenge of slow, error-prone drive-thru ordering by implementing a real-time voice AI system that enables natural conversational ordering through Amazon Nova 2 Sonic. Customers interact with a digital menu board that processes their spoken orders through streaming audio, while the system dynamically updates the visual display and manages cart information in real time. The implementation generates AI-powered menu images and securely handles order data, loyalty information, and conversation history through managed services. You can reduce order errors, accelerate service times, and deliver a consistent customer experience while lowering operational costs through intelligent voice automation.

## Benefits

### Accelerate drive-thru ordering with voice AI

Enable near real-time, conversational voice ordering at your drive-thru using streaming audio processing. Reduce customer wait times and increase order throughput without adding staff.

### Eliminate infrastructure with serverless architecture

Deploy a fully managed, serverless ordering system that scales automatically with demand. Reduce operational costs while maintaining consistent performance during peak hours.

### Protect customer data with layered security

Secure every interaction with encryption, scoped credentials, and traffic filtering built into the architecture. Maintain customer trust while meeting compliance requirements across your restaurant locations.

## How it works

This architecture diagram shows how Amazon Nova 2 Sonic enables near real-time voice AI ordering for quick-service restaurant drive-thru using AWS serverless services. [Download the architecture diagram.](downloads/drive-thru-voice-ai-using-amazon-bedrock.pdf)

![Architecture diagram for Drive Thru Voice AI using Amazon Bedrock](/images/solutions/drive-thru-voice-ai-using-amazon-bedrock/images/drive-thru-voice-ai-using-amazon-bedrock.png)

1. **Step 1**: You access the digital menu board hosted on AWS Amplify, which loads the React-based ordering interface.
1. **Step 2**: Amazon Cognito manages temporary AWS credentials with scoped IAM permissions and secures access to backend services through token-based authorization.
1. **Step 3**: The Digital Menu Board uses the AWS SDK BidirectionalStreaming API to establish a SigV4-signed WebSocket session with Amazon Bedrock, a fully managed service with built-in security, privacy, and responsible AI. The app passes tool definitions and a system prompt to Amazon Nova 2 Sonic, enabling the model to orchestrate tool calls and process streaming audio.
1. **Step 4**: Amazon Nova 2 Sonic processes your streaming audio and invokes tools defined at the application level. The app's tool router captures model requests with parameters to manipulate the UI and trigger API calls.
1. **Step 5**: You initiate voice input via a button or sensor trigger. Amazon API Gateway routes tool requests to Amazon DynamoDB tables for menu, cart, order, loyalty, and chat data.
1. **Step 6**: Amazon CloudFront delivers AI-generated menu images stored in Amazon Simple Storage Service, protected by AWS WAF, a web application firewall that filters malicious traffic and blocks unauthorized access.
1. **Step 7**: AWS Lambda invokes Stability AI's Stable Image Core model through Amazon Bedrock to generate menu images, stores the image binary in Amazon S3, and updates the image reference in Amazon DynamoDB. (This happens once during the solution deployment)
1. **Step 8**: AWS KMS encrypts DynamoDB tables. Amazon Simple Queue Service dead letter queues capture failed AWS Lambda invocations for retry and alerting. Amazon CloudWatch provides centralized monitoring and logging.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-voice-ai-powered-drive-thru-with-amazon-nova-sonic)

## Related content

- **Voice AI powered drive-thru ordering with Amazon Nova 2 Sonic and dynamic menu displays**: Learn how to implement voice AI ordering for drive-thru restaurants using Amazon Nova 2 Sonic.

[Read the blog](https://aws.amazon.com/blogs/machine-learning/voice-ai-powered-drive-thru-ordering-with-amazon-nova-sonic-and-dynamic-menu-displays/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
