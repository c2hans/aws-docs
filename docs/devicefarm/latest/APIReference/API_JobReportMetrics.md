---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_JobReportMetrics.html
---

# JobReportMetrics
<a name="API_JobReportMetrics"></a>

Contains aggregated metrics across all jobs in a run.

## Contents
<a name="API_JobReportMetrics_Contents"></a>

 ** averageJobExecutionDurationSeconds **   <a name="devicefarm-Type-JobReportMetrics-averageJobExecutionDurationSeconds"></a>
The average execution duration of jobs in the run, in seconds.
Type: Double
Required: No

 ** jobsErrored **   <a name="devicefarm-Type-JobReportMetrics-jobsErrored"></a>
The number of jobs that errored.
Type: Integer
Required: No

 ** jobsFailed **   <a name="devicefarm-Type-JobReportMetrics-jobsFailed"></a>
The number of jobs that failed.
Type: Integer
Required: No

 ** jobsPassed **   <a name="devicefarm-Type-JobReportMetrics-jobsPassed"></a>
The number of jobs that passed.
Type: Integer
Required: No

 ** jobsPassedPercentage **   <a name="devicefarm-Type-JobReportMetrics-jobsPassedPercentage"></a>
The percentage of jobs that passed.
Type: Double
Required: No

 ** jobsSkipped **   <a name="devicefarm-Type-JobReportMetrics-jobsSkipped"></a>
The number of jobs that were skipped.
Type: Integer
Required: No

 ** jobsStopped **   <a name="devicefarm-Type-JobReportMetrics-jobsStopped"></a>
The number of jobs that were stopped.
Type: Integer
Required: No

 ** jobsTotal **   <a name="devicefarm-Type-JobReportMetrics-jobsTotal"></a>
The total number of jobs in the run.
Type: Integer
Required: No

 ** medianJobExecutionDurationSeconds **   <a name="devicefarm-Type-JobReportMetrics-medianJobExecutionDurationSeconds"></a>
The median execution duration of jobs in the run, in seconds.
Type: Double
Required: No

 ** totalJobExecutionDurationSeconds **   <a name="devicefarm-Type-JobReportMetrics-totalJobExecutionDurationSeconds"></a>
The total execution duration of all jobs in the run, in seconds.
Type: Double
Required: No

## See Also
<a name="API_JobReportMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/JobReportMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/JobReportMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/JobReportMetrics)
