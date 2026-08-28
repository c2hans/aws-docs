---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AccountAssignment.html
---

# AccountAssignment
<a name="API_AccountAssignment"></a>

The assignment that indicates a principal's limited access to a specified AWS account with a specified permission set.

**Note**
The term *principal* here refers to a user or group that is defined in IAM Identity Center.

## Contents
<a name="API_AccountAssignment_Contents"></a>

 ** AccountId **   <a name="singlesignon-Type-AccountAssignment-AccountId"></a>
The identifier of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** PermissionSetArn **   <a name="singlesignon-Type-AccountAssignment-PermissionSetArn"></a>
The ARN of the permission set. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}`
Required: No

 ** PrincipalId **   <a name="singlesignon-Type-AccountAssignment-PrincipalId"></a>
An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the [IAM Identity Center Identity Store API Reference](/singlesignon/latest/IdentityStoreAPIReference/welcome.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** PrincipalType **   <a name="singlesignon-Type-AccountAssignment-PrincipalType"></a>
The entity type for which the assignment will be created.
Type: String
Valid Values: `USER | GROUP`
Required: No

## See Also
<a name="API_AccountAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AccountAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AccountAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AccountAssignment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
