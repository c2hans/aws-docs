---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_LegalHold.html
---

# LegalHold
<a name="API_LegalHold"></a>

A legal hold is an administrative tool that helps prevent backups from being deleted while under a hold. While the hold is in place, backups under a hold cannot be deleted and lifecycle policies that would alter the backup status (such as transition to cold storage) are delayed until the legal hold is removed. A backup can have more than one legal hold. Legal holds are applied to one or more backups (also known as recovery points). These backups can be filtered by resource types and by resource IDs.

## Contents
<a name="API_LegalHold_Contents"></a>

 ** CancellationDate **   <a name="Backup-Type-LegalHold-CancellationDate"></a>
The time when the legal hold was cancelled.
Type: Timestamp
Required: No

 ** CreationDate **   <a name="Backup-Type-LegalHold-CreationDate"></a>
The time when the legal hold was created.
Type: Timestamp
Required: No

 ** Description **   <a name="Backup-Type-LegalHold-Description"></a>
The description of a legal hold.
Type: String
Required: No

 ** LegalHoldArn **   <a name="Backup-Type-LegalHold-LegalHoldArn"></a>
The Amazon Resource Name (ARN) of the legal hold; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: No

 ** LegalHoldId **   <a name="Backup-Type-LegalHold-LegalHoldId"></a>
The ID of the legal hold.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-LegalHold-Status"></a>
The status of the legal hold.
Type: String
Valid Values: `CREATING | ACTIVE | CANCELING | CANCELED`
Required: No

 ** Title **   <a name="Backup-Type-LegalHold-Title"></a>
The title of a legal hold.
Type: String
Required: No

## See Also
<a name="API_LegalHold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/LegalHold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/LegalHold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/LegalHold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
