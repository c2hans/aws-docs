---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingRecoveryPointSelection.html
---

# RestoreTestingRecoveryPointSelection
<a name="API_RestoreTestingRecoveryPointSelection"></a>

 `RecoveryPointSelection` has five parameters (three required and two optional). The values you specify determine which recovery point is included in the restore test. You must indicate with `Algorithm` if you want the latest recovery point within your `SelectionWindowDays` or if you want a random recovery point, and you must indicate through `IncludeVaults` from which vaults the recovery points can be chosen.

 `Algorithm` (*required*) Valid values: "`LATEST_WITHIN_WINDOW`" or "`RANDOM_WITHIN_WINDOW`".

 `Recovery point types` (*required*) Valid values: "`SNAPSHOT`" and/or "`CONTINUOUS`". Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm`.

 `IncludeVaults` (*required*). You must include one or more backup vaults. Use the wildcard ["\*"] or specific ARNs.

 `SelectionWindowDays` (*optional*) Value must be an integer (in days) from 1 to 365. If not included, the value defaults to `30`.

 `ExcludeVaults` (*optional*). You can choose to input one or more specific backup vault ARNs to exclude those vaults' contents from restore eligibility. Or, you can include a list of selectors. If this parameter and its value are not included, it defaults to empty list.

## Contents
<a name="API_RestoreTestingRecoveryPointSelection_Contents"></a>

 ** Algorithm **   <a name="Backup-Type-RestoreTestingRecoveryPointSelection-Algorithm"></a>
Acceptable values include "LATEST\_WITHIN\_WINDOW" or "RANDOM\_WITHIN\_WINDOW"
Type: String
Valid Values: `LATEST_WITHIN_WINDOW | RANDOM_WITHIN_WINDOW`
Required: No

 ** ExcludeVaults **   <a name="Backup-Type-RestoreTestingRecoveryPointSelection-ExcludeVaults"></a>
Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.
Type: Array of strings
Required: No

 ** IncludeVaults **   <a name="Backup-Type-RestoreTestingRecoveryPointSelection-IncludeVaults"></a>
Accepted values include wildcard ["\*"] or by specific ARNs or ARN wilcard replacement ["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...] ["arn:aws:backup:\*:\*:backup-vault:asdf-\*", ...]
Type: Array of strings
Required: No

 ** RecoveryPointTypes **   <a name="Backup-Type-RestoreTestingRecoveryPointSelection-RecoveryPointTypes"></a>
These are the types of recovery points.
Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm`.
Type: Array of strings
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

 ** SelectionWindowDays **   <a name="Backup-Type-RestoreTestingRecoveryPointSelection-SelectionWindowDays"></a>
Accepted values are integers from 1 to 365. If not included, the value defaults to 30. The selection window is calculated from the actual job execution time, not the plan's scheduled start time.
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingRecoveryPointSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingRecoveryPointSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingRecoveryPointSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingRecoveryPointSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
