---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-3a.-launch-the-hub-stack-for-aws-organizations.html
---

# Step 3a. Launch the hub stack for AWS Organizations
<a name="step-3a.-launch-the-hub-stack-for-aws-organizations"></a>

This CloudFormation template deploys the Quota Monitor for AWS into your primary account.

**Note**
This template must be launched in a member account of your Organizations that is registered as delegated administrator for StackSets.
You are responsible for the cost of the AWS services used while running this solution. Review the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-hub.template` CloudFormation template.

    [![launch button](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-hub.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
You can launch this template in any AWS Region.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Deployment Configuration</b> </td><td></td><td></td></tr>
  <tr><td> <b>Deployment Mode</b> </td><td> <code>Organizations</code> </td><td>The solution supports two deployment modes:<br /> <b> Organizations (default) - Monitor quota usage across your Organization. </b> Hybrid - Monitor quota usage monitoring across your Organization and secondary accounts.</td></tr>
  <tr><td> <b>Regions List</b> </td><td> <code>ALL</code> </td><td>The list of AWS Regions where the Service Quotas spoke templates should be deployed. Options are ALL or a comma separated list of AWS Regions (for example, <code>us-east-1</code>).</td></tr>
  <tr><td> <b>SNS Spoke Region</b> </td><td>&lt;Optional input&gt;</td><td>Optionally, specify the AWS Region to launch the decentralized SNS stack in the spoke accounts. If left empty, the stack will not be launched.</td></tr>
  <tr><td> <b>Management Account Id</b> </td><td> <code>\*</code> </td><td>Organization’s management Id to scope permissions down for Stackset creation.</td></tr>
  <tr><td> <b>StackSet Deployment Options</b> </td><td></td><td></td></tr>
  <tr><td> <b>Region Concurrency</b> </td><td> <code>PARALLEL</code> </td><td>Selection of whether to deploy the StackSets into AWS Regions in parallel (default) or sequentially.</td></tr>
  <tr><td> <b>Percentage Maximum concurrent accounts</b> </td><td> <code>100</code> </td><td>Percentage of accounts per AWS Region to which you can deploy stacks at one time.</td></tr>
  <tr><td> <b>Percentage Failure tolerance</b> </td><td> <code>0</code> </td><td>Percentage of account, per AWS Region, for which stacks can fail before CloudFormation stops the operation in that Region.</td></tr>
  <tr><td> <b>Notification Configuration</b> </td><td></td><td></td></tr>
  <tr><td> <b>Email Notification</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Email address to receive alert notifications.</td></tr>
  <tr><td> <b>Slack Notification</b> </td><td> <code>No</code> </td><td>Choose <code>Yes</code> if you want to receive Slack notifications for quota utilization alerts. You can specify the Slackhook web URL later in the Systems Manager Parameter Store (see <a href="step-7.-configure-notifications-optional.md">Step 7: Configure notifications</a>.</td></tr>
  <tr><td> <b>Stackset Stack Configuration Parameters</b> </td><td></td><td></td></tr>
  <tr><td> <b>Notification Threshold</b> </td><td> <code>80</code> </td><td>The percentage threshold for quota utilization notifications.</td></tr>
  <tr><td> <b>Monitoring Frequency</b> </td><td> <code>rate (12 hours)</code> </td><td>How often the quota monitoring scan should run. Available choices are every 6 or 12 hours.</td></tr>
  <tr><td> <b>Report OK Notiﬁcations</b> </td><td> <code>No</code> </td><td>Whether to save the <code>OK</code> notiﬁcations in the summary table on the hub account.</td></tr>
  <tr><td> <b>SageMaker AI Monitoring</b> </td><td> <code>Yes</code> </td><td>Choose <code>Yes</code> to enable monitoring for SageMaker AI quotas, or <code>No</code> to disable it. Enabling SageMaker AI monitoring might consume a high number of quotas, which could lead to higher usage costs.</td></tr>
  <tr><td> <b>Connect Monitoring</b> </td><td> <code>Yes</code> </td><td>Select <code>Yes</code> to enable monitoring for Amazon Connect quotas, or <code>No</code> to disable it. Keep in mind enabling Connect monitoring might consume a high number of quotas, which could result in higher usage costs.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately five minutes.

1. In the subscription notification email, select the **SubscribeURL** link to turn on Amazon SNS email notifications.
   + Customizing SageMaker and Amazon Connect services monitoring \*

Because monitoring SageMaker and Amazon Connect services can incur high costs, this solution allows you to enable or disable monitoring for these services at the hub template level. This setting applies to all spoke accounts in your deployment.

To change these settings:

1. Update the hub stack in CloudFormation.

1. Modify the **SageMaker Monitoring** and **Connect Monitoring** parameters as needed.

1. Apply the stack update.

**Note**
Changing these parameters during a stack update affects all spoke accounts. If you leave them unchanged, the existing monitoring customizations in the spoke accounts remain intact.
For spoke account-specific customization, you can modify the monitoring status in their Service DynamoDB table after deployment. The table includes entries for each service, such as SageMaker and Amazon Connect, with a **Monitored** field that can be set to `true` or `false`.

**Important**
Steps 4a and 4b are critical for the solution to function correctly. Without updating these, the solution won’t know which accounts, OUs, or Regions to monitor.
