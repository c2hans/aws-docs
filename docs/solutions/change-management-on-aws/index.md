---
source_url: https://docs.aws.amazon.com/solutions/change-management-on-aws/index.html
---

---
title: 'Guidance for Change Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/change-management-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Change Management on AWS

## Overview

Change Management enables you to deploy planned alterations to all configurable items that are in your environment within the defined scope, such as production and test. An approved change is an action which alters resource configuration implemented with a minimized and accepted risk to an existing IT infrastructure.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/change-management-on-aws.pdf)

![Architecture diagram](/images/solutions/change-management-on-aws/images/change-management-on-aws-1.png)

1. **Step 1**: (CF30 - S1) Deploy an AWS Config recorder and delivery channel in the management account and all member accounts to track changes of all AWS Config supported resources. Note: AWS Control Tower will automatically deploy AWS Config and delivery channels in all AWS Control Tower managed member accounts and regions.
1. **Step 2**: (CF30 - S2) Use AWS Organizations to delegate the administration of AWS Systems Manager and AWS CloudFormation to the operation tooling account. This will allow you to deploy changes by automation to accounts within your organization. For application-specific changes, we recommend using an application deployment account (not depicted here).
1. **Step 3**: (CF30 - S4) Enable and configure an AWS Config aggregator in your operations tooling account to provide visibility to the resources, resource configurations, and changes in your organization.
1. **Step 4**: (CF30 - S4) Configure all AWS Config delivery channels to send AWS Config snapshots and history to a centralized Amazon Simple Storage Service (Amazon S3) bucket in your log archive account to maintain a record of all historical changes. Note: If you are using AWS Control Tower, each AWS Config recorder has a delivery channel configured to send to the AWS Control Tower S3 log bucket.
[Read usage guidelines](/solutions/guidance-disclaimers/)
