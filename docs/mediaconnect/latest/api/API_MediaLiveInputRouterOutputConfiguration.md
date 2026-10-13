---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaLiveInputRouterOutputConfiguration.html
---

# MediaLiveInputRouterOutputConfiguration
<a name="API_MediaLiveInputRouterOutputConfiguration"></a>

Configuration settings for connecting a router output to a MediaLive input.

To connect the router output to the MediaLive input, provide both `mediaLiveInputArn` and `mediaLivePipelineId`. To disconnect it, call the update operation and omit both fields while keeping this configuration object.

**Note**
You can't change `destinationTransitEncryption` while the router output is connected to a MediaLive input. To change it, first disconnect the router output, then update the encryption.

## Contents
<a name="API_MediaLiveInputRouterOutputConfiguration_Contents"></a>

 ** destinationTransitEncryption **   <a name="mediaconnect-Type-MediaLiveInputRouterOutputConfiguration-destinationTransitEncryption"></a>
The encryption configuration for the MediaLive input when connected to this router output.
Type: [MediaLiveTransitEncryption](API_MediaLiveTransitEncryption.md) object
Required: Yes

 ** mediaLiveInputArn **   <a name="mediaconnect-Type-MediaLiveInputRouterOutputConfiguration-mediaLiveInputArn"></a>
The ARN of the MediaLive input to connect to this router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):medialive:[a-z0-9-]+:[0-9]{12}:input:[a-zA-Z0-9]+`
Required: No

 ** mediaLivePipelineId **   <a name="mediaconnect-Type-MediaLiveInputRouterOutputConfiguration-mediaLivePipelineId"></a>
The index of the MediaLive pipeline to connect to this router output.
Type: String
Valid Values: `PIPELINE_0 | PIPELINE_1`
Required: No

## See Also
<a name="API_MediaLiveInputRouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaLiveInputRouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaLiveInputRouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaLiveInputRouterOutputConfiguration)
