---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringSchedules.html
---

# ListMonitoringSchedules
<a name="API_ListMonitoringSchedules"></a>

Returns list of all monitoring schedules.

## Request Syntax
<a name="API_ListMonitoringSchedules_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "EndpointName": "{{string}}",
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "MonitoringJobDefinitionName": "{{string}}",
   "MonitoringTypeEquals": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitoringSchedules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-CreationTimeAfter"></a>
A filter that returns only monitoring schedules created after a specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-CreationTimeBefore"></a>
A filter that returns only monitoring schedules created before a specified time.
Type: Timestamp
Required: No

 ** [EndpointName](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-EndpointName"></a>
Name of a specific endpoint to fetch schedules for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [LastModifiedTimeAfter](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-LastModifiedTimeAfter"></a>
A filter that returns only monitoring schedules modified after a specified time.
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-LastModifiedTimeBefore"></a>
A filter that returns only monitoring schedules modified before a specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-MaxResults"></a>
The maximum number of jobs to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MonitoringJobDefinitionName](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-MonitoringJobDefinitionName"></a>
Gets a list of the monitoring schedules for the specified monitoring job definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MonitoringTypeEquals](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-MonitoringTypeEquals"></a>
A filter that returns only the monitoring schedules for the specified monitoring type.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

 ** [NameContains](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-NameContains"></a>
Filter for monitoring schedules whose name contains a specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-SortBy"></a>
Whether to sort the results by the `Status`, `CreationTime`, or `ScheduledTime` field. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-SortOrder"></a>
Whether to sort the results in `Ascending` or `Descending` order. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListMonitoringSchedules_RequestSyntax) **   <a name="sagemaker-ListMonitoringSchedules-request-StatusEquals"></a>
A filter that returns only monitoring schedules modified before a specified time.
Type: String
Valid Values: `Pending | Failed | Scheduled | Stopped`
Required: No

## Response Syntax
<a name="API_ListMonitoringSchedules_ResponseSyntax"></a>

```
{
   "MonitoringScheduleSummaries": [
      {
         "CreationTime": number,
         "EndpointName": "string",
         "LastModifiedTime": number,
         "MonitoringJobDefinitionName": "string",
         "MonitoringScheduleArn": "string",
         "MonitoringScheduleName": "string",
         "MonitoringScheduleStatus": "string",
         "MonitoringType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitoringSchedules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringScheduleSummaries](#API_ListMonitoringSchedules_ResponseSyntax) **   <a name="sagemaker-ListMonitoringSchedules-response-MonitoringScheduleSummaries"></a>
A JSON array in which each element is a summary for a monitoring schedule.
Type: Array of [MonitoringScheduleSummary](API_MonitoringScheduleSummary.md) objects

 ** [NextToken](#API_ListMonitoringSchedules_ResponseSyntax) **   <a name="sagemaker-ListMonitoringSchedules-response-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListMonitoringSchedules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListMonitoringSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMonitoringSchedules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMonitoringSchedules)
