---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ParentInstanceConfiguration.html
---

# ParentInstanceConfiguration
<a name="API_ParentInstanceConfiguration"></a>

Settings for building on an instance that is already running, instead of an instance that Image Builder launches for the build.

## Contents
<a name="API_ParentInstanceConfiguration_Contents"></a>

 ** autoScalingGroup **   <a name="imagebuilder-Type-ParentInstanceConfiguration-autoScalingGroup"></a>
The Amazon EC2 Auto Scaling group that Image Builder takes the build instance from. This is required when you specify `parentInstance`.
Type: [AutoScalingGroupConfiguration](API_AutoScalingGroupConfiguration.md) object
Required: Yes

## See Also
<a name="API_ParentInstanceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ParentInstanceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ParentInstanceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ParentInstanceConfiguration)
