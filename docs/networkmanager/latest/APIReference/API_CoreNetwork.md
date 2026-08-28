---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetwork.html
---

# CoreNetwork
<a name="API_CoreNetwork"></a>

Describes a core network.

## Contents
<a name="API_CoreNetwork_Contents"></a>

 ** CoreNetworkArn **   <a name="networkmanager-Type-CoreNetwork-CoreNetworkArn"></a>
The ARN of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-CoreNetwork-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-CoreNetwork-CreatedAt"></a>
The timestamp when a core network was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-CoreNetwork-Description"></a>
The description of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Edges **   <a name="networkmanager-Type-CoreNetwork-Edges"></a>
The edges within a core network.
Type: Array of [CoreNetworkEdge](API_CoreNetworkEdge.md) objects
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-CoreNetwork-GlobalNetworkId"></a>
The ID of the global network that your core network is a part of.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** NetworkFunctionGroups **   <a name="networkmanager-Type-CoreNetwork-NetworkFunctionGroups"></a>
The network function groups associated with a core network.
Type: Array of [CoreNetworkNetworkFunctionGroup](API_CoreNetworkNetworkFunctionGroup.md) objects
Required: No

 ** Segments **   <a name="networkmanager-Type-CoreNetwork-Segments"></a>
The segments within a core network.
Type: Array of [CoreNetworkSegment](API_CoreNetworkSegment.md) objects
Required: No

 ** State **   <a name="networkmanager-Type-CoreNetwork-State"></a>
The current state of a core network.
Type: String
Valid Values: `CREATING | UPDATING | AVAILABLE | DELETING`
Required: No

 ** Tags **   <a name="networkmanager-Type-CoreNetwork-Tags"></a>
The list of key-value tags associated with a core network.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_CoreNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
