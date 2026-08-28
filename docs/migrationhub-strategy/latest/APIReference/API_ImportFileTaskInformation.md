---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ImportFileTaskInformation.html
---

# ImportFileTaskInformation
<a name="API_ImportFileTaskInformation"></a>

 Information about the import file tasks you request.

## Contents
<a name="API_ImportFileTaskInformation_Contents"></a>

 ** completionTime **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-completionTime"></a>
 The time that the import task completes.
Type: Timestamp
Required: No

 ** id **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-id"></a>
 The ID of the import file task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** importName **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-importName"></a>
 The name of the import task given in `StartImportFileTask`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** inputS3Bucket **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-inputS3Bucket"></a>
 The S3 bucket where the import file is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`
Required: No

 ** inputS3Key **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-inputS3Key"></a>
 The Amazon S3 key name of the import file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** numberOfRecordsFailed **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-numberOfRecordsFailed"></a>
 The number of records that failed to be imported.
Type: Integer
Required: No

 ** numberOfRecordsSuccess **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-numberOfRecordsSuccess"></a>
 The number of records successfully imported.
Type: Integer
Required: No

 ** startTime **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-startTime"></a>
 Start time of the import task.
Type: Timestamp
Required: No

 ** status **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-status"></a>
 Status of import file task.
Type: String
Valid Values: `ImportInProgress | ImportFailed | ImportPartialSuccess | ImportSuccess | DeleteInProgress | DeleteFailed | DeletePartialSuccess | DeleteSuccess`
Required: No

 ** statusReportS3Bucket **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-statusReportS3Bucket"></a>
 The S3 bucket name for status report of import task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`
Required: No

 ** statusReportS3Key **   <a name="migrationhubstrategy-Type-ImportFileTaskInformation-statusReportS3Key"></a>
 The Amazon S3 key name for status report of import task. The report contains details about whether each record imported successfully or why it did not.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ImportFileTaskInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ImportFileTaskInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ImportFileTaskInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ImportFileTaskInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
