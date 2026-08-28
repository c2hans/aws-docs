---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedAccessConfiguration.html
---

# UnusedAccessConfiguration
<a name="API_UnusedAccessConfiguration"></a>

Contains information about an unused access analyzer.

## Contents
<a name="API_UnusedAccessConfiguration_Contents"></a>

 ** analysisRule **   <a name="accessanalyzer-Type-UnusedAccessConfiguration-analysisRule"></a>
Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.
Type: [AnalysisRule](API_AnalysisRule.md) object
Required: No

 ** unusedAccessAge **   <a name="accessanalyzer-Type-UnusedAccessConfiguration-unusedAccessAge"></a>
The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.
Type: Integer
Required: No

## See Also
<a name="API_UnusedAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedAccessConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
