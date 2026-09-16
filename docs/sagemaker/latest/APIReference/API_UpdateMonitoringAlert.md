---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMonitoringAlert.html
---

# UpdateMonitoringAlert
<a name="API_UpdateMonitoringAlert"></a>

Update the parameters of a model monitor alert.

## Request Syntax
<a name="API_UpdateMonitoringAlert_RequestSyntax"></a>

```
{
   "DatapointsToAlert": {{number}},
   "EvaluationPeriod": {{number}},
   "MonitoringAlertName": "{{string}}",
   "MonitoringScheduleName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMonitoringAlert_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatapointsToAlert](#API_UpdateMonitoringAlert_RequestSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-request-DatapointsToAlert"></a>
Within `EvaluationPeriod`, how many execution failures will raise an alert.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** [EvaluationPeriod](#API_UpdateMonitoringAlert_RequestSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-request-EvaluationPeriod"></a>
The number of most recent monitoring executions to consider when evaluating alert status.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** [MonitoringAlertName](#API_UpdateMonitoringAlert_RequestSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-request-MonitoringAlertName"></a>
The name of a monitoring alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MonitoringScheduleName](#API_UpdateMonitoringAlert_RequestSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-request-MonitoringScheduleName"></a>
The name of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_UpdateMonitoringAlert_ResponseSyntax"></a>

```
{
   "MonitoringAlertName": "string",
   "MonitoringScheduleArn": "string"
}
```

## Response Elements
<a name="API_UpdateMonitoringAlert_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringAlertName](#API_UpdateMonitoringAlert_ResponseSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-response-MonitoringAlertName"></a>
The name of a monitoring alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [MonitoringScheduleArn](#API_UpdateMonitoringAlert_ResponseSyntax) **   <a name="sagemaker-UpdateMonitoringAlert-response-MonitoringScheduleArn"></a>
The Amazon Resource Name (ARN) of the monitoring schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_UpdateMonitoringAlert_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMonitoringAlert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateMonitoringAlert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateMonitoringAlert)
