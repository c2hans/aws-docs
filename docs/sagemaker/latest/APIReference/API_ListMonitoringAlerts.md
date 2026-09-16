---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringAlerts.html
---

# ListMonitoringAlerts
<a name="API_ListMonitoringAlerts"></a>

Gets the alerts for a single monitoring schedule.

## Request Syntax
<a name="API_ListMonitoringAlerts_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MonitoringScheduleName": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitoringAlerts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMonitoringAlerts_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlerts-request-MaxResults"></a>
The maximum number of results to display. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MonitoringScheduleName](#API_ListMonitoringAlerts_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlerts-request-MonitoringScheduleName"></a>
The name of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [NextToken](#API_ListMonitoringAlerts_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlerts-request-NextToken"></a>
If the result of the previous `ListMonitoringAlerts` request was truncated, the response includes a `NextToken`. To retrieve the next set of alerts in the history, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListMonitoringAlerts_ResponseSyntax"></a>

```
{
   "MonitoringAlertSummaries": [
      {
         "Actions": {
            "ModelDashboardIndicator": {
               "Enabled": boolean
            }
         },
         "AlertStatus": "string",
         "DatapointsToAlert": number,
         "EvaluationPeriod": number,
         "MonitoringAlertName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitoringAlerts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringAlertSummaries](#API_ListMonitoringAlerts_ResponseSyntax) **   <a name="sagemaker-ListMonitoringAlerts-response-MonitoringAlertSummaries"></a>
A JSON array where each element is a summary for a monitoring alert.
Type: Array of [MonitoringAlertSummary](API_MonitoringAlertSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [NextToken](#API_ListMonitoringAlerts_ResponseSyntax) **   <a name="sagemaker-ListMonitoringAlerts-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of alerts, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListMonitoringAlerts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListMonitoringAlerts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMonitoringAlerts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMonitoringAlerts)
