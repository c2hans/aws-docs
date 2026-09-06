---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

**Important**
 **Upgrading to v4.0.0 or later:** The solution preserves your existing auto-remediation settings across the upgrade. If you are upgrading from **v2.x**, the solution automatically migrates the auto-remediation settings from your v2 EventBridge rules to the new DynamoDB-backed configuration during the stack update. Controls that you had auto-remediation enabled for in v2 stay enabled in v4, and controls without a v3\+ equivalent are skipped and listed in the migration AWS Lambda function’s Amazon CloudWatch logs. If you are upgrading from **v3.x**, your auto-remediation settings already reside in the DynamoDB-backed configuration and carry over unchanged, so no migration is required. If the migration encounters a per-control failure or aborts before any controls are written, the `SO0111-ASR-MigrationAutoRemediation` Lambda function publishes an Amazon SNS notification to the existing `SO0111-ASR_Topic`. **To receive that notification, you must have a confirmed subscription on `SO0111-ASR_Topic` before starting the v4 stack update.** Refer to [Upgrading from v2.x to v4.0.0 or later](#upgrading-from-v2-to-v4).
 **Upgrading to v3.x from v2.x:** Re-enable automated remediation rules manually in the Admin account after the stack update. Refer to [Enable fully-automated remediations](enable-fully-automated-remediations.md).
If you are using the `Reuse Orchestrator Log Group` parameter to retain logs, ensure it is set appropriately during stack update to avoid log group recreation or loss of log retention settings. Refer to [Deploy the solution](deployment.md). If you are performing a stack update to v2.3.0\+ from an earlier version choose "no"

## Upgrading from versions prior to v1.4
<a name="v1.3.0-or-v1.3.1-to-v1.3.2"></a>

If you have previously deployed the solution prior to v1.4.x, uninstall, then install the latest version:

1. Uninstall the previously deployed solution. Refer to [Uninstall the solution](uninstall-the-solution.md).

1. Launch the latest template. Refer to [Deploy the solution](deploy-the-solution.md).
**Note**
If you are upgrading from v1.2.1 or earlier to v1.3.0 or later, set `Reuse Orchestrator Log Group` to `No`. If you are reinstalling v1.3.0 or later, you can select `Yes` for this option. This option allows you to continue to log to the same Log Group for the Orchestrator Step Functions.

## Upgrading from v1.4 and later
<a name="earlier-versions-to-v1.3.2"></a>

If you are upgrading from v1.4.x, update all stacks or StackSets as follows:

1. Update the stack in the Security Hub admin account using the [latest template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template).

1. In each member account, update the permissions from the latest template.

1. In each member account in all Regions where currently deployed, update the member stack from the latest template.

1. If the Web UI is enabled and you updated parameters such as `TicketGenFunctionName`, invalidate the CloudFront cache to reflect changes immediately:

   ```
   aws cloudfront create-invalidation \
     --distribution-id <distribution-id> \
     --paths "/aws-exports.json"
   ```

## Upgrading from v2.0.x
<a name="upgrading-from-v2.0.x"></a>

If you are upgrading from v2.0.x, upgrade to v2.3.0 first. Updating to v2.1.0–2.1.1 fails in CloudFormation.

## Upgrading from v2.1.4 or earlier
<a name="upgrading-from-v2.1.4"></a>

If you are upgrading from v2.1.4 or earlier, **you must upgrade to v2.3.0 before upgrading to any version higher than v2.3.0.** Otherwise, the stack update operation will fail. Alternatively, you can delete and re-deploy the solution’s stacks rather than performing a stack update.

## Upgrading from v2.x to v4.0.0 or later
<a name="upgrading-from-v2-to-v4"></a>

Starting in v4.0.0, the solution preserves your auto-remediation settings across the v2 to v4 upgrade. In v2, per-control Amazon EventBridge rules stored the auto-remediation state. In v3 and later, the solution stores it in the Remediation Configuration Amazon DynamoDB table in the admin account. During the v4 stack update, a custom resource scans your existing v2 `_AutoTrigger` rules, translates each rule’s standard-specific control ID to the corresponding security control ID, and writes the previously enabled controls to the DynamoDB table.

The migration covers all five v2 playbooks:
+  `SC` (AWS Security Hub Service-managed security controls) — control IDs are written to DynamoDB unchanged.
+  `AFSBP` (AWS Foundational Security Best Practices) — control IDs are written to DynamoDB unchanged.
+  `NIST80053R5` (NIST 800-53 Revision 5) — control IDs are written to DynamoDB unchanged.
+  `PCI` (PCI DSS v3.2.1) — the leading `PCI.` prefix is removed (for example, `PCI.S3.5` becomes `S3.5`).
+  `CIS` (CIS AWS Foundations Benchmark v1.2.0, v1.4.0, and v3.0.0) — each CIS control ID is mapped to the security control its v2 SSM remediation document targeted.

Migration outcomes:
+ Controls migrated successfully need no action — they are auto-remediation enabled in v4 the same way they were in v2.
+ Controls that the migration skips fall into two categories: CIS rules without an ASR remediation in v2, and controls v3\+ does not ship. Skipped controls are listed in the `SO0111-ASR-MigrationAutoRemediation` AWS Lambda function’s Amazon CloudWatch logs.
+ If the migration encounters a per-control failure (for example, a transient throttling error during the DynamoDB update) or aborts before any controls are written, `SO0111-ASR-MigrationAutoRemediation` publishes an Amazon SNS notification to the existing `SO0111-ASR_Topic` topic. The notification body lists the affected control IDs and is prefixed with `[ASR v2 → v3/v4 migration]`.
+ The custom resource only runs during the initial v3/v4 stack update. Subsequent stack updates do not re-run migration.

**Note**
 **Subscribe to the SNS topic before upgrading.** Migration failure notifications publish to the solution’s existing `SO0111-ASR_Topic` Amazon SNS topic. If you do not have a confirmed subscription on that topic before the upgrade, the failure notification does not reach you. In that case, you only see the failure in the `SO0111-ASR-MigrationAutoRemediation` AWS Lambda function’s Amazon CloudWatch logs. To subscribe an endpoint, retrieve the topic ARN from AWS Systems Manager Parameter Store at `/Solutions/SO0111/SNS_Topic_ARN` and add an SNS subscription (email, SQS, AWS Lambda function, or any other supported protocol) before starting the v4 stack update. Confirm any email subscriptions through the AWS confirmation email so the topic is ready to deliver before the migration runs.

If migration is unable to write a control you want auto-remediated in v4, enable it manually in the Remediation Configuration DynamoDB table. Refer to [Enable fully-automated remediations](enable-fully-automated-remediations.md).
