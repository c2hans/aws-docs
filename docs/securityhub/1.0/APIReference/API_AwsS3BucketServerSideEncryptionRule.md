---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketServerSideEncryptionRule.html
---

# AwsS3BucketServerSideEncryptionRule
<a name="API_AwsS3BucketServerSideEncryptionRule"></a>

An encryption rule to apply to the S3 bucket.

## Contents
<a name="API_AwsS3BucketServerSideEncryptionRule_Contents"></a>

 ** ApplyServerSideEncryptionByDefault **   <a name="securityhub-Type-AwsS3BucketServerSideEncryptionRule-ApplyServerSideEncryptionByDefault"></a>
Specifies the default server-side encryption to apply to new objects in the bucket. If a `PUT` object request doesn't specify any server-side encryption, this default encryption is applied.
Type: [AwsS3BucketServerSideEncryptionByDefault](API_AwsS3BucketServerSideEncryptionByDefault.md) object
Required: No

## See Also
<a name="API_AwsS3BucketServerSideEncryptionRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
