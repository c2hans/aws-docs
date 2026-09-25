---
source_url: https://docs.aws.amazon.com//solutions/instance-scheduler-on-aws//index.html
---

---
title: 'Instance Scheduler on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Instance Scheduler on AWS

Configure start and stop schedules for your Amazon EC2 and Amazon RDS instances to manage costs

- **Version**: 3.2.10
- **Released**: 9/2026
- **Author**: AWS
- **Est. deployment time**: 5 mins
- **Estimated cost**: [See details](/solutions/latest/instance-scheduler-on-aws/cost.html)

## Overview

Instance Scheduler on AWS automates the starting and stopping of various AWS services, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon EC2 Auto Scaling Groups, and Amazon Relational Database Service (Amazon RDS) instances. Automating this process helps reduce operational costs by stopping and starting resources as needed. This AWS Solution uses resource tags and AWS Lambda to automatically stop and start instances based on a schedule you define, and it can be deployed across multiple AWS Regions. When compared to a setup where you leave all your instances continuously running at full utilization (even when those resources aren't being used), this solution can lead to significant cost savings by aligning your workloads with the AWS Well-Architected Cost Optimization best practices.

## Benefits

### Cross-account instance scheduling

This solution includes a template that creates the AWS Identity and Access Management (IAM) roles necessary to start and stop instances in secondary accounts.

### Automated tagging

This solution can automatically add tags to all instances when it starts or stops. The solution also includes macros that allow you to add variable information to the tags.

### Configure schedules or periods using Scheduler CLI

This solution includes a command line interface (CLI) that provides commands for configuring schedules and periods. The CLI allows customers to estimate cost savings for a given schedule.

### Configure schedules or periods using AWS Systems Manager maintenance window

For Amazon EC2 instances, this solution can use Systems Manager maintenance windows defined in the same AWS Region as the instances and start and stop the instances for the maintenance window.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation templates or get started with the resources below.

[View implementation guide](/solutions/latest/instance-scheduler-on-aws/solution-overview.html)

![Architecture diagram](/images/solutions/instance-scheduler-on-aws/images/instance-scheduler-on-aws-1.png)

1. **Step 1**: An Amazon EventBridge Rule triggers the orchestration Lambda function at configurable intervals (default: every 5 minutes).
1. **Step 2**: The EventBridge rule invokes an AWS Lambda orchestration function that queries the DynamoDB configuration table to identify active scheduling targets. The orchestrator then invokes parallel scheduling Lambda functions for each active target.
1. **Step 3**: Schedule definitions and periods are stored in an Amazon DynamoDB configuration table. You can define any number of schedules and periods in this table to control when your instances start and stop.
1. **Step 4**: A DynamoDB registry table automatically tracks all managed resources. When resources are tagged for scheduling, they are registered in this table in response to AWS tagging events.
1. **Step 5**: Each scheduling Lambda function describes tagged resources, evaluates their schedules against the current time, and executes the appropriate start or stop actions. 1. For Amazon EC2 instances, if a start operation fails due to insufficient capacity, the solution can be configured to attempt to resize the instance to alternate instance types before retrying the start operation.
1. **Step 6**: Schedule management is available through the DynamoDB console, scheduler CLI tool, or AWS CloudFormation Custom resources. The solution deploys with several example schedules pre-configured.
1. **Step 7**: Cross-account deployments use a hub-spoke architecture where spoke accounts automatically self-register with the hub account. Spoke stacks must be deployed in the same region as the hub stack and must be either pre-approved by the hub stack or members of the same AWS Organization.
1. **Step 8**: The solution publishes scheduling and registration events to EventBridge buses in the hub account (global events) and spoke accounts (local events per region).
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Go to guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Finstance-scheduler-on-aws%2Flatest%2Finstance-scheduler-on-aws.template&redirectId=SolutionWeb)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template)
[Download remote template](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws-remote.template)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/instance-scheduler-on-aws/tree/main)

- **Download implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/instance-scheduler-on-aws.pdf)

## Related content

- **Resource Scheduler**: With Quick Setup, a capability of AWS Systems Manager, you can configure Resource Scheduler to automate the starting and stopping of your Amazon EC2 instances across your AWS accounts and AWS Regions. Resource Scheduler provides a simple user interface (UI). To learn more about Resource Scheduler, review related resources in the implementation guide.

[Get started](https://us-west-2.console.aws.amazon.com/systems-manager/quick-setup/create-configuration)

- **Cost Optimization with AWS**: Build modern, scalable applications on AWS to transform your organization, all while optimizing costs through Cost Optimization with AWS. The variety of AWS pricing options provides you with the flexibility to design your purchase plan to meet your specific workload needs.

[Learn more](https://aws.amazon.com/aws-cost-management/cost-optimization/)

- **Cost Optimization Pillar - AWS Well Architected Labs**: This repository contains documentation and code in the format of hands-on labs to help you learn, measure, and build cost optimized workloads using well-architected best practices.

[Learn more](https://wellarchitectedlabs.com/)

- **Cloud Foundations - Guidance for Cloud Financial Management on AWS**: This Guidance helps you set up a Cloud Financial Management (CFM) capability to manage and optimize your expenses for cloud services. This capability includes near real-time visibility and cost and usage analysis to support decision-making for topics such as spend dashboards, optimization, spend limits, chargeback, and anomaly detection and response.

[Explore guidance](https://aws.amazon.com/solutions/guidance/cloud-financial-management-on-aws/)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/instance-scheduler-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/instance-scheduler-on-aws/latest/rss.xml)
