---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html
---

# Policy
<a name="API_Policy"></a>

An AWS Firewall Manager policy.

## Contents
<a name="API_Policy_Contents"></a>

 ** ExcludeResourceTags **   <a name="fms-Type-Policy-ExcludeResourceTags"></a>
If set to `True`, resources with the tags that are specified in the `ResourceTag` array are not in scope of the policy. If set to `False`, and the `ResourceTag` array is not null, only resources with the specified tags are in scope of the policy.
Type: Boolean
Required: Yes

 ** PolicyName **   <a name="fms-Type-Policy-PolicyName"></a>
The name of the AWS Firewall Manager policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** RemediationEnabled **   <a name="fms-Type-Policy-RemediationEnabled"></a>
Indicates if the policy should be automatically applied to new resources.
Type: Boolean
Required: Yes

 ** ResourceType **   <a name="fms-Type-Policy-ResourceType"></a>
The type of resource protected by or in scope of the policy. This is in the format shown in the [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html). To apply this policy to multiple resource types, specify a resource type of `ResourceTypeList` and then specify the resource types in a `ResourceTypeList`.
The following are valid resource types for each Firewall Manager policy type:
+  AWS WAF Classic - `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, and `AWS::ElasticLoadBalancingV2::LoadBalancer`.
+  AWS WAF - `AWS::ApiGateway::Stage`, `AWS::ElasticLoadBalancingV2::LoadBalancer`, and `AWS::CloudFront::Distribution`.
+ Shield Advanced - `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::EC2::EIP`, and `AWS::CloudFront::Distribution`.
+ Network ACL - `AWS::EC2::Subnet`.
+ Security group usage audit - `AWS::EC2::SecurityGroup`.
+ Security group content audit - `AWS::EC2::SecurityGroup`, `AWS::EC2::NetworkInterface`, and `AWS::EC2::Instance`.
+ DNS Firewall, AWS Network Firewall, and third-party firewall - `AWS::EC2::VPC`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** SecurityServicePolicyData **   <a name="fms-Type-Policy-SecurityServicePolicyData"></a>
Details about the security service that is being used to protect the resources.
Type: [SecurityServicePolicyData](API_SecurityServicePolicyData.md) object
Required: Yes

 ** DeleteUnusedFMManagedResources **   <a name="fms-Type-Policy-DeleteUnusedFMManagedResources"></a>
Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.
By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.
This option is not available for Shield Advanced or AWS WAF Classic policies.
Type: Boolean
Required: No

 ** ExcludeMap **   <a name="fms-Type-Policy-ExcludeMap"></a>
Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap`, AWS Firewall Manager applies the policy to all accounts specified by the `IncludeMap`, and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap`, then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap`.
You can specify account IDs, OUs, or a combination:
+ Specify account IDs by setting the key to `ACCOUNT`. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
+ Specify OUs by setting the key to `ORG_UNIT`. For example, the following is a valid map: `{“ORG_UNIT” : [“ouid111”, “ouid112”]}`.
+ Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”], “ORG_UNIT” : [“ouid111”, “ouid112”]}`.
Type: String to array of strings map
Valid Keys: `ACCOUNT | ORG_UNIT`
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** IncludeMap **   <a name="fms-Type-Policy-IncludeMap"></a>
Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap`, AWS Firewall Manager applies the policy to all accounts specified by the `IncludeMap`, and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap`, then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap`.
You can specify account IDs, OUs, or a combination:
+ Specify account IDs by setting the key to `ACCOUNT`. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
+ Specify OUs by setting the key to `ORG_UNIT`. For example, the following is a valid map: `{“ORG_UNIT” : [“ouid111”, “ouid112”]}`.
+ Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”], “ORG_UNIT” : [“ouid111”, “ouid112”]}`.
Type: String to array of strings map
Valid Keys: `ACCOUNT | ORG_UNIT`
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PolicyDescription **   <a name="fms-Type-Policy-PolicyDescription"></a>
Your description of the AWS Firewall Manager policy.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PolicyId **   <a name="fms-Type-Policy-PolicyId"></a>
The ID of the AWS Firewall Manager policy.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** PolicyStatus **   <a name="fms-Type-Policy-PolicyStatus"></a>
Indicates whether the policy is in or out of an admin's policy or Region scope.
+  `ACTIVE` - The administrator can manage and delete the policy.
+  `OUT_OF_ADMIN_SCOPE` - The administrator can view the policy, but they can't edit or delete the policy. Existing policy protections stay in place. Any new resources that come into scope of the policy won't be protected.
Type: String
Valid Values: `ACTIVE | OUT_OF_ADMIN_SCOPE`
Required: No

 ** PolicyUpdateToken **   <a name="fms-Type-Policy-PolicyUpdateToken"></a>
A unique identifier for each update to the policy. When issuing a `PutPolicy` request, the `PolicyUpdateToken` in the request must match the `PolicyUpdateToken` of the current policy version. To get the `PolicyUpdateToken` of the current policy version, use a `GetPolicy` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ResourceSetIds **   <a name="fms-Type-Policy-ResourceSetIds"></a>
The unique identifiers of the resource sets used by the policy.
Type: Array of strings
Length Constraints: Fixed length of 22.
Pattern: `^[a-z0-9A-Z]{22}$`
Required: No

 ** ResourceTagLogicalOperator **   <a name="fms-Type-Policy-ResourceTagLogicalOperator"></a>
Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.
Default: `AND`
Type: String
Valid Values: `AND | OR`
Required: No

 ** ResourceTags **   <a name="fms-Type-Policy-ResourceTags"></a>
An array of `ResourceTag` objects.
Type: Array of [ResourceTag](API_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ResourceTypeList **   <a name="fms-Type-Policy-ResourceTypeList"></a>
An array of `ResourceType` objects. Use this only to specify multiple resource types. To specify a single resource type, use `ResourceType`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_Policy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/Policy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/Policy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/Policy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
