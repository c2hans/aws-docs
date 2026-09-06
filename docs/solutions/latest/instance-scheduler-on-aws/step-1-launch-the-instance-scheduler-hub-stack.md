---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/step-1-launch-the-instance-scheduler-hub-stack.html
---

# Step 1: Launch the instance scheduler hub stack
<a name="step-1-launch-the-instance-scheduler-hub-stack"></a>

Follow the step-by-step instructions in this section to deploy the solution into your account.

 **Time to deploy:** Approximately five minutes

 [![Launch solution](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/launch-solution-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template&redirectId=ImplementationGuide)

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the\* instance-scheduler-on-aws.template\* AWS CloudFormation template.

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/step-1-launch-the-instance-scheduler-hub-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately five minutes.
