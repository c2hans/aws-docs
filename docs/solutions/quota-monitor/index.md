---
source_url: https://docs.aws.amazon.com//solutions/quota-monitor//index.html
---

---
title: 'Quota Monitor for AWS'
canonical_url: https://docs.aws.amazon.com/solutions/quota-monitor/
source: aws-documentation
generated_on: 2026-10-08
---

# Quota Monitor for AWS

Monitor resource usage and receive notifications when approaching quotas

- **Version**: 6.3.15
- **Released**: 9/2026
- **Author**: AWS
- **Est. deployment time**: 5 mins
- **Estimated cost**: [See details](/solutions/latest/quota-monitor-for-aws/plan-your-deployment.html)

## Overview

**Important: This solution will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement.** **Customers can explore using [AWS Service Quota](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)s for proactive usage monitoring and automated management of your service quotas. [Service Quotas Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html) provides a fully AWS-managed alternative that covers the most common quota monitoring and alerting needs without requiring customer-managed infrastructure.** **Planning your migration: When transitioning to Automatic Management, note these key differences to ensure full coverage: it uses standardized AWS-defined thresholds (80% and 95%), focuses on resource quotas (not API rate limits), and supports a subset of services. To view supported quotas in your account, navigate to the [Automatic Management section](https://console.aws.amazon.com/servicequotas/home/amSettings) in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/).** Quota Monitor for AWS helps you proactively track your resource usage and sends email or Slack notifications when you approach quotas. Tracking your usage against Service Quotas helps you plan for requesting a quota increase before you exceed the quota. This AWS Solution leverages AWS Trusted Advisor and Service Quotas to monitor AWS resource usage and raise alerts. You can use this solution in any AWS Region, including AWS GovCloud (US) Regions. This solution includes a Hub template that you deploy in your monitoring account. Additionally, the solution provides a Service Quotas spoke template and a Trusted Advisor spoke template. You must deploy each of these templates in the accounts that need quota monitoring.

## Benefits

### Track resource usage

Provision the services necessary to proactively track resource usage and send notifications when you approach quotas.

### Receive notifications through email or Slack

Request quota increases or shut down resources before you reach a service quota, based on quota notifications you receive through email or your existing Slack channel.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation templates. This solution provides multiple templates, including a Hub template, a Service Quotas spoke template, and a Trusted Advisor spoke template.

[View implementation guide](/solutions/latest/quota-monitor-for-aws/architecture-overview.html)

![Architecture diagram](/images/solutions/quota-monitor/images/quota-monitor-1.png)

1. **Step 1**: **Reporting** - This workflow provisions an Amazon Simple Notification Service topic, Amazon Simple Queue Service (Amazon SQS) queue, AWS Lambda function summarizer, and Amazon DynamoDB table. The queue receives usage events from all monitored accounts. The Lambda function puts all usage data on the DynamoDB table.
1. **Step 2**: **Centralized event collection** - The workflow provisions a custom Amazon EventBridge bus, a corresponding rule, and Amazon Simple Notification Service topic to raise alerts. The workflow raises alerts for quota usage and defines alert levels as: OK (less than 80% utilization), WARN (80% to 99% utilization), and ERROR (100% utilization).
1. **Step 3**: **Deployment management** - The workflow provisions Parameter Store, an Amazon EventBridge rule, a Lambda function, and CloudFormation StackSets.
1. **Step 4**: **Quota list generation** - The Service Quotas spoke template launches this workflow. The workflow provisions a Lambda function and two DynamoDB tables. The workflow manages an active and validated list of Service Quotas that support usage monitoring using Amazon CloudWatch metrics.
1. **Step 5**: **Quota utilization alerting** - The workflow provisions a schedule-based Lambda function, custom Amazon EventBridge bus, and an Amazon EventBridge rule. The CW Poller function queries the quota list table and retrieves usage data for those quotas from Amazon CloudWatch metrics. The workflow sends the usage data as events to the EventBridge bus. The spoke bus routes these usage events to both the centralized bus and the spoke SNS bus (if provided).
1. **Step 6**: **Spoke account notifications** - The Spoke SNS template launches this workflow. The workflow provisions notification resources in the spoke account to decentralize notifications. Specifically, it provisions an Amazon EventBridge bus with a rule that routes messages to the SNS publisher Lambda function. This function applies any notification muting rules configured through the notification muting parameter in the SSM Parameter Store. The Lambda function then publishes the relevant events to the SNS topic in the spoke account.
1. **Step 7**: **Trusted Advisor alerting** - The Trusted Advisor spoke template launches this workflow. The workflow provisions a Lambda function and an Amazon EventBridge rule to support quota usage monitoring using Trusted Advisor. The Lambda function executes at an interval of 24 hours to refresh Trusted Advisor checks. The Events rule routes Trusted Advisor usage events to the centralized bus.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/quota-monitor-for-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.Launch in the AWS Console (no AWS Organizations)Launch instructions (with AWS Organizations)

[Launch in the AWS Console](https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/template?stackName=QuotaMonitorNoOUHub&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-hub-no-ou.template&redirectId=SolutionWeb)
[Launch instructions](/solutions/latest/quota-monitor-for-aws/deploy-the-solution.html#step-1.-choose-your-deployment-scenario&redirectId=SolutionWeb)

## Deployment options

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/quota-monitor-for-aws/quota-monitor-for-aws.pdf#solution-overviewl)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/quota-monitor-for-aws)

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download CloudFormation templates](/solutions/latest/quota-monitor-for-aws/aws-cloudformation-templates.html)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/quota-monitor-for-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/quota-monitor-for-aws/latest/rss.xml)
