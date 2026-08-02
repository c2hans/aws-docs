---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-5.-launch-the-spoke-sns-stacks-when-not-using-aws-organizations-or-hybrid-environments.html
---

# Step 5. Launch the spoke SNS stacks when not using AWS Organizations or hybrid environments
<a name="step-5.-launch-the-spoke-sns-stacks-when-not-using-aws-organizations-or-hybrid-environments"></a>

Follow these steps to launch the components necessary for adding decentralized notifications to secondary accounts. Launch this stack in a single Region in every account where you want a separate SNS topic. Ensure that you launch this stack before the **sq spoke stacks** in [Step 6](step-6.-launch-the-spoke-stacks-optional.md).

**Note**
You are responsible for the cost of the AWS services used while running this solution. Review the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-sns-spoke.template` CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws/latest/quota-monitor-sns-spoke.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws/latest/quota-monitor-sns-spoke.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL appears in the **Amazon S3 URL** text box, then choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console under the **Status** column. The status should show as `CREATE_COMPLETE`` in approximately five minutes.
