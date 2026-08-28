---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_RegionalBucket.html
---

# RegionalBucket
<a name="API_control_RegionalBucket"></a>

The container for the regional bucket.

## Contents
<a name="API_control_RegionalBucket_Contents"></a>

 ** Bucket **   <a name="AmazonS3-Type-control_RegionalBucket-Bucket"></a>

Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** CreationDate **   <a name="AmazonS3-Type-control_RegionalBucket-CreationDate"></a>
The creation date of the regional bucket
Type: Timestamp
Required: Yes

 ** PublicAccessBlockEnabled **   <a name="AmazonS3-Type-control_RegionalBucket-PublicAccessBlockEnabled"></a>

Type: Boolean
Required: Yes

 ** BucketArn **   <a name="AmazonS3-Type-control_RegionalBucket-BucketArn"></a>
The Amazon Resource Name (ARN) for the regional bucket.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.
Required: No

 ** OutpostId **   <a name="AmazonS3-Type-control_RegionalBucket-OutpostId"></a>
The AWS Outposts ID of the regional bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_control_RegionalBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/RegionalBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/RegionalBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/RegionalBucket)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
