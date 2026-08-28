---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisLogExportS3OutputConfiguration.html
---

# AnalysisLogExportS3OutputConfiguration
<a name="API_AnalysisLogExportS3OutputConfiguration"></a>

Contains output information for an analysis log export with an S3 output type.

The exported logs are written under the bucket and key prefix that you specify. The path includes the collaboration ID, the protected query ID, and the analysis log export ID. Because the path includes the export ID, exporting the same query more than once doesn't overwrite the logs from an earlier export.

**Note**
The exported logs are encrypted using the default encryption configuration of the destination bucket. AWS Clean Rooms doesn't accept a KMS key for log export. To encrypt the exported logs with a customer managed key, configure the bucket's default encryption to use that key before you export.

## Contents
<a name="API_AnalysisLogExportS3OutputConfiguration_Contents"></a>

 ** bucket **   <a name="API-Type-AnalysisLogExportS3OutputConfiguration-bucket"></a>
The S3 bucket that the exported analysis logs are written to. The bucket must be in the same AWS Region as the collaboration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** keyPrefix **   <a name="API-Type-AnalysisLogExportS3OutputConfiguration-keyPrefix"></a>
The S3 key prefix under which the exported analysis logs are written.
Only one export can be in progress at a time for a given query and destination. To export the same query twice at once, use a different key prefix for the second export.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\w!.=*/-]*`
Required: No

## See Also
<a name="API_AnalysisLogExportS3OutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisLogExportS3OutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisLogExportS3OutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisLogExportS3OutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
