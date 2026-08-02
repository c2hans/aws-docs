---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/step-1.-launch-the-stack.html
---

# Step 1. Launch the stack
<a name="step-1.-launch-the-stack"></a>

This automated AWS CloudFormation template deploys the Landing Zone Accelerator on AWS in the AWS Cloud. You must complete the applicable steps in [Prerequisites](prerequisites.md) before launching the stack.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `AWSAccelerator-InstallerStack` CloudFormation template. [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Flanding-zone-accelerator-on-aws%2Flatest%2FAWSAccelerator-InstallerStack.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Flanding-zone-accelerator-on-aws%2Flatest%2FAWSAccelerator-InstallerStack.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution recommends using the AWS Control Tower service, which isn’t currently available in all AWS Regions. We recommend launching this solution in an AWS Region where AWS Control Tower is available. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. We recommend you name your stack `AWSAccelerator-InstallerStack` to match the naming convention used by additional stacks that will be created by the Landing Zone Accelerator on AWS. For information about naming character limitations, refer to [IAM and STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/step-1.-launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next.**

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template might create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately eight minutes.
