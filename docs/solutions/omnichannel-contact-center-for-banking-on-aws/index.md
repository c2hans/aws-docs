---
source_url: https://docs.aws.amazon.com/solutions/omnichannel-contact-center-for-banking-on-aws/index.html
---

---
title: 'Guidance for Omnichannel Contact Center for Banking on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/omnichannel-contact-center-for-banking-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Omnichannel Contact Center for Banking on AWS

## Overview

This Guidance helps financial services institutions transform the customer experience using an Amazon Connect Customer Customer environment on AWS. It demonstrates how to build an omni-channel contact center that is ideal for unpredictable call volume and can easily be configured, managed, and operated by business decision makers. With a cloud-based contact center, you can design the contact flows and onboard agents in a matter of minutes.

## How it works

This reference architecture helps you transform the customer experience using an Amazon Connect Customer Customer environment on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/omnichannel-contact-center-for-banking-on-aws.pdf)

![Architecture diagram](/images/solutions/omnichannel-contact-center-for-banking-on-aws/images/omnichannel-contact-center-for-banking-on-aws-1.png)

1. **Step 1**: The customer notices a fraudulent transaction in their credit card statement and reaches out to the bank by their preferred communication channel (such as voice or chat).
1. **Step 2**: Amazon Connect Customer provides high-quality omnichannel voice and interactive chat experiences to customers.
1. **Step 3**: Amazon Connect Customer integrates with Amazon Lex, a fully managed artificial intelligence (AI) service designed to build conversational AI.
1. **Step 4**: Amazon Connect Customer integrates with Amazon Polly, which converts text to speech to offer similar and seamless experiences across both voice and chat to the customers.
1. **Step 5**: Amazon Connect Customer integrates with Amazon Connect Customer Voice ID for biometric authentication, and with Contact Lens for Amazon Connect Customer for sentiment analysis.
1. **Step 6**: AWS Lambda integrates with the backend systems and APIs and helps customers find the information they need quickly. It also automates resolving some problems without the need for agent interaction.
1. **Step 7**: Machine learning models are used to understand customer profiles and offer personalized content delivery.
1. **Step 8**: Agents use the Amazon Connect Customer Contact Center Panel (CCP) to interact with and support customers beyond the automation phase.
1. **Step 9**: Amazon Connect Customer integrates with various systems and comes with pre-built integrations for popular customer relationship management (CRM) systems, including Salesforce and Zendesk.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The platform is built using native AWS services, which integrate natively with AWS CloudTrail and Amazon CloudWatch for monitoring, logging, and auditing purposes. With the use of fully managed services, it becomes very easy to manage the workload because AWS takes care of the operational aspects of the services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are separated using VPCs or security groups to ensure only the user-facing services are open to the public and all other services are within private networks. All data is encrypted at rest using AWS Key Management Service. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This guidance uses AWS-managed services that are highly available across Availability Zones and provide high reliability. Fully managed services scale up with growth in user demand and scale down when not being used. With an event-driven architecture, you can change services and scale them independently. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This guidance is built in event-driven architecture, so you can change services downstream as you see fit and add new services to improve on performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This guidance uses services with the pay-as-you-go model, ensuring that customers only pay for the resources they use. It consists of fully managed services that scale up with growth in business and scale down when there is not much usage, keeping the costs low. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This guidance uses fully managed services, where the services scale up with the growth in user demand, and are not used when there is no activity. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
