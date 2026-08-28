---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_GatewayNetwork.html
---

# GatewayNetwork
<a name="API_GatewayNetwork"></a>

The network settings for a gateway.

## Contents
<a name="API_GatewayNetwork_Contents"></a>

 ** cidrBlock **   <a name="mediaconnect-Type-GatewayNetwork-cidrBlock"></a>
A unique IP address range to use for this network. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-GatewayNetwork-name"></a>
The name of the network. This name is used to reference the network and must be unique among networks in this gateway.
Type: String
Required: Yes

## See Also
<a name="API_GatewayNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/GatewayNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/GatewayNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/GatewayNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
