---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallUnexpectedFirewallRoutesViolation.html
---

# NetworkFirewallUnexpectedFirewallRoutesViolation
<a name="API_NetworkFirewallUnexpectedFirewallRoutesViolation"></a>

Violation detail for an unexpected route that's present in a route table.

## Contents
<a name="API_NetworkFirewallUnexpectedFirewallRoutesViolation_Contents"></a>

 ** FirewallEndpoint **   <a name="fms-Type-NetworkFirewallUnexpectedFirewallRoutesViolation-FirewallEndpoint"></a>
The endpoint of the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** FirewallSubnetId **   <a name="fms-Type-NetworkFirewallUnexpectedFirewallRoutesViolation-FirewallSubnetId"></a>
The subnet ID for the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** RouteTableId **   <a name="fms-Type-NetworkFirewallUnexpectedFirewallRoutesViolation-RouteTableId"></a>
The ID of the route table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolatingRoutes **   <a name="fms-Type-NetworkFirewallUnexpectedFirewallRoutesViolation-ViolatingRoutes"></a>
The routes that are in violation.
Type: Array of [Route](API_Route.md) objects
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallUnexpectedFirewallRoutesViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallUnexpectedFirewallRoutesViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallUnexpectedFirewallRoutesViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallUnexpectedFirewallRoutesViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallUnexpectedFirewallRoutesViolation)
