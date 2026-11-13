---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_KeyFrameFabricSwitchingConfiguration.html
---

# KeyFrameFabricSwitchingConfiguration
<a name="API_KeyFrameFabricSwitchingConfiguration"></a>

The switching configuration where the router output waits for a key frame on the new router input before it switches.

## Contents
<a name="API_KeyFrameFabricSwitchingConfiguration_Contents"></a>

 ** keyFrameWaitMilliseconds **   <a name="mediaconnect-Type-KeyFrameFabricSwitchingConfiguration-keyFrameWaitMilliseconds"></a>
The maximum time, in milliseconds, that the router output waits for a key frame on the new input before it switches. Set this value to at least the GOP (Group of Pictures) duration of your content, which your upstream encoder determines. If the wait time is shorter than the GOP duration, MediaConnect makes a best effort to switch without a key frame. The default is 3000.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

## See Also
<a name="API_KeyFrameFabricSwitchingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/KeyFrameFabricSwitchingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/KeyFrameFabricSwitchingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/KeyFrameFabricSwitchingConfiguration)
