---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaLiveChannelRouterInputConfiguration.html
---

# MediaLiveChannelRouterInputConfiguration
<a name="API_MediaLiveChannelRouterInputConfiguration"></a>

Configuration settings for connecting a router input to a MediaLive channel output.

## Contents
<a name="API_MediaLiveChannelRouterInputConfiguration_Contents"></a>

 ** sourceTransitDecryption **   <a name="mediaconnect-Type-MediaLiveChannelRouterInputConfiguration-sourceTransitDecryption"></a>
The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive. This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.
Type: [MediaLiveTransitEncryption](API_MediaLiveTransitEncryption.md) object
Required: Yes

 ** mediaLiveChannelArn **   <a name="mediaconnect-Type-MediaLiveChannelRouterInputConfiguration-mediaLiveChannelArn"></a>
The ARN of the MediaLive channel to connect to this router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):medialive:[a-z0-9-]+:[0-9]{12}:channel:[a-zA-Z0-9]+`
Required: No

 ** mediaLiveChannelOutputName **   <a name="mediaconnect-Type-MediaLiveChannelRouterInputConfiguration-mediaLiveChannelOutputName"></a>
The name of the MediaLive channel output to connect to this router input.
Type: String
Required: No

 ** mediaLivePipelineId **   <a name="mediaconnect-Type-MediaLiveChannelRouterInputConfiguration-mediaLivePipelineId"></a>
The index of the MediaLive pipeline to connect to this router input.
Type: String
Valid Values: `PIPELINE_0 | PIPELINE_1`
Required: No

## See Also
<a name="API_MediaLiveChannelRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaLiveChannelRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaLiveChannelRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaLiveChannelRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
