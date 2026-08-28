---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 5-10 minutes

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `SECURESTREAM.template` AWS CloudFormation template.

   [![Secure Media Delivery at the Edge on AWS launch solution button](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/secure-media-delivery-at-the-edge-on-aws/latest/secure-media-delivery-at-the-edge-on-aws.template)

1.  The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

    **Session Revocation**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html)

    **Key Rotation Frequency**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html)

   **DASH Stream **

    If you do not have a video asset available in DASH format, you can leave the inputs empty in which case example values will be set. You can augment these inputs after the stack is deployed.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html)

    **HLS Stream**

    If you do not have a video asset available in HLS format, you can leave the inputs empty in which case example values will be set. You can augment these inputs after the stack is deployed.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/step-1-launch-the-stack.html)

1.  Choose **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 5 to 10 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
