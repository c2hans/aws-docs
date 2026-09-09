---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringExecutions.html
---

# ListMonitoringExecutions
<a name="API_ListMonitoringExecutions"></a>

Returns list of all monitoring job executions.

## Request Syntax
<a name="API_ListMonitoringExecutions_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}",
   "MaxResults": {{number}},
   "MonitoringJobDefinitionName": "{{string}}",
   "MonitoringScheduleName": "{{string}}",
   "MonitoringTypeEquals": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMonitoringExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-EndpointName"></a>
Name of a specific endpoint to fetch jobs for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MaxResults](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-MaxResults"></a>
The maximum number of jobs to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MonitoringJobDefinitionName](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-MonitoringJobDefinitionName"></a>
Gets a list of the monitoring job runs of the specified monitoring job definitions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MonitoringScheduleName](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-MonitoringScheduleName"></a>
Name of a specific schedule to fetch jobs for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MonitoringTypeEquals](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-MonitoringTypeEquals"></a>
A filter that returns only the monitoring job runs of the specified monitoring type.
Type: String
Valid Values: `DataQuality | ModelQuality | ModelBias | ModelExplainability`
Required: No

 ** [NextToken](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-SortBy"></a>
Whether to sort the results by the `Status`, `CreationTime`, or `ScheduledTime` field. The default is `CreationTime`.
Type: String
Valid Values: `CreationTime | ScheduledTime | Status`
Required: No

 ** [SortOrder](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-SortOrder"></a>
Whether to sort the results in `Ascending` or `Descending` order. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListMonitoringExecutions_RequestSyntax) **   <a name="sagemaker-ListMonitoringExecutions-request-StatusEquals"></a>
A filter that retrieves only jobs with a specific status.
Type: String
Valid Values: `Pending | Completed | CompletedWithViolations | InProgress | Failed | Stopping | Stopped`
Required: No

## Response Syntax
<a name="API_ListMonitoringExecutions_ResponseSyntax"></a>

```
{
   "MonitoringExecutionSummaries": [
      {
         "EndpointName": "string",
         "FailureReason": "string",
         "MonitoringExecutionStatus": "string",
         "MonitoringJobDefinitionName": "string",
         "MonitoringScheduleName": "string",
         "MonitoringType": "string",
         "ProcessingJobArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitoringExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonitoringExecutionSummaries](#API_ListMonitoringExecutions_ResponseSyntax) **   <a name="sagemaker-ListMonitoringExecutions-response-MonitoringExecutionSummaries"></a>
A JSON array in which each element is a summary for a monitoring execution.
Type: Array of [MonitoringExecutionSummary](API_MonitoringExecutionSummary.md) objects

 ** [NextToken](#API_ListMonitoringExecutions_ResponseSyntax) **   <a name="sagemaker-ListMonitoringExecutions-response-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListMonitoringExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListMonitoringExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMonitoringExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMonitoringExecutions)
