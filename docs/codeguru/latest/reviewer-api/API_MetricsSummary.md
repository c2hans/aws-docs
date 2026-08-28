---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_MetricsSummary.html
---

# MetricsSummary
<a name="API_MetricsSummary"></a>

Information about metrics summaries.

## Contents
<a name="API_MetricsSummary_Contents"></a>

 ** FindingsCount **   <a name="reviewer-Type-MetricsSummary-FindingsCount"></a>
Total number of recommendations found in the code review.
Type: Long
Required: No

 ** MeteredLinesOfCodeCount **   <a name="reviewer-Type-MetricsSummary-MeteredLinesOfCodeCount"></a>
Lines of code metered in the code review. For the initial code review pull request and all subsequent revisions, this includes all lines of code in the files added to the pull request. In subsequent revisions, for files that already existed in the pull request, this includes only the changed lines of code. In both cases, this does not include non-code lines such as comments and import statements. For example, if you submit a pull request containing 5 files, each with 500 lines of code, and in a subsequent revision you added a new file with 200 lines of code, and also modified a total of 25 lines across the initial 5 files, `MeteredLinesOfCodeCount` includes the first 5 files (5 \* 500 = 2,500 lines), the new file (200 lines) and the 25 changed lines of code for a total of 2,725 lines of code.
Type: Long
Required: No

 ** SuppressedLinesOfCodeCount **   <a name="reviewer-Type-MetricsSummary-SuppressedLinesOfCodeCount"></a>
Lines of code suppressed in the code review based on the `excludeFiles` element in the `aws-codeguru-reviewer.yml` file. For full repository analyses, this number includes all lines of code in the files that are suppressed. For pull requests, this number only includes the *changed* lines of code that are suppressed. In both cases, this number does not include non-code lines such as comments and import statements. For example, if you initiate a full repository analysis on a repository containing 5 files, each file with 100 lines of code, and 2 files are listed as excluded in the `aws-codeguru-reviewer.yml` file, then `SuppressedLinesOfCodeCount` returns 200 (2 \* 100) as the total number of lines of code suppressed. However, if you submit a pull request for the same repository, then `SuppressedLinesOfCodeCount` only includes the lines in the 2 files that changed. If only 1 of the 2 files changed in the pull request, then `SuppressedLinesOfCodeCount` returns 100 (1 \* 100) as the total number of lines of code suppressed.
Type: Long
Required: No

## See Also
<a name="API_MetricsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/MetricsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/MetricsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/MetricsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
