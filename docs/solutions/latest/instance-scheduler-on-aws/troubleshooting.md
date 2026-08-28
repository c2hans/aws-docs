---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the solution.

Known issue resolution provides instructions to mitigate known errors. If these instructions don’t address your issue, [Contact Support](contact-aws-support.md) provides instructions for opening an Support case for this solution.

## Known issue resolution
<a name="known-issue-resolution"></a>

### Problem: Instances not being scheduled in a remote account (v1.4-v3.0)
<a name="problem-instances-not-being-scheduled-in-a-remote-account"></a>

If you notice instances are not being scheduled in a remote account.

### Resolution
<a name="resolution"></a>

Update the hub stack with the secondary account ID or complete the following task:

1. In the primary account, navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/)

1. In the navigation pane, select **Logs** > **Log Groups**.

1. Select the log group named ` <STACK_NAME>-logs`

1. Search for the log stream for the Account ID (remote account).

1. For example, If there is no log stream named with the account ID, go to the DynamoDB console and select the table named ` <STACK_NAME>-<ConfigTable>-<RANDOM>`.

1. Select **Explore Items** and select **Run**.

1. Select the item type Config.

1. Check if the attribute remote\_account\_ids has the account ID.

1. Check if the Account ID is not visible in this attribute.

1. If the solution is configured to aws organizations, then uninstall and reinstall the remote template in the remote account.

1. If the solution is configured to use remote Account IDs, update the cloudformation parameter **Provide Organization Id OR List of Remote Account IDs** with the list of account IDs where the instances are to be scheduled and where the remote template is deployed.

### Problem: Instances not being scheduled (v3.1\+)
<a name="problem-instances-not-being-scheduled-v3.1"></a>

If you notice instances are not being scheduled.

### Resolution
<a name="resolution-1"></a>

1. Verify the resource has an **IS-ManagedBy** tag applied.

1. If the tag is not present, delete and recreate the Schedule tag to retrigger registration.

1. If the tag is still not being applied, verify the region is enabled for scheduling:

   1. Check the hub/spoke stack configuration for the region, or

   1. Navigate to the [EventBridge console](https://console.aws.amazon.com/events/) in the same region as the resource and verify that the default event bus has event rules with the prefix **IS-Tagging**.

1. If the region is not enabled, update the Instance Scheduler stack to include the region in the regions CloudFormation parameter.

1. If the issue persists, review the [solution administration logs](monitor-the-solution.md#logging-and-notifications) for hub registration errors.

1. Confirm that your organization does not have policies in place that would prevent events from being forwarded from your account to the solution hub account.

### Problem: Encrypted EC2 instances not starting
<a name="problem-encrypted-ec2-instances-not-starting"></a>

Instance Scheduler is reporting that EC2 instances with encrypted EBS volumes are being started, but they never actually start.

### Resolution
<a name="resolution-2"></a>

Refer to [Encrypted EC2 EBS Volumes](security-1.md#encrypted-ec2-ebs-volumes) for how to grant Instance Scheduler access to be able to schedule EC2 instances with encrypted EBS volumes

### Problem: Unexpected API costs from informational tagging
<a name="problem-unexpected-api-costs-from-informational-tagging"></a>

Unexpectedly high costs from AWS Resource Groups Tagging API calls, AWS Config evaluations, or related remediation actions.

### Resolution
<a name="resolution-tagging-costs"></a>

Instance Scheduler writes [informational tags](monitor-the-solution.md#informational-tags) to managed resources on each scheduling interval. If your environment enforces tag governance through AWS Config rules, tag policies, or automated remediation, ensure that Instance Scheduler’s tag keys are permitted. For the full list of tag keys and configuration guidance, refer to [Tag governance considerations](monitor-the-solution.md#informational-tag-conflict-with-tag-policies).

If you are unable to update your tag governance policies, disable informational tagging by setting the **Enable informational tagging** parameter to `No` on the hub stack.

### Problem: RDS Instances not stopping when Create RDS Snapshots is Enabled
<a name="problem-rds-instances-not-stopping-when-create-rds-snapshots-is-enabled"></a>

RDS Instances are not being stopped and the solution’s scheduler logs are reporting (AccessDenied) errors when calling the `StopDBInstance` operation due to not having `rds:CreateDBSnapshot` permission.

### Resolution
<a name="resolution-3"></a>

Update the solution to v3.0.5 or newer or alternatively add the `rds:CreateDBSnapshot` permission to the solution’s scheduler role in each scheduled account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
