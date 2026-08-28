---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_PrincipalRoleEntitlement.html
---

# PrincipalRoleEntitlement
<a name="API_PrincipalRoleEntitlement"></a>

Specifies a principal-to-role entitlement that grants an IAM Identity Center principal permission to assume an IAM role.

## Contents
<a name="API_PrincipalRoleEntitlement_Contents"></a>

 ** principal **   <a name="accountaccess-Type-PrincipalRoleEntitlement-principal"></a>
The principal (user or group) that is granted access to assume the IAM role.
Type: [Principal](API_Principal.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** roleArn **   <a name="accountaccess-Type-PrincipalRoleEntitlement-roleArn"></a>
The ARN of the IAM role that the principal can assume.
Type: String
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/([a-zA-Z0-9+=,.@_-]+/)*[a-zA-Z0-9+=,.@_-]+`
Required: Yes

## See Also
<a name="API_PrincipalRoleEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/PrincipalRoleEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/PrincipalRoleEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/PrincipalRoleEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
