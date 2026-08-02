---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobProgressSummary.html
---

# JobProgressSummary
<a name="API_control_JobProgressSummary"></a>

Describes the total number of tasks that the specified job has started, the number of tasks that succeeded, and the number of tasks that failed.

## Contents
<a name="API_control_JobProgressSummary_Contents"></a>

 ** NumberOfTasksFailed **   <a name="AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed"></a>

Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** NumberOfTasksSucceeded **   <a name="AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded"></a>

Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Timers **   <a name="AmazonS3-Type-control_JobProgressSummary-Timers"></a>
The JobTimers attribute of a job's progress summary.
Type: [JobTimers](API_control_JobTimers.md) data type
Required: No

 ** TotalNumberOfTasks **   <a name="AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks"></a>

Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_control_JobProgressSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobProgressSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobProgressSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobProgressSummary)
