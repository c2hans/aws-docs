---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_StandardRouterInputConfiguration.html
---

# StandardRouterInputConfiguration
<a name="API_StandardRouterInputConfiguration"></a>

The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.

## Contents
<a name="API_StandardRouterInputConfiguration_Contents"></a>

 ** networkInterfaceArn **   <a name="mediaconnect-Type-StandardRouterInputConfiguration-networkInterfaceArn"></a>
The Amazon Resource Name (ARN) of the network interface associated with the standard router input.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** protocolConfiguration **   <a name="mediaconnect-Type-StandardRouterInputConfiguration-protocolConfiguration"></a>
The configuration settings for the protocol used by the standard router input.
Type: [RouterInputProtocolConfiguration](API_RouterInputProtocolConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** protocol **   <a name="mediaconnect-Type-StandardRouterInputConfiguration-protocol"></a>
The protocol used by the standard router input.
Type: String
Valid Values: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
Required: No

## See Also
<a name="API_StandardRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/StandardRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/StandardRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/StandardRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
