---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceCriteria.html
---

# ResourceCriteria
<a name="API_ResourceCriteria"></a>

A leaf condition that matches resources by tag or by resource-type-specific configuration.

## Contents
<a name="API_ResourceCriteria_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** albConfig **   <a name="networksecuritymanager-Type-ResourceCriteria-albConfig"></a>
Filter criteria specific to Application Load Balancers.
Type: [AlbConfiguration](API_AlbConfiguration.md) object
Required: No

 ** tags **   <a name="networksecuritymanager-Type-ResourceCriteria-tags"></a>
Tag key-value pairs used to match resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ResourceCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceCriteria)
