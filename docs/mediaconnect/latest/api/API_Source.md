---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Source.html
---

# Source
<a name="API_Source"></a>

 The settings for the source of the flow.

## Contents
<a name="API_Source_Contents"></a>

 ** name **   <a name="mediaconnect-Type-Source-name"></a>
 The name of the source.
Type: String
Required: Yes

 ** sourceArn **   <a name="mediaconnect-Type-Source-sourceArn"></a>
 The ARN of the source.
Type: String
Required: Yes

 ** connectedRouterOutputArn **   <a name="mediaconnect-Type-Source-connectedRouterOutputArn"></a>
The ARN of the router output that's currently connected to this source.
Type: String
Required: No

 ** dataTransferSubscriberFeePercent **   <a name="mediaconnect-Type-Source-dataTransferSubscriberFeePercent"></a>
 Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Type: Integer
Required: No

 ** decryption **   <a name="mediaconnect-Type-Source-decryption"></a>
 The type of encryption that is used on the content ingested from this source.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** description **   <a name="mediaconnect-Type-Source-description"></a>
 A description for the source. This value is not used or seen outside of the current MediaConnect account.
Type: String
Required: No

 ** entitlementArn **   <a name="mediaconnect-Type-Source-entitlementArn"></a>
 The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
Type: String
Required: No

 ** gatewayBridgeSource **   <a name="mediaconnect-Type-Source-gatewayBridgeSource"></a>
 The source configuration for cloud flows receiving a stream from a bridge.
Type: [GatewayBridgeSource](API_GatewayBridgeSource.md) object
Required: No

 ** ingestIp **   <a name="mediaconnect-Type-Source-ingestIp"></a>
 The IP address that the flow will be listening on for incoming content.
Type: String
Required: No

 ** ingestPort **   <a name="mediaconnect-Type-Source-ingestPort"></a>
 The port that the flow will be listening on for incoming content.
Type: Integer
Required: No

 ** mediaStreamSourceConfigurations **   <a name="mediaconnect-Type-Source-mediaStreamSourceConfigurations"></a>
 The media streams that are associated with the source, and the parameters for those associations.
Type: Array of [MediaStreamSourceConfiguration](API_MediaStreamSourceConfiguration.md) objects
Required: No

 ** peerIpAddress **   <a name="mediaconnect-Type-Source-peerIpAddress"></a>
The IP address of the device that is currently sending content to this source.
+ For sources that use protocols where you specify the origin (such as SRT Caller), this value matches the configured origin address.
+ For sources that use listener protocols (such as SRT Listener or RTP), this value shows the address of the connected sender.
+ Peer IP addresses aren't available for entitlements and CDI/ST2110 sources.
+ The peer IP address might not be visible for flows that haven't been started yet, or flows that were started before May 2025. In these cases, restart your flow to see the peer IP address.
Type: String
Required: No

 ** routerIntegrationState **   <a name="mediaconnect-Type-Source-routerIntegrationState"></a>
Indicates if router integration is enabled or disabled on the flow source.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** routerIntegrationTransitDecryption **   <a name="mediaconnect-Type-Source-routerIntegrationTransitDecryption"></a>
The decryption configuration for the flow source when router integration is enabled.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** senderControlPort **   <a name="mediaconnect-Type-Source-senderControlPort"></a>
 The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** senderIpAddress **   <a name="mediaconnect-Type-Source-senderIpAddress"></a>
 The IP address that the flow communicates with to initiate connection with the sender.
Type: String
Required: No

 ** transport **   <a name="mediaconnect-Type-Source-transport"></a>
 Attributes related to the transport stream that are used in the source.
Type: [Transport](API_Transport.md) object
Required: No

 ** vpcInterfaceName **   <a name="mediaconnect-Type-Source-vpcInterfaceName"></a>
 The name of the VPC interface that is used for this source.
Type: String
Required: No

 ** whitelistCidr **   <a name="mediaconnect-Type-Source-whitelistCidr"></a>
 The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: String
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Source)
