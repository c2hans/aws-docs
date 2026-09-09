---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineVersions.html
---

# ListPipelineVersions
<a name="API_ListPipelineVersions"></a>

Gets a list of all versions of the pipeline.

## Request Syntax
<a name="API_ListPipelineVersions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PipelineName": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelineVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPipelineVersions_RequestSyntax) **   <a name="sagemaker-ListPipelineVersions-request-MaxResults"></a>
The maximum number of pipeline versions to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPipelineVersions_RequestSyntax) **   <a name="sagemaker-ListPipelineVersions-request-NextToken"></a>
If the result of the previous `ListPipelineVersions` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline versions, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [PipelineName](#API_ListPipelineVersions_RequestSyntax) **   <a name="sagemaker-ListPipelineVersions-request-PipelineName"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,255})`
Required: Yes

 ** [SortOrder](#API_ListPipelineVersions_RequestSyntax) **   <a name="sagemaker-ListPipelineVersions-request-SortOrder"></a>
The sort order for the results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListPipelineVersions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PipelineVersionSummaries": [
      {
         "LastExecutionPipelineExecutionArn": "string",
         "PipelineArn": "string",
         "PipelineVersionDescription": "string",
         "PipelineVersionDisplayName": "string",
         "PipelineVersionId": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipelineVersions_ResponseSyntax) **   <a name="sagemaker-ListPipelineVersions-response-NextToken"></a>
If the result of the previous `ListPipelineVersions` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipeline versions, use this token in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [PipelineVersionSummaries](#API_ListPipelineVersions_ResponseSyntax) **   <a name="sagemaker-ListPipelineVersions-response-PipelineVersionSummaries"></a>
Contains a sorted list of pipeline version summary objects matching the specified filters. Each version summary includes the pipeline version ID, the creation date, and the last pipeline execution created from that version. This list can be empty.
Type: Array of [PipelineVersionSummary](API_PipelineVersionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPipelineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPipelineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListPipelineVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListPipelineVersions)
