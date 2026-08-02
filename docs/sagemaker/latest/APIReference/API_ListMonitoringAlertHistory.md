---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringAlertHistory.html
---

# ListMonitoringAlertHistory
<a name="API_ListMonitoringAlertHistory"></a>

Gets a list of past alerts in a model monitoring schedule.

## Request Syntax
<a name="API_ListMonitoringAlertHistory_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "MonitoringAlertName": "{{string}}",
   "MonitoringScheduleName": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitoringAlertHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-CreationTimeAfter"></a>
A filter that returns only alerts created on or after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-CreationTimeBefore"></a>
A filter that returns only alerts created on or before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-MaxResults"></a>
The maximum number of results to display. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MonitoringAlertName](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-MonitoringAlertName"></a>
The name of a monitoring alert.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MonitoringScheduleName](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-MonitoringScheduleName"></a>
The name of a monitoring schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-NextToken"></a>
If the result of the previous `ListMonitoringAlertHistory` request was truncated, the response includes a `NextToken`. To retrieve the next set of alerts in the history, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-SortBy"></a>
The field used to sort results. The default is `CreationTime`.
Type: String
Valid Values: `CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-SortOrder"></a>
The sort order, whether `Ascending` or `Descending`, of the alert history. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListMonitoringAlertHistory_RequestSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-request-StatusEquals"></a>
A filter that retrieves only alerts with a specific status.
Type: String
Valid Values: `InAlert | OK`
Required: No

## Response Syntax
<a name="API_ListMonitoringAlertHistory_ResponseSyntax"></a>

```
{
   "MonitoringAlertHistory": [
      {
         "AlertStatus": "string",
         "CreationTime": number,
         "MonitoringAlertName": "string",
         "MonitoringScheduleName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitoringAlertHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringAlertHistory](#API_ListMonitoringAlertHistory_ResponseSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-response-MonitoringAlertHistory"></a>
An alert history for a model monitoring schedule.
Type: Array of [MonitoringAlertHistorySummary](API_MonitoringAlertHistorySummary.md) objects

 ** [NextToken](#API_ListMonitoringAlertHistory_ResponseSyntax) **   <a name="sagemaker-ListMonitoringAlertHistory-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of alerts, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListMonitoringAlertHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListMonitoringAlertHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMonitoringAlertHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMonitoringAlertHistory)
