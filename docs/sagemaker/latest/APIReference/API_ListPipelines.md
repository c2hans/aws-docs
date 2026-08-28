---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelines.html
---

# ListPipelines
<a name="API_ListPipelines"></a>

Gets a list of pipelines.

## Request Syntax
<a name="API_ListPipelines_RequestSyntax"></a>

```
{
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PipelineNamePrefix": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatedAfter](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-CreatedAfter"></a>
A filter that returns the pipelines that were created after a specified time.
Type: Timestamp
Required: No

 ** [CreatedBefore](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-CreatedBefore"></a>
A filter that returns the pipelines that were created before a specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-MaxResults"></a>
The maximum number of pipelines to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-NextToken"></a>
If the result of the previous `ListPipelines` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipelines, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [PipelineNamePrefix](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-PipelineNamePrefix"></a>
The prefix of the pipeline name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,255}`
Required: No

 ** [SortBy](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-SortBy"></a>
The field by which to sort results. The default is `CreatedTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListPipelines_RequestSyntax) **   <a name="sagemaker-ListPipelines-request-SortOrder"></a>
The sort order for results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListPipelines_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PipelineSummaries": [
      {
         "CreationTime": number,
         "LastExecutionTime": number,
         "LastModifiedTime": number,
         "PipelineArn": "string",
         "PipelineDescription": "string",
         "PipelineDisplayName": "string",
         "PipelineName": "string",
         "RoleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipelines_ResponseSyntax) **   <a name="sagemaker-ListPipelines-response-NextToken"></a>
If the result of the previous `ListPipelines` request was truncated, the response includes a `NextToken`. To retrieve the next set of pipelines, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [PipelineSummaries](#API_ListPipelines_ResponseSyntax) **   <a name="sagemaker-ListPipelines-response-PipelineSummaries"></a>
Contains a sorted list of `PipelineSummary` objects matching the specified filters. Each `PipelineSummary` consists of PipelineArn, PipelineName, ExperimentName, PipelineDescription, CreationTime, LastModifiedTime, LastRunTime, and RoleArn. This list can be empty.
Type: Array of [PipelineSummary](API_PipelineSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListPipelines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListPipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListPipelines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListPipelines)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
