---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/deployment.html
---

# Automated deployment
<a name="deployment"></a>

Before you launch the automated deployment, review the [considerations](cfct-considerations.md). Follow the step-by-step instructions in this section to configure and deploy the solution into your AWS Control Tower management account.

**Time to deploy:** Approximately 15 minutes

## Prerequisites
<a name="prerequisites"></a>

CfCT must be deployed in your AWS Control Tower management account, and in your AWS Control Tower home Region. If you do not have a landing zone set up, see [Getting started with AWS Control Tower](getting-started-with-control-tower.md).

## Deployment steps
<a name="what-we-cover"></a>

The procedure for deploying CfCT consists of two major steps. For detailed instructions, follow the links for each step.

[Step 1. Launch the stack](step1.md)
+ Launch the CloudFormation template into your management account.
+ Review the template parameters, and adjust if necessary.

[Step 2. Create a custom package](step2.md)
+ Create a custom configuration package.

**Important**
To download the correct AWS CloudFormation template and launch CfCT, follow the GitHub link given in this section. Do not follow older links to any previously specified S3 buckets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
