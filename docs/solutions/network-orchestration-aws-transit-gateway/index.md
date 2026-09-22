---
source_url: https://docs.aws.amazon.com//solutions/network-orchestration-aws-transit-gateway//index.html
---

---
title: 'Guidance for Network Orchestration for AWS Transit Gateway'
canonical_url: https://docs.aws.amazon.com/solutions/network-orchestration-aws-transit-gateway/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Network Orchestration for AWS Transit Gateway

## Overview

This Guidance demonstrates how to automate the setup and management of transit networks across distributed AWS environments through centralized orchestration. By capturing subnet and VPC tagging events and coordinating Transit Gateway attachments, route configurations, and cross-account resource sharing from a hub account, it eliminates manual network provisioning tasks. Conditional approval rules based on AWS Organizations membership streamline governance by automatically processing network change requests. You gain a unified dashboard to visualize, monitor, control, and audit your global network topology, significantly reducing operational overhead while ensuring consistency and compliance across your entire AWS infrastructure.

## Benefits

### Automate cross-account network connectivity

Eliminate manual networking tasks by using tag-based events to automatically trigger Transit Gateway attachment workflows across your AWS accounts. Your teams can connect VPCs without requiring deep networking expertise or raising tickets with a central network team.

### Accelerate network provisioning with governance

Apply organizational unit-based approval rules to automatically approve, reject, or escalate attachment requests, reducing provisioning time while maintaining consistent network governance. Real-time notifications keep administrators informed of attachment status throughout the workflow.

### Gain centralized network visibility

Maintain a complete, auditable record of all Transit Gateway attachments and workflow history in a single, durable data store. Your network operations teams can track attachment state and routing changes across all spoke accounts from one centralized location.

## How it works

This architecture diagram illustrates how Network Orchestration for AWS Transit Gateway works. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram](downloads/network-orchestration-aws-transit-gateway.pdf)

![Architecture diagram for Network Orchestration for AWS Transit Gateway](/images/solutions/network-orchestration-aws-transit-gateway/images/network-orchestration-aws-transit-gateway.png)

1. **Step 1**: An administrator tags a subnet with Attach-to-TGW (to create a TGW attachment and add routes to subnet route table) and/or the VPC with Associate-with / Propagate-to (to configure TGW route table association and propagation). Amazon EventBridge in the spoke account captures the tag-change event and forwards it to the hub accounts' EventBridge Bus.
1. **Step 2**: Amazon EventBridge (in the hub account) receives the cross-account event and triggers the orchestration workflow.
1. **Step 3**: AWS Lambda processes the event and initiates the AWS Step Functions state machine.
1. **Step 4**: AWS Step Functions orchestrates the multi-step attachment workflow: - Retrieve account metadata (name, OU path) from AWS Organizations for approval requiring routing decisions. - Create or validate the Transit Gateway VPC attachment via the shared TGW resource (shared through AWS Resource Access Manager). - Associate the attachment with the TGW Route table specified in the Associate-with tag, and enables route table propagation specified in the Propagate-to tag. - Updates the VPC route table in the spoke account with routes pointing to the TGW attachment.
1. **Step 5**: AWS Resource Access Manager shares the Transit Gateway from hub account to the spoke account, enabling cross-account attachment.
1. **Step 6**: AWS Transit Gateway in the hub account processes the attachment request and associates it with/propagates to the designated route table.
1. **Step 7**: AWS Organizations is queried to retrieve account name and OU path. This information drives conditional approval rules (auto-approve / reject / require-approval based on OU membership) and is applied as tags to the TGW attachment for identification.
1. **Step 8**: Amazon DynamoDB stores the state of all attachments, and workflow execution history.
1. **Step 9**: Amazon Simple Notification Service sends notifications to administrators about the attachment status (success/failure/approval required).
1. **Step 10**: The VPC route table in the spoke account is updated with routes directing traffic through the Transit Gateway attachment.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/guidance-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/network-orchestration-for-aws-transit-gateway)

[Read usage guidelines](/solutions/guidance-disclaimers/)
