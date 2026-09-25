---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceScope.html
---

# ResourceScope
<a name="API_ResourceScope"></a>

Defines which resources of a given type are in scope. Exactly one of `includeAll`, `include`, or `exclude` is set.

## Contents
<a name="API_ResourceScope_Contents"></a>

 ** exclude **   <a name="networksecuritymanager-Type-ResourceScope-exclude"></a>
Excludes the resources that match the specified criteria or explicit ARNs.
Type: [ResourceSet](API_ResourceSet.md) object
Required: No

 ** include **   <a name="networksecuritymanager-Type-ResourceScope-include"></a>
Includes the resources that match the specified criteria or explicit ARNs.
Type: [ResourceSet](API_ResourceSet.md) object
Required: No

 ** includeAll **   <a name="networksecuritymanager-Type-ResourceScope-includeAll"></a>
Includes all resources of the resource type.
Type: Boolean
Required: No

## See Also
<a name="API_ResourceScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceScope)
