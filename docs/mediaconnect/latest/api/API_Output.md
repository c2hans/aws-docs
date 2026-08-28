---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Output.html
---

# Output
<a name="API_Output"></a>

The settings for an output.

## Contents
<a name="API_Output_Contents"></a>

 ** name **   <a name="mediaconnect-Type-Output-name"></a>
 The name of the output. This value must be unique within the current flow.
Type: String
Required: Yes

 ** outputArn **   <a name="mediaconnect-Type-Output-outputArn"></a>
 The ARN of the output.
Type: String
Required: Yes

 ** bridgeArn **   <a name="mediaconnect-Type-Output-bridgeArn"></a>
 The ARN of the bridge added to this output.
Type: String
Required: No

 ** bridgePorts **   <a name="mediaconnect-Type-Output-bridgePorts"></a>
 The bridge output ports currently in use.
Type: Array of integers
Required: No

 ** connectedRouterInputArn **   <a name="mediaconnect-Type-Output-connectedRouterInputArn"></a>
The ARN of the router input that's connected to this flow output.
Type: String
Required: No

 ** dataTransferSubscriberFeePercent **   <a name="mediaconnect-Type-Output-dataTransferSubscriberFeePercent"></a>
 Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Type: Integer
Required: No

 ** description **   <a name="mediaconnect-Type-Output-description"></a>
 A description of the output.
Type: String
Required: No

 ** destination **   <a name="mediaconnect-Type-Output-destination"></a>
 The address where you want to send the output.
Type: String
Required: No

 ** encryption **   <a name="mediaconnect-Type-Output-encryption"></a>
 The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Type: [Encryption](API_Encryption.md) object
Required: No

 ** entitlementArn **   <a name="mediaconnect-Type-Output-entitlementArn"></a>
 The ARN of the entitlement on the originator''s flow. This value is relevant only on entitled flows.
Type: String
Required: No

 ** listenerAddress **   <a name="mediaconnect-Type-Output-listenerAddress"></a>
 The IP address that the receiver requires in order to establish a connection with the flow. For public networking, the ListenerAddress is represented by the elastic IP address of the flow. For private networking, the ListenerAddress is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the Zixi pull or SRT listener protocol.
Type: String
Required: No

 ** mediaLiveInputArn **   <a name="mediaconnect-Type-Output-mediaLiveInputArn"></a>
 The input ARN of the MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Type: String
Required: No

 ** mediaStreamOutputConfigurations **   <a name="mediaconnect-Type-Output-mediaStreamOutputConfigurations"></a>
 The configuration for each media stream that is associated with the output.
Type: Array of [MediaStreamOutputConfiguration](API_MediaStreamOutputConfiguration.md) objects
Required: No

 ** outputStatus **   <a name="mediaconnect-Type-Output-outputStatus"></a>
 An indication of whether the output is transmitting data or not.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** peerIpAddress **   <a name="mediaconnect-Type-Output-peerIpAddress"></a>
The IP address of the device that is currently receiving content from this output.
+ For outputs that use protocols where you specify the destination (such as SRT Caller or Zixi Push), this value matches the configured destination address.
+ For outputs that use listener protocols (such as SRT Listener), this value shows the address of the connected receiver.
+ Peer IP addresses aren't available for entitlements, managed MediaLive outputs, NDI® sources and outputs, and CDI/ST2110 outputs.
+ The peer IP address might not be visible for flows that haven't been started yet, or flows that were started before May 2025. In these cases, restart your flow to see the peer IP address.
Type: String
Required: No

 ** port **   <a name="mediaconnect-Type-Output-port"></a>
 The port to use when content is distributed to this output.
Type: Integer
Required: No

 ** routerIntegrationState **   <a name="mediaconnect-Type-Output-routerIntegrationState"></a>
Indicates if router integration is enabled or disabled on the flow output.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** routerIntegrationTransitEncryption **   <a name="mediaconnect-Type-Output-routerIntegrationTransitEncryption"></a>
The encryption configuration for the output when router integration is enabled.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** transport **   <a name="mediaconnect-Type-Output-transport"></a>
 Attributes related to the transport stream that are used in the output.
Type: [Transport](API_Transport.md) object
Required: No

 ** vpcInterfaceAttachment **   <a name="mediaconnect-Type-Output-vpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this output.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## See Also
<a name="API_Output_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Output)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Output)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Output)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
