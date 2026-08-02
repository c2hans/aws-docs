---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_RouteHasOutOfScopeEndpointViolation.html
---

# RouteHasOutOfScopeEndpointViolation
<a name="API_RouteHasOutOfScopeEndpointViolation"></a>

Contains details about the route endpoint that violates the policy scope.

## Contents
<a name="API_RouteHasOutOfScopeEndpointViolation_Contents"></a>

 ** CurrentFirewallSubnetRouteTable **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-CurrentFirewallSubnetRouteTable"></a>
The route table associated with the current firewall subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** CurrentInternetGatewayRouteTable **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-CurrentInternetGatewayRouteTable"></a>
The current route table associated with the Internet Gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** FirewallSubnetId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-FirewallSubnetId"></a>
The ID of the firewall subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** FirewallSubnetRoutes **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-FirewallSubnetRoutes"></a>
The list of firewall subnet routes.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** InternetGatewayId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-InternetGatewayId"></a>
The ID of the Internet Gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** InternetGatewayRoutes **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-InternetGatewayRoutes"></a>
The routes in the route table associated with the Internet Gateway.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** RouteTableId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-RouteTableId"></a>
The ID of the route table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SubnetAvailabilityZone **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-SubnetAvailabilityZone"></a>
The subnet's Availability Zone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** SubnetAvailabilityZoneId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-SubnetAvailabilityZoneId"></a>
The ID of the subnet's Availability Zone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** SubnetId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-SubnetId"></a>
The ID of the subnet associated with the route that violates the policy scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoutes **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-ViolatingRoutes"></a>
The list of routes that violate the route table.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** VpcId **   <a name="fms-Type-RouteHasOutOfScopeEndpointViolation-VpcId"></a>
The VPC ID of the route that violates the policy scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_RouteHasOutOfScopeEndpointViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/RouteHasOutOfScopeEndpointViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/RouteHasOutOfScopeEndpointViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/RouteHasOutOfScopeEndpointViolation)
