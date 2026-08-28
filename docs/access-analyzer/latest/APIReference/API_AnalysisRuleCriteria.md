---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalysisRuleCriteria.html
---

# AnalysisRuleCriteria
<a name="API_AnalysisRuleCriteria"></a>

The criteria for an analysis rule for an analyzer. The criteria determine which entities will generate findings.

## Contents
<a name="API_AnalysisRuleCriteria_Contents"></a>

 ** accountIds **   <a name="accessanalyzer-Type-AnalysisRuleCriteria-accountIds"></a>
A list of AWS account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.
Type: Array of strings
Required: No

 ** resourceTags **   <a name="accessanalyzer-Type-AnalysisRuleCriteria-resourceTags"></a>
An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.
For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.
Type: Array of string to string maps
Required: No

## See Also
<a name="API_AnalysisRuleCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalysisRuleCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalysisRuleCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalysisRuleCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
