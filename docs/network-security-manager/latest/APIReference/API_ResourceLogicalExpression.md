---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceLogicalExpression.html
---

# ResourceLogicalExpression
<a name="API_ResourceLogicalExpression"></a>

A logical expression that selects resources. Exactly one of `criteria`, `and`, `or`, or `not` is set.

## Contents
<a name="API_ResourceLogicalExpression_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** and **   <a name="networksecuritymanager-Type-ResourceLogicalExpression-and"></a>
A list of subexpressions that must all match.
Type: Array of [ResourceLogicalExpression](#API_ResourceLogicalExpression) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** criteria **   <a name="networksecuritymanager-Type-ResourceLogicalExpression-criteria"></a>
A leaf condition that matches resources by tag or by resource-type-specific configuration.
Type: [ResourceCriteria](API_ResourceCriteria.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** not **   <a name="networksecuritymanager-Type-ResourceLogicalExpression-not"></a>
A subexpression that must not match.
Type: [ResourceLogicalExpression](#API_ResourceLogicalExpression) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** or **   <a name="networksecuritymanager-Type-ResourceLogicalExpression-or"></a>
A list of subexpressions of which at least one must match.
Type: Array of [ResourceLogicalExpression](#API_ResourceLogicalExpression) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_ResourceLogicalExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceLogicalExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceLogicalExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceLogicalExpression)
