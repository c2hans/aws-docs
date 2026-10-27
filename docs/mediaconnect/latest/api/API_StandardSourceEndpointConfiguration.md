---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardSourceEndpointConfiguration.html
---

# StandardSourceEndpointConfiguration
<a name="API_StandardSourceEndpointConfiguration"></a>

The configuration settings for a standard source endpoint.

## Contents
<a name="API_StandardSourceEndpointConfiguration_Contents"></a>

 ** name **   <a name="mediaconnect-Type-StandardSourceEndpointConfiguration-name"></a>
The name of the source endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 164.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?`
Required: Yes

 ** protocolConfiguration **   <a name="mediaconnect-Type-StandardSourceEndpointConfiguration-protocolConfiguration"></a>
The protocol configuration for the source endpoint.
Type: [StandardSourceEndpointProtocolConfiguration](API_StandardSourceEndpointProtocolConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sourceNetworkingConfiguration **   <a name="mediaconnect-Type-StandardSourceEndpointConfiguration-sourceNetworkingConfiguration"></a>
The networking configuration for the source endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).
Type: [StandardSourceEndpointNetworkingConfiguration](API_StandardSourceEndpointNetworkingConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** protocol **   <a name="mediaconnect-Type-StandardSourceEndpointConfiguration-protocol"></a>
The protocol used by the source endpoint. Valid values include the following:
+  `RTP` – Real-time Transport Protocol.
+  `RIST` – Reliable Internet Stream Transport.
+  `SRT_CALLER` – Secure Reliable Transport (SRT) in caller mode.
+  `SRT_LISTENER` – Secure Reliable Transport (SRT) in listener mode.
Type: String
Valid Values: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
Required: No

 ** sourceNetworkingType **   <a name="mediaconnect-Type-StandardSourceEndpointConfiguration-sourceNetworkingType"></a>
The networking type of the source endpoint. Valid values include the following:
+  `PUBLIC` – The source endpoint is publicly accessible.
+  `VPC` – The source endpoint is in a virtual private cloud (VPC).
Type: String
Valid Values: `PUBLIC | VPC`
Required: No

## See Also
<a name="API_StandardSourceEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardSourceEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardSourceEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardSourceEndpointConfiguration)
