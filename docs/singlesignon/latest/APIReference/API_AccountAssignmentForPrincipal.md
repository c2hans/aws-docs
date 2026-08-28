---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AccountAssignmentForPrincipal.html
---

# AccountAssignmentForPrincipal
<a name="API_AccountAssignmentForPrincipal"></a>

A structure that describes an assignment of an AWS account to a principal and the permissions that principal has in the account.

## Contents
<a name="API_AccountAssignmentForPrincipal_Contents"></a>

 ** AccountId **   <a name="singlesignon-Type-AccountAssignmentForPrincipal-AccountId"></a>
The account ID number of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** PermissionSetArn **   <a name="singlesignon-Type-AccountAssignmentForPrincipal-PermissionSetArn"></a>
The ARN of the IAM Identity Center permission set assigned to this principal for this AWS account.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: No

 ** PrincipalId **   <a name="singlesignon-Type-AccountAssignmentForPrincipal-PrincipalId"></a>
The ID of the principal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** PrincipalType **   <a name="singlesignon-Type-AccountAssignmentForPrincipal-PrincipalType"></a>
The type of the principal.
Type: String
Valid Values: `USER | GROUP`
Required: No

## See Also
<a name="API_AccountAssignmentForPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AccountAssignmentForPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AccountAssignmentForPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AccountAssignmentForPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
