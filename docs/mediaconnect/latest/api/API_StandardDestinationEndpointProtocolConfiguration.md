---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardDestinationEndpointProtocolConfiguration.html
---

# StandardDestinationEndpointProtocolConfiguration
<a name="API_StandardDestinationEndpointProtocolConfiguration"></a>

The protocol configuration for a standard destination endpoint. This is a union type, so exactly one of its members is set, depending on the protocol that the destination endpoint uses.

## Contents
<a name="API_StandardDestinationEndpointProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-StandardDestinationEndpointProtocolConfiguration-rist"></a>
The configuration settings for a destination endpoint that uses the RIST protocol.
Type: [RistStandardDestinationEndpointConfiguration](API_RistStandardDestinationEndpointConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-StandardDestinationEndpointProtocolConfiguration-rtp"></a>
The configuration settings for a destination endpoint that uses the RTP protocol.
Type: [RtpStandardDestinationEndpointConfiguration](API_RtpStandardDestinationEndpointConfiguration.md) object
Required: No

 ** srtCaller **   <a name="mediaconnect-Type-StandardDestinationEndpointProtocolConfiguration-srtCaller"></a>
The configuration settings for a destination endpoint that uses SRT in caller mode.
Type: [SrtCallerStandardDestinationEndpointConfiguration](API_SrtCallerStandardDestinationEndpointConfiguration.md) object
Required: No

 ** srtListener **   <a name="mediaconnect-Type-StandardDestinationEndpointProtocolConfiguration-srtListener"></a>
The configuration settings for a destination endpoint that uses SRT in listener mode.
Type: [SrtListenerStandardDestinationEndpointConfiguration](API_SrtListenerStandardDestinationEndpointConfiguration.md) object
Required: No

## See Also
<a name="API_StandardDestinationEndpointProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardDestinationEndpointProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardDestinationEndpointProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardDestinationEndpointProtocolConfiguration)
