---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminScopeSelectionInput.html
---

# AdminScopeSelectionInput
<a name="API_AdminScopeSelectionInput"></a>

A selection of accounts and organizational units. This is the input form, which uses account and organizational unit IDs.

## Contents
<a name="API_AdminScopeSelectionInput_Contents"></a>

 ** accounts **   <a name="networksecuritymanager-Type-AdminScopeSelectionInput-accounts"></a>
The AWS accounts in the selection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: No

 ** organizationalUnits **   <a name="networksecuritymanager-Type-AdminScopeSelectionInput-organizationalUnits"></a>
The AWS Organizations organizational units (OUs) in the selection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_AdminScopeSelectionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminScopeSelectionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminScopeSelectionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminScopeSelectionInput)
