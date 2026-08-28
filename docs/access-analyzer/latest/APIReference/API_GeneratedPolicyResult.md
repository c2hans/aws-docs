---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GeneratedPolicyResult.html
---

# GeneratedPolicyResult
<a name="API_GeneratedPolicyResult"></a>

Contains the text for the generated policy and its details.

## Contents
<a name="API_GeneratedPolicyResult_Contents"></a>

 ** properties **   <a name="accessanalyzer-Type-GeneratedPolicyResult-properties"></a>
A `GeneratedPolicyProperties` object that contains properties of the generated policy.
Type: [GeneratedPolicyProperties](API_GeneratedPolicyProperties.md) object
Required: Yes

 ** generatedPolicies **   <a name="accessanalyzer-Type-GeneratedPolicyResult-generatedPolicies"></a>
The text to use as the content for the new policy. The policy is created using the [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html) action.
Type: Array of [GeneratedPolicy](API_GeneratedPolicy.md) objects
Required: No

## See Also
<a name="API_GeneratedPolicyResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GeneratedPolicyResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GeneratedPolicyResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GeneratedPolicyResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
