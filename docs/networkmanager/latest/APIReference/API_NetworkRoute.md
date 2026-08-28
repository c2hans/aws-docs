---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NetworkRoute.html
---

# NetworkRoute
<a name="API_NetworkRoute"></a>

Describes a network route.

## Contents
<a name="API_NetworkRoute_Contents"></a>

 ** DestinationCidrBlock **   <a name="networkmanager-Type-NetworkRoute-DestinationCidrBlock"></a>
A unique identifier for the route, such as a CIDR block.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Destinations **   <a name="networkmanager-Type-NetworkRoute-Destinations"></a>
The destinations.
Type: Array of [NetworkRouteDestination](API_NetworkRouteDestination.md) objects
Required: No

 ** PrefixListId **   <a name="networkmanager-Type-NetworkRoute-PrefixListId"></a>
The ID of the prefix list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-NetworkRoute-State"></a>
The route state. The possible values are `active` and `blackhole`.
Type: String
Valid Values: `ACTIVE | BLACKHOLE`
Required: No

 ** Type **   <a name="networkmanager-Type-NetworkRoute-Type"></a>
The route type. The possible values are `propagated` and `static`.
Type: String
Valid Values: `PROPAGATED | STATIC`
Required: No

## See Also
<a name="API_NetworkRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
