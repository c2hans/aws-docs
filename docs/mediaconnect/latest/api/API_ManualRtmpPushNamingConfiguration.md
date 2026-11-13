---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ManualRtmpPushNamingConfiguration.html
---

# ManualRtmpPushNamingConfiguration
<a name="API_ManualRtmpPushNamingConfiguration"></a>

The manual RTMP naming configuration, where you specify the application and stream names.

## Contents
<a name="API_ManualRtmpPushNamingConfiguration_Contents"></a>

 ** applicationName **   <a name="mediaconnect-Type-ManualRtmpPushNamingConfiguration-applicationName"></a>
The name of the RTMP application. Together with the stream name, the application name forms the RTMP URL path, in the pattern `rtmp://ingestAddress/applicationName/streamName`.
Type: String
Required: Yes

 ** streamName **   <a name="mediaconnect-Type-ManualRtmpPushNamingConfiguration-streamName"></a>
The name of the RTMP stream. The stream name forms the final segment of the RTMP URL path.
Type: String
Required: Yes

## See Also
<a name="API_ManualRtmpPushNamingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ManualRtmpPushNamingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ManualRtmpPushNamingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ManualRtmpPushNamingConfiguration)
