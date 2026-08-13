---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/launch-the-deployment-stack.html
---

# Launch the deployment stack
<a name="launch-the-deployment-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 100-120 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `scene-intelligence-with-rosbag-on-aws-create.template` CloudFormation template.

    [![launch button](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=Scene-intelligence-with-rosbag-on-aws-role&templateURL=https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-create.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses the Amazon MWAA service, which is not currently available in all AWS Regions. You must launch this solution in a Region where Amazon MWAA is available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Select **Next**.

1. On the **Configure stack options** page, choose **Next** after reviewing the settings.

1. On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 100-120 minutes.
