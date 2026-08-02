---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ExportJobSummary.html
---

# ExportJobSummary
<a name="API_BKS_ExportJobSummary"></a>

This is the summary of an export job.

## Contents
<a name="API_BKS_ExportJobSummary_Contents"></a>

 ** ExportJobIdentifier **   <a name="Backup-Type-BKS_ExportJobSummary-ExportJobIdentifier"></a>
This is the unique string that identifies a specific export job.
Type: String
Required: Yes

 ** CompletionTime **   <a name="Backup-Type-BKS_ExportJobSummary-CompletionTime"></a>
This is a timestamp of the time the export job compeleted.
Type: Timestamp
Required: No

 ** CreationTime **   <a name="Backup-Type-BKS_ExportJobSummary-CreationTime"></a>
This is a timestamp of the time the export job was created.
Type: Timestamp
Required: No

 ** ExportJobArn **   <a name="Backup-Type-BKS_ExportJobSummary-ExportJobArn"></a>
This is the unique ARN (Amazon Resource Name) that belongs to the new export job.
Type: String
Required: No

 ** SearchJobArn **   <a name="Backup-Type-BKS_ExportJobSummary-SearchJobArn"></a>
The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-BKS_ExportJobSummary-Status"></a>
The status of the export job is one of the following:
 `CREATED`; `RUNNING`; `FAILED`; or `COMPLETED`.
Type: String
Valid Values: `RUNNING | FAILED | COMPLETED`
Required: No

 ** StatusMessage **   <a name="Backup-Type-BKS_ExportJobSummary-StatusMessage"></a>
A status message is a string that is returned for an export job.
A status message is included for any status other than `COMPLETED` without issues.
Type: String
Required: No

## See Also
<a name="API_BKS_ExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ExportJobSummary)
