---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-3-launch-the-hub-stack.html
---

# Step 3: Launch the hub stack
<a name="step-3-launch-the-hub-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the hub stack into your hub account.

1. Sign in to the AWS Management Console with your AWS network hub account and select the button to launch the `network-orchestration-hub.template` CloudFormation template. \+{ [![network orchestration hub launch button](https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=STNO-role&templateURL=https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-hub.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar. See [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for more information on selecting a Region.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

   For **Parameters**, review the parameters for the template and modify them as necessary. This stack uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-3-launch-the-hub-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately 25 minutes.

After the stack is created, you receive two emails that contain temporary passwords for the read-only user and the admin user. If you enabled approval notification, Amazon SNS sends a subscription confirmation email with a link to the solution’s web UI. You can also find the link to the web UI in the CloudFormation stack **Outputs** tab. The link is the **Value** of the **Console URL**. The system-generated password must be changed the first time you sign in.

**Note**
The temporary account expires if you don’t sign in within seven days. Your new password must be at least 10 characters long.
