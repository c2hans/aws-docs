---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Report.html
---

# Report
<a name="API_Report"></a>

Information about the results from running a series of test cases during the run of a build project. The test cases are specified in the buildspec for the build project using one or more paths to the test case files. You can specify any type of tests you want, such as unit tests, integration tests, and functional tests.

## Contents
<a name="API_Report_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="CodeBuild-Type-Report-arn"></a>
 The ARN of the report run.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** codeCoverageSummary **   <a name="CodeBuild-Type-Report-codeCoverageSummary"></a>
A `CodeCoverageReportSummary` object that contains a code coverage summary for this report.
Type: [CodeCoverageReportSummary](API_CodeCoverageReportSummary.md) object
Required: No

 ** created **   <a name="CodeBuild-Type-Report-created"></a>
 The date and time this report run occurred.
Type: Timestamp
Required: No

 ** executionId **   <a name="CodeBuild-Type-Report-executionId"></a>
 The ARN of the build run that generated this report.
Type: String
Required: No

 ** expired **   <a name="CodeBuild-Type-Report-expired"></a>
 The date and time a report expires. A report expires 30 days after it is created. An expired report is not available to view in CodeBuild.
Type: Timestamp
Required: No

 ** exportConfig **   <a name="CodeBuild-Type-Report-exportConfig"></a>
 Information about where the raw data used to generate this report was exported.
Type: [ReportExportConfig](API_ReportExportConfig.md) object
Required: No

 ** name **   <a name="CodeBuild-Type-Report-name"></a>
 The name of the report that was run.
Type: String
Required: No

 ** reportGroupArn **   <a name="CodeBuild-Type-Report-reportGroupArn"></a>
 The ARN of the report group associated with this report.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** status **   <a name="CodeBuild-Type-Report-status"></a>
 The status of this report.
Type: String
Valid Values: `GENERATING | SUCCEEDED | FAILED | INCOMPLETE | DELETING`
Required: No

 ** testSummary **   <a name="CodeBuild-Type-Report-testSummary"></a>
 A `TestReportSummary` object that contains information about this test report.
Type: [TestReportSummary](API_TestReportSummary.md) object
Required: No

 ** truncated **   <a name="CodeBuild-Type-Report-truncated"></a>
 A boolean that specifies if this report run is truncated. The list of test cases is truncated after the maximum number of test cases is reached.
Type: Boolean
Required: No

 ** type **   <a name="CodeBuild-Type-Report-type"></a>
The type of the report that was run.
CODE\_COVERAGE
A code coverage report.
TEST
A test report.
Type: String
Valid Values: `TEST | CODE_COVERAGE`
Required: No

## See Also
<a name="API_Report_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Report)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Report)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Report)
