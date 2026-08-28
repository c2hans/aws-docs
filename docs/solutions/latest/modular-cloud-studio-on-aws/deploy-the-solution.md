---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

Follow the step-by-step instructions to configure and deploy the solution into your account.

Before you launch the solution, review the [Cost](cost.md), [architecture overview](architecture-overview.md), [security](security1.md), and other considerations discussed in this guide.

 **Time to deploy:** Approximately 7-10 minutes to deploy the MCS solution stack.

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution. For more information, see the [Anonymized data collection](reference.md#anonymized-data-collection) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
