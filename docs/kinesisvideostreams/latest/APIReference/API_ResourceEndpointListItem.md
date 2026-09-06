---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ResourceEndpointListItem.html
---

# ResourceEndpointListItem
<a name="API_ResourceEndpointListItem"></a>

An object that describes the endpoint of the signaling channel returned by the `GetSignalingChannelEndpoint` API.

The media server endpoint will correspond to the `WEBRTC` Protocol.

## Contents
<a name="API_ResourceEndpointListItem_Contents"></a>

 ** Protocol **   <a name="KinesisVideo-Type-ResourceEndpointListItem-Protocol"></a>
The protocol of the signaling channel returned by the `GetSignalingChannelEndpoint` API.
Type: String
Valid Values: `WSS | HTTPS | WEBRTC`
Required: No

 ** ResourceEndpoint **   <a name="KinesisVideo-Type-ResourceEndpointListItem-ResourceEndpoint"></a>
The endpoint of the signaling channel returned by the `GetSignalingChannelEndpoint` API.
Type: String
Required: No

## See Also
<a name="API_ResourceEndpointListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/ResourceEndpointListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/ResourceEndpointListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/ResourceEndpointListItem)
