---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestReportSummary.html
---

# TestReportSummary
<a name="API_TestReportSummary"></a>

 Information about a test report.

## Contents
<a name="API_TestReportSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** durationInNanoSeconds **   <a name="CodeBuild-Type-TestReportSummary-durationInNanoSeconds"></a>
 The number of nanoseconds it took to run all of the test cases in this report.
Type: Long
Required: Yes

 ** statusCounts **   <a name="CodeBuild-Type-TestReportSummary-statusCounts"></a>
 A map that contains the number of each type of status returned by the test results in this `TestReportSummary`.
Type: String to integer map
Required: Yes

 ** total **   <a name="CodeBuild-Type-TestReportSummary-total"></a>
 The number of test cases in this `TestReportSummary`. The total includes truncated test cases.
Type: Integer
Required: Yes

## See Also
<a name="API_TestReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/TestReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/TestReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/TestReportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
