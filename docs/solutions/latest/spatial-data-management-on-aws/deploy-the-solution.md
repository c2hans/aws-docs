---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This section provides detailed instructions for deploying the Spatial Data Management Application to your AWS account.

## Deployment Overview
<a name="deployment-overview"></a>

The solution is deployed using AWS CloudFormation, which creates all necessary resources in a single operation. The deployment typically takes approximately 45 minutes to complete.

## Prerequisites
<a name="deployment-prerequisites"></a>

Before you deploy, ensure you have:
+ Completed [deployment planning](plan-your-deployment.md) including AWS Region selection
+ AWS Command Line Interface (AWS CLI) installed and configured
+ Appropriate AWS Identity and Access Management (IAM) permissions for AWS CloudFormation stack creation
+ Verified solution availability in your target Region

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
