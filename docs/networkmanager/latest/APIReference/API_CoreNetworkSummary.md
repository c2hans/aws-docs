---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkSummary.html
---

# CoreNetworkSummary
<a name="API_CoreNetworkSummary"></a>

Returns summary information about a core network.

## Contents
<a name="API_CoreNetworkSummary_Contents"></a>

 ** CoreNetworkArn **   <a name="networkmanager-Type-CoreNetworkSummary-CoreNetworkArn"></a>
a core network ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-CoreNetworkSummary-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** Description **   <a name="networkmanager-Type-CoreNetworkSummary-Description"></a>
The description of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-CoreNetworkSummary-GlobalNetworkId"></a>
The global network ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** OwnerAccountId **   <a name="networkmanager-Type-CoreNetworkSummary-OwnerAccountId"></a>
The ID of the account owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-CoreNetworkSummary-State"></a>
The state of a core network.
Type: String
Valid Values: `CREATING | UPDATING | AVAILABLE | DELETING`
Required: No

 ** Tags **   <a name="networkmanager-Type-CoreNetworkSummary-Tags"></a>
The key-value tags associated with a core network summary.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_CoreNetworkSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
