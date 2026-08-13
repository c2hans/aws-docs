---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestReportMetrics.html
---

# TestReportMetrics
<a name="API_TestReportMetrics"></a>

Contains aggregated metrics across all tests in a job.

## Contents
<a name="API_TestReportMetrics_Contents"></a>

 ** medianTestExecutionDurationSeconds **   <a name="devicefarm-Type-TestReportMetrics-medianTestExecutionDurationSeconds"></a>
The median execution duration of tests in the job, in seconds.
Type: Double
Required: No

 ** testsErrored **   <a name="devicefarm-Type-TestReportMetrics-testsErrored"></a>
The number of tests that errored.
Type: Integer
Required: No

 ** testsFailed **   <a name="devicefarm-Type-TestReportMetrics-testsFailed"></a>
The number of tests that failed.
Type: Integer
Required: No

 ** testsOther **   <a name="devicefarm-Type-TestReportMetrics-testsOther"></a>
The number of tests with other result types.
Type: Integer
Required: No

 ** testsPassed **   <a name="devicefarm-Type-TestReportMetrics-testsPassed"></a>
The number of tests that passed.
Type: Integer
Required: No

 ** testsPassedPercentage **   <a name="devicefarm-Type-TestReportMetrics-testsPassedPercentage"></a>
The percentage of tests that passed.
Type: Double
Required: No

 ** testsSkipped **   <a name="devicefarm-Type-TestReportMetrics-testsSkipped"></a>
The number of tests that were skipped.
Type: Integer
Required: No

 ** testsTotal **   <a name="devicefarm-Type-TestReportMetrics-testsTotal"></a>
The total number of tests in the job.
Type: Integer
Required: No

 ** totalTestExecutionDurationSeconds **   <a name="devicefarm-Type-TestReportMetrics-totalTestExecutionDurationSeconds"></a>
The total execution duration of all tests in the job, in seconds.
Type: Double
Required: No

## See Also
<a name="API_TestReportMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestReportMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestReportMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestReportMetrics)
