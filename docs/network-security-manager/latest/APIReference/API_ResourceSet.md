---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceSet.html
---

# ResourceSet
<a name="API_ResourceSet"></a>

A set of resources defined by explicit ARNs, a logical expression, or both.

## Contents
<a name="API_ResourceSet_Contents"></a>

 ** explicitArns **   <a name="networksecuritymanager-Type-ResourceSet-explicitArns"></a>
An explicit list of resource ARNs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** expression **   <a name="networksecuritymanager-Type-ResourceSet-expression"></a>
A logical expression that selects resources by combining criteria with AND, OR, and NOT operators.
Type: [ResourceLogicalExpression](API_ResourceLogicalExpression.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ResourceSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceSet)
