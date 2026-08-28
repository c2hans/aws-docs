---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ImportTask.html
---

# ImportTask
<a name="API_ImportTask"></a>

Import task.

## Contents
<a name="API_ImportTask_Contents"></a>

 ** arn **   <a name="mgn-Type-ImportTask-arn"></a>
ImportTask arn.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** creationDateTime **   <a name="mgn-Type-ImportTask-creationDateTime"></a>
Import task creation datetime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** endDateTime **   <a name="mgn-Type-ImportTask-endDateTime"></a>
Import task end datetime.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** importID **   <a name="mgn-Type-ImportTask-importID"></a>
Import task id.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `import-[0-9a-zA-Z]{17}`
Required: No

 ** progressPercentage **   <a name="mgn-Type-ImportTask-progressPercentage"></a>
Import task progress percentage.
Type: Float
Required: No

 ** s3BucketSource **   <a name="mgn-Type-ImportTask-s3BucketSource"></a>
Import task s3 bucket source.
Type: [S3BucketSource](API_S3BucketSource.md) object
Required: No

 ** status **   <a name="mgn-Type-ImportTask-status"></a>
Import task status.
Type: String
Valid Values: `PENDING | STARTED | FAILED | SUCCEEDED`
Required: No

 ** summary **   <a name="mgn-Type-ImportTask-summary"></a>
Import task summary.
Type: [ImportTaskSummary](API_ImportTaskSummary.md) object
Required: No

 ** tags **   <a name="mgn-Type-ImportTask-tags"></a>
Import task tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ImportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
