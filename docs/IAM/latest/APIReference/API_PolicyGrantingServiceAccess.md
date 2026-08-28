---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyGrantingServiceAccess.html
---

# PolicyGrantingServiceAccess
<a name="API_PolicyGrantingServiceAccess"></a>

Contains details about the permissions policies that are attached to the specified identity (user, group, or role).

This data type is an element of the [ListPoliciesGrantingServiceAccessEntry](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccessEntry.html) object.

## Contents
<a name="API_PolicyGrantingServiceAccess_Contents"></a>

 ** PolicyName **
The policy name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** PolicyType **
The policy type. For more information about these policy types, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.
Type: String
Valid Values: `INLINE | MANAGED`
Required: Yes

 ** EntityName **
The name of the entity (user or role) to which the inline policy is attached.
This field is null for managed policies. For more information about these policy types, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** EntityType **
The type of entity (user or role) that used the policy to access the service to which the inline policy is attached.
This field is null for managed policies. For more information about these policy types, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the *IAM User Guide*.
Type: String
Valid Values: `USER | ROLE | GROUP`
Required: No

 ** PolicyArn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_PolicyGrantingServiceAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PolicyGrantingServiceAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PolicyGrantingServiceAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PolicyGrantingServiceAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
