---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelQualityJobDefinitions.html
---

# ListModelQualityJobDefinitions
<a name="API_ListModelQualityJobDefinitions"></a>

Gets a list of model quality monitoring job definitions in your account.

## Request Syntax
<a name="API_ListModelQualityJobDefinitions_RequestSyntax"></a>

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
<a name="API_ListModelQualityJobDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-CreationTimeAfter"></a>
A filter that returns only model quality monitoring job definitions created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-CreationTimeBefore"></a>
A filter that returns only model quality monitoring job definitions created before the specified time.
Type: Timestamp
Required: No

 ** [EndpointName](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-EndpointName"></a>
A filter that returns only model quality monitoring job definitions that are associated with the specified endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [MaxResults](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-MaxResults"></a>
The maximum number of results to return in a call to `ListModelQualityJobDefinitions`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-NameContains"></a>
A string in the transform job name. This filter returns only model quality monitoring job definitions whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-NextToken"></a>
If the result of the previous `ListModelQualityJobDefinitions` request was truncated, the response includes a `NextToken`. To retrieve the next set of model quality monitoring job definitions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-SortBy"></a>
The field to sort results by. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelQualityJobDefinitions_RequestSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-request-SortOrder"></a>
Whether to sort the results in `Ascending` or `Descending` order. The default is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelQualityJobDefinitions_ResponseSyntax"></a>

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
<a name="API_ListModelQualityJobDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobDefinitionSummaries](#API_ListModelQualityJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-response-JobDefinitionSummaries"></a>
A list of summaries of model quality monitoring job definitions.
Type: Array of [MonitoringJobDefinitionSummary](API_MonitoringJobDefinitionSummary.md) objects

 ** [NextToken](#API_ListModelQualityJobDefinitions_ResponseSyntax) **   <a name="sagemaker-ListModelQualityJobDefinitions-response-NextToken"></a>
If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of model quality monitoring job definitions, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelQualityJobDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelQualityJobDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelQualityJobDefinitions)
