---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineExecutions.html
---

# ListPipelineExecutions
<a name="API_ListPipelineExecutions"></a>

Gets a list of the pipeline executions.

## Request Syntax
<a name="API_ListPipelineExecutions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PipelineName": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelineExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPipelineExecutions_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutions-request-MaxResults"></a>
The maximum number of pipeline executions to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPipelineExecutions_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutions-request-NextToken"></a>
If the result of the previous `ListPipelineExecutions` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline executions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [PipelineName](#API_ListPipelineExecutions_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutions-request-PipelineName"></a>
The name or Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,255})`
Required: Yes

 ** [SortBy](#API_ListPipelineExecutions_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutions-request-SortBy"></a>
The field by which to sort results. The default is `CreatedTime`.
Type: String
Valid Values: `CreationTime | PipelineExecutionArn`
Required: No

 ** [SortOrder](#API_ListPipelineExecutions_RequestSyntax) **   <a name="sagemaker-ListPipelineExecutions-request-SortOrder"></a>
The sort order for results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListPipelineExecutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PipelineExecutionSummaries": [
      {
         "PipelineExecutionArn": "string",
         "PipelineExecutionDescription": "string",
         "PipelineExecutionDisplayName": "string",
         "PipelineExecutionFailureReason": "string",
         "PipelineExecutionStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="sagemaker-ListPipelineExecutions-response-NextToken"></a>
If the result of the previous `ListPipelineExecutions` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline executions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [PipelineExecutionSummaries](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="sagemaker-ListPipelineExecutions-response-PipelineExecutionSummaries"></a>
Contains a sorted list of pipeline execution summary objects matching the specified filters. Each run summary includes the Amazon Resource Name (ARN) of the pipeline execution, the run date, and the status. This list can be empty.
Type: Array of [PipelineExecutionSummary](API_PipelineExecutionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPipelineExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPipelineExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListPipelineExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListPipelineExecutions)
