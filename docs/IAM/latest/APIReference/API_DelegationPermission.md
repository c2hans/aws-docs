---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DelegationPermission.html
---

# DelegationPermission
<a name="API_DelegationPermission"></a>

Contains information about the permissions being delegated in a delegation request.

## Contents
<a name="API_DelegationPermission_Contents"></a>

 ** Parameters.member.N **
A list of policy parameters that define the scope and constraints of the delegated permissions.
Type: Array of [PolicyParameter](API_PolicyParameter.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** PolicyTemplateArn **
This ARN maps to a pre-registered policy content for this partner. See the [partner onboarding documentation]() to understand how to create a delegation template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_DelegationPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DelegationPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DelegationPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DelegationPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
