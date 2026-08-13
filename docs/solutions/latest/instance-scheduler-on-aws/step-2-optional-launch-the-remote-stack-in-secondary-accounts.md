---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/step-2-optional-launch-the-remote-stack-in-secondary-accounts.html
---

# Step 2 (Optional): Launch the remote stack in secondary accounts
<a name="step-2-optional-launch-the-remote-stack-in-secondary-accounts"></a>

**Important**
The remote stack must be deployed in the same Region as the hub stack.

This automated AWS CloudFormation template configures secondary account permissions that will allow the hub stack to schedule instances in other accounts. Install the remote template only after the primary/hub stack has been successfully installed in the Hub account.

 [![Launch solution](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/launch-solution-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws-remote.template&redirectID=ImplementationGuide)

1. Sign in to the AWS Management Console of the applicable secondary account and select the button to launch the instance-scheduler-on-aws-remote AWS CloudFormation template.

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar. If the hub stack is configured to use AWS Organizations, then deploy the remote template in the same region as the hub stack.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify Details** page, assign a name to your remote stack.

1. Under **Parameters**, review the parameter for the template, and modify it.

1. If the AWS Organizations option is enabled and the hub stack is similarly configured, there are no further changes required in the main stack to start the scheduling.

1. If the AWS Organization option is set to No, then the hub stack should be updated with the new Account ID.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="3"> <b>Infrastructure</b> </td></tr>
  <tr><td> <b>Namespace</b> </td><td> <code>default</code> </td><td>Unique identifier used to differentiate between multiple solution deployments. Must be set to the same value as the hub stack.</td></tr>
  <tr><td> <b>Use AWS Organizations</b> </td><td> <code>No</code> </td><td>Use AWS Organizations to automate spoke account registration. Must be set to the same value as the hub stack.</td></tr>
  <tr><td> <b>Hub Account ID</b> </td><td> <i>&lt;Requires Input&gt;</i> </td><td>Account ID of the Instance Scheduler on AWS hub stack that will schedule resources in this account.</td></tr>
  <tr><td> <b>Schedule tag key</b> </td><td> <code>Schedule</code> </td><td>The tag key that the solution reads to determine the schedule for a resource. Must be set to the same value as the hub stack.</td></tr>
  <tr><td colspan="3"> <b>Member-Account Scheduling</b> </td></tr>
  <tr><td> <b>Region(s)</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>List of Regions where instances will be scheduled. For example, <code>us-east-1</code>,<code>us-west-1</code>. (this does not have to be the same region list as the hub). If you leave this parameter blank, the solution will use the current Region.</td></tr>
  <tr><td> <b>KMS Key ARNs for EC2</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>Comma-separated list of KMS ARNs to grant the solution kms:CreateGrant permissions to provide the EC2 service with decrypt permissions for encrypted EBS volumes. This allows the scheduler to start EC2 instances with attached encrypted EBS volumes. Provide (*) to give limited access to all KMS keys; leave blank to disable. For details, refer to <a href="security-1.md#encrypted-ec2-ebs-volumes">Encrypted EC2 EBS Volumes</a>.</td></tr>
  <tr><td> <b>License Manager ARNs for EC2</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>Comma-separated list of License Manager configuration ARNs to grant Instance Scheduler permissions to start EC2 instances managed by License Manager. Leave blank to disable. For details, refer to <a href="security-1.md#ec2-license-manager">EC2 License Manager</a>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Be sure to check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of `CREATE_COMPLETE` in approximately five minutes.
