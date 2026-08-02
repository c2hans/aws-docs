---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-4-launch-the-spoke-stacks.html
---

# Step 4: Launch the spoke stack(s)
<a name="step-4-launch-the-spoke-stacks"></a>

Follow the step-by-step instructions in this section to configure and deploy the spoke stack(s) into your account(s).

**Note**
You must wait for the hub stack deployment to complete before you launch the spoke templates. The spoke templates depend on the EventBridge rule created during the hub stack launch. Additionally, deploy all templates in the same Region.

1. Sign in to your AWS spoke account using the AWS Management Console and select the button to launch the `network-orchestration-spoke.template` CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=STNO-role&templateURL=https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-spoke.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=STNO-role&templateURL=https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-spoke.template&redirectId=ImplementationGuide)

1. Launch this template in the same Region as the hub template. The template launches in the US East (N. Virginia) Region by default.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. For **Parameters**, review the parameters for the template and modify them as necessary. This stack uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-4-launch-the-spoke-stacks.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately three to four minutes.
