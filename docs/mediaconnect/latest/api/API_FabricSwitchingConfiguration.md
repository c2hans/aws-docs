---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FabricSwitchingConfiguration.html
---

# FabricSwitchingConfiguration
<a name="API_FabricSwitchingConfiguration"></a>

The configuration settings for switching between router inputs.

## Contents
<a name="API_FabricSwitchingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** immediate **   <a name="mediaconnect-Type-FabricSwitchingConfiguration-immediate"></a>
The switching configuration where the router output switches to the new router input immediately.
Type: [ImmediateFabricSwitchingConfiguration](API_ImmediateFabricSwitchingConfiguration.md) object
Required: No

 ** keyFrame **   <a name="mediaconnect-Type-FabricSwitchingConfiguration-keyFrame"></a>
The switching configuration where the router output waits for a key frame on the new router input before it switches.
Type: [KeyFrameFabricSwitchingConfiguration](API_KeyFrameFabricSwitchingConfiguration.md) object
Required: No

## See Also
<a name="API_FabricSwitchingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FabricSwitchingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FabricSwitchingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FabricSwitchingConfiguration)
