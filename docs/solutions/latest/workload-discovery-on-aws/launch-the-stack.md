---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

This automated AWS CloudFormation template deploys Workload Discovery on AWS in the AWS Cloud. You must gather deployment parameter details before launching the stack. For details, refer to [Prerequisites](prerequisites.md).

 **Time to deploy:** Approximately 30 minutes

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the `workload-discovery-on-aws.template` AWS CloudFormation template.

    [![Launch Stack](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=workload-discovery&templateURL=https://s3.amazonaws.com/solutions-reference/workload-discovery-on-aws/latest/workload-discovery-on-aws.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses services that are not available in all AWS Regions. Refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for a list of supported AWS Regions.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/launch-the-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the boxes acknowledging that the template creates IAM resources and require certain capabilities.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 30 minutes.
**Note**
If deleted, this stack removes all resources. If the stack is updated, it retains the Amazon Cognito user pool to ensure that configured users aren’t lost.
