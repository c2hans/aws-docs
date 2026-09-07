---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/step-1.-option-1-launch-the-stack-in-aws-regions.html
---

# Step 1. (Option 1) Launch the stack in AWS Regions
<a name="step-1.-option-1-launch-the-stack-in-aws-regions"></a>

**Important**
 The following deployment instructions apply to AWS Regions only. For deployment in AWS China Regions refer to [Option 2](step-1.-option-2-launch-the-stack-in-aws-china-regions.md).

 **Deploy the AWS CloudFormation template for Option 1 – AWS Regions**

**Note**
You are responsible for the cost of the AWS services used while running this Guidance. For more details, visit the [Cost](cost.md) section in this guide, and refer to the pricing webpage for each AWS service used in this Guidance.

1. Sign in to the AWS Management Console and use the button below to launch the `DataTransferHub-cognito.template` CloudFormation template. Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/data-transfer-hub/latest/DataTransferHub-cognito.template) as a starting point for your own implementation.

   [![Blue oval button with white text reading "Launch solution".](https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/images/launch-solution.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/template?stackName=DataTransferHub&templateURL=https://s3.amazonaws.com/solutions-reference/data-transfer-hub/latest/DataTransferHub-cognito.template&redirectId=ImplementationGuide)

1.  The template launches in the US East (N. Virginia) Region by default. To launch the Guidance in a different AWS Region, use the Region selector in the console navigation bar.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your Guidance stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this Guidance template and modify them as necessary. This Guidance uses the following default values:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/data-transfer-hub/step-1.-option-1-launch-the-stack-in-aws-regions.html)

1.  Choose **Next**.

1.  On the **Configure Stack Options** page, keep the default values and choose **Next**.

1.  On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1.  Choose **Create stack** to deploy the stack.

 You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 15 minutes.
