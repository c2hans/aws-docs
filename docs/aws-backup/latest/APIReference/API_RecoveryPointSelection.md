---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RecoveryPointSelection.html
---

# RecoveryPointSelection
<a name="API_RecoveryPointSelection"></a>

This specifies criteria to assign a set of resources, such as resource types or backup vaults.

## Contents
<a name="API_RecoveryPointSelection_Contents"></a>

 ** DateRange **   <a name="Backup-Type-RecoveryPointSelection-DateRange"></a>
This is a resource filter containing FromDate: DateTime and ToDate: DateTime. Both values are required. Future DateTime values are not permitted.
The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds ((milliseconds are optional). For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: [DateRange](API_DateRange.md) object
Required: No

 ** ResourceIdentifiers **   <a name="Backup-Type-RecoveryPointSelection-ResourceIdentifiers"></a>
These are the resources included in the resource selection (including type of resources and vaults).
Type: Array of strings
Required: No

 ** VaultNames **   <a name="Backup-Type-RecoveryPointSelection-VaultNames"></a>
These are the names of the vaults in which the selected recovery points are contained.
Type: Array of strings
Required: No

## See Also
<a name="API_RecoveryPointSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RecoveryPointSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
