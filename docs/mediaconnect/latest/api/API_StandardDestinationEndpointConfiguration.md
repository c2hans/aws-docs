---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardDestinationEndpointConfiguration.html
---

# StandardDestinationEndpointConfiguration
<a name="API_StandardDestinationEndpointConfiguration"></a>

The configuration settings for a standard destination endpoint.

## Contents
<a name="API_StandardDestinationEndpointConfiguration_Contents"></a>

 ** destinationNetworkingConfiguration **   <a name="mediaconnect-Type-StandardDestinationEndpointConfiguration-destinationNetworkingConfiguration"></a>
The networking configuration for the destination endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).
Type: [StandardDestinationEndpointNetworkingConfiguration](API_StandardDestinationEndpointNetworkingConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="mediaconnect-Type-StandardDestinationEndpointConfiguration-name"></a>
The name of the destination endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 164.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?`
Required: Yes

 ** protocolConfiguration **   <a name="mediaconnect-Type-StandardDestinationEndpointConfiguration-protocolConfiguration"></a>
The protocol configuration for the destination endpoint.
Type: [StandardDestinationEndpointProtocolConfiguration](API_StandardDestinationEndpointProtocolConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** destinationNetworkingType **   <a name="mediaconnect-Type-StandardDestinationEndpointConfiguration-destinationNetworkingType"></a>
The networking type of the destination endpoint. Valid values include the following:
+  `PUBLIC` – The destination endpoint is publicly accessible.
+  `VPC` – The destination endpoint is in a virtual private cloud (VPC).
Type: String
Valid Values: `PUBLIC | VPC`
Required: No

 ** protocol **   <a name="mediaconnect-Type-StandardDestinationEndpointConfiguration-protocol"></a>
The protocol used by the destination endpoint. Valid values include the following:
+  `RTP` – Real-time Transport Protocol.
+  `RIST` – Reliable Internet Stream Transport.
+  `SRT_CALLER` – Secure Reliable Transport (SRT) in caller mode.
+  `SRT_LISTENER` – Secure Reliable Transport (SRT) in listener mode.
Type: String
Valid Values: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
Required: No

## See Also
<a name="API_StandardDestinationEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardDestinationEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardDestinationEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardDestinationEndpointConfiguration)
