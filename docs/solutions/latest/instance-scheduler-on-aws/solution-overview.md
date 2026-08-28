---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html
---

# Automate starting and stopping AWS instances
<a name="solution-overview"></a>

The Instance Scheduler on AWS solution automates the starting and stopping of various AWS services including [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) (Amazon RDS) instances.

This solution helps reduce operational costs by stopping resources that are not in use and starting resources when their capacity is needed. For example, a company can use Instance Scheduler on AWS to automatically stop instances outside of business hours every day. If you leave all of your instances running at full utilization, this solution can result in up to 70% cost savings for those instances that are only necessary during regular business hours (weekly utilization reduced from 168 hours to 50 hours).

Instance Scheduler on AWS leverages Amazon Web Services (AWS) resource tags and [AWS Lambda](https://aws.amazon.com/lambda/) to automatically stop and restart instances across multiple AWS Regions and accounts on a customer-defined schedule. This solution also allows you to use hibernation for stopped EC2 instances.

This implementation guide provides an overview of the Instance Scheduler on AWS solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the AWS Cloud.

This guide is intended for IT infrastructure architects, administrators, and DevOps professionals who want to implement Instance Scheduler on AWS in their environment.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. The estimated cost for running this solution in the US East (N. Virginia) Region is USD $13.15 per month. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [AWS Well-Architected Security](aws-well-architected-design-considerations.md), [Security](security-1.md)  |
| Configure schedules. |  [Scheduler configuration table](scheduler-configuration-table.md)  |
| Know which AWS Regions are supported for this solution. |  [Supported AWS Regions](#supported-aws-regions)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation templates](aws-cloudformation-templates.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/instance-scheduler-on-aws/tree/main)  |

## Supported AWS Regions
<a name="supported-aws-regions"></a>

You can deploy Instance Scheduler in any AWS Region, including AWS GovCloud (US) Regions and some [opt-in Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs\_homepage\_addtlrcs#optinregion) (Regions that are disabled by default). After you deploy the solution, you can configure it to apply the appropriate start or stop actions to tagged EC2 and RDS DB instances in any Region(s) of your account. If you use cross-account instance scheduling, the solution applies actions to instances in all configured Regions in all accounts.

**Important**
Instance Scheduler on AWS actions affect appropriately tagged instances in all AWS Regions of your account, even though the Lambda function is running in a single Region.

You can use multiple deployments of the solution to schedule a large number of instances, or instances in many accounts and Regions. When you deploy multiple schedulers, use a different tag name for each stack, and configure a set of non-overlapping Regions for each deployment.

Each deployment checks every instance in every configured Region in an account for the tag key that identifies resources it should schedule. If the Regions for multiple deployments overlap, each instance will be checked by multiple deployments.

**Note**
Instance Scheduler on AWS can target instances within any opt-in region for scheduling, even when the solution stacks are deployed in standard AWS regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
