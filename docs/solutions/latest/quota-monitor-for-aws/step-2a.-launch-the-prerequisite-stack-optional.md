---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-2a.-launch-the-prerequisite-stack-optional.html
---

# Step 2a. Launch the prerequisite stack (optional)
<a name="step-2a.-launch-the-prerequisite-stack-optional"></a>

**Note**
Use the prerequisite stack only for Organizations deployments.

The solution provides a supplemental prerequisite template. When you deploy this automated CloudFormation template in an Organizations management account, a Lambda function checks for the following prerequisites:

1. Checks that the **AWS Organizations** **All Features** is activated.

1. Adds a member account as the designated administrator for CloudFormation StackSets.
**Note**
The solution deploys service-managed StackSets. You must allow trusted access with AWS Organizations in the organization management account before you can use service-managed permissions on the AWS CloudFormation console (refer to [Enable trusted access with AWS Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html?icmpid=docs_cfn_console) in the *AWS CloudFormation User Guide*) or AWS Organizations console (refer to [Enabling trusted access with AWS CloudFormation Stacksets](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html#integrate-enable-ta-cloudformation) in the *AWS Organizations User Guide*).

The Lambda function installs the prerequisites. If there are errors during prerequisite installation, a stack rollback occurs with an error message.

Use the following procedures to deploy the `quota-monitor-prerequisite.template` CloudFormation template.

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-prerequisite.template` CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-prerequisite.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-prerequisite.template&redirectId=ImplementationGuide)
**Note**
You must launch the template in the US East (N. Virginia) or AWS GovCloud (US-West) Region of the [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) for the management account.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

| Parameter | Default | Description |
| --- | --- | --- |
|  **Quota Monitor Monitoring Account**  |  {{<Requires input>}}  | Account ID for the primary account. This account will also be configured as the StackSets administrator account. |

1. Choose **Next**.

1. On the **Configure stack options\*page, choose \*Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should receive a `CREATE_COMPLETE` status in less than two minutes.
