---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtmpPushRouterOutputConfiguration.html
---

# RtmpPushRouterOutputConfiguration
<a name="API_RtmpPushRouterOutputConfiguration"></a>

The configuration settings for a router output that pushes a stream to a destination using the RTMP (Real-Time Messaging Protocol) protocol, or RTMPS (RTMP over TLS) when TLS encryption is specified. These settings include the destination address and port, the application and stream names, and optional TLS encryption configuration.

## Contents
<a name="API_RtmpPushRouterOutputConfiguration_Contents"></a>

 ** applicationName **   <a name="mediaconnect-Type-RtmpPushRouterOutputConfiguration-applicationName"></a>
The name of the RTMP application on the destination server. Together with the stream name, the application name forms the RTMP URL path, in the pattern `rtmp://destinationAddress/applicationName/streamName`.
Type: String
Required: Yes

 ** destinationAddress **   <a name="mediaconnect-Type-RtmpPushRouterOutputConfiguration-destinationAddress"></a>
The IP address or hostname of the destination RTMP server that the router output pushes the stream to. Provide only the server address; specify the application and stream names separately.
Type: String
Required: Yes

 ** destinationPort **   <a name="mediaconnect-Type-RtmpPushRouterOutputConfiguration-destinationPort"></a>
The TCP port on the destination RTMP server. For RTMP, valid values range from `1024` to `65535`. For RTMPS (RTMP over TLS), valid values are `443` or `1024` to `65535`. RTMP typically uses port `1935`, and RTMPS typically uses port `443`.
Type: Integer
Valid Range: Minimum value of 443. Maximum value of 65535.
Required: Yes

 ** streamName **   <a name="mediaconnect-Type-RtmpPushRouterOutputConfiguration-streamName"></a>
The name of the RTMP stream that the output publishes to the destination application. The stream name forms the final segment of the RTMP URL path.
Type: String
Required: Yes

 ** tlsEncryption **   <a name="mediaconnect-Type-RtmpPushRouterOutputConfiguration-tlsEncryption"></a>
The TLS encryption settings for the output. When you specify these settings, the output uses RTMPS (RTMP over TLS) to establish a secure, encrypted connection to the destination server.
Type: [TlsEncryption](API_TlsEncryption.md) object
Required: No

## See Also
<a name="API_RtmpPushRouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtmpPushRouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtmpPushRouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtmpPushRouterOutputConfiguration)
