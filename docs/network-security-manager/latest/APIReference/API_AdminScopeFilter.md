---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminScopeFilter.html
---

# AdminScopeFilter
<a name="API_AdminScopeFilter"></a>

Determines which accounts and organizational units are in an administrator's scope. This is the reference form, which includes display metadata.

## Contents
<a name="API_AdminScopeFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** excludeOnly **   <a name="networksecuritymanager-Type-AdminScopeFilter-excludeOnly"></a>
The accounts and organizational units to exclude from the administrator's scope. All others are in scope.
Type: [AdminScopeSelection](API_AdminScopeSelection.md) object
Required: No

 ** includeAll **   <a name="networksecuritymanager-Type-AdminScopeFilter-includeAll"></a>
All accounts and organizational units are in scope.
Type: Structure
Required: No

 ** includeOnly **   <a name="networksecuritymanager-Type-AdminScopeFilter-includeOnly"></a>
Only the specified accounts and organizational units are in the administrator's scope.
Type: [AdminScopeSelection](API_AdminScopeSelection.md) object
Required: No

## See Also
<a name="API_AdminScopeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminScopeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminScopeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminScopeFilter)
