---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DestinationProperties.html
---

# DestinationProperties
<a name="API_DestinationProperties"></a>

Contains the Amazon Resource Name (ARN) of the resource to publish to, such as an S3 bucket, and the ARN of the KMS key to use to encrypt published findings.

## Contents
<a name="API_DestinationProperties_Contents"></a>

 ** destinationArn **   <a name="guardduty-Type-DestinationProperties-destinationArn"></a>
The ARN of the resource to publish to.
To specify an S3 bucket folder use the following format: `arn:aws:s3:::DOC-EXAMPLE-BUCKET/myFolder/`
Type: String
Required: No

 ** expectedBucketOwner **   <a name="guardduty-Type-DestinationProperties-expectedBucketOwner"></a>
The 12-digit AWS account ID of the account that owns the Amazon S3 bucket specified in the `DestinationArn` parameter.
When you provide this value, GuardDuty verifies that the specified account owns the bucket before it exports findings. If the account ID doesn't match the actual owner of the bucket, GuardDuty doesn't export findings to that bucket. This helps prevent GuardDuty from exporting your findings to a bucket that a different AWS account owns (for example, if the original bucket was deleted and its name was later claimed by another account). If you don't specify this value, GuardDuty doesn't perform this verification. GuardDuty strongly recommends that you provide the expected bucket owner when possible.
When you update a publishing destination, omitting this field leaves the currently stored value unchanged. This field appears in the response only if it was provided when the publishing destination was created or updated.
For more information, see [Verifying the Amazon S3 bucket owner](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html#guardduty-exportfindings-expected-bucket-owner) in the *Amazon GuardDuty User Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** kmsKeyArn **   <a name="guardduty-Type-DestinationProperties-kmsKeyArn"></a>
The ARN of the KMS key to use for encryption.
Type: String
Required: No

## See Also
<a name="API_DestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DestinationProperties)
