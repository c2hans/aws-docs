---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpPushOutputSettings.html
---

# RtmpPushOutputSettings
<a name="API_RtmpPushOutputSettings"></a>

The settings for an output that pushes a stream to a destination using the RTMP (Real-Time Messaging Protocol) protocol, or RTMPS (RTMP over TLS) when TLS encryption is specified. These settings include the application and stream names, and optional TLS encryption configuration.

## Contents
<a name="API_RtmpPushOutputSettings_Contents"></a>

 ** applicationName **   <a name="mediaconnect-Type-RtmpPushOutputSettings-applicationName"></a>
The name of the RTMP application on the destination server. Together with the stream name, the application name forms the RTMP URL path, in the pattern `rtmp://destinationAddress/applicationName/streamName`.
Type: String
Required: Yes

 ** streamName **   <a name="mediaconnect-Type-RtmpPushOutputSettings-streamName"></a>
The name of the RTMP stream that the output publishes to the destination application. The stream name forms the final segment of the RTMP URL path.
Type: String
Required: Yes

 ** tlsEncryption **   <a name="mediaconnect-Type-RtmpPushOutputSettings-tlsEncryption"></a>
The TLS encryption settings for the output. When you specify these settings, the output uses RTMPS (RTMP over TLS) to establish a secure, encrypted connection to the destination server.
Type: [TlsEncryption](API_TlsEncryption.md) object
Required: No

## See Also
<a name="API_RtmpPushOutputSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpPushOutputSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpPushOutputSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpPushOutputSettings)
