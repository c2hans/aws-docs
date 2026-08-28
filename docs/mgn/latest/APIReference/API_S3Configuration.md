---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

Configuration for an S3 location.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** s3Bucket **   <a name="mgn-Type-S3Configuration-s3Bucket"></a>
The name of the S3 bucket.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: No

 ** s3BucketOwner **   <a name="mgn-Type-S3Configuration-s3BucketOwner"></a>
The AWS account ID of the S3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** s3Key **   <a name="mgn-Type-S3Configuration-s3Key"></a>
The S3 key (path) for the object.
Type: String
Pattern: `[^\x00]{1,1024}`
Required: No

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/S3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
