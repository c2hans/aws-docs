---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_PrincipalFilter.html
---

# PrincipalFilter
<a name="API_PrincipalFilter"></a>

Specifies filter criteria for a principal.

## Contents
<a name="API_PrincipalFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** identityCenter **   <a name="accountaccess-Type-PrincipalFilter-identityCenter"></a>
The IAM Identity Center principal filter criteria.
Type: [IdentityCenterPrincipalFilter](API_IdentityCenterPrincipalFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PrincipalFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/PrincipalFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/PrincipalFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/PrincipalFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
