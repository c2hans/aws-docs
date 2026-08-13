---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-6.-launch-the-spoke-stacks-optional.html
---

# Step 6. Launch the spoke stacks when not using AWS Organizations or hybrid environments
<a name="step-6.-launch-the-spoke-stacks-optional"></a>

Use the following procedure to launch the components necessary to monitor quotas in secondary accounts. You must launch the spoke stack in every account you want to monitor (including the account where the hub stack is deployed). You can deploy the Service Quotas spoke stack in all Regions, but only deploy the Trusted Advisor spoke stack in the Regions where the service’s data plane resides, specifically, US East 1 (N. Virginia) and AWS GovCloud (US-West).

Enter the secondary account IDs in the `/QuotaMonitor/Accounts` Systems Manager Parameter Store provisioned by the primary template before you launch this template in secondary accounts. If you are using Organizations or a hybrid deployment mode, spoke template deployments are managed by CloudFormation StackSets.

**Note**
You are responsible for the cost of the AWS services used while running this solution. Review the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-sq-spoke.template` CloudFormation template.

    [![launch button](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-sq-spoke.template&redirectId=ImplementationGuide)

1. The template is launched in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
You must launch `quota-monitor-ta-spoke.template` in the US East (N. Virginia) or AWS GovCloud (US-West) Region. You can launch the `quota-monitor-sq-spoke.template` in any AWS Region where you need quota monitoring.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the following parameter for the template and modify it as necessary.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-6.-launch-the-spoke-stacks-optional.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. The status should show as `CREATE_COMPLETE` in approximately five minutes.
