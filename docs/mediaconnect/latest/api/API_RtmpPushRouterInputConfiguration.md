---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpPushRouterInputConfiguration.html
---

# RtmpPushRouterInputConfiguration
<a name="API_RtmpPushRouterInputConfiguration"></a>

The configuration settings for a router input using the RTMP (Real-Time Messaging Protocol) protocol.

## Contents
<a name="API_RtmpPushRouterInputConfiguration_Contents"></a>

 ** namingConfiguration **   <a name="mediaconnect-Type-RtmpPushRouterInputConfiguration-namingConfiguration"></a>
The configuration settings for the application and stream names.
Type: [RtmpPushNamingConfiguration](API_RtmpPushNamingConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** port **   <a name="mediaconnect-Type-RtmpPushRouterInputConfiguration-port"></a>
The port number for the RTMP protocol. The only valid value is `1935`.
Type: Integer
Valid Range: Fixed value of 1935.
Required: Yes

 ** namingType **   <a name="mediaconnect-Type-RtmpPushRouterInputConfiguration-namingType"></a>
The naming type. If you specify it, it must match the naming configuration.
Type: String
Valid Values: `MANUAL | AUTOMATIC`
Required: No

## See Also
<a name="API_RtmpPushRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpPushRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpPushRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpPushRouterInputConfiguration)
