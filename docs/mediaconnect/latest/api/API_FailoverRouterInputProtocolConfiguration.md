---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FailoverRouterInputProtocolConfiguration.html
---

# FailoverRouterInputProtocolConfiguration
<a name="API_FailoverRouterInputProtocolConfiguration"></a>

Protocol configuration settings for failover router inputs.

## Contents
<a name="API_FailoverRouterInputProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-FailoverRouterInputProtocolConfiguration-rist"></a>
The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
Type: [RistRouterInputConfiguration](API_RistRouterInputConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-FailoverRouterInputProtocolConfiguration-rtp"></a>
The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
Type: [RtpRouterInputConfiguration](API_RtpRouterInputConfiguration.md) object
Required: No

 ** srtCaller **   <a name="mediaconnect-Type-FailoverRouterInputProtocolConfiguration-srtCaller"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.
Type: [SrtCallerRouterInputConfiguration](API_SrtCallerRouterInputConfiguration.md) object
Required: No

 ** srtListener **   <a name="mediaconnect-Type-FailoverRouterInputProtocolConfiguration-srtListener"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.
Type: [SrtListenerRouterInputConfiguration](API_SrtListenerRouterInputConfiguration.md) object
Required: No

## See Also
<a name="API_FailoverRouterInputProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FailoverRouterInputProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FailoverRouterInputProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FailoverRouterInputProtocolConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
