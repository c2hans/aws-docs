---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_S3BucketSource.html
---

# S3BucketSource
<a name="API_S3BucketSource"></a>

S3 bucket source.

## Contents
<a name="API_S3BucketSource_Contents"></a>

 ** s3Bucket **   <a name="mgn-Type-S3BucketSource-s3Bucket"></a>
S3 bucket source s3 bucket.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: Yes

 ** s3Key **   <a name="mgn-Type-S3BucketSource-s3Key"></a>
S3 bucket source s3 key.
Type: String
Pattern: `[^\x00]{1,1020}\.csv`
Required: Yes

 ** s3BucketOwner **   <a name="mgn-Type-S3BucketSource-s3BucketOwner"></a>
S3 bucket source s3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

## See Also
<a name="API_S3BucketSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/S3BucketSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/S3BucketSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/S3BucketSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
