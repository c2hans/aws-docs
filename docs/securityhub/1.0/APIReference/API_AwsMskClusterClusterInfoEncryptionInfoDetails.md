---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterClusterInfoEncryptionInfoDetails.html
---

# AwsMskClusterClusterInfoEncryptionInfoDetails
<a name="API_AwsMskClusterClusterInfoEncryptionInfoDetails"></a>

 Includes encryption-related information, such as the AWS KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

## Contents
<a name="API_AwsMskClusterClusterInfoEncryptionInfoDetails_Contents"></a>

 ** EncryptionAtRest **   <a name="securityhub-Type-AwsMskClusterClusterInfoEncryptionInfoDetails-EncryptionAtRest"></a>
 The data-volume encryption details. You can't update encryption at rest settings for existing clusters.
Type: [AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails](API_AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails.md) object
Required: No

 ** EncryptionInTransit **   <a name="securityhub-Type-AwsMskClusterClusterInfoEncryptionInfoDetails-EncryptionInTransit"></a>
 The settings for encrypting data in transit.
Type: [AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails](API_AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails.md) object
Required: No

## See Also
<a name="API_AwsMskClusterClusterInfoEncryptionInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoDetails)
