---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails.html
---

# AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails"></a>

 The data-volume encryption details. You can't update encryption at rest settings for existing clusters.

## Contents
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails_Contents"></a>

 ** DataVolumeKMSKeyId **   <a name="securityhub-Type-AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails-DataVolumeKMSKeyId"></a>
 The Amazon Resource Name (ARN) of the AWS KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails)
