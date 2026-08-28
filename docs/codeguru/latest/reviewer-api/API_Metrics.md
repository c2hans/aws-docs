---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Metrics.html
---

# Metrics
<a name="API_Metrics"></a>

Information about the statistics from the code review.

## Contents
<a name="API_Metrics_Contents"></a>

 ** FindingsCount **   <a name="reviewer-Type-Metrics-FindingsCount"></a>
Total number of recommendations found in the code review.
Type: Long
Required: No

 ** MeteredLinesOfCodeCount **   <a name="reviewer-Type-Metrics-MeteredLinesOfCodeCount"></a>
 `MeteredLinesOfCodeCount` is the number of lines of code in the repository where the code review happened. This does not include non-code lines such as comments and blank lines.
Type: Long
Required: No

 ** SuppressedLinesOfCodeCount **   <a name="reviewer-Type-Metrics-SuppressedLinesOfCodeCount"></a>
 `SuppressedLinesOfCodeCount` is the number of lines of code in the repository where the code review happened that CodeGuru Reviewer did not analyze. The lines suppressed in the analysis is based on the `excludeFiles` variable in the `aws-codeguru-reviewer.yml` file. This number does not include non-code lines such as comments and blank lines.
Type: Long
Required: No

## See Also
<a name="API_Metrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/Metrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/Metrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/Metrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
