---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_DeploymentCoverageEntry.html
---

# DeploymentCoverageEntry
<a name="API_DeploymentCoverageEntry"></a>

Coverage information for one firewall type within a deployment. It lists the deployment's policies that have this firewall type. It also lists the resource types in the deployment's scope that the firewall type protects.

## Contents
<a name="API_DeploymentCoverageEntry_Contents"></a>

 ** firewallType **   <a name="networksecuritymanager-Type-DeploymentCoverageEntry-firewallType"></a>
The firewall type that the policies in this entry share.
Type: String
Valid Values: `WAF | SHIELD_ADVANCED`
Required: Yes

 ** inScopeResourceTypes **   <a name="networksecuritymanager-Type-DeploymentCoverageEntry-inScopeResourceTypes"></a>
The resource types in the deployment's scope that this firewall type protects. This list is empty if the scope does not select any resource types that the firewall type protects.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `AWS::ApiGateway::Stage | AWS::CloudFront::Distribution | AWS::EC2::EIP | AWS::ElasticLoadBalancingV2::LoadBalancer::application | AWS::ElasticLoadBalancing::LoadBalancer`
Required: Yes

 ** policyArns **   <a name="networksecuritymanager-Type-DeploymentCoverageEntry-policyArns"></a>
The Amazon Resource Names (ARNs) of the deployment's policies that have this firewall type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

## See Also
<a name="API_DeploymentCoverageEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/DeploymentCoverageEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/DeploymentCoverageEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/DeploymentCoverageEntry)
