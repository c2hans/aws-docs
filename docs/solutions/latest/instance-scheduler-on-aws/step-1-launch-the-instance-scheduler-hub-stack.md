---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/step-1-launch-the-instance-scheduler-hub-stack.html
---

# Step 1: Launch the instance scheduler hub stack
<a name="step-1-launch-the-instance-scheduler-hub-stack"></a>

Follow the step-by-step instructions in this section to deploy the solution into your account.

 **Time to deploy:** Approximately five minutes

 [![Launch solution](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/launch-solution-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template&redirectId=ImplementationGuide)

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the\* instance-scheduler-on-aws.template\* AWS CloudFormation template.

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="3"> <b>Infrastructure</b> </td></tr>
  <tr><td> <b>Namespace</b> </td><td> <code>default</code> </td><td>Provide a unique identifier to differentiate between multiple solution deployments (no spaces). Example: Dev.</td></tr>
  <tr><td> <b>Use AWS Organizations</b> </td><td> <code>No</code> </td><td>Use AWS Organizations to automate spoke account registration.</td></tr>
  <tr><td> <b>Organization ID/Remote Account IDs</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td> <i>If you’re using AWS Organizations this field is required.</i> Provide the Organization ID, for example, <code>o-xxxxyyy</code>. Otherwise, provide a comma separated list of trusted spoke Account IDs that can register themselves for scheduling (maximum 40), such as <code>1111111111, 2222222222</code> </td></tr>
  <tr><td> <b>Schedule tag key</b> </td><td> <code>Schedule</code> </td><td>The tag key that the solution reads to determine the schedule for a resource. The value on a resource specifies the name of the schedule. If you choose to modify the default value, assign a name that is easy to apply consistently and correctly across all necessary instances. <b>Note</b>: The tag key is case sensitive.</td></tr>
  <tr><td> <b>Retain data and logs</b> </td><td> <code>Enabled</code> </td><td>Enable deletion protection for DynamoDB tables used by the solution. This causes the tables to be retained when deleting this stack. To delete the tables when deleting this stack, first disable this parameter.</td></tr>
  <tr><td colspan="3"> <b>Global Settings</b> </td></tr>
  <tr><td> <b>Enable scheduling</b> </td><td> <code>Yes</code> </td><td>Set to <code>No</code> to suspend all scheduling operations.</td></tr>
  <tr><td> <b>Default time zone</b> </td><td> <code>UTC</code> </td><td>Default IANA (International assigned Numbers Authority) time zone identifier for schedules that do not specify a time zone. For a list of valid time zone identifiers, refer to the <b>TZ identifier</b> column of the <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">List of tz database time zones</a>.</td></tr>
  <tr><td> <b>Scheduling interval (minutes)</b> </td><td> <code>5</code> </td><td>Interval in minutes between scheduler runs. Shorter intervals increase accuracy and responsiveness but also increase costs. Production deployments require a minimum of 5 minutes for stable operation; shorter values are for small-scale testing only.</td></tr>
  <tr><td> <b>Enable EC2 SSM maintenance windows</b> </td><td> <code>No</code> </td><td>Allow schedules to specify one or more Systems Manger maintenance window names. Instance Scheduler on AWS will then ensure that instances tagged with that schedule are started at least ten minutes before associated maintenance windows.</td></tr>
  <tr><td> <b>Create RDS instance snapshots on stop</b> </td><td> <code>No</code> </td><td>Choose whether to create a snapshot before stopping RDS DB instances. <b>Note:</b> Snapshots are not available for Amazon Aurora clusters.</td></tr>
  <tr><td> <b>ASG action name prefix</b> </td><td> <code>IS-</code> </td><td>The prefix that the solution uses when naming Scheduled Scaling actions for Auto Scaling groups. Actions with this prefix will be added and removed by the solution as needed.</td></tr>
  <tr><td> <b>ASG scheduled tag key</b> </td><td> <code>scheduled</code> </td><td>Deprecated. This parameter exists for migration purposes only and should not be edited.</td></tr>
  <tr><td colspan="3"> <b>Hub-Account Scheduling</b> </td></tr>
  <tr><td> <b>Region(s)</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>List of Regions where instances will be scheduled. For example, <code>us-east-1</code>,<code>us-west-1</code>. NOTE: If you leave this parameter blank, the solution will use the current Region.</td></tr>
  <tr><td> <b>KMS Key ARNs for EC2</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>Comma-separated list of KMS ARNs to grant Instance Scheduler on AWS kms:CreateGrant permissions to provide the EC2 service with decrypt permissions for encrypted EBS volumes. This allows the scheduler to start EC2 instances with attached encrypted EBS volumes. Provide (*) to give limited access to all KMS keys; leave blank to disable. For details on the created policy, refer to <a href="security-1.md#encrypted-ec2-ebs-volumes">Encrypted EC2 EBS Volumes</a>.</td></tr>
  <tr><td> <b>License Manager ARNs for EC2</b> </td><td> <i>&lt;Optional Input&gt;</i> </td><td>Comma-separated list of License Manager configuration ARNs to grant Instance Scheduler permissions to start EC2 instances managed by License Manager. Leave blank to disable. For details, refer to <a href="security-1.md#ec2-license-manager">EC2 License Manager</a>.</td></tr>
  <tr><td colspan="3"> <b>Monitoring</b> </td></tr>
  <tr><td> <b>Enable informational tagging</b> </td><td> <code>Yes</code> </td><td>When enabled, Instance Scheduler writes informational tags to managed resources indicating the last scheduling action taken and any errors encountered. For more information, refer to <a href="monitor-the-solution.md#informational-tags">Informational tags</a>.</td></tr>
  <tr><td> <b>Enable CloudWatch Debug Logs</b> </td><td> <code>No</code> </td><td>Enable debug-level logging in CloudWatch logs.</td></tr>
  <tr><td> <b>Log retention period (days)</b> </td><td> <code>30</code> </td><td>The log retention period for CloudWatch logs in days.</td></tr>
  <tr><td> <b>Operational Monitoring</b> </td><td> <code>Enabled</code> </td><td>Deploy an operational insights dashboard to CloudWatch and gather custom metric data on the solution’s operation. The dashboard can be disabled to reduce <a href="monitor-the-solution.md#additional-costs-associated-with-this-feature">associated costs</a> if desired.</td></tr>
  <tr><td colspan="3"> <b>Other</b> </td></tr>
  <tr><td> <b>SchedulingRequestHandler Memory size (MB)</b> </td><td> <code>512</code> </td><td>The memory size of the AWS Lambda function that schedules resources. Increase if you are experiencing high memory usage or timeouts.</td></tr>
  <tr><td> <b>Orchestrator Memory size (MB)</b> </td><td> <code>512</code> </td><td>The memory size of the orchestrator Lambda function. Increase if you are experiencing high memory usage or timeouts.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately five minutes.
