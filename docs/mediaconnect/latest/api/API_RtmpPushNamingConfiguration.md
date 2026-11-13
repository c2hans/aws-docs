---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpPushNamingConfiguration.html
---

# RtmpPushNamingConfiguration
<a name="API_RtmpPushNamingConfiguration"></a>

The configuration settings for the RTMP (Real-Time Messaging Protocol) application and stream names.

## Contents
<a name="API_RtmpPushNamingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** automatic **   <a name="mediaconnect-Type-RtmpPushNamingConfiguration-automatic"></a>
The naming configuration where MediaConnect generates the application and stream names.
Type: [AutomaticRtmpPushNamingConfiguration](API_AutomaticRtmpPushNamingConfiguration.md) object
Required: No

 ** manual **   <a name="mediaconnect-Type-RtmpPushNamingConfiguration-manual"></a>
The naming configuration where you specify the application and stream names.
Type: [ManualRtmpPushNamingConfiguration](API_ManualRtmpPushNamingConfiguration.md) object
Required: No

## See Also
<a name="API_RtmpPushNamingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpPushNamingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpPushNamingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpPushNamingConfiguration)
