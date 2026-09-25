---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceAssociation.html
---

# ResourceAssociation
<a name="API_ResourceAssociation"></a>

Describes an association between a resource and another entity.

## Contents
<a name="API_ResourceAssociation_Contents"></a>

 ** arn **   <a name="networksecuritymanager-Type-ResourceAssociation-arn"></a>
The ARN of the associated resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** resourceType **   <a name="networksecuritymanager-Type-ResourceAssociation-resourceType"></a>
The type of the associated resource, such as `Policy`, `Template`, or `Deployment`.
Type: String
Valid Values: `Rule | Template | Policy | Deployment | Scope`
Required: Yes

## See Also
<a name="API_ResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceAssociation)
