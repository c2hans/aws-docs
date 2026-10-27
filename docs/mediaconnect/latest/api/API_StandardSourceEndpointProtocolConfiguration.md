---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardSourceEndpointProtocolConfiguration.html
---

# StandardSourceEndpointProtocolConfiguration
<a name="API_StandardSourceEndpointProtocolConfiguration"></a>

The protocol configuration for a standard source endpoint. This is a union type, so exactly one of its members is set, depending on the protocol that the source endpoint uses.

## Contents
<a name="API_StandardSourceEndpointProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-StandardSourceEndpointProtocolConfiguration-rist"></a>
The configuration settings for a source endpoint that uses the RIST protocol.
Type: [RistStandardSourceEndpointConfiguration](API_RistStandardSourceEndpointConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-StandardSourceEndpointProtocolConfiguration-rtp"></a>
The configuration settings for a source endpoint that uses the RTP protocol.
Type: [RtpStandardSourceEndpointConfiguration](API_RtpStandardSourceEndpointConfiguration.md) object
Required: No

 ** srtCaller **   <a name="mediaconnect-Type-StandardSourceEndpointProtocolConfiguration-srtCaller"></a>
The configuration settings for a source endpoint that uses SRT in caller mode.
Type: [SrtCallerStandardSourceEndpointConfiguration](API_SrtCallerStandardSourceEndpointConfiguration.md) object
Required: No

 ** srtListener **   <a name="mediaconnect-Type-StandardSourceEndpointProtocolConfiguration-srtListener"></a>
The configuration settings for a source endpoint that uses SRT in listener mode.
Type: [SrtListenerStandardSourceEndpointConfiguration](API_SrtListenerStandardSourceEndpointConfiguration.md) object
Required: No

## See Also
<a name="API_StandardSourceEndpointProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardSourceEndpointProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardSourceEndpointProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardSourceEndpointProtocolConfiguration)
