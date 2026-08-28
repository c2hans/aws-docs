---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageStringFilter.html
---

# CoverageStringFilter
<a name="API_CoverageStringFilter"></a>

Contains details of a coverage string filter.

## Contents
<a name="API_CoverageStringFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-CoverageStringFilter-comparison"></a>
The operator to compare strings on.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-CoverageStringFilter-value"></a>
The value to compare strings on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_CoverageStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CoverageStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CoverageStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CoverageStringFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
