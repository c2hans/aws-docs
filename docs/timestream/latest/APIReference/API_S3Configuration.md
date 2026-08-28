---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

The configuration that specifies an S3 location.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** BucketName **   <a name="timestream-Type-S3Configuration-BucketName"></a>
The bucket name of the customer S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: No

 ** EncryptionOption **   <a name="timestream-Type-S3Configuration-EncryptionOption"></a>
The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key or AWS managed key.
Type: String
Valid Values: `SSE_S3 | SSE_KMS`
Required: No

 ** KmsKeyId **   <a name="timestream-Type-S3Configuration-KmsKeyId"></a>
The AWS KMS key ID for the customer S3 location when encrypting with an AWS managed key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ObjectKeyPrefix **   <a name="timestream-Type-S3Configuration-ObjectKeyPrefix"></a>
The object key preview for the customer S3 location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 928.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: No

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/S3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
