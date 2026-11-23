---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceCoverageSummary.html
---

# ResourceCoverageSummary

Describes how an AWS Network Security Manager entity covers a protected resource.

## Contents
<a name="API_ResourceCoverageSummary_Contents"></a>

 ** coverageStatus **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-coverageStatus"></a>
Specifies whether the entity contributes to the effective configuration of the resource for its firewall type. For firewall types that combine policies, such as AWS WAF and AWS Shield Advanced, every policy that covers the resource is `IN_EFFECT`. For firewall types that apply a single policy, only the highest-priority policy is `IN_EFFECT` and the others are `SUPERSEDED`.
Type: String
Valid Values: `IN_EFFECT | SUPERSEDED`
Required: No

 ** deploymentArns **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-deploymentArns"></a>
The Amazon Resource Names (ARNs) of the deployments through which the entity covers the resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** entityArn **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-entityArn"></a>
The Amazon Resource Name (ARN) of the entity that covers the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** entityType **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-entityType"></a>
The type of the entity that covers the resource, such as `Policy`.
Type: String
Valid Values: `Rule | Template | Policy | Deployment | Scope`
Required: No

 ** firewallType **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-firewallType"></a>
The firewall type of the policy that covers the resource. This is present when `entityType` is `Policy`.
Type: String
Valid Values: `WAF | SHIELD_ADVANCED | IGW_FIREWALL`
Required: No

 ** resourceArn **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-resourceArn"></a>
The Amazon Resource Name (ARN) of the protected resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** resourceOwnerAccountId **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-resourceOwnerAccountId"></a>
The AWS account ID that owns the protected resource. This can differ from the account that owns the entity.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: No

 ** resourceType **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-resourceType"></a>
The type of the protected resource, in AWS CloudFormation format.
Type: String
Valid Values: `AWS::ApiGateway::Stage | AWS::CloudFront::Distribution | AWS::EC2::EIP | AWS::ElasticLoadBalancingV2::LoadBalancer::application | AWS::ElasticLoadBalancing::LoadBalancer | AWS::EC2::VPC | AWS::EC2::Subnet`
Required: No

 ** updatedAt **   <a name="networksecuritymanager-Type-ResourceCoverageSummary-updatedAt"></a>
The time when AWS Network Security Manager last evaluated the coverage.
Type: Timestamp
Required: No

## See Also
<a name="API_ResourceCoverageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceCoverageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceCoverageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceCoverageSummary)
