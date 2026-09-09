---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringJobDefinitionSummary.html
---

# MonitoringJobDefinitionSummary
<a name="API_MonitoringJobDefinitionSummary"></a>

Summary information about a monitoring job.

## Contents
<a name="API_MonitoringJobDefinitionSummary_Contents"></a>

 ** EndpointName **   <a name="sagemaker-Type-MonitoringJobDefinitionSummary-EndpointName"></a>
The name of the endpoint that the job monitors.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** MonitoringJobDefinitionArn **   <a name="sagemaker-Type-MonitoringJobDefinitionSummary-MonitoringJobDefinitionArn"></a>
The Amazon Resource Name (ARN) of the monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** MonitoringJobDefinitionName **   <a name="sagemaker-Type-MonitoringJobDefinitionSummary-MonitoringJobDefinitionName"></a>
The name of the monitoring job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## See Also
<a name="API_MonitoringJobDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringJobDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringJobDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringJobDefinitionSummary)
