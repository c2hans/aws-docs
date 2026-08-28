---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessAnalysisRule.html
---

# InternalAccessAnalysisRule
<a name="API_InternalAccessAnalysisRule"></a>

Contains information about analysis rules for the internal access analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

## Contents
<a name="API_InternalAccessAnalysisRule_Contents"></a>

 ** inclusions **   <a name="accessanalyzer-Type-InternalAccessAnalysisRule-inclusions"></a>
A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.
Type: Array of [InternalAccessAnalysisRuleCriteria](API_InternalAccessAnalysisRuleCriteria.md) objects
Required: No

## See Also
<a name="API_InternalAccessAnalysisRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessAnalysisRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
