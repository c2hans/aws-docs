---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaConnectFlowRouterOutputConfiguration.html
---

# MediaConnectFlowRouterOutputConfiguration
<a name="API_MediaConnectFlowRouterOutputConfiguration"></a>

Configuration settings for connecting a router output to a MediaConnect flow source.

## Contents
<a name="API_MediaConnectFlowRouterOutputConfiguration_Contents"></a>

 ** destinationTransitEncryption **   <a name="mediaconnect-Type-MediaConnectFlowRouterOutputConfiguration-destinationTransitEncryption"></a>
The encryption configuration for the flow destination when connected to this router output.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: Yes

 ** flowArn **   <a name="mediaconnect-Type-MediaConnectFlowRouterOutputConfiguration-flowArn"></a>
The ARN of the flow to connect to this router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: No

 ** flowSourceArn **   <a name="mediaconnect-Type-MediaConnectFlowRouterOutputConfiguration-flowSourceArn"></a>
The ARN of the flow source to connect to this router output.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:source:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_MediaConnectFlowRouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaConnectFlowRouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaConnectFlowRouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaConnectFlowRouterOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
