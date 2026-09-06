---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_TargetS3ConfigurationUpdate.html
---

# TargetS3ConfigurationUpdate
<a name="API_TargetS3ConfigurationUpdate"></a>

Updated S3 configuration for storing target network artifacts.

## Contents
<a name="API_TargetS3ConfigurationUpdate_Contents"></a>

 ** s3Bucket **   <a name="mgn-Type-TargetS3ConfigurationUpdate-s3Bucket"></a>
The updated name of the S3 bucket.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: No

 ** s3BucketOwner **   <a name="mgn-Type-TargetS3ConfigurationUpdate-s3BucketOwner"></a>
The updated AWS account ID of the S3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

## See Also
<a name="API_TargetS3ConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/TargetS3ConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/TargetS3ConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/TargetS3ConfigurationUpdate)
