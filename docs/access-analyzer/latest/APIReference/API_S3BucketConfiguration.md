---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_S3BucketConfiguration.html
---

# S3BucketConfiguration
<a name="API_S3BucketConfiguration"></a>

Proposed access control configuration for an Amazon S3 bucket. You can propose a configuration for a new Amazon S3 bucket or an existing Amazon S3 bucket that you own by specifying the Amazon S3 bucket policy, bucket ACLs, bucket BPA settings, Amazon S3 access points, and multi-region access points attached to the bucket. If the configuration is for an existing Amazon S3 bucket and you do not specify the Amazon S3 bucket policy, the access preview uses the existing policy attached to the bucket. If the access preview is for a new resource and you do not specify the Amazon S3 bucket policy, the access preview assumes a bucket without a policy. To propose deletion of an existing bucket policy, you can specify an empty string. For more information about bucket policy limits, see [Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html).

## Contents
<a name="API_S3BucketConfiguration_Contents"></a>

 ** accessPoints **   <a name="accessanalyzer-Type-S3BucketConfiguration-accessPoints"></a>
The configuration of Amazon S3 access points or multi-region access points for the bucket. You can propose up to 10 new access points per bucket.
Type: String to [S3AccessPointConfiguration](API_S3AccessPointConfiguration.md) object map
Key Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`
Required: No

 ** bucketAclGrants **   <a name="accessanalyzer-Type-S3BucketConfiguration-bucketAclGrants"></a>
The proposed list of ACL grants for the Amazon S3 bucket. You can propose up to 100 ACL grants per bucket. If the proposed grant configuration is for an existing bucket, the access preview uses the proposed list of grant configurations in place of the existing grants. Otherwise, the access preview uses the existing grants for the bucket.
Type: Array of [S3BucketAclGrantConfiguration](API_S3BucketAclGrantConfiguration.md) objects
Required: No

 ** bucketPolicy **   <a name="accessanalyzer-Type-S3BucketConfiguration-bucketPolicy"></a>
The proposed bucket policy for the Amazon S3 bucket.
Type: String
Required: No

 ** bucketPublicAccessBlock **   <a name="accessanalyzer-Type-S3BucketConfiguration-bucketPublicAccessBlock"></a>
The proposed block public access configuration for the Amazon S3 bucket.
Type: [S3PublicAccessBlockConfiguration](API_S3PublicAccessBlockConfiguration.md) object
Required: No

## See Also
<a name="API_S3BucketConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/S3BucketConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/S3BucketConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/S3BucketConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
