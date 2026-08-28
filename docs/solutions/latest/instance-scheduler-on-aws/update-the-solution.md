---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

Instance Scheduler is designed to be safe to update in-place using AWS CloudFormation. The general procedure to do this is as follows:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), on the account/region where your Hub stack is installed,select `instance-scheduler-on-aws`, and select **Update stack**.

1. Select **Make a direct update**.

1. Select **Replace existing template**.

1. Under **Specify template**:
   + Select **Amazon S3 URL**.
   + Copy the link of the [latest template](aws-cloudformation-templates.md).
   + Paste the link in the **Amazon S3 URL** box.
   + Verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**. Choose **Next** again.

1. Under **Parameters**, review the parameters for the template and modify them as necessary (see list of breaking changes below for any required parameter updates).For details about each of the parameters For details about the parameters, see [Step 1. Launch the instance scheduler stack](step-1-launch-the-instance-scheduler-hub-stack.md).

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **View change set** and verify the changes.

1. Choose **Update stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive an **UPDATE\_COMPLETE** status in a few minutes.

Repeat the above steps for the aws-instance-scheduler-remote stacks in each of your spoke accounts.

## Breaking Changes in Specific Versions
<a name="breaking-changes"></a>

When updating the solution, you can upgrade directly from any older version to any newer version without loss of critical data or interruption to scheduling. Please see below for a list of behavioral and breaking changes in each major version.

A full changelog can be viewed on [the solution’s GitHub page](https://github.com/aws-solutions/instance-scheduler-on-aws/releases)

## v1.5.0
<a name="updating-to-v1.5.x"></a>

Version 1.5.0 replaces the need to provide a list of cross-account scheduling role ARNs with the ability to automatically manage them through your AWS Organization. If you don’t want to use AWS Organizations, you can instead provide a list of Spoke Account IDs and Instance Scheduler will manage the scheduling roles for you.

When updating to v1.5.0 or newer, you must:

1. Update the hub template using the normal update instructions while updating the following parameters:

   1. Choose a unique namespace for the solution.

   1. Select whether you would like to **Use AWS Organizations** to manage spoke registration going forward.

      1. If you selected **Yes** replace **Organization ID/Remote Account IDs** with the ID of your AWS Organization.

      1. If you selected **No** replace **OrganizationID/RemoteAccountIDs** with a comma-separated list of the Account IDs of your Spoke accounts.

1. Update all remote stacks using the normal update instructions while updating the following parameters :

   1. Namespace - same as you chose for the hub account.

   1. Use AWS Organizations - same as hub account.

   1. Hub Account ID - Account ID of the hub account (should be unchanged from before).

## v3.0.0
<a name="updating-to-v3.x"></a>

v3.0.0 Adds support for EC2 autoscaling groups and breaks apart the solution’s core lambda function into separate functions with dedicated responsibilities to provide better security isolation for each individual function. This release also updates scheduling log behavior to include "SchedulingDecision" logs for better insight into scheduling operations.

V3.0.0 contains the following breaking changes compared to previous versions:
+ "CloudWatch Metrics" feature in 1.5.x has been replaced with the [Operational Insights Dashboard](monitor-the-solution.md#operational-insights-dashboard).
+ Per-schedule metrics in CloudWatch have been moved from Schedule/Service/MetricName → Schedule/Service/SchedulingInterval/MetricName.
+ All existing metrics will remain, but new metrics will now be gathered under the new namespace and will be made available in the solution dashboard.
+ KMS key ARNs for use with encrypted EBS volumes on EC2 DB instances must now be provided to the hub/spoke CloudFormation stack in their respective accounts. (For more information, refer to [Encrypted EC2 EBS Volumes](security-1.md#encrypted-ec2-ebs-volumes).)
  + If you are scheduling EC2s with Encrypted EBS Volumes, you will need to copy the KMS key arns being used to your hub/spoke stack parameters.
+ The CloudFormation parameter for scheduled services has been broken up into individual parameters for each supported service.
  + All services will be enabled by default and can be disabled individually.
+ Instance Scheduler 3.0 is not backwards compatible with older versions of the Instance Scheduler CLI.
  + You will need to update to the latest version of the Instance Scheduler CLI to continue using CLI commands.

In addition to the above, the schema of the Maintenance Window table has been updated and will be replaced as part of the update. This will reset tracking for EC2 maintenance windows for the first few minutes after updating to v3.x and in rare cases may cause instances currently within a maintenance window to be stopped prematurely immediately following the update. After this data has been regenerated scheduling operations will continue as normal.

## v3.1.0
<a name="updating-to-v3.1.x"></a>

v3.1.0 refactors the core infrastructure of the solution to use AWS tagging events to track when resources are tagged for scheduling. Please ensure that your organization’s permissions will allow these tagging events to be sent from member accounts to your central hub account.

When updating to v3.1.0 or newer:
+ Spoke accounts now declare scheduled regions independently of the hub account. Each spoke stack must specify which regions to schedule in that account using the **Region(s)** parameter.
+ AWS Organizations mode is now required for deployments with more than 40 total accounts. If you have more than 40 accounts and are not using Organizations mode, you must enable it during the update.
+ If you have EC2 instances managed in AWS License Manager that you want to schedule, add the License Manager configuration ARNs to the **License Manager Configuration ARNs** parameter in your hub/spoke CloudFormation stacks. For more information, refer to [EC2 License Manager](security-1.md#ec2-license-manager).
+ The solution will automatically apply an IS-ManagedBy tag to resources after they are tagged for scheduling to indicate they are being managed by the scheduler.
+  *(Restored in v3.2.0)* Scheduled instance resizing (defining `period-name@size` in a schedule) was temporarily removed in v3.1.0 but has been re-implemented in v3.2.0 and newer. Refer to [Instance type](schedule-reference.md#instance-type).
+ Listing member accounts via an SSM parameter (passing `{param: ssm-param-name}` to the accounts parameter on the hub stack) is no longer supported. All trusted accounts must be passed to the hub stack at deploy-time.
+ Instance Scheduler will require up to 6 unique tags on resources during scheduling. Please ensure sufficient tagging capacity on resources when combined with the rest of your organization’s tagging strategy.
+ Per-schedule metrics have been removed from CloudWatch.
+ Solution logs have been repackaged into separate administrative and scheduling log groups and optimized for querying with CloudWatch Log Insights. Please refer to [Monitoring the Solution](monitor-the-solution.md) for more information.
+ Start and stop tags are no longer configurable through CloudFormation parameters. The solution now uses fixed tag names with richer information for tracking scheduling actions.

**Important**
Instance Scheduler writes up to 6 unique tags to managed resources during normal operation. Ensure that your tag governance policies (such as AWS Config rules, tag policies, or automated remediation) are configured to allow these tags. For a full list of tags and important governance considerations, refer to [Informational tags](monitor-the-solution.md#informational-tags).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
