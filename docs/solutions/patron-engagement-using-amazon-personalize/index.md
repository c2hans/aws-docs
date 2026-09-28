---
source_url: https://docs.aws.amazon.com/solutions/patron-engagement-using-amazon-personalize/index.html
---

---
title: 'Guidance for Patron Engagement Using Amazon Personalize'
canonical_url: https://docs.aws.amazon.com/solutions/patron-engagement-using-amazon-personalize/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Patron Engagement Using Amazon Personalize

## Overview

This Guidance allows you to personalize the betting and gaming app experience, increasing patron engagement and retention through automated, pre-built machine learning (ML) algorithms. Though many betting and gaming apps have the capability to offer players recommended content, they often lack the uniquely personalized experience that social media and video streaming algorithms offer. Betting and gaming operators can adopt recommendation algorithms from Amazon Personalize, which can be integrated and optimized to drive engagement. This creates a scalable, personalized, and omni-channel experience of recommended games, pre-game and in-game betting lines, and promotional offers through low-code management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/patron-engagement-using-amazon-personalize.pdf)

![Architecture diagram](/images/solutions/patron-engagement-using-amazon-personalize/images/patron-engagement-using-amazon-personalize-1.png)

1. **Step 1**: AWS Glue DataBrew connects to a database to retrieve games (items), player accounts (users), and player interactions (historic user interaction) data.
1. **Step 2**: AWS Glue DataBrew transforms the data to create .csv training files uploaded to Amazon Simple Storage Service (Amazon S3) for upload to Amazon Personalize datasets and a games JSON file uploaded to Amazon S3.
1. **Step 3**: Amazon Personalize datasets train the models backing custom solution versions, a combination of a recipe (algorithm) and training parameters.
1. **Step 4**: The Amazon Personalize batch interface uses the item-to-item similarities (SIMS) recipe to create a batch file of game recommendations saved both to Amazon S3 and as custom solution versions.
1. **Step 5**: AWS Lambda retrieves game recommendations from Amazon S3 and imports them to Amazon DynamoDB.
1. **Step 6**: Amazon Kinesis Agent collects real-time player interaction (clickstream) events and sends the events to Amazon Kinesis Data Streams with a Lambda consumer.
1. **Step 7**: Lambda normalizes player interaction events by transforming them to match the custom solution training parameters and forwarding them to the Amazon Personalize event tracker for ongoing custom solution version training.
1. **Step 8**: The gaming app requests games from the player account management (PAM) platform to populate a recommended games section of the lobby user interface (UI).
1. **Step 9**: The PAM uses the player's last played game to request similar games from DynamoDB, used to populate a UI component linking the player's last gameplay to similar games.
1. **Step 10**: In parallel, the PAM requests real-time, personalized game recommendations from Amazon Personalize campaigns and the deployed custom solution version to populate UI components of popular games, trending games, and games tailored for the player.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Personalize allows betting and gaming customers to measure the impact of recommendations with metric attribution and A/B testing. Metric attribution creates reports based on patron interactions, games data, and specified interaction event metrics. Amazon Personalize aggregates metric calculations for interaction events and sends the reports to Amazon CloudWatch to be viewed. A/B tests allow betting and gaming customers to test the performance of Amazon Personalize recipes, using CloudWatch metrics to report on the efficacy of recipes through split testing. Amazon Personalize provides betting and gaming customers the ability to measure business outcomes with event metric attribution for reporting and evaluation of each event type. Amazon Personalize performs the calculations and sends reports to CloudWatch or Amazon S3 for stakeholders to evaluate the business impact, helping customers develop a more data-driven personalization strategy. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Key Management Service (AWS KMS) encrypts data stored and at rest within Amazon Personalize. AWS KMS is also used to encrypt data sent to other AWS services, including personally identifiable information (PII). You can use your own AWS KMS customer master key (CMK) to encrypt data imported into Amazon Personalize domains. This gives you control over encryption of sensitive customer data. AWS Identity and Access Management (IAM) allows betting and gaming administrators to securely control access to AWS resources and least privilege access. This is achieved by assigning roles to granular access policies and permissions to services and users on AWS, providing temporary security credentials for access rather than long-term credentials. You can attach policies to roles to control the type of access, actions, and resources available to the role. Roles make it easier to delegate access while maintaining control over permissions. As business needs change, administrators can modify the policies of a role rather than individual users. Amazon Personalize does not handle redaction of sensitive data from its output. Proper configuration of encryption, IAM policies, and input data handling helps Amazon Personalize securely process customer data while meeting privacy and compliance requirements. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudWatch allows betting and gaming customers to monitor and visualize Amazon Personalize, Amazon S3, Lambda, and DynamoDB metrics. CloudWatch metrics used in this Guidance can be used to create alerts, notifications, and visualization. CloudWatch alarms allow setting thresholds for metrics and configuring notifications or actions when thresholds are breached. This helps administrators take automatic recovery actions if a service becomes unavailable or responds slowly. CloudWatch logs can be used to monitor and troubleshoot issues with Lambda functions. Logs from application code executions provide insights to debug issues. With CloudWatch, metrics and logs from different AWS accounts, Regions, or resources can be aggregated in one place, providing a centralized view of overall health and performance of distributed applications. DynamoDB is used as the database for Amazon Personalize. It automatically spreads the data and traffic for the recommendation application across multiple Availability Zones (AZs) to maintain resilience. Customer interaction data is stored in Amazon S3, which provides durable storage of data across multiple AZs and replicates data to help ensure resilience against component failure or unavailability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Personalize provides performant ML algorithms. The service performs real-time personalization with low latency recommendations and auto scales resources to handle traffic bursts without affecting performance. Amazon Personalize uses pre-trained models to deliver real-time, low-latency recommendations, even during major events that spike traffic. When an Amazon Personalize model is trained, it is deployed across multiple AZs. If one AZ becomes unavailable, Amazon Personalize continues functioning using the model replicas in other AZs without any interruption. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Personalize helps manage recommendation system costs by providing controls to specify auto scaling limits and the model retraining schedule. Amazon Personalize batch recommendations do not require a campaign and offer additional cost savings for personalization use cases that do not require real-time updates. By using DynamoDB for batch recommendations, you decrease the number of real-time Amazon Personalize calls, reducing feature costs. Batch recommendations allow you to pre-compute recommendations for large numbers of users or items in one operation and store them for later use. This is more cost-effective than generating recommendations for every user request. You can also schedule batch recommendation jobs during off-peak hours when AWS resources are cheaper. This helps reduce costs compared to real-time recommendations which need to respond instantly. The pre-computed batch recommendations can then be served from cost-effective storage such as Amazon S3 instead of re-computing for every request using more expensive compute. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses managed services that optimize usage of the architecture diagram’s underlying resources. Amazon Personalize, Amazon S3, Lambda, and DynamoDB can help improve sustainability when used together. For example, batch recommendations generated by Amazon Personalize and stored in cost-effective storage like Amazon S3 help reduce the need to re-compute recommendations for every user request. This optimization lowers overall compute usage and improves efficiency. Lambda functions can be used to pre-process and analyze user data before training models with Amazon Personalize. This consolidation of workloads in the cloud drives further reduction in resource requirements compared to on-premises data centers. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
