---
source_url: https://docs.aws.amazon.com/solutions/near-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer/index.html
---

---
title: 'Guidance for Near Real-time Monitoring of AWS Elastic Disaster Recovery using Amazon Q Developer'
canonical_url: https://docs.aws.amazon.com/solutions/near-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Near Real-time Monitoring of AWS Elastic Disaster Recovery using Amazon Q Developer

## Overview

This Guidance demonstrates how to enhance your disaster recovery operations by integrating Amazon Q Developer with Slack for real-time monitoring and alerts. By implementing this solution, organizations can significantly improve their business continuity capabilities through automated notifications of critical events affecting Elastic Disaster Recovery-protected resources. The integration enables proactive issue identification and faster incident response times, leading to improved operational resilience and reduced recovery time objectives (RTOs). This streamlined approach to disaster recovery monitoring helps organizations maintain business operations and meet their compliance requirements while minimizing potential downtime and data loss risks.

## Benefits

### Enhance disaster recovery monitoring

Deploy real-time monitoring for AWS Elastic Disaster Recovery events through Amazon Q Developer's integration with Slack. Your team can receive immediate notifications about critical replication status changes, allowing for faster response to potential disaster recovery issues.

### Simplify DR management

Leverage natural language interactions with Amazon Q Developer to query your disaster recovery environment and analyze server states without complex commands. This conversational interface helps technical teams quickly understand DR status and receive intelligent recommendations for optimizing recovery posture.

### Accelerate incident response

Automate the routing of critical AWS Elastic Disaster Recovery events through EventBridge rules and SNS notifications to your team's Slack channels. This streamlined workflow helps your organization identify potential issues early and coordinate faster responses to maintain business continuity during recovery scenarios.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/near-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer.pdf)

![Architecture diagram](/images/solutions/near-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer/images/near-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer-1.png)

1. **Step 1**: An administrator installs the AWS Elastic Disaster Recovery (AWS DRS) Replication Agent on production Amazon Elastic Compute Cloud (Amazon EC2) instances to enable disaster recovery (DR) monitoring.
1. **Step 2**: The AWS DRS service automatically generates and sends events about resource status to the Amazon EventBridge default event bus.
1. **Step 3**: Amazon EventBridge Rules filter events based on predefined patterns to identify critical AWS DRS events.
1. **Step 4**: Amazon EventBridge automatically routes matched events to an Amazon SNS topic for notification distribution.
1. **Step 5**: Amazon Q Developer configured with Slack integration subscribes to the Amazon Simple Notification Service (Amazon SNS) topic to receive AWS DRS events.
1. **Step 6**: Amazon Q Developer provides natural language querying of AWS DRS environments, analyzing server states and offering optimization recommendations. Through conversational AI in Slack, users can interact with the AWS DRS infrastructure, execute CLI commands, and receive automated notifications about resource replication status. Teams gain visibility into DR operations through designated Slack channels.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-real-time-monitoring-of-aws-elastic-disaster-recovery-using-amazon-q-developer/tree/main)

[Read usage guidelines](/solutions/guidance-disclaimers/)
