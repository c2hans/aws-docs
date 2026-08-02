---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-1-launch-the-organization-role-stack-optional.html
---

# Step 1: Launch the organization role stack (optional)
<a name="step-1-launch-the-organization-role-stack-optional"></a>

Follow the step-by-step instructions in this section to configure and deploy the organization role stack into your Organizations management account. This optional step helps you add a OU path and VPC name in the attachment tags for tracking and auditing.

1. Sign in to your AWS Organizations management account using the AWS Management Console and select the button to launch the `network-orchestration-organization-role.template` AWS CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=STNO-role&templateURL=https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-organization-role.template&redirectID=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?stackName=STNO-role&templateURL=https://solutions-reference.s3.amazonaws.com/network-orchestration-for-aws-transit-gateway/latest/network-orchestration-organization-role.template&redirectID=ImplementationGuide)

1. Launch this template in the same Region as you plan to launch the hub and spoke templates. The organization role template launches in the US East (N. Virginia) Region by default.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. For **Parameters**, review the parameters for the template and modify them as necessary. This stack uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/step-1-launch-the-organization-role-stack-optional.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Choose the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately three to four minutes.

**Note**
After the stack deploys, record the ARN for the role from the **Outputs** tab of the stack. You need this ARN as input for the **Account List or AWS Organizations ARN** parameter in the hub template.
