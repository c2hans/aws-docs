---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PolicyIdentifier.html
---

# PolicyIdentifier
<a name="API_PolicyIdentifier"></a>

Identifies one or more policies as a union type. Specify exactly one of `PolicyType`, `PolicyArn`, or `InlinePolicyIdentifier` to identify policies by their type, by Amazon Resource Name (ARN), or by the name of an inline policy and the entity it is attached to.

## Contents
<a name="API_PolicyIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** InlinePolicyIdentifier **
An inline policy identifier consisting of a policy name and the entity it is attached to. Wildcard characters (`*` and `?`) in the entity name can match multiple entities.
Type: [InlinePolicyIdentifierType](API_InlinePolicyIdentifierType.md) object
Required: No

 ** PolicyArn **
The Amazon Resource Name (ARN) of an AWS managed policy or a customer managed policy that is attached to an IAM user, group, or role. Wildcard characters are supported in the resource name portion of the ARN to match multiple managed policies: use at most one `*` (matches any sequence of characters, including none), and any number of `?` (each matches exactly one character).
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** PolicyType **
The policy type to identify. All policies of the specified type are matched.
Type: String
Valid Values: `inline | aws-managed | user-managed | permission-boundary | scp | rcp`
Required: No

## See Also
<a name="API_PolicyIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PolicyIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PolicyIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PolicyIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
