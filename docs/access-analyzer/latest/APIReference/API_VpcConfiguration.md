---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The proposed virtual private cloud (VPC) configuration for the Amazon S3 access point. VPC configuration does not apply to multi-region access points. For more information, see [VpcConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_VpcConfiguration.html).

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** vpcId **   <a name="accessanalyzer-Type-VpcConfiguration-vpcId"></a>
 If this field is specified, this access point will only allow connections from the specified VPC ID.
Type: String
Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/VpcConfiguration)
