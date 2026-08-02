---
source_url: https://docs.aws.amazon.com/solutions/omni-channel-customer-engagement-for-travel-and-hospitality-on-aws/index.html
---

# Guidance for Omni-Channel Customer Engagement for Travel & Hospitality on AWS

Deliver personalized customer service by improving the customer experience through their channel of choice, at every stage of the traveler and guest journey

## Overview

<p>This Guidance features an integrated user interface for Travel & Hospitality customer service teams. With built-in voice, text, chat, and email applications, customer service teams can respond to customers from a single screen and build new workflows with their existing customer service applications. Customer service that spans multiple channels can improve loyalty program net promoter scores (NPS) and customer satisfaction scores (CSAT), while also reducing costs.<br/></p>

## How it works

### Airlines

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/guidance-for-omni-channel-customer-engagement-for-lodging-ra.pdf)Step 1Use Amazon Simple Storage Service (Amazon S3) to store website and configuration files, and Amazon CloudFront to serve the unified user interface.Step 2Invoke AWS Lambda to provide personalized recommendations for guests and data through Amazon API Gateway. API access is controlled through Amazon Cognito.Step 3A serverless database architecture runs on Amazon DynamoDB to collect key guest 360 data from several sources, including data processing workload outputs and systems of records.Step 4Use a chatbot powered by Amazon Lex to ask guest input data, and automate the delivery of personalized user interactions and recommendations.Step 5Use a search service powered by Amazon OpenSearch Service to recommend available products in the data bank index.Step 6Use a mail or mobile push notification service to send recommendations to guests. Schedule the notifications using Amazon Pinpoint.### Lodging

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/guidance-for-omni-channel-customer-engagement-for-lodging-ra.pdf)Step 1Use Amazon Simple Storage Service (Amazon S3) to store website and configuration files, and Amazon CloudFront to serve the unified user interface.Step 2Invoke AWS Lambda to provide personalized recommendations for guests and data through Amazon API Gateway. API access is controlled through Amazon Cognito.Step 3A serverless database architecture runs on Amazon DynamoDB to collect key guest 360 data from several sources, including data processing workload outputs and systems of records.Step 4Use a chatbot powered by Amazon Lex to ask guest input data, and automate the delivery of personalized user interactions and recommendations.Step 5Use a search service powered by Amazon OpenSearch Service to recommend available products in the data bank index.Step 6Use a mail or mobile push notification service to send recommendations to guests. Schedule the notifications using Amazon Pinpoint.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The reference architecture can be scripted using an Amazon CloudFormation template. You can next add the CloudFormation template to your own development pipeline, and deploy in your cloud environment. Using Amazon CloudWatch, you can get Observability with level metrics, and personalize dashboards and logs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Using Amazon Cognito user pools, you can use identity pools to provide built-in user management. The AWS Lambda backend has access only to the services they need, with least privilege roles. The customer data in Amazon DynamoDB is encrypted at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All the serverless components are highly available, and automatically scale based on usage. We recommend Amazon DynamoDB cross-Region deployment for higher availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless architectures give you the ability to provision the exact resources that the workload needs. CloudWatch Alarms and Lambda metrics allow monitoring for expected performance. For more unexpected traffic, Amazon DynamoDB can be configured as on-demand; otherwise use provisioned mode for consistent traffic. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless architectures have a pay-per-value pricing model and scale based on demand. A good implementation is to share the same key-value tag for assets that belong to a project programmatically, and then create custom reports in AWS Cost Explorer using the key value tags. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By choosing serverless services, you use only the resources that you need, reducing unnecessary emissions. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
