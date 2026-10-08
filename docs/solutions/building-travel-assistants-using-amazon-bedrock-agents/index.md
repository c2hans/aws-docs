---
source_url: https://docs.aws.amazon.com/solutions/building-travel-assistants-using-amazon-bedrock-agents/index.html
---

---
title: 'Guidance for Building Travel Assistants Using Amazon Bedrock Agents'
canonical_url: https://docs.aws.amazon.com/solutions/building-travel-assistants-using-amazon-bedrock-agents/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Building Travel Assistants Using Amazon Bedrock Agents

## Overview

This Guidance demonstrates how organizations in the travel and hospitality (T&H) industry can build an intelligent virtual assistant that uses generative AI to streamline every aspect of travel planning. Through a personalized chat interface, the virtual concierge curates tailored travel itineraries, handles all bookings, and provides recommendations for flights, accommodations, activities, and local experiences based on individual preferences, budgets, and travel styles. Once bookings are made, the virtual concierge supports travelers with any questions or changes for a stress-free and flexible travel experience.<br/>

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-travel-assistants-using-amazon-bedrock-agents.pdf)

![Architecture diagram](/images/solutions/building-travel-assistants-using-amazon-bedrock-agents/images/building-travel-assistants-using-amazon-bedrock-agents-1.png)

1. **Step 1**: Index FAQs and documents stored on Amazon Simple Storage Service (Amazon S3) using Amazon Bedrock Knowledge Bases to build vector knowledge stores for enterprise data.
1. **Step 2**: Use Amazon Cognito to authenticate the guest or traveler. Initiate the conversation using the chat interface from your existing web and mobile app. Amazon API Gateway serves as the entry point for client requests, routing to an AWS Lambda function that invokes Amazon Bedrock Agents.
1. **Step 3**: Amazon Bedrock Guardrails provides an external validation flow that allows you to check user inputs and large language model (LLM) responses against a set of topic denial rules, harmful content, text, or sensitive information before going back to the user. This helps protect your brand image and secure your applications.
1. **Step 4**: Amazon Bedrock Agents takes into account the task sent by the user, alongside the conversation history, available actions, knowledge bases, and provided instructions in the prompt to create a plan to retrieve the necessary data to craft a response. The action group actions will be defined in a Lambda function that will load an API schema from Amazon S3.
1. **Step 5**: The ideation action will use an identifier from the authenticated user to query a customer data and loyalty system and retrieve previous booking and interaction data, loyalty status, available perks and offers, and more. Based on this data and the user requirements, a customized travel destination and itinerary will be offered back to the user.
1. **Step 6**: Once the user has decided on a destination and a date, the availability action will query (such as available flights and hotels) and present the options to the user. When ready to book, the booking action will connect to booking systems to complete the booking and offer a summary back to the user.
1. **Step 7**: The existing bookings Q&A action retrieves the users existing bookings, and based on the question from the user, selects the appropriate metadata filters (such as airline or hotel) to query the knowledge base, confirming the response is based on the correct data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud Development Kit (AWS CDK) allows you to define AWS resources using traditional programming languages. By defining all AWS resources with AWS CDK, you can replicate deployments and safely deploy changes and updates to workloads. Amazon CloudWatch proactively monitors applications and infrastructure, helping identify anomalies, troubleshoot issues, and ensure peak efficiency. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito securely manages user identities and access for web and mobile applications, minimizing custom identity management code while enhancing security through multi-factor authentication. Amazon Bedrock provides data privacy and security through encryption at rest and in transit, access controls, and support for regulatory standards. Amazon Bedrock Guardrails implement safeguards for generative AI applications, filtering undesirable content and protecting against data leaks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon Bedrock offers provisioned throughput, enabling application performance scaling to meet user base demands. This capability helps ensure reliable service delivery, handling fluctuations in demand. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock provides a wide range of foundation models, allowing selection of the most appropriate model for specific use cases and requirements. Additionally, Amazon Bedrock Knowledge Bases offers various vector database options, optimizing for factors like cost, operational overhead, and data location. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The S3 Intelligent-Tiering storage class automatically moves data to the most cost-effective access tier, reducing storage costs without impacting performance. This helps ensure that the raw knowledgebase files that you upload to your S3 bucket are correctly handled and moved to cheaper storage classes when they are no longer frequently accessed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda runs code without provisioning or managing servers, automatically scaling to meet demand, reusing execution environments, and optimizing resource utilization. This serverless approach contributes to a more sustainable architecture and minimizes energy consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
