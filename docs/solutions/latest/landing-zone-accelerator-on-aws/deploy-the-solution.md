---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses AWS CloudFormation templates and stacks to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources described in the template.

## Deployment process overview
<a name="deployment-overview"></a>

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-details.md), [network security](security.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately eight minutes for the `AWSAccelerator-Installer` CloudFormation stack and 45 minutes for the initial run of the `AWSAccelerator-Pipeline` pipeline.

**Note**
If you have previously deployed this solution, refer to [Update the solution](update-the-solution.md) for update instructions.

Use the following steps to deploy this solution on AWS. For detailed instructions, follow the links for each step.

 [Step 1. Launch the stack](step-1.-launch-the-stack.md)
+ Launch the AWS CloudFormation template into your AWS account.
+ Review the templates parameters and enter or adjust the default values as needed.

 [Step 2. Await initial environment deployment](step-2.-await-initial-environment-deployment.md)
+ Await successful completion of `AWSAccelerator-Pipeline` pipeline.

 [Step 3. Update the configuration files](step-3.-update-the-configuration-files.md)
+ Navigate to the stored Landing Zone Accelerator on AWS configuration files.
+ Update the configuration files to match the desired state of your environment.
+ Release a change manually to the `AWSAccelerator-Pipeline` pipeline.

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution. For more information, refer to the [Anonymized data collection](reference.md#collection-of-operational-metrics) section of this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
