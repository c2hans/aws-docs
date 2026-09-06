---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ComplianceViolator.html
---

# ComplianceViolator
<a name="API_ComplianceViolator"></a>

Details of the resource that is not protected by the policy.

## Contents
<a name="API_ComplianceViolator_Contents"></a>

 ** Metadata **   <a name="fms-Type-ComplianceViolator-Metadata"></a>
Metadata about the resource that doesn't comply with the policy scope.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ResourceId **   <a name="fms-Type-ComplianceViolator-ResourceId"></a>
The resource ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ResourceType **   <a name="fms-Type-ComplianceViolator-ResourceType"></a>
The resource type. This is in the format shown in the [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html). For example: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::CloudFront::Distribution`, or `AWS::NetworkFirewall::FirewallPolicy`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolationReason **   <a name="fms-Type-ComplianceViolator-ViolationReason"></a>
The reason that the resource is not protected by the policy.
Type: String
Valid Values: `WEB_ACL_MISSING_RULE_GROUP | RESOURCE_MISSING_WEB_ACL | RESOURCE_INCORRECT_WEB_ACL | RESOURCE_MISSING_SHIELD_PROTECTION | RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION | RESOURCE_MISSING_SECURITY_GROUP | RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP | SECURITY_GROUP_UNUSED | SECURITY_GROUP_REDUNDANT | FMS_CREATED_SECURITY_GROUP_EDITED | MISSING_FIREWALL | MISSING_FIREWALL_SUBNET_IN_AZ | MISSING_EXPECTED_ROUTE_TABLE | NETWORK_FIREWALL_POLICY_MODIFIED | FIREWALL_SUBNET_IS_OUT_OF_SCOPE | INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE | FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE | UNEXPECTED_FIREWALL_ROUTES | UNEXPECTED_TARGET_GATEWAY_ROUTES | TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY | INVALID_ROUTE_CONFIGURATION | MISSING_TARGET_GATEWAY | INTERNET_TRAFFIC_NOT_INSPECTED | BLACK_HOLE_ROUTE_DETECTED | BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET | RESOURCE_MISSING_DNS_FIREWALL | ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT | FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT | INVALID_NETWORK_ACL_ENTRY | WEB_ACL_CONFIGURATION_OR_SCOPE_OF_USE`
Required: No

## See Also
<a name="API_ComplianceViolator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ComplianceViolator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ComplianceViolator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ComplianceViolator)
