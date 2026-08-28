---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Bucket.html
---

# Bucket
<a name="API_Bucket"></a>

 In terms of implementation, a Bucket is a resource.

## Contents
<a name="API_Bucket_Contents"></a>

 ** BucketArn **   <a name="AmazonS3-Type-Bucket-BucketArn"></a>
The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify AWS resources across all of AWS.
This parameter is only supported for S3 directory buckets. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[^:]+:(s3|s3express):.*`
Required: No

 ** BucketRegion **   <a name="AmazonS3-Type-Bucket-BucketRegion"></a>
 `BucketRegion` indicates the AWS region where the bucket is located. If the request contains at least one valid parameter, it is included in the response.
Type: String
Required: No

 ** CreationDate **   <a name="AmazonS3-Type-Bucket-CreationDate"></a>
Date the bucket was created. This date can change when making changes to your bucket, such as editing its bucket policy.
Type: Timestamp
Required: No

 ** Name **   <a name="AmazonS3-Type-Bucket-Name"></a>
The name of the bucket.
Type: String
Required: No

## See Also
<a name="API_Bucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Bucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Bucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Bucket)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
