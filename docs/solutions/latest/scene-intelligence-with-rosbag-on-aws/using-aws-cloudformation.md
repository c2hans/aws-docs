---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/using-aws-cloudformation.html
---

# Using AWS CloudFormation
<a name="using-aws-cloudformation"></a>

This solution uses a CloudFormation template to handle the uninstallation workflow.

 **Time to deploy:** Approximately 100-120 minutes

## AWS CloudFormation template for uninstallation
<a name="aws-cloudformation-template-for-uninstallation"></a>

You can download the CloudFormation template for uninstalling this solution before deploying it.

 [![View template button](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-delete.template) **scene-intelligence-with-rosbag-on-aws-delete.template** Use this template to destroy the modules related to the solution and all associated components orchestrated by an open source GitOps library called `seedfarmer`.

This CloudFormation template uninstalls the Scene Intelligence with Rosbag on AWS solution in the AWS Cloud.

## Prerequisites for uninstallation
<a name="prerequisites-for-uninstallation"></a>

You must meet the following prerequisites before launching the uninstallation stack:
+ Administrative permissions, or permissions sufficient to create and configure the AWS services used by these stacks.

## Launch the uninstallation stack
<a name="launch-the-uninstallation-stack"></a>

Follow the step-by-step instructions in this section to uninstall the solution from your account.

 **Time to deploy:** Approximately 100-120 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `scene-intelligence-with-rosbag-on-aws-delete.template` AWS CloudFormation template.

    [![launch solution](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=Scene-intelligence-with-rosbag-on-aws-role&amp;templateURL=https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-delete.template)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses the Amazon MWAA service, which is not currently available in all AWS Regions. You must launch this solution in a Region where Amazon MWAA is available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Select **Next**.

1. On the **Configure stack options** page, choose **Next** after reviewing the settings.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 100 - 120 minutes

After the stack reaches CREATE\_COMPLETE status, the modules and the associated components related to Scene Intelligence with Rosbag on AWS solution will be destroyed. If the stack deployment fails, refer to [Troubleshooting](troubleshooting.md).

You can then delete the CloudFormation stacks which deployed and destroyed the Scene Intelligence with Rosbag on AWS solution from the AWS Management Console or by using the AWS Command Line Interface.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
