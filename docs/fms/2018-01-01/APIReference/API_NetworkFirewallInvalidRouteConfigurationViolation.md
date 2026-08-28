---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallInvalidRouteConfigurationViolation.html
---

# NetworkFirewallInvalidRouteConfigurationViolation
<a name="API_NetworkFirewallInvalidRouteConfigurationViolation"></a>

Violation detail for the improperly configured subnet route. It's possible there is a missing route table route, or a configuration that causes traffic to cross an Availability Zone boundary.

## Contents
<a name="API_NetworkFirewallInvalidRouteConfigurationViolation_Contents"></a>

 ** ActualFirewallEndpoint **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ActualFirewallEndpoint"></a>
The actual firewall endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ActualFirewallSubnetId **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ActualFirewallSubnetId"></a>
The actual subnet ID for the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ActualFirewallSubnetRoutes **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ActualFirewallSubnetRoutes"></a>
The actual firewall subnet routes that are expected.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** ActualInternetGatewayRoutes **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ActualInternetGatewayRoutes"></a>
The actual internet gateway routes.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** AffectedSubnets **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-AffectedSubnets"></a>
The subnets that are affected.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** CurrentFirewallSubnetRouteTable **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-CurrentFirewallSubnetRouteTable"></a>
The subnet route table for the current firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** CurrentInternetGatewayRouteTable **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-CurrentInternetGatewayRouteTable"></a>
The route table for the current internet gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedFirewallEndpoint **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ExpectedFirewallEndpoint"></a>
The firewall endpoint that's expected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedFirewallSubnetId **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ExpectedFirewallSubnetId"></a>
The expected subnet ID for the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedFirewallSubnetRoutes **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ExpectedFirewallSubnetRoutes"></a>
The firewall subnet routes that are expected.
Type: Array of [ExpectedRoute](API_ExpectedRoute.md) objects
Required: No

 ** ExpectedInternetGatewayRoutes **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ExpectedInternetGatewayRoutes"></a>
The expected routes for the internet gateway.
Type: Array of [ExpectedRoute](API_ExpectedRoute.md) objects
Required: No

 ** InternetGatewayId **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-InternetGatewayId"></a>
The internet gateway ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** IsRouteTableUsedInDifferentAZ **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-IsRouteTableUsedInDifferentAZ"></a>
Information about whether the route table is used in another Availability Zone.
Type: Boolean
Required: No

 ** RouteTableId **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-RouteTableId"></a>
The route table ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoute **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-ViolatingRoute"></a>
The route that's in violation.
Type: [Route](API_Route.md) object
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallInvalidRouteConfigurationViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallInvalidRouteConfigurationViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallInvalidRouteConfigurationViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallInvalidRouteConfigurationViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallInvalidRouteConfigurationViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
