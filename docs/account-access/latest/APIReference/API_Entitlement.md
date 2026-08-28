---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_Entitlement.html
---

# Entitlement
<a name="API_Entitlement"></a>

Specifies the entitlement configuration for an account access manager application, defining which principal can assume which IAM role.

## Contents
<a name="API_Entitlement_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** principalRole **   <a name="accountaccess-Type-Entitlement-principalRole"></a>
The principal-to-role mapping for the entitlement.
Type: [PrincipalRoleEntitlement](API_PrincipalRoleEntitlement.md) object
Required: No

## See Also
<a name="API_Entitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/Entitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/Entitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/Entitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
