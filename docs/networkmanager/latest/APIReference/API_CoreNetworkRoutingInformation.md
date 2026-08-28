---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CoreNetworkRoutingInformation.html
---

# CoreNetworkRoutingInformation
<a name="API_CoreNetworkRoutingInformation"></a>

Routing information for a core network, including route details and BGP attributes.

## Contents
<a name="API_CoreNetworkRoutingInformation_Contents"></a>

 ** AsPath **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-AsPath"></a>
The BGP AS path for the route.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Communities **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-Communities"></a>
The BGP community values for the route.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** LocalPreference **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-LocalPreference"></a>
The BGP local preference value for the route.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Med **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-Med"></a>
The BGP Multi-Exit Discriminator (MED) value for the route.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** NextHop **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-NextHop"></a>
The next hop information for the route.
Type: [RoutingInformationNextHop](API_RoutingInformationNextHop.md) object
Required: No

 ** Prefix **   <a name="networkmanager-Type-CoreNetworkRoutingInformation-Prefix"></a>
The IP prefix for the route.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CoreNetworkRoutingInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CoreNetworkRoutingInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CoreNetworkRoutingInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CoreNetworkRoutingInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
