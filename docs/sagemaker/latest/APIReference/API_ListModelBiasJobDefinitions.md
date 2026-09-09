---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelBiasJobDefinitions.html
---

# ListModelBiasJobDefinitions
<a name="API_ListModelBiasJobDefinitions"></a>

Lists model bias jobs definitions that satisfy various filters.

## Request Syntax
<a name="API_ListModelBiasJobDefinitions_RequestSyntax"></a>

```
{
   "EndpointName": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelBiasJobDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointName](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-EndpointName"></a>
Name of the endpoint to monitor for model bias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MaxResults](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-MaxResults"></a>
The maximum number of model bias jobs to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-NameContains"></a>
Filter for model bias jobs whose name contains a specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-SortBy"></a>
Whether to sort results by the `Name` or `CreationTime` field. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelBiasJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-request-SortOrder"></a>
Whether to sort the results in `Ascending` or `Descending` order. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelBiasJobDefinitions_ResponseSyntax"></a>

```
{
   "JobDefinitionSummaries": [
      {
         "EndpointName": "string",
         "MonitoringJobDefinitionArn": "string",
         "MonitoringJobDefinitionName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelBiasJobDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionSummaries](#API_ListModelBiasJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-response-JobDefinitionSummaries"></a>
A JSON array in which each element is a summary for a model bias jobs.
Type: Array of [MonitoringJobDefinitionSummary](API_MonitoringJobDefinitionSummary.md) objects

 ** [NextToken](#API_ListModelBiasJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelBiasJobDefinitions-response-NextToken"></a>
The token returned if the response is truncated. To retrieve the next set of job executions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelBiasJobDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelBiasJobDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelBiasJobDefinitions)
