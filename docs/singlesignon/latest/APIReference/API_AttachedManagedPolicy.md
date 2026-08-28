---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachedManagedPolicy.html
---

# AttachedManagedPolicy
<a name="API_AttachedManagedPolicy"></a>

A structure that stores a list of managed policy ARNs that describe the associated AWS managed policy.

## Contents
<a name="API_AttachedManagedPolicy_Contents"></a>

 ** Arn **   <a name="singlesignon-Type-AttachedManagedPolicy-Arn"></a>
The ARN of the AWS managed policy. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:iam::aws:policy((/[A-Za-z0-9\.,\+@=_-]+)*)/([A-Za-z0-9\.,\+=@_-]+)`
Required: No

 ** Name **   <a name="singlesignon-Type-AttachedManagedPolicy-Name"></a>
The name of the AWS managed policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_AttachedManagedPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AttachedManagedPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AttachedManagedPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AttachedManagedPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
