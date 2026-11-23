---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ResponderGatewayConfigParameters.html
---

# ResponderGatewayConfigParameters

A requested responder gateway configuration.

## Contents
<a name="API_ResponderGatewayConfigParameters_Contents"></a>

 ** port **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-port"></a>
The networking port.
Type: Integer
Required: Yes

 ** protocol **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-protocol"></a>
The networking protocol.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

 ** clientRoutingPolicy **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-clientRoutingPolicy"></a>
The gateway's client routing policy.
Type: String
Valid Values: `AVAILABILITY_ZONE_AFFINITY | ANY_AVAILABILITY_ZONE`
Required: No

 ** description **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-description"></a>
The gateway's description.
Type: String
Required: No

 ** domainName **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-domainName"></a>
The gateway's domain name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`
Required: No

 ** listenerConfig **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-listenerConfig"></a>
Listener configuration for the protocols (HTTP, HTTPS, or both) accepted by the gateway.
Type: [ListenerConfig](API_ListenerConfig.md) object
Required: No

 ** managedEndpointConfiguration **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-managedEndpointConfiguration"></a>
Describes the configuration of a managed endpoint.
Type: [ManagedEndpointConfiguration](API_ManagedEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** trustStoreConfiguration **   <a name="rtbfabric-Type-ResponderGatewayConfigParameters-trustStoreConfiguration"></a>
Describes the configuration of a trust store.
Type: [TrustStoreConfiguration](API_TrustStoreConfiguration.md) object
Required: No

## See Also
<a name="API_ResponderGatewayConfigParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ResponderGatewayConfigParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ResponderGatewayConfigParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ResponderGatewayConfigParameters)
