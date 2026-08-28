---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkNetworkFunctionGroupIdentifier.html
---

# CoreNetworkNetworkFunctionGroupIdentifier
<a name="API_CoreNetworkNetworkFunctionGroupIdentifier"></a>

Describes a core network

## Contents
<a name="API_CoreNetworkNetworkFunctionGroupIdentifier_Contents"></a>

 ** CoreNetworkId **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroupIdentifier-CoreNetworkId"></a>
The ID of the core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** EdgeLocation **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroupIdentifier-EdgeLocation"></a>
The location for the core network edge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** NetworkFunctionGroupName **   <a name="networkmanager-Type-CoreNetworkNetworkFunctionGroupIdentifier-NetworkFunctionGroupName"></a>
The network function group name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkNetworkFunctionGroupIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroupIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroupIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkNetworkFunctionGroupIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
