---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScanJobCreator.html
---

# ScanJobCreator
<a name="API_ScanJobCreator"></a>

Contains identifying information about the creation of a scan job, including the backup plan and rule that initiated the scan.

## Contents
<a name="API_ScanJobCreator_Contents"></a>

 ** BackupPlanArn **   <a name="Backup-Type-ScanJobCreator-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.
Type: String
Required: Yes

 ** BackupPlanId **   <a name="Backup-Type-ScanJobCreator-BackupPlanId"></a>
The ID of the backup plan.
Type: String
Required: Yes

 ** BackupPlanVersion **   <a name="Backup-Type-ScanJobCreator-BackupPlanVersion"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
Type: String
Required: Yes

 ** BackupRuleId **   <a name="Backup-Type-ScanJobCreator-BackupRuleId"></a>
Uniquely identifies the backup rule that initiated the scan job.
Type: String
Required: Yes

## See Also
<a name="API_ScanJobCreator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScanJobCreator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScanJobCreator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScanJobCreator)
