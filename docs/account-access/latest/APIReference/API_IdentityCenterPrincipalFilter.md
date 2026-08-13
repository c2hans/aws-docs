---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_IdentityCenterPrincipalFilter.html
---

# IdentityCenterPrincipalFilter
<a name="API_IdentityCenterPrincipalFilter"></a>

Specifies filter criteria for an IAM Identity Center principal.

## Contents
<a name="API_IdentityCenterPrincipalFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** groupId **   <a name="accountaccess-Type-IdentityCenterPrincipalFilter-groupId"></a>
The unique identifier of a group in IAM Identity Center to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** userId **   <a name="accountaccess-Type-IdentityCenterPrincipalFilter-userId"></a>
The unique identifier of a user in IAM Identity Center to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

## See Also
<a name="API_IdentityCenterPrincipalFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/IdentityCenterPrincipalFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/IdentityCenterPrincipalFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/IdentityCenterPrincipalFilter)
