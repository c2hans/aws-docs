---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackComplianceScoresFilters.html
---

# ConformancePackComplianceScoresFilters
<a name="API_ConformancePackComplianceScoresFilters"></a>

A list of filters to apply to the conformance pack compliance score result set.

## Contents
<a name="API_ConformancePackComplianceScoresFilters_Contents"></a>

 ** ConformancePackNames **   <a name="config-Type-ConformancePackComplianceScoresFilters-ConformancePackNames"></a>
The names of the conformance packs whose compliance scores you want to include in the conformance pack compliance score result set. You can include up to 25 conformance packs in the `ConformancePackNames` array of strings, each with a character limit of 256 characters for the conformance pack name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

## See Also
<a name="API_ConformancePackComplianceScoresFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackComplianceScoresFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackComplianceScoresFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackComplianceScoresFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
