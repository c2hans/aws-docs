---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ImportDataRule.html
---

# ImportDataRule
<a name="API_S3Files_ImportDataRule"></a>

Specifies a rule that controls how data is imported from S3 into the file system.

## Contents
<a name="API_S3Files_ImportDataRule_Contents"></a>

 ** prefix **   <a name="AmazonS3-Type-S3Files_ImportDataRule-prefix"></a>
The S3 key prefix that scopes this import rule. Only objects with keys beginning with this prefix are subject to the rule.
Type: String
Pattern: `(|.*/)`
Required: Yes

 ** sizeLessThan **   <a name="AmazonS3-Type-S3Files_ImportDataRule-sizeLessThan"></a>
The upper size limit in bytes for this import rule. Only objects with a size strictly less than this value will have data imported into the file system.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 52673613135872.
Required: Yes

 ** trigger **   <a name="AmazonS3-Type-S3Files_ImportDataRule-trigger"></a>
The event that triggers data import. Valid values are `ON_DIRECTORY_FIRST_ACCESS` (import when a directory is first accessed) and `ON_FILE_ACCESS` (import when a file is accessed).
Type: String
Valid Values: `ON_DIRECTORY_FIRST_ACCESS | ON_FILE_ACCESS`
Required: Yes

## See Also
<a name="API_S3Files_ImportDataRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ImportDataRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ImportDataRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ImportDataRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
