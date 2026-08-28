---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListResourcePoliciesResponseResourcePolicy.html
---

# ListResourcePoliciesResponseResourcePolicy
<a name="API_ListResourcePoliciesResponseResourcePolicy"></a>

Contains details about a policy for a resource.

## Contents
<a name="API_ListResourcePoliciesResponseResourcePolicy_Contents"></a>

 ** PolicyArn **   <a name="mpa-Type-ListResourcePoliciesResponseResourcePolicy-PolicyArn"></a>
Amazon Resource Name (ARN) for policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** PolicyName **   <a name="mpa-Type-ListResourcePoliciesResponseResourcePolicy-PolicyName"></a>
Name of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** PolicyType **   <a name="mpa-Type-ListResourcePoliciesResponseResourcePolicy-PolicyType"></a>
The type of policy.
Type: String
Valid Values: `AWS_MANAGED | AWS_RAM`
Required: No

## See Also
<a name="API_ListResourcePoliciesResponseResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ListResourcePoliciesResponseResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ListResourcePoliciesResponseResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ListResourcePoliciesResponseResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
