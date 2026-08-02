---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateConfig.html
---

# LaunchTemplateConfig
<a name="API_LaunchTemplateConfig"></a>

Describes a launch template and overrides.

## Contents
<a name="API_LaunchTemplateConfig_Contents"></a>

 ** LaunchTemplateSpecification ** (request), ** launchTemplateSpecification ** (response)
The launch template to use. Make sure that the launch template does not contain the `NetworkInterfaceId` parameter because you can't specify a network interface ID in a Spot Fleet.
Type: [FleetLaunchTemplateSpecification](API_FleetLaunchTemplateSpecification.md) object
Required: No

 ** Overrides.N **
Any parameters that you specify override the same parameters in the launch template.
Type: Array of [LaunchTemplateOverrides](API_LaunchTemplateOverrides.md) objects
Required: No

## See Also
<a name="API_LaunchTemplateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateConfig)
