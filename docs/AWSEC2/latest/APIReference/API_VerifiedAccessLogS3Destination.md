---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessLogS3Destination.html
---

# VerifiedAccessLogS3Destination
<a name="API_VerifiedAccessLogS3Destination"></a>

Options for Amazon S3 as a logging destination.

## Contents
<a name="API_VerifiedAccessLogS3Destination_Contents"></a>

 ** bucketName **
The bucket name.
Type: String
Required: No

 ** bucketOwner **
The AWS account number that owns the bucket.
Type: String
Required: No

 ** deliveryStatus **
The delivery status.
Type: [VerifiedAccessLogDeliveryStatus](API_VerifiedAccessLogDeliveryStatus.md) object
Required: No

 ** enabled **
Indicates whether logging is enabled.
Type: Boolean
Required: No

 ** prefix **
The bucket prefix.
Type: String
Required: No

## See Also
<a name="API_VerifiedAccessLogS3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessLogS3Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessLogS3Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessLogS3Destination)
