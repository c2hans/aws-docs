---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step1-deploy-accountpool-stack.html
---

# Step 1: Deploy the AccountPool stack
<a name="step1-deploy-accountpool-stack"></a>

In this step, you will deploy the resources required to set up Organizational Units (OUs), Service Control Policies (SCPs), roles, and Regions.

**Important**
Ensure that you log into the **Org Management** account for deploying the AccountPool stack.

**Note**
Refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for a list of supported AWS Regions.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `AccountPool` stack CloudFormation template.

 [![Launch Stack](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-AccountPool.template&redirectId=ImplementationGuide)

The template launches in the US East (N.Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack** details page, enter a stack name for your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the AWS Identity and Access Management User Guide.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step1-deploy-accountpool-stack.html)

1. Choose **Next**.

1. On the **Configure stack options** page, review and select to acknowledge the messages under **Capabilities and transforms**, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

**Note**
Always include `us-east-1` as an ISB Managed Region to enable AWS global services. For example, if you want to enable `eu-west-1`, the parameter value should be `us-east-1,eu-west-1`.
