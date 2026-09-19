---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/launch-target-account-stack.html
---

# Step 3: Launch the target account stack in the target AWS account
<a name="launch-target-account-stack"></a>

This automated AWS CloudFormation template deploys IAM roles in the target AWS account to allow the factory account to assume roles and perform MGN actions in the target account. Repeat this step for each target account. If the factory stack in the previous step is a target account, it will need to have this target stack deployed to it.

**Note**
The target account must be initialized for AWS Application Migration Service before launching this stack, refer to [Initializing Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html) in the *Application Migration Service User Guide* for more details.
The target account stack must be launched in the same Region as the factory stack in the previous step regardless of which Region will be used as the migration target Region. This stack is for cross account permissions only.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home). Choose **Create stack** then select **With new resources**, to start the deployment of the template. You can also [download the template](https://solutions-reference.s3.amazonaws.com/cloud-migration-factory-on-aws/latest/aws-cloud-migration-factory-solution-target-account.template) as a starting point for your own implementation.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>FactoryAWSAccountId</b> </td><td> <code>111122223333</code> </td><td>Enter an account ID where the Migration Factory was deployed. Launch this stack in the same AWS Region as the Migration Factory stack. </td></tr>
  <tr><td> <b>Replatform</b> </td><td> <code>Yes</code> </td><td>Turn on this option if you plan to use the Replatform EC2 module of this solution</td></tr>
  <tr><td> <b>RehostMGN</b> </td><td> <code>Yes</code> </td><td>Turn on this option if you plan to use the Rehost MGN module of this solution</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next.**

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 5 minutes.
