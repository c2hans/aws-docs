---
source_url: https://docs.aws.amazon.com/solutions/near-real-time-airport-gate-change-information-on-aws/index.html
---

---
title: 'Guidance for Near Real-Time Airport Gate Change Information on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/near-real-time-airport-gate-change-information-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Near Real-Time Airport Gate Change Information on AWS

## Overview

This Guidance helps airlines and airports provide updates about flight information to passengers in near real time. Sometimes, information displayed on airline applications may differ from flight information display screens in airport terminals. This architecture uses Amazon EventBridge or Kafka to share data from legacy technology systems, such as an airport operational database (AODB), and give passengers consistent and reliable flight updates. Airports and airlines can improve the travel experience through advanced ML-powered analytics and voice, chat, and mobile interactions with passengers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/near-real-time-airport-gate-change-information-on-aws.pdf)

![Architecture diagram](/images/solutions/near-real-time-airport-gate-change-information-on-aws/images/near-real-time-airport-gate-change-information-on-aws-1.png)

1. **Step 1**: The airport ground crew makes a change to gate allocations, and this change is stored in the AODB.
1. **Step 2**: AWS Database Migration Service (AWS DMS) captures changes in the AODB. It is configured to use change data capture (CDC) to catch all updates.
1. **Step 3**: AWS DMS uses Amazon Managed Streaming for Apache Kafka (Amazon MSK) as the destination for changes. Kafka is included for customers who want to consume events from applications that are not AWS-native. This allows airports to facilitate both AWS- and non-AWS-based consumers. You may also use Amazon Kinesis Data Streams instead of Amazon MSK.
1. **Step 4**: An AWS Lambda function processes events from Kafka or Kinesis Data Streams. It can transform the structure of events and send them to Amazon EventBridge.
1. **Step 5**: EventBridge rules are configured to publish rules to different client targets. For example, if a gate change is made to flight number "ABC123," an EventBridge rule can route all events that have a flight number starting with "ABC" to Airline 1.
1. **Step 6**: Airlines have EventBridge clients in their accounts, to which the airport is allowed to push events. Airlines can use Lambda to pull a list of passengers affected by the change and notify them through Amazon Simple Notification Service (Amazon SNS).
1. **Step 7**: Passengers receive notifications in near real time.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can deploy this architecture using AWS CloudFormation, which uses repeatable templates and represents the architecture stack in code. You can also use Amazon CloudWatch and AWS X-Ray to gain visibility into what is happening across your system. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS DMS connects as a user on the database to capture changes. Amazon MSK supports a native integration with Lambda. Lambda uses an execution role to access Amazon MSK. EventBridge uses AWS Identity and Access Management (IAM) policies to permit cross-account access. External parties accessing Amazon MSK directly can use IP restrictions and certificates. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Consider deploying AWS DMS with a multi-Availability Zone configuration to ensure that changes are captured, even in the event of an outage. Additionally, you should familiarize yourself with Lambda concurrency limits in the Region you plan to run this system and set CloudWatch alarms to monitor resources. Lambda is used for stateless compute, which processes received messages. If Lambda fails to process messages from Amazon MSK, it will retry. EventBridge allows for messages to be replayed, retried, and delivered to multiple destinations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

We included Kafka in this Guidance to provide an interface for data consumers that aren’t built on AWS, meaning they are unable to integrate with EventBridge natively. For airlines that do have a serverless-first application on AWS, we chose EventBridge to quickly respond to changes in airport infrastructure. We chose AWS DMS as a managed service to stream changes from the source database and Lambda as a cost-effective serverless compute layer for processing events. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Services such as Lambda and EventBridge allow customers to pay only for the resources they consume. For services such as AWS DMS and Amazon MSK, it is important that you regularly review your resource sizing to ensure cost effectiveness. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses a serverless-first approach, through services such as Lambda and EventBridge. Lambda can be configured to use ARM processors for more sustainable compute. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
