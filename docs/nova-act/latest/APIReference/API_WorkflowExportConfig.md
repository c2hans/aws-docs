---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_WorkflowExportConfig.html
---

# WorkflowExportConfig
<a name="API_WorkflowExportConfig"></a>

Configuration settings for exporting workflow execution data and logs to Amazon Simple Storage Service (Amazon S3).

## Contents
<a name="API_WorkflowExportConfig_Contents"></a>

 ** s3BucketName **   <a name="novaact-Type-WorkflowExportConfig-s3BucketName"></a>
The name of your Amazon S3 bucket, that Nova Act uses to export your workflow data. Note that the IAM role used to access Nova Act must also have write permissions to this bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: Yes

 ** s3KeyPrefix **   <a name="novaact-Type-WorkflowExportConfig-s3KeyPrefix"></a>
An optional prefix for Amazon S3 object keys to organize exported data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9!\-_.*'()]+(?:/[a-zA-Z0-9!\-_.*'()]+)*`
Required: No

## See Also
<a name="API_WorkflowExportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/WorkflowExportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/WorkflowExportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/WorkflowExportConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
