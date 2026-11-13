---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpPushSourceSettings.html
---

# RtmpPushSourceSettings
<a name="API_RtmpPushSourceSettings"></a>

The settings for the RTMP (Real-Time Messaging Protocol) source.

## Contents
<a name="API_RtmpPushSourceSettings_Contents"></a>

 ** applicationName **   <a name="mediaconnect-Type-RtmpPushSourceSettings-applicationName"></a>
The name of the RTMP application. Together with the stream name, the application name forms the RTMP URL path, in the pattern `rtmp://ingestAddress/applicationName/streamName`.
Type: String
Required: Yes

 ** namingType **   <a name="mediaconnect-Type-RtmpPushSourceSettings-namingType"></a>
The naming type that the source uses. With `AUTOMATIC` naming, MediaConnect generates the application and stream names.
Type: String
Valid Values: `MANUAL | AUTOMATIC`
Required: Yes

 ** streamName **   <a name="mediaconnect-Type-RtmpPushSourceSettings-streamName"></a>
The name of the RTMP stream. The stream name forms the final segment of the RTMP URL path.
Type: String
Required: Yes

## See Also
<a name="API_RtmpPushSourceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpPushSourceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpPushSourceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpPushSourceSettings)
