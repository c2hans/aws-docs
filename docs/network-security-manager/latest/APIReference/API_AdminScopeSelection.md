---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminScopeSelection.html
---

# AdminScopeSelection
<a name="API_AdminScopeSelection"></a>

A selection of accounts and organizational units. This is the reference form, which includes display metadata.

## Contents
<a name="API_AdminScopeSelection_Contents"></a>

 ** accounts **   <a name="networksecuritymanager-Type-AdminScopeSelection-accounts"></a>
The AWS accounts in the selection.
Type: Array of [AccountReference](API_AccountReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** organizationalUnits **   <a name="networksecuritymanager-Type-AdminScopeSelection-organizationalUnits"></a>
The AWS Organizations organizational units (OUs) in the selection.
Type: Array of [OrganizationalUnitReference](API_OrganizationalUnitReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

## See Also
<a name="API_AdminScopeSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminScopeSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminScopeSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminScopeSelection)
