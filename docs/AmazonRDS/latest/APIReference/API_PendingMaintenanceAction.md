---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PendingMaintenanceAction.html
---

# PendingMaintenanceAction
<a name="API_PendingMaintenanceAction"></a>

Provides information about a pending maintenance action for a resource.

## Contents
<a name="API_PendingMaintenanceAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **
The type of pending maintenance action that is available for the resource.
For more information about maintenance actions, see [Maintaining a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html).
Valid Values:
+  `ca-certificate-rotation`
+  `db-upgrade`
+  `hardware-maintenance`
+  `os-upgrade`
+  `serverless-platform-version-update`
+  `system-update`
For more information about these actions, see [Maintenance actions for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-aurora) or [Maintenance actions for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-rds).
Type: String
Required: No

 ** AutoAppliedAfterDate **
The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date.
Type: Timestamp
Required: No

 ** CurrentApplyDate **
The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the `ApplyPendingMaintenanceAction` API, the `AutoAppliedAfterDate`, and the `ForcedApplyDate`. This value is blank if an opt-in request has not been received and nothing has been specified as `AutoAppliedAfterDate` or `ForcedApplyDate`.
Type: Timestamp
Required: No

 ** Description **
A description providing more detail about the maintenance action.
Type: String
Required: No

 ** ForcedApplyDate **
The date when the maintenance action is automatically applied.
On this date, the maintenance action is applied to the resource as soon as possible, regardless of the maintenance window for the resource. There might be a delay of one or more days from this date before the maintenance action is applied.
Type: Timestamp
Required: No

 ** OptInStatus **
Indicates the type of opt-in request that has been received for the resource.
Type: String
Required: No

## See Also
<a name="API_PendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PendingMaintenanceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PendingMaintenanceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PendingMaintenanceAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
