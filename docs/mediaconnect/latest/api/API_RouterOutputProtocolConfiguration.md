---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputProtocolConfiguration.html
---

# RouterOutputProtocolConfiguration
<a name="API_RouterOutputProtocolConfiguration"></a>

The protocol configuration settings for a router output.

## Contents
<a name="API_RouterOutputProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-RouterOutputProtocolConfiguration-rist"></a>
The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.
Type: [RistRouterOutputConfiguration](API_RistRouterOutputConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-RouterOutputProtocolConfiguration-rtp"></a>
The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.
Type: [RtpRouterOutputConfiguration](API_RtpRouterOutputConfiguration.md) object
Required: No

 ** srtCaller **   <a name="mediaconnect-Type-RouterOutputProtocolConfiguration-srtCaller"></a>
The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.
Type: [SrtCallerRouterOutputConfiguration](API_SrtCallerRouterOutputConfiguration.md) object
Required: No

 ** srtListener **   <a name="mediaconnect-Type-RouterOutputProtocolConfiguration-srtListener"></a>
The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.
Type: [SrtListenerRouterOutputConfiguration](API_SrtListenerRouterOutputConfiguration.md) object
Required: No

## See Also
<a name="API_RouterOutputProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputProtocolConfiguration)
