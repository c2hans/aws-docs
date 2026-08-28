---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CodeCoverageReportSummary.html
---

# CodeCoverageReportSummary
<a name="API_CodeCoverageReportSummary"></a>

Contains a summary of a code coverage report.

Line coverage measures how many statements your tests cover. A statement is a single instruction, not including comments, conditionals, etc.

Branch coverage determines if your tests cover every possible branch of a control structure, such as an `if` or `case` statement.

## Contents
<a name="API_CodeCoverageReportSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** branchCoveragePercentage **   <a name="CodeBuild-Type-CodeCoverageReportSummary-branchCoveragePercentage"></a>
The percentage of branches that are covered by your tests.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** branchesCovered **   <a name="CodeBuild-Type-CodeCoverageReportSummary-branchesCovered"></a>
The number of conditional branches that are covered by your tests.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** branchesMissed **   <a name="CodeBuild-Type-CodeCoverageReportSummary-branchesMissed"></a>
The number of conditional branches that are not covered by your tests.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** lineCoveragePercentage **   <a name="CodeBuild-Type-CodeCoverageReportSummary-lineCoveragePercentage"></a>
The percentage of lines that are covered by your tests.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** linesCovered **   <a name="CodeBuild-Type-CodeCoverageReportSummary-linesCovered"></a>
The number of lines that are covered by your tests.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** linesMissed **   <a name="CodeBuild-Type-CodeCoverageReportSummary-linesMissed"></a>
The number of lines that are not covered by your tests.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CodeCoverageReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/CodeCoverageReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/CodeCoverageReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/CodeCoverageReportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
