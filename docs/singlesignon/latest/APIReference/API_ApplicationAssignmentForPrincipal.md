---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationAssignmentForPrincipal.html
---

# ApplicationAssignmentForPrincipal
<a name="API_ApplicationAssignmentForPrincipal"></a>

A structure that describes an application to which a principal is assigned.

## Contents
<a name="API_ApplicationAssignmentForPrincipal_Contents"></a>

 ** ApplicationArn **   <a name="singlesignon-Type-ApplicationAssignmentForPrincipal-ApplicationArn"></a>
The ARN of the application to which the specified principal is assigned.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** PrincipalId **   <a name="singlesignon-Type-ApplicationAssignmentForPrincipal-PrincipalId"></a>
The unique identifier of the principal assigned to the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** PrincipalType **   <a name="singlesignon-Type-ApplicationAssignmentForPrincipal-PrincipalType"></a>
The type of the principal assigned to the application.
Type: String
Valid Values: `USER | GROUP`
Required: No

## See Also
<a name="API_ApplicationAssignmentForPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ApplicationAssignmentForPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ApplicationAssignmentForPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ApplicationAssignmentForPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
