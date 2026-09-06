---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceMarketOptions.html
---

# LaunchTemplateInstanceMarketOptions
<a name="API_LaunchTemplateInstanceMarketOptions"></a>

The market (purchasing) option for the instances.

## Contents
<a name="API_LaunchTemplateInstanceMarketOptions_Contents"></a>

 ** marketType **
The market type.
Type: String
Valid Values: `spot | capacity-block | interruptible-capacity-reservation | on-demand`
Required: No

 ** spotOptions **
The options for Spot Instances.
Type: [LaunchTemplateSpotMarketOptions](API_LaunchTemplateSpotMarketOptions.md) object
Required: No

## See Also
<a name="API_LaunchTemplateInstanceMarketOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateInstanceMarketOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateInstanceMarketOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateInstanceMarketOptions)
