---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_UserPolicyGrantPrincipal.html
---

# UserPolicyGrantPrincipal
<a name="API_UserPolicyGrantPrincipal"></a>

The user policy grant principal.

## Contents
<a name="API_UserPolicyGrantPrincipal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** allUsersGrantFilter **   <a name="datazone-Type-UserPolicyGrantPrincipal-allUsersGrantFilter"></a>
The all users grant filter of the user policy grant principal.
Type: [AllUsersGrantFilter](API_AllUsersGrantFilter.md) object
Required: No

 ** userIdentifier **   <a name="datazone-Type-UserPolicyGrantPrincipal-userIdentifier"></a>
The user ID of the user policy grant principal.
Type: String
Pattern: `.*(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$).*`
Required: No

## See Also
<a name="API_UserPolicyGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/UserPolicyGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/UserPolicyGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/UserPolicyGrantPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
