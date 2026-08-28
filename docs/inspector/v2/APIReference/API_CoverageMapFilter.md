---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoverageMapFilter.html
---

# CoverageMapFilter
<a name="API_CoverageMapFilter"></a>

Contains details of a coverage map filter.

## Contents
<a name="API_CoverageMapFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-CoverageMapFilter-comparison"></a>
The operator to compare coverage on.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** key **   <a name="inspector2-Type-CoverageMapFilter-key"></a>
The tag key associated with the coverage map filter.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** value **   <a name="inspector2-Type-CoverageMapFilter-value"></a>
The tag value associated with the coverage map filter.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CoverageMapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CoverageMapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CoverageMapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CoverageMapFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
