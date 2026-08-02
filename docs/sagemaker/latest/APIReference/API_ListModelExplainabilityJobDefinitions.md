---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelExplainabilityJobDefinitions.html
---

# ListModelExplainabilityJobDefinitions
<a name="API_ListModelExplainabilityJobDefinitions"></a>

Lists model explainability job definitions that satisfy various filters.

## Request Syntax
<a name="API_ListModelExplainabilityJobDefinitions_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "EndpointName": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelExplainabilityJobDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-CreationTimeAfter"></a>
A filter that returns only model explainability jobs created after a specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-CreationTimeBefore"></a>
A filter that returns only model explainability jobs created before a specified time.
Type: Timestamp
Required: No

 ** [EndpointName](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-EndpointName"></a>
Name of the endpoint to monitor for model explainability.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MaxResults](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-MaxResults"></a>
The maximum number of jobs to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-NameContains"></a>
Filter for model explainability jobs whose name contains a specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-SortBy"></a>
Whether to sort results by the `Name` or `CreationTime` field. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelExplainabilityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-request-SortOrder"></a>
Whether to sort the results in `Ascending` or `Descending` order. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelExplainabilityJobDefinitions_ResponseSyntax"></a>

```
{
   "JobDefinitionSummaries": [
      {
         "CreationTime": number,
         "EndpointName": "string",
         "MonitoringJobDefinitionArn": "string",
         "MonitoringJobDefinitionName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelExplainabilityJobDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionSummaries](#API_ListModelExplainabilityJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-response-JobDefinitionSummaries"></a>
A JSON array in which each element is a summary for a explainability bias jobs.
Type: Array of [MonitoringJobDefinitionSummary](API_MonitoringJobDefinitionSummary.md) objects

 ** [NextToken](#API_ListModelExplainabilityJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelExplainabilityJobDefinitions-response-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelExplainabilityJobDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelExplainabilityJobDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelExplainabilityJobDefinitions)
