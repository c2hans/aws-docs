---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_PrincipalRoleEntitlementFilter.html
---

# PrincipalRoleEntitlementFilter
<a name="API_PrincipalRoleEntitlementFilter"></a>

Specifies filter criteria for principal-to-role entitlements. All specified criteria must match for an entitlement to be returned.

## Contents
<a name="API_PrincipalRoleEntitlementFilter_Contents"></a>

 ** account **   <a name="accountaccess-Type-PrincipalRoleEntitlementFilter-account"></a>
The 12-digit AWS account ID to filter entitlements by.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** principal **   <a name="accountaccess-Type-PrincipalRoleEntitlementFilter-principal"></a>
The principal to filter entitlements by.
Type: [PrincipalFilter](API_PrincipalFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** roleArn **   <a name="accountaccess-Type-PrincipalRoleEntitlementFilter-roleArn"></a>
The IAM role ARN to filter entitlements by.
Type: String
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/([a-zA-Z0-9+=,.@_-]+/)*[a-zA-Z0-9+=,.@_-]+`
Required: No

## See Also
<a name="API_PrincipalRoleEntitlementFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/PrincipalRoleEntitlementFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/PrincipalRoleEntitlementFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/PrincipalRoleEntitlementFilter)
