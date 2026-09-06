---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_EbsConfiguration.html
---

# EbsConfiguration
<a name="API_EbsConfiguration"></a>

The Amazon EBS configuration of a cluster instance.

## Contents
<a name="API_EbsConfiguration_Contents"></a>

 ** EbsBlockDeviceConfigs **   <a name="EMR-Type-EbsConfiguration-EbsBlockDeviceConfigs"></a>
An array of Amazon EBS volume specifications attached to a cluster instance.
Type: Array of [EbsBlockDeviceConfig](API_EbsBlockDeviceConfig.md) objects
Required: No

 ** EbsOptimized **   <a name="EMR-Type-EbsConfiguration-EbsOptimized"></a>
Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.
Type: Boolean
Required: No

## See Also
<a name="API_EbsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/EbsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/EbsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/EbsConfiguration)
