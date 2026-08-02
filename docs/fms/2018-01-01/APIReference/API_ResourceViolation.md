---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceViolation.html
---

# ResourceViolation
<a name="API_ResourceViolation"></a>

Violation detail based on resource type.

## Contents
<a name="API_ResourceViolation_Contents"></a>

 ** AwsEc2InstanceViolation **   <a name="fms-Type-ResourceViolation-AwsEc2InstanceViolation"></a>
Violation detail for an EC2 instance.
Type: [AwsEc2InstanceViolation](API_AwsEc2InstanceViolation.md) object
Required: No

 ** AwsEc2NetworkInterfaceViolation **   <a name="fms-Type-ResourceViolation-AwsEc2NetworkInterfaceViolation"></a>
Violation detail for a network interface.
Type: [AwsEc2NetworkInterfaceViolation](API_AwsEc2NetworkInterfaceViolation.md) object
Required: No

 ** AwsVPCSecurityGroupViolation **   <a name="fms-Type-ResourceViolation-AwsVPCSecurityGroupViolation"></a>
Violation detail for security groups.
Type: [AwsVPCSecurityGroupViolation](API_AwsVPCSecurityGroupViolation.md) object
Required: No

 ** DnsDuplicateRuleGroupViolation **   <a name="fms-Type-ResourceViolation-DnsDuplicateRuleGroupViolation"></a>
Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC is already associated with the VPC and can't be associated again.
Type: [DnsDuplicateRuleGroupViolation](API_DnsDuplicateRuleGroupViolation.md) object
Required: No

 ** DnsRuleGroupLimitExceededViolation **   <a name="fms-Type-ResourceViolation-DnsRuleGroupLimitExceededViolation"></a>
Violation detail for a DNS Firewall policy that indicates that the VPC reached the limit for associated DNS Firewall rule groups. Firewall Manager tried to associate another rule group with the VPC and failed.
Type: [DnsRuleGroupLimitExceededViolation](API_DnsRuleGroupLimitExceededViolation.md) object
Required: No

 ** DnsRuleGroupPriorityConflictViolation **   <a name="fms-Type-ResourceViolation-DnsRuleGroupPriorityConflictViolation"></a>
Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC has the same priority as a rule group that's already associated.
Type: [DnsRuleGroupPriorityConflictViolation](API_DnsRuleGroupPriorityConflictViolation.md) object
Required: No

 ** FirewallSubnetIsOutOfScopeViolation **   <a name="fms-Type-ResourceViolation-FirewallSubnetIsOutOfScopeViolation"></a>
Contains details about the firewall subnet that violates the policy scope.
Type: [FirewallSubnetIsOutOfScopeViolation](API_FirewallSubnetIsOutOfScopeViolation.md) object
Required: No

 ** FirewallSubnetMissingVPCEndpointViolation **   <a name="fms-Type-ResourceViolation-FirewallSubnetMissingVPCEndpointViolation"></a>
The violation details for a third-party firewall's VPC endpoint subnet that was deleted.
Type: [FirewallSubnetMissingVPCEndpointViolation](API_FirewallSubnetMissingVPCEndpointViolation.md) object
Required: No

 ** InvalidNetworkAclEntriesViolation **   <a name="fms-Type-ResourceViolation-InvalidNetworkAclEntriesViolation"></a>
Violation detail for the entries in a network ACL resource.
Type: [InvalidNetworkAclEntriesViolation](API_InvalidNetworkAclEntriesViolation.md) object
Required: No

 ** NetworkFirewallBlackHoleRouteDetectedViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallBlackHoleRouteDetectedViolation"></a>
Violation detail for an internet gateway route with an inactive state in the customer subnet route table or Network Firewall subnet route table.
Type: [NetworkFirewallBlackHoleRouteDetectedViolation](API_NetworkFirewallBlackHoleRouteDetectedViolation.md) object
Required: No

 ** NetworkFirewallInternetTrafficNotInspectedViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallInternetTrafficNotInspectedViolation"></a>
Violation detail for the subnet for which internet traffic hasn't been inspected.
Type: [NetworkFirewallInternetTrafficNotInspectedViolation](API_NetworkFirewallInternetTrafficNotInspectedViolation.md) object
Required: No

 ** NetworkFirewallInvalidRouteConfigurationViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallInvalidRouteConfigurationViolation"></a>
The route configuration is invalid.
Type: [NetworkFirewallInvalidRouteConfigurationViolation](API_NetworkFirewallInvalidRouteConfigurationViolation.md) object
Required: No

 ** NetworkFirewallMissingExpectedRoutesViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallMissingExpectedRoutesViolation"></a>
Expected routes are missing from AWS Network Firewall.
Type: [NetworkFirewallMissingExpectedRoutesViolation](API_NetworkFirewallMissingExpectedRoutesViolation.md) object
Required: No

 ** NetworkFirewallMissingExpectedRTViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallMissingExpectedRTViolation"></a>
Violation detail for an Network Firewall policy that indicates that a subnet is not associated with the expected Firewall Manager managed route table.
Type: [NetworkFirewallMissingExpectedRTViolation](API_NetworkFirewallMissingExpectedRTViolation.md) object
Required: No

 ** NetworkFirewallMissingFirewallViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallMissingFirewallViolation"></a>
Violation detail for an Network Firewall policy that indicates that a subnet has no Firewall Manager managed firewall in its VPC.
Type: [NetworkFirewallMissingFirewallViolation](API_NetworkFirewallMissingFirewallViolation.md) object
Required: No

 ** NetworkFirewallMissingSubnetViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallMissingSubnetViolation"></a>
Violation detail for an Network Firewall policy that indicates that an Availability Zone is missing the expected Firewall Manager managed subnet.
Type: [NetworkFirewallMissingSubnetViolation](API_NetworkFirewallMissingSubnetViolation.md) object
Required: No

 ** NetworkFirewallPolicyModifiedViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallPolicyModifiedViolation"></a>
Violation detail for an Network Firewall policy that indicates that a firewall policy in an individual account has been modified in a way that makes it noncompliant. For example, the individual account owner might have deleted a rule group, changed the priority of a stateless rule group, or changed a policy default action.
Type: [NetworkFirewallPolicyModifiedViolation](API_NetworkFirewallPolicyModifiedViolation.md) object
Required: No

 ** NetworkFirewallUnexpectedFirewallRoutesViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallUnexpectedFirewallRoutesViolation"></a>
There's an unexpected firewall route.
Type: [NetworkFirewallUnexpectedFirewallRoutesViolation](API_NetworkFirewallUnexpectedFirewallRoutesViolation.md) object
Required: No

 ** NetworkFirewallUnexpectedGatewayRoutesViolation **   <a name="fms-Type-ResourceViolation-NetworkFirewallUnexpectedGatewayRoutesViolation"></a>
There's an unexpected gateway route.
Type: [NetworkFirewallUnexpectedGatewayRoutesViolation](API_NetworkFirewallUnexpectedGatewayRoutesViolation.md) object
Required: No

 ** PossibleRemediationActions **   <a name="fms-Type-ResourceViolation-PossibleRemediationActions"></a>
A list of possible remediation action lists. Each individual possible remediation action is a list of individual remediation actions.
Type: [PossibleRemediationActions](API_PossibleRemediationActions.md) object
Required: No

 ** RouteHasOutOfScopeEndpointViolation **   <a name="fms-Type-ResourceViolation-RouteHasOutOfScopeEndpointViolation"></a>
Contains details about the route endpoint that violates the policy scope.
Type: [RouteHasOutOfScopeEndpointViolation](API_RouteHasOutOfScopeEndpointViolation.md) object
Required: No

 ** ThirdPartyFirewallMissingExpectedRouteTableViolation **   <a name="fms-Type-ResourceViolation-ThirdPartyFirewallMissingExpectedRouteTableViolation"></a>
The violation details for a third-party firewall that has the Firewall Manager managed route table that was associated with the third-party firewall has been deleted.
Type: [ThirdPartyFirewallMissingExpectedRouteTableViolation](API_ThirdPartyFirewallMissingExpectedRouteTableViolation.md) object
Required: No

 ** ThirdPartyFirewallMissingFirewallViolation **   <a name="fms-Type-ResourceViolation-ThirdPartyFirewallMissingFirewallViolation"></a>
The violation details for a third-party firewall that's been deleted.
Type: [ThirdPartyFirewallMissingFirewallViolation](API_ThirdPartyFirewallMissingFirewallViolation.md) object
Required: No

 ** ThirdPartyFirewallMissingSubnetViolation **   <a name="fms-Type-ResourceViolation-ThirdPartyFirewallMissingSubnetViolation"></a>
The violation details for a third-party firewall's subnet that's been deleted.
Type: [ThirdPartyFirewallMissingSubnetViolation](API_ThirdPartyFirewallMissingSubnetViolation.md) object
Required: No

 ** WebACLHasIncompatibleConfigurationViolation **   <a name="fms-Type-ResourceViolation-WebACLHasIncompatibleConfigurationViolation"></a>
The violation details for a web ACL whose configuration is incompatible with the Firewall Manager policy.
Type: [WebACLHasIncompatibleConfigurationViolation](API_WebACLHasIncompatibleConfigurationViolation.md) object
Required: No

 ** WebACLHasOutOfScopeResourcesViolation **   <a name="fms-Type-ResourceViolation-WebACLHasOutOfScopeResourcesViolation"></a>
The violation details for a web ACL that's associated with at least one resource that's out of scope of the Firewall Manager policy.
Type: [WebACLHasOutOfScopeResourcesViolation](API_WebACLHasOutOfScopeResourcesViolation.md) object
Required: No

## See Also
<a name="API_ResourceViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ResourceViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ResourceViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ResourceViolation)
