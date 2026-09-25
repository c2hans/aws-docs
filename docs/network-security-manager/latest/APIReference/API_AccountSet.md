---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AccountSet.html
---

# AccountSet
<a name="API_AccountSet"></a>

A set of AWS accounts and organizational units.

## Contents
<a name="API_AccountSet_Contents"></a>

 ** accountIds **   <a name="networksecuritymanager-Type-AccountSet-accountIds"></a>
The list of AWS account IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: No

 ** organizationalUnits **   <a name="networksecuritymanager-Type-AccountSet-organizationalUnits"></a>
The AWS Organizations organizational units (OUs) in the selection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 0. Maximum length of 68.
Required: No

## See Also
<a name="API_AccountSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AccountSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AccountSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AccountSet)
