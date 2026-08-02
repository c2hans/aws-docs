---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallUnexpectedGatewayRoutesViolation.html
---

# NetworkFirewallUnexpectedGatewayRoutesViolation
<a name="API_NetworkFirewallUnexpectedGatewayRoutesViolation"></a>

Violation detail for an unexpected gateway route that’s present in a route table.

## Contents
<a name="API_NetworkFirewallUnexpectedGatewayRoutesViolation_Contents"></a>

 ** GatewayId **   <a name="fms-Type-NetworkFirewallUnexpectedGatewayRoutesViolation-GatewayId"></a>
Information about the gateway ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** RouteTableId **   <a name="fms-Type-NetworkFirewallUnexpectedGatewayRoutesViolation-RouteTableId"></a>
Information about the route table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoutes **   <a name="fms-Type-NetworkFirewallUnexpectedGatewayRoutesViolation-ViolatingRoutes"></a>
The routes that are in violation.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallUnexpectedGatewayRoutesViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallUnexpectedGatewayRoutesViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallUnexpectedGatewayRoutesViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallUnexpectedGatewayRoutesViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallUnexpectedGatewayRoutesViolation)
