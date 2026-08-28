---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallBlackHoleRouteDetectedViolation.html
---

# NetworkFirewallBlackHoleRouteDetectedViolation
<a name="API_NetworkFirewallBlackHoleRouteDetectedViolation"></a>

Violation detail for an internet gateway route with an inactive state in the customer subnet route table or Network Firewall subnet route table.

## Contents
<a name="API_NetworkFirewallBlackHoleRouteDetectedViolation_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-NetworkFirewallBlackHoleRouteDetectedViolation-RouteTableId"></a>
Information about the route table ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoutes **   <a name="fms-Type-NetworkFirewallBlackHoleRouteDetectedViolation-ViolatingRoutes"></a>
Information about the route or routes that are in violation.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** ViolationTarget **   <a name="fms-Type-NetworkFirewallBlackHoleRouteDetectedViolation-ViolationTarget"></a>
The subnet that has an inactive state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallBlackHoleRouteDetectedViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallBlackHoleRouteDetectedViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallBlackHoleRouteDetectedViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallBlackHoleRouteDetectedViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallBlackHoleRouteDetectedViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
