---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallInternetTrafficNotInspectedViolation.html
---

# NetworkFirewallInternetTrafficNotInspectedViolation
<a name="API_NetworkFirewallInternetTrafficNotInspectedViolation"></a>

Violation detail for the subnet for which internet traffic that hasn't been inspected.

## Contents
<a name="API_NetworkFirewallInternetTrafficNotInspectedViolation_Contents"></a>

 ** ActualFirewallSubnetRoutes **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ActualFirewallSubnetRoutes"></a>
The actual firewall subnet routes.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** ActualInternetGatewayRoutes **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ActualInternetGatewayRoutes"></a>
The actual internet gateway routes.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** CurrentFirewallSubnetRouteTable **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-CurrentFirewallSubnetRouteTable"></a>
Information about the subnet route table for the current firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** CurrentInternetGatewayRouteTable **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-CurrentInternetGatewayRouteTable"></a>
The current route table for the internet gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedFirewallEndpoint **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ExpectedFirewallEndpoint"></a>
The expected endpoint for the current firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedFirewallSubnetRoutes **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ExpectedFirewallSubnetRoutes"></a>
The firewall subnet routes that are expected.
Type: Array of [ExpectedRoute](API_ExpectedRoute.md) objects
Required: No

 ** ExpectedInternetGatewayRoutes **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ExpectedInternetGatewayRoutes"></a>
The internet gateway routes that are expected.
Type: Array of [ExpectedRoute](API_ExpectedRoute.md) objects
Required: No

 ** FirewallSubnetId **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-FirewallSubnetId"></a>
The firewall subnet ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** InternetGatewayId **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-InternetGatewayId"></a>
The internet gateway ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** IsRouteTableUsedInDifferentAZ **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-IsRouteTableUsedInDifferentAZ"></a>
Information about whether the route table is used in another Availability Zone.
Type: Boolean
Required: No

 ** RouteTableId **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-RouteTableId"></a>
Information about the route table ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SubnetAvailabilityZone **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-SubnetAvailabilityZone"></a>
The subnet Availability Zone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** SubnetId **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-SubnetId"></a>
The subnet ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoutes **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-ViolatingRoutes"></a>
The route or routes that are in violation.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallInternetTrafficNotInspectedViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallInternetTrafficNotInspectedViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallInternetTrafficNotInspectedViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallInternetTrafficNotInspectedViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallInternetTrafficNotInspectedViolation)
