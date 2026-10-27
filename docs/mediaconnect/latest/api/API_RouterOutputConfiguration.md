---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputConfiguration.html
---

# RouterOutputConfiguration
<a name="API_RouterOutputConfiguration"></a>

The configuration settings for a router output.

## Contents
<a name="API_RouterOutputConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** mediaConnectFlow **   <a name="mediaconnect-Type-RouterOutputConfiguration-mediaConnectFlow"></a>
Configuration settings for connecting a router output to a MediaConnect flow source.
To connect the router output to the flow source, provide both `flowArn` and `flowSourceArn`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `destinationTransitEncryption` while the router output is connected to a flow source. To change it, first disconnect the router output, then update the encryption.
Type: [MediaConnectFlowRouterOutputConfiguration](API_MediaConnectFlowRouterOutputConfiguration.md) object
Required: No

 ** mediaLiveInput **   <a name="mediaconnect-Type-RouterOutputConfiguration-mediaLiveInput"></a>
Configuration settings for connecting a router output to a MediaLive input.
To connect the router output to the MediaLive input, provide both `mediaLiveInputArn` and `mediaLivePipelineId`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `destinationTransitEncryption` while the router output is connected to a MediaLive input. To change it, first disconnect the router output, then update the encryption.
Type: [MediaLiveInputRouterOutputConfiguration](API_MediaLiveInputRouterOutputConfiguration.md) object
Required: No

 ** sourceEndpoint **   <a name="mediaconnect-Type-RouterOutputConfiguration-sourceEndpoint"></a>
Configuration settings for a router output that is represented by a source endpoint.
Type: [SourceEndpointRouterOutputConfiguration](API_SourceEndpointRouterOutputConfiguration.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-RouterOutputConfiguration-standard"></a>
The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.
Type: [StandardRouterOutputConfiguration](API_StandardRouterOutputConfiguration.md) object
Required: No

## See Also
<a name="API_RouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputConfiguration)
