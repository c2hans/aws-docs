---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_Checksum.html
---

# Checksum
<a name="API_edge_Checksum"></a>

Information about the checksum of a model deployed on a device.

## Contents
<a name="API_edge_Checksum_Contents"></a>

 ** Sum **   <a name="sagemaker-Type-edge_Checksum-Sum"></a>
The checksum of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: No

 ** Type **   <a name="sagemaker-Type-edge_Checksum-Type"></a>
The type of the checksum.
Type: String
Valid Values: `SHA1`
Required: No

## See Also
<a name="API_edge_Checksum_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-edge-2020-09-23/Checksum)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-edge-2020-09-23/Checksum)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-edge-2020-09-23/Checksum)
