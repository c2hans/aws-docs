---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_BlockPublicAccess.html
---

# BlockPublicAccess
<a name="API_BlockPublicAccess"></a>

Contains information on how the bucker owner's S3 Block Public Access settings are being applied to the S3 bucket. See [S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html) for more information.

## Contents
<a name="API_BlockPublicAccess_Contents"></a>

 ** blockPublicAcls **   <a name="guardduty-Type-BlockPublicAccess-blockPublicAcls"></a>
Indicates if S3 Block Public Access is set to `BlockPublicAcls`.
Type: Boolean
Required: No

 ** blockPublicPolicy **   <a name="guardduty-Type-BlockPublicAccess-blockPublicPolicy"></a>
Indicates if S3 Block Public Access is set to `BlockPublicPolicy`.
Type: Boolean
Required: No

 ** ignorePublicAcls **   <a name="guardduty-Type-BlockPublicAccess-ignorePublicAcls"></a>
Indicates if S3 Block Public Access is set to `IgnorePublicAcls`.
Type: Boolean
Required: No

 ** restrictPublicBuckets **   <a name="guardduty-Type-BlockPublicAccess-restrictPublicBuckets"></a>
Indicates if S3 Block Public Access is set to `RestrictPublicBuckets`.
Type: Boolean
Required: No

## See Also
<a name="API_BlockPublicAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/BlockPublicAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/BlockPublicAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/BlockPublicAccess)
