---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ScopeConfiguration.html
---

# ScopeConfiguration
<a name="API_ScopeConfiguration"></a>

Defines which accounts and resources are in scope.

## Contents
<a name="API_ScopeConfiguration_Contents"></a>

 ** resourceScopes **   <a name="networksecuritymanager-Type-ScopeConfiguration-resourceScopes"></a>
The resource-level scoping configuration, keyed by resource type, that defines which resources within the selected accounts are in scope.
Type: String to [ResourceScope](API_ResourceScope.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Valid Keys: `AWS::ApiGateway::Stage | AWS::CloudFront::Distribution | AWS::EC2::EIP | AWS::ElasticLoadBalancingV2::LoadBalancer::application | AWS::ElasticLoadBalancing::LoadBalancer`
Required: Yes

 ** accountFilter **   <a name="networksecuritymanager-Type-ScopeConfiguration-accountFilter"></a>
The account filter that determines which accounts are in scope. When set, exactly one of `includeAll`, `include`, or `exclude` is set.
Organization administrators must include an account filter in every scope configuration. Single-account administrators must omit it: a scope without an account filter applies only to the administrator's own account. The presence of an account filter is fixed when the scope is created: an update can't add an account filter to a scope that was created without one, or remove the account filter from a scope that was created with one.
Type: [AccountFilter](API_AccountFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ScopeConfiguration)
