---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_JobInsights.html
---

# JobInsights
<a name="API_JobInsights"></a>

Contains insights for a job, including report status, and test-level aggregated metrics such as per test execution time and median test execution time.

## Contents
<a name="API_JobInsights_Contents"></a>

 ** status **   <a name="devicefarm-Type-JobInsights-status"></a>
The status of the insights report for the job.
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | SKIPPED | ERRORED`
Required: No

 ** testReport **   <a name="devicefarm-Type-JobInsights-testReport"></a>
The test-level aggregated report for the job.
Type: [TestReport](API_TestReport.md) object
Required: No

## See Also
<a name="API_JobInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/JobInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/JobInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/JobInsights)
