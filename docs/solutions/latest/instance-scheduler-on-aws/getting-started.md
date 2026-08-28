---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/getting-started.html
---

# Getting started
<a name="getting-started"></a>

This guide contains a brief overview and instructions to deploy the solution quickly. This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

## Deployment process overview
<a name="deployment-process-overview"></a>

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [Privacy notice](https://aws.amazon.com/privacy/).

To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution.

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 5-10 minutes (not including configuration).

 [Step 1: Launch the instance scheduler stack](step-1-launch-the-instance-scheduler-hub-stack.md)

1. Launch the AWS CloudFormation template in your AWS account.

1. Enter values for the required parameters.

1. Review the other template parameters, and adjust if necessary.

 [Step 2 (Optional): Launch the remote stack in secondary accounts](step-2-optional-launch-the-remote-stack-in-secondary-accounts.md)

1. Launch the AWS CloudFormation template in your AWS account.

1. Enter values for the required parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
