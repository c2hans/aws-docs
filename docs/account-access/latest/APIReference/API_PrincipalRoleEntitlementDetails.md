---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_PrincipalRoleEntitlementDetails.html
---

# PrincipalRoleEntitlementDetails
<a name="API_PrincipalRoleEntitlementDetails"></a>

Contains detailed information about a principal-to-role entitlement, including the target account.

## Contents
<a name="API_PrincipalRoleEntitlementDetails_Contents"></a>

 ** account **   <a name="accountaccess-Type-PrincipalRoleEntitlementDetails-account"></a>
The 12-digit AWS account ID where the IAM role resides.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** principal **   <a name="accountaccess-Type-PrincipalRoleEntitlementDetails-principal"></a>
The principal (user or group) that is granted access to assume the IAM role.
Type: [Principal](API_Principal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** roleArn **   <a name="accountaccess-Type-PrincipalRoleEntitlementDetails-roleArn"></a>
The ARN of the IAM role that the principal can assume.
Type: String
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/([a-zA-Z0-9+=,.@_-]+/)*[a-zA-Z0-9+=,.@_-]+`
Required: Yes

 ** accountName **   <a name="accountaccess-Type-PrincipalRoleEntitlementDetails-accountName"></a>
The friendly name of the AWS account where the IAM role resides.
Type: String
Required: No

## See Also
<a name="API_PrincipalRoleEntitlementDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/PrincipalRoleEntitlementDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/PrincipalRoleEntitlementDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/PrincipalRoleEntitlementDetails)
