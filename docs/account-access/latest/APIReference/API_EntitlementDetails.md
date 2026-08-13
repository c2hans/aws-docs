---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_EntitlementDetails.html
---

# EntitlementDetails
<a name="API_EntitlementDetails"></a>

Contains detailed information about an entitlement, including the principal, IAM role, and target account.

## Contents
<a name="API_EntitlementDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** principalRole **   <a name="accountaccess-Type-EntitlementDetails-principalRole"></a>
The principal-to-role mapping details for the entitlement, including the target account.
Type: [PrincipalRoleEntitlementDetails](API_PrincipalRoleEntitlementDetails.md) object
Required: No

## See Also
<a name="API_EntitlementDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/EntitlementDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/EntitlementDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/EntitlementDetails)
