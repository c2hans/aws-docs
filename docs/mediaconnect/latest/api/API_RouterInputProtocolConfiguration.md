---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputProtocolConfiguration.html
---

# RouterInputProtocolConfiguration
<a name="API_RouterInputProtocolConfiguration"></a>

The protocol configuration settings for a router input.

## Contents
<a name="API_RouterInputProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-RouterInputProtocolConfiguration-rist"></a>
The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
Type: [RistRouterInputConfiguration](API_RistRouterInputConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-RouterInputProtocolConfiguration-rtp"></a>
The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
Type: [RtpRouterInputConfiguration](API_RtpRouterInputConfiguration.md) object
Required: No

 ** srtCaller **   <a name="mediaconnect-Type-RouterInputProtocolConfiguration-srtCaller"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.
Type: [SrtCallerRouterInputConfiguration](API_SrtCallerRouterInputConfiguration.md) object
Required: No

 ** srtListener **   <a name="mediaconnect-Type-RouterInputProtocolConfiguration-srtListener"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.
Type: [SrtListenerRouterInputConfiguration](API_SrtListenerRouterInputConfiguration.md) object
Required: No

## See Also
<a name="API_RouterInputProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputProtocolConfiguration)
