---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/overview.html
---

# Monitor Amazon WorkSpaces usage and optimize costs with the Cost Optimizer for Amazon WorkSpaces solution
<a name="overview"></a>

The Cost Optimizer for [Amazon WorkSpaces](https://aws.amazon.com/workspaces) solution analyzes all of your WorkSpaces usage data and automatically converts the WorkSpace to the most cost-effective billing option (hourly or monthly), depending on your individual usage. Amazon WorkSpaces is a fully managed, secure Desktop-as-a-Service (DaaS) offering that eliminates the need for you to procure, deploy, and manage complex virtual desktop environments.

This solution helps you monitor your WorkSpaces usage and optimize costs and uses [AWS CloudFormation](http://aws.amazon.com/cloudformation/) to automatically provision and configure the necessary Amazon Web Services, Inc. (AWS) services to convert the billing mode for individual WorkSpaces. This solution supports a multi-account environment in [AWS Organizations](https://aws.amazon.com/organizations/) and is capable of running in the AWS GovCloud (US-West) Region to monitor WorkSpaces across AWS GovCloud (US) Regions.

This implementation guide provides architectural considerations and configuration steps for deploying this solution on the AWS Cloud. It includes links to CloudFormation templates that launch, configure, and run the AWS compute, management, storage, and other services required to deploy this solution on AWS, using AWS best practices for security and availability.

This guide is intended for solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals who want to Cost Optimizer for Amazon WorkSpaces in their environment.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution<br />The estimated cost for running this solution in the US East (N. Virginia) Region is USD $5.00 per month. |  [Cost](cost.md)  |
| Understand the security considerations for this solution |  [Security](security.md)  |
| Know how to deploy the solution |  [Deploy the solution](deploy-the-solution.md)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution |  [AWS CloudFormation templates](templates.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution |  [GitHub repository](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cost Optimizer for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
