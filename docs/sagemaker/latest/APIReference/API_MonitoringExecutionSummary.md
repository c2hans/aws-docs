---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringExecutionSummary.html
---

# MonitoringExecutionSummary
<a name="API_MonitoringExecutionSummary"></a>

Summary of information about the last monitoring job to run.

## Contents
<a name="API_MonitoringExecutionSummary_Contents"></a>

 ** MonitoringExecutionStatus **   <a name="sagemaker-Type-MonitoringExecutionSummary-MonitoringExecutionStatus"></a>
The status of the monitoring job.
Type: String
Valid Values: `Pending | Completed | CompletedWithViolations | InProgress | Failed | Stopping | Stopped`
Required: Yes

 ** MonitoringScheduleName **   <a name="sagemaker-Type-MonitoringExecutionSummary-MonitoringScheduleName"></a>
The name of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** EndpointName **   <a name="sagemaker-Type-MonitoringExecutionSummary-EndpointName"></a>
The name of the endpoint used to run the monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-MonitoringExecutionSummary-FailureReason"></a>
Contains the reason a monitoring job failed, if it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** MonitoringJobDefinitionName **   <a name="sagemaker-Type-MonitoringExecutionSummary-MonitoringJobDefinitionName"></a>
The name of the monitoring job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** MonitoringType **   <a name="sagemaker-Type-MonitoringExecutionSummary-MonitoringType"></a>
The type of the monitoring job.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

 ** ProcessingJobArn **   <a name="sagemaker-Type-MonitoringExecutionSummary-ProcessingJobArn"></a>
The Amazon Resource Name (ARN) of the monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## See Also
<a name="API_MonitoringExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringExecutionSummary)
