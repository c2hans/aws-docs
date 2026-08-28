---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_SequenceStoreS3Access.html
---

# SequenceStoreS3Access
<a name="API_SequenceStoreS3Access"></a>

The S3 access metadata of the sequence store.

## Contents
<a name="API_SequenceStoreS3Access_Contents"></a>

 ** accessLogLocation **   <a name="omics-Type-SequenceStoreS3Access-accessLogLocation"></a>
Location of the access logs.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,800})/)?`
Required: No

 ** s3AccessPointArn **   <a name="omics-Type-SequenceStoreS3Access-s3AccessPointArn"></a>
This is ARN of the access point associated with the S3 bucket storing read sets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`
Required: No

 ** s3Uri **   <a name="omics-Type-SequenceStoreS3Access-s3Uri"></a>
The S3 URI of the sequence store.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})`
Required: No

## See Also
<a name="API_SequenceStoreS3Access_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/SequenceStoreS3Access)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/SequenceStoreS3Access)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/SequenceStoreS3Access)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
