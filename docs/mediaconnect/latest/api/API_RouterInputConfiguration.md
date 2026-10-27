---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputConfiguration.html
---

# RouterInputConfiguration
<a name="API_RouterInputConfiguration"></a>

The configuration settings for a router input.

## Contents
<a name="API_RouterInputConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** destinationEndpoint **   <a name="mediaconnect-Type-RouterInputConfiguration-destinationEndpoint"></a>
Configuration settings for a router input that is represented by a destination endpoint.
Type: [DestinationEndpointRouterInputConfiguration](API_DestinationEndpointRouterInputConfiguration.md) object
Required: No

 ** failover **   <a name="mediaconnect-Type-RouterInputConfiguration-failover"></a>
Configuration settings for a failover router input that allows switching between two input sources.
Type: [FailoverRouterInputConfiguration](API_FailoverRouterInputConfiguration.md) object
Required: No

 ** mediaConnectFlow **   <a name="mediaconnect-Type-RouterInputConfiguration-mediaConnectFlow"></a>
Configuration settings for connecting a router input to a flow output.
To connect the router input to the flow output, provide both `flowArn` and `flowOutputArn`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.
You can't change `sourceTransitDecryption` while the router input is connected to a flow output. To change it, first disconnect the router input, then update the decryption.
Type: [MediaConnectFlowRouterInputConfiguration](API_MediaConnectFlowRouterInputConfiguration.md) object
Required: No

 ** mediaLiveChannel **   <a name="mediaconnect-Type-RouterInputConfiguration-mediaLiveChannel"></a>
Configuration settings for connecting a router input to a MediaLive channel output.
To connect the router input to the MediaLive channel output, provide all three of `mediaLiveChannelArn`, `mediaLivePipelineId`, and `mediaLiveChannelOutputName`. To disconnect it, call the update operation and omit all three fields while keeping this configuration object.
You can't change `sourceTransitDecryption` while the router input is connected to a MediaLive channel output. To change it, first disconnect the router input, then update the decryption.
Type: [MediaLiveChannelRouterInputConfiguration](API_MediaLiveChannelRouterInputConfiguration.md) object
Required: No

 ** merge **   <a name="mediaconnect-Type-RouterInputConfiguration-merge"></a>
Configuration settings for a merge router input that combines two input sources.
Type: [MergeRouterInputConfiguration](API_MergeRouterInputConfiguration.md) object
Required: No

 ** standard **   <a name="mediaconnect-Type-RouterInputConfiguration-standard"></a>
The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.
Type: [StandardRouterInputConfiguration](API_StandardRouterInputConfiguration.md) object
Required: No

## See Also
<a name="API_RouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputConfiguration)
