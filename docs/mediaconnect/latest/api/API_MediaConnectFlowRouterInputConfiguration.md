---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaConnectFlowRouterInputConfiguration.html
---

# MediaConnectFlowRouterInputConfiguration
<a name="API_MediaConnectFlowRouterInputConfiguration"></a>

Configuration settings for connecting a router input to a flow output.

## Contents
<a name="API_MediaConnectFlowRouterInputConfiguration_Contents"></a>

 ** sourceTransitDecryption **   <a name="mediaconnect-Type-MediaConnectFlowRouterInputConfiguration-sourceTransitDecryption"></a>
The decryption configuration for the flow source when connected to this router input.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: Yes

 ** flowArn **   <a name="mediaconnect-Type-MediaConnectFlowRouterInputConfiguration-flowArn"></a>
The ARN of the flow to connect to.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: No

 ** flowOutputArn **   <a name="mediaconnect-Type-MediaConnectFlowRouterInputConfiguration-flowOutputArn"></a>
The ARN of the flow output to connect to this router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:output:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_MediaConnectFlowRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaConnectFlowRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaConnectFlowRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaConnectFlowRouterInputConfiguration)
