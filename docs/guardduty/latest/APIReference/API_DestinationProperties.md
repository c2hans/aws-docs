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
