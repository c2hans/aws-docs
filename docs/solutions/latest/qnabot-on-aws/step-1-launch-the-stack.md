---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-1-launch-the-stack.html
---

# Step 1: Launch the stack
<a name="step-1-launch-the-stack"></a>

This automated AWS CloudFormation template deploys the QnABot on AWS guidance in the AWS Cloud. You must set up an AWS account before launching the stack.

**Note**
You are responsible for the cost of the AWS services used while running this guidance. For more details, see the [Cost](cost.md) section in this guide, and reference to the pricing webpage for each AWS service used in this guidance.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `qnabot-on-aws-main.template` AWS CloudFormation template.

    **Launch guidance**

    [![Launch Stack](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/launch-solution.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create?templateURL=https://solutions-reference.s3.amazonaws.com/qnabot-on-aws/latest/qnabot-on-aws-main.template&redirectId=ImplementationGuide)

   The template launches in the US East (N. Virginia) Region by default. To launch the guidance in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This guidance uses Amazon Lex, which is not currently available in all AWS Regions. You must launch this guidance in an AWS Region where Amazon Lex is available. For the most current availability by Region, see the [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) list.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your guidance stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this guidance template and modify them as necessary. This guidance uses the following default values.
**Note**
Amazon Lex V1 has been deprecated and removed from QnABot v6.1.0. Amazon Lex V2 is used by default.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/step-1-launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, keep the default settings.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template might create IAM resources with custom names, and the box acknowledging that AWS CloudFormation might require the CAPABILITY\_AUTO\_EXPAND capability.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 30-45 minutes.

When the stack deployment is complete, the **Output** tab displays the following information:
+  **ContentDesignerURL** - URL to launch the content designer UI
+  **ClientURL** - URL to launch the end user client webpage
+  **CloudWatchDashboardURL** - URL to launch the CloudWatch dashboard for monitoring
+  **FeedbackSNSTopic** - Topic name to allow feedback notifications
+  **LexV2 bot information** - Data for configuring integration with contact centers and web clients.

**Note**
In addition to the primary AWS Lambda functions, this guidance includes the `solution-helper` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When you run this guidance, the `solution-helper` Lambda function is not regularly active; however, you must not delete it because it is necessary to manage associated resources.
